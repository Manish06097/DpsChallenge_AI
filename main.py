from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import pickle

app = FastAPI()

# Load the pre-trained model from the pickle file
with open('model/model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)


def predict_chance( Year, Month,Category='Alkoholunfälle', Accident_type='insgesamt',):
    #prediction=regressor.predict([[Category, Accident_type, Year, Month]]) #predictions using our model
    
    # Pre-processing user input    
    if Category == "Verkehrsunfälle":
        Category = 0
    elif Category == "Alkoholunfälle":
        Category = 1
    elif Category == "Fluchtunfälle":
        Category = 2


    if Accident_type == "insgesamt":
        Accident_type = 0
    elif Accident_type == "Verletzte und Getötete":
        Accident_type = 1
    elif Accident_type == "mit Personenschäden":
        Accident_type = 2   
    prediction=model.predict([[Category, Accident_type, Year, Month]]) #predictions using our model     

    return prediction[0] 

class PredictionInput(BaseModel):
    
    year: int
    month: int

   

@app.post("/predict")
def predict(input_data: PredictionInput):

    try:
        # Create a DataFrame from the input data
        
        Year= input_data.year,
        Year = int(Year[0])
        Month= input_data.month

    


        # Make the prediction

        return {"prediction": predict_chance(Year,Month)}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

class PredictionInput1(BaseModel):
    
    year: int
    month: int
    category: str = "Alkoholunfälle"
    accident_type: str = "insgesamt"

    

@app.post("/predict1")
def predict1(input_data: PredictionInput1):
    try:
        # Create a DataFrame from the input data
        
        Year= input_data.year,
        Year = int(Year[0])
        Month= input_data.month
    


        # Make the prediction

        return {"prediction": predict_chance(Year,Month,input_data.category, input_data.accident_type)}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
