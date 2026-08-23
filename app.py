from flask import Flask, render_template, request
from pandas import DataFrame
import pickle
import io
import base64
import matplotlib
import matplotlib.pyplot as plt
import shap
import numpy as np

# Force matplotlib to not use any Xwindows backend to prevent threading crashes in Flask
matplotlib.use('Agg')

# Load models and transformers
model = pickle.load(open("./models/model.pkl", 'rb'))
ct = pickle.load(open("./models/ct.pkl", "rb"))
le = pickle.load(open("./models/le.pkl", "rb"))

app = Flask(__name__) 

@app.route('/')
def hello_world():
    return render_template('index.html')
    
@app.get('/form')
def show_form():
    return render_template('form.html')

@app.post('/submit_form')
def submit_form():
    # ML Data Extraction
    data = [{
        "Age": int(request.form["inputAge"]),
        "Gender": request.form["inputGender"],
        "self_employed": request.form["inputSelfEmployed"],
        "family_history": request.form["inputFamilyHistory"],
        "work_interfere": request.form["inputWorkInterference"],
        "no_employees": request.form["inputNoOfEmp"],
        "remote_work": request.form["inputRemoteWork"],
        "tech_company": request.form["inputTechCompany"],
        "benefits": request.form["inputBenefits"],
        "care_options": request.form["inputCareOptions"],
        "wellness_program": request.form["inputWellnessProgram"],
        "seek_help": request.form["inputSeekHelp"],
        "anonymity": request.form["inputAnonymity"],
        "leave": request.form["inputLeave"],
        "mental_health_consequence": request.form["inputMentalHealthConsequence"],
        "phys_health_consequence": request.form["inputPhysHealthConsequence"],
        "coworkers": request.form["inputCoworkers"],
        "supervisor": request.form["inputSupervisor"],
        "mental_health_interview": request.form["inputMentalHealthInterview"],
        "phys_health_interview": request.form["inputPhysHealthInterview"],
        "mental_vs_physical": request.form["inputMentalVsPhysical"],
        "obs_consequence": request.form["inputObsConsequence"],
    }]
    
    df = DataFrame.from_records(data)
    x = ct.transform(df)
    y = model.predict(x)
    treatment = le.inverse_transform(y)[0]

    # PHQ-9 Score Calculation
    phq_score = 0
    for i in range(1, 10):
        # Extract phq1 through phq9, default to 0 if missing
        phq_score += int(request.form.get(f"phq{i}", 0))
        
    # Determine severity based on standard medical thresholds
    if phq_score >= 20:
        phq_severity = "Severe"
    elif phq_score >= 15:
        phq_severity = "Moderately Severe"
    elif phq_score >= 10:
        phq_severity = "Moderate"
    elif phq_score >= 5:
        phq_severity = "Mild"
    else:
        phq_severity = "None / Minimal"

    # --- SHAP EXPLAINER INTEGRATION (Base64 Memory Buffer) ---
    try:
        feature_names = ct.get_feature_names_out()
        
        # 1. Create a baseline 'masker' of zeroes matching the shape of the user's input array
        baseline = np.zeros((1, x.shape[1]))
        
        # 2. Initialize the explainer using the explicit predict function and the baseline
        explainer = shap.Explainer(model.predict, baseline, feature_names=feature_names)
        shap_values = explainer(x)

        plt.figure(figsize=(8, 5))
        
        # 3. shap_values is a 2D array, we need the first dimension for the waterfall plot
        shap.plots.waterfall(shap_values[0], show=False)
        plt.tight_layout()
        
        # Save plot to a temporary memory buffer
        buf = io.BytesIO()
        plt.savefig(buf, format="png")
        plt.close()
        buf.seek(0)
        
        # Encode the image to base64 string
        plot_data = base64.b64encode(buf.read()).decode("utf-8")
        
    except Exception as e:
        print(f"Error generating SHAP plot: {e}")
        plot_data = None
        plt.close()
    # ----------------------------------

    # Pass the new plot_data variable to the template
    return render_template('result.html', 
                           prediction=treatment, 
                           phq_score=phq_score, 
                           phq_severity=phq_severity,
                           plot_data=plot_data)

@app.post('/book_session')
def book_session():
    first_name = request.form.get("firstName", "").strip()
    last_name = request.form.get("lastName", "").strip()
    phone = request.form.get("phoneNumber", "").strip()
    email = request.form.get("mailAddress", "").strip()
    address = request.form.get("address", "").strip()
    pincode = request.form.get("pincode", "").strip()
    terms = request.form.get("terms")

    # Backend validation check
    if not all([first_name, last_name, phone, email, address, pincode, terms]):
        return "Error: All fields are required and terms must be accepted.", 400

    full_name = f"{first_name} {last_name}"
    return render_template('booking_success.html', name=full_name, phone=phone, email=email)

if __name__=="__main__":
    app.run(debug=False, port=8000)