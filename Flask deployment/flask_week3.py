from flask import Flask, request, jsonify, json
import pickle
import warnings
warnings.filterwarnings("ignore")
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
#with open("models.pkl","rb") as file:
     #models = pickle.load(file)

@app.route("/week3/flask",methods = ["POST"])



def prediction_model1():
     #weight_model = request.get_json()
     #prediction = models["model"].predict(weight_model)
     #return jsonify({"Prediction": prediction.tolist()})

   with open("models.pkl","rb") as file:
      models = pickle.load(file)
      x=[]
      for keys,values in json.loads(request.data).items():
         x.append(values)
   return(models["model"].predict([x]).tolist())

   

#def prediction_model2():
 #    waist_model = request.get_json
  #   prediction = models["model2"].predict(waist_model)
     #return jsonify({"Prediction":prediction.tolist()})


#def predict():
    #data = request.get_json()
    #weight_prediction = models["model"].predict(data)
    #waist_prediction = models["model2"].predict(data)
    #return jsonify({"Weight Prediction": weight_prediction.tolist(), "Waist Prediction": waist_prediction.tolist()})