# Changelog

All notable changes to the "Mental Health Prediction Using Machine Learning" project will be documented in this file.

## [1.0.0] - 2026-08-25

### Added

- **Clinical Safety Override**: Implemented backend logic to automatically override the AI's baseline prediction if the user's PHQ-9 clinical score indicates moderate to severe symptoms (>=10), ensuring patient safety takes precedence.

- **Counselling Booking Flow**: Added `/book_session` POST endpoint in `app.py` and created the `booking_success.html` confirmation view with full input validation.
- **Standardized Clinical Assessment (PHQ-9)**: Embedded the 9-question Patient Health Questionnaire directly into `form.html` utilizing Jinja templating.
- **Dual-Scoring Pipeline**: Updated `app.py` backend to process rule-based PHQ-9 scores (0–27 severity thresholds) concurrently with the Machine Learning model prediction.
- **Explainable AI (XAI) Integration**: Integrated SHAP (SHapley Additive exPlanations) to dynamically generate Waterfall plots, giving users visual transparency into prediction factors.
- **Resources & Crisis Helplines**: Embedded 24/7 localized emergency contact details and support helplines directly onto the `result.html` output page.
- **Docker Deployment**: Created a production-ready `Dockerfile` based on `python:3.12-slim` and configured `gunicorn` for deployment.
- **Frontend UI Templates**: Created `result.html` and `booking_success.html` templates styled consistently with Bootstrap 5 and custom CSS.
- **Form Validation**: Added client-side HTML5 validation and pattern matching across forms, as well as backend fallback checks.

### Changed

- **SHAP Rendering Architecture**: Migrated from physical file-based plot generation to an in-memory Base64 encoding buffer (`io.BytesIO()`) to prevent browser caching issues and support concurrent users safely on cloud platforms.
- **Backend Optimization**: Cleaned up `app.py` by removing unused dependencies (`SQLAlchemy`, `datetime`, `os`) to optimize startup time and reduce container memory footprint.
- **Project Structure**: Restructured the workspace into modular directories (`models/`, `static/`, `templates/`) for production readiness.
- **Dependencies (`requirements.txt`)**: Removed strict version pinning for Python 3.12.10 compatibility; added `xgboost`, `shap`, and `gunicorn`.
- **Backend Routing (`app.py`)**: Updated form endpoints to render Jinja2 templates and added non-GUI Matplotlib backend configuration (`matplotlib.use('Agg')`) to safely render SHAP plots.
- **Data Preprocessing (`app.ipynb`)**: Configured `OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=-1)` in `ColumnTransformer` to handle unseen categories gracefully.
- **Visualizations (`app.ipynb`)**: Replaced deprecated `sns.distplot()` calls with `sns.histplot()` to eliminate warning logs.
- **Model Artifacts**: Regenerated `model.pkl`, `ct.pkl`, and `le.pkl` binaries within the Python 3.12.10 environment to fix Scikit-Learn (v1.9.0) unpickling version mismatches.

### Fixed

- **XGBoost Import Path (`app.ipynb`)**: Resolved module resolution errors by updating the deprecated `xgboost.sklearn` import to `from xgboost import XGBClassifier`.
- **Data Imputation (`app.ipynb`)**: Addressed dataset `NaN` values prior to model fitting to prevent `ValueError: Input X contains NaN` runtime crashes.
