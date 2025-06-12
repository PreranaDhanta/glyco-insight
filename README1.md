# 🧠 Glyco Insight – Smart Diabetes Prediction & PDF Report Generator

**Glyco Insight** is a machine learning–powered web application that helps users predict the likelihood of diabetes using medical inputs. Built with **Python**, **Flask**, and **Scikit-learn**, the app provides instant diagnostic results and offers a downloadable **PDF report**, making it an excellent showcase for health-focused AI solutions.

## 🚀 Key Features

- 🧪 **Predicts diabetes** using a trained **SVM (Support Vector Machine)** model
- 🔢 Accepts 8 key medical input parameters:
  - Name
  - email
  - Pregnancies
  - Glucose
  - Blood Pressure
  - Skin Thickness
  - Insulin
  - BMI
  - Diabetes Pedigree Function
  - Age
- 📉 Uses `StandardScaler` to preprocess user input
- 📃 Generates a downloadable **PDF diagnostic report** via `xhtml2pdf`
- 💡 Clean, user-friendly interface built with HTML + CSS
- ✅ Backend powered by Flask for fast and lightweight deployment

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS, Jinja2 (Flask Templates)  
- **Backend**: Flask (Python)  
- **Machine Learning**: Scikit-learn (SVM), StandardScaler  
- **PDF Generation**: xhtml2pdf  
- **Deployment**: Render / Heroku / Streamlit Cloud (optional)

## 📂 Project Structure
glyco-insight/
├── app.py
├── diabetes_model.pkl
├── requirements.txt
├── static/
│   └── style.css
├── templates/
│   ├── index.html
│   ├── result.html
│   └── report_template.html





## ⚙️ How to Run Locally

```bash
git clone https://github.com/yourusername/glyco-insight.git
cd glyco-insight
python -m venv venv
venv\Scripts\activate   # On Windows
pip install -r requirements.txt
python app.py
