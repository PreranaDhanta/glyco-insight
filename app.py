from flask import Flask, render_template, request, make_response
from xhtml2pdf import pisa
from io import BytesIO
import numpy as np
import pickle

app = Flask(__name__)

# Load the trained model and scaler
with open('diabetes_model.pkl', 'rb') as f:
    scaler, model = pickle.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    name = request.form.get('name')
    email = request.form.get('email')

    # Extract features
    feature_names = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
                     'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
    features = [float(request.form.get(field)) for field in feature_names]

    # Preprocess input
    input_array = np.array(features).reshape(1, -1)
    input_scaled = scaler.transform(input_array)
    prediction = model.predict(input_scaled)

    # Build prediction output
    prediction_dict = {0: 'Not Diabetic', 1: 'Diabetic'}
    model_index = int(prediction[0])
    accuracy = 0.856  # Example static accuracy; replace if dynamic

    input_dict = {name: value for name, value in zip(feature_names, features)}

    result = [
        input_dict,           # [0] input data as dict
        prediction_dict,      # [1] prediction mapping
        [name, email],        # [2] personal info
        accuracy              # [3] model accuracy
    ]

    return render_template('result.html', result=result, model=model_index)

@app.route('/download_pdf', methods=['POST'])
def download_pdf():
    data = request.form.to_dict()
    input_data = eval(data['input_data'])  # Should be a dictionary

    rendered = render_template('report_template.html',
                               name=data['name'],
                               email=data['email'],
                               input_data=input_data,
                               prediction=data['prediction'],
                               accuracy=float(data['accuracy']))
    pdf = BytesIO()
    pisa.CreatePDF(BytesIO(rendered.encode('utf-8')), dest=pdf)
    response = make_response(pdf.getvalue())
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=report.pdf'
    return response

if __name__ == '__main__':
    app.run(debug=True)
