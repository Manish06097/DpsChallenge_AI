# Digital Product System challenge Artificial Intelligence Engineer

The project is submitted for a challenge for the Digital Product School (DPS). In the project a dataframe consisting of historical values of the accidents from different categories in the city of Munich, Germany.

## Description

This challenge for Artificial Intelligence Engineer Consists of 3 tasks.

- Mission 1: Create a AI Model
            Cleaning the data,  visualizing the historical accidents from the dataframe,Training a model to forecast future values.
- Mission 2: Publish source code & Deploy
           Deploying the model with an endpoint that accepts POST requests in JSON body
- Mission 3: Sending the URL of the task

### Files

 - **Accident_Prediction_Model.ipynb**: A jupyter notebook contains a step-by-step of importing the data, cleaning, and then visualizing the result after that loads the preprocessed data, then estimating the parameters passed for the model: `Random Forest regressor`. The model is trained and tested on the year 2020 data, the model is then evaluated and exported for deployment.
 - **main.py**:  thisx server file  forecasting and returns the result. The latter is the endpoint, which is deployed through `Fastapi`.


 #### Note
The endpoint accepts a POST request with a JSON body like this:
```
{
"year" : 2021,
"month" : 1
}
```
It return prediction in the following format:
```
{
"prediction" : value
}
```


## Packages:
- pandas
- numpy
- matplotlib
- sklearn
- pickle
- Fastapi
- pydantic

## Visualization:
visualization historically the number of accidents per category
### Accidents Category Visualization per year:

<img src="./images/TotalaccidentCategoryperMonth.png"/>

<br />

### Number of accidents per category:

<img src="./images/TotalaccidentperCategoryperyear.png"/>

<br />

### Number of accidents per Accident Type:

<img src="./images/Totalaccidentpertypepermonth.png"/>

<br />

### Number of accidents per Accident Type:

<img src="./images/Totalaccidentpertypeperyear.png"/>

<br />


