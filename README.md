# Mental Health Prediction & Assessment System

🚀 **Live Demo:** [Predict Your Mental Health Now](https://mental-health-prediction-using-machine-42cn.onrender.com/)

An end-to-end Machine Learning web application designed to evaluate mental health indicators, perform standardized clinical depression screenings (PHQ-9), and provide visual decision transparency using Explainable AI (SHAP).

---

## Key Features

- **Machine Learning Risk Prediction:** Utilizes an optimized AdaBoost Classifier trained on tech workplace survey data to predict mental health treatment likelihood.
- **Clinical PHQ-9 Screening:** Integrated 9-question Patient Health Questionnaire providing immediate severity scoring (0 to 27 scale) alongside AI predictions.
- **Clinical Safety Override:** System architecture ensures patient safety by prioritizing standardized clinical symptom thresholds (PHQ-9 >= 10) over demographic-based AI predictions when determining final risk outputs.
- **Explainable AI (XAI):** Implements SHAP (SHapley Additive exPlanations) to render dynamic Waterfall plots explaining feature contributions for each prediction.
- **Interactive Counselling Booking:** Seamless form interface allowing users to schedule sessions directly with mental health specialists.
- **Crisis Assistance:** Localized emergency contact info and 24/7 helplines embedded directly into result views.
- **Containerized Deployment:** Includes production-ready Docker support powered by Gunicorn.

---

## Tech Stack

- **Machine Learning & Data Science:** Python 3.12, Scikit-Learn, Pandas, NumPy, XGBoost, SHAP
- **Backend Framework:** Flask, Gunicorn
- **Frontend:** HTML5, CSS3, Bootstrap 5, Jinja2
- **DevOps & Tooling:** Docker, VS Code, Render

---

## Model Performance

Multiple classification algorithms were trained, tuned, and evaluated during exploratory data analysis:

- **AdaBoost Classifier (Tuned):** ~86.9% Accuracy (Selected Final Model)
- **Random Forest Classifier**
- **XGBoost Classifier**
- **Logistic Regression**

Model evaluation was validated using Confusion Matrices, ROC-AUC curves, and Precision-Recall metrics.

---

## Project Structure

```text
├── models/                  # Serialized ML artifacts (.pkl)
│   ├── model.pkl            # Trained AdaBoost Classifier
│   ├── ct.pkl               # ColumnTransformer pipeline
│   └── le.pkl               # LabelEncoder object
├── static/                  # Static assets (CSS, JS, generated plots)
│   ├── css/
│   └── images/              # Dynamic SHAP plot storage
├── templates/               # HTML Jinja2 Templates
│   ├── index.html           # Landing page & booking form
│   ├── form.html            # Primary ML & PHQ-9 assessment form
│   ├── result.html          # Dynamic prediction & XAI dashboard
│   └── booking_success.html # Appointment confirmation view
├── app.ipynb                # Jupyter Notebook for Data Cleaning, EDA & Training
├── app.py                   # Flask Application Backend
├── Dockerfile               # Production Containerization Specification
├── requirements.txt         # Unpinned Python dependencies
├── changelog.md             # Project version history
└── survey.csv               # Kaggle OSMI Mental Health Dataset
```

---

## How to Run Locally

### Prerequisites

- **Python 3.10+ installed**

- **Git**

### Step-by-Step Setup

1. **Clone the Repository**:

```Bash
git clone https://github.com/starJeet000/Mental-Health-Prediction-Using-Machine-Learning.git

cd Mental-Health-Prediction-Using-Machine-Learning
```

2. **Create and Activate Virtual Environment:**

```bash
#Windows (PowerShell)
python -m venv .venv
.venv\Scripts\Activate.ps1

#Linux / macOS
python3 -m venv .venv
source .venv/bin/activate
```

3. **Install Dependencies:**

```bash
pip install -r requirements.txt
```

4. **Run the Flask Server:**

```bash
python app.py
```

5. **Access the Web App:**

Open your browser and navigate to `http://127.0.0.1:8000`.

---

## Running with Docker

To build and run the application inside a Docker container:

```bash
### Build the Docker image

docker build -t mental-health-app .

### Run the container

docker run -p 8000:8000 mental-health-app
```

Navigate to `http://localhost:8000` in your browser.

---

## Disclaimer

_This application is built for educational and preliminary screening purposes only. It is not a substitute for professional medical advice, diagnosis, or treatment._
