import pickle

from flask import Flask
from flask import request
from flask import jsonify

MODEL_FILE_NAME = 'model1.bin'
DV_FILE_NAME = 'dv.bin'


with open(DV_FILE_NAME, 'rb') as dv_file, open(MODEL_FILE_NAME, 'rb') as model_file:
    dv = pickle.load(dv_file)
    model = pickle.load(model_file)


app = Flask('score')

@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()
    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0, 1]

    result = {
        "score_proba": float(y_pred)
    }
    print("Prediction result:", result)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9696)
