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

![image](https://github.com/Manish06097/DpsChallenge_AI/assets/73208573/b01efbaa-427c-40ce-b542-0aa2c26200ea)

<br />

### Number of accidents per category:

![image](https://github.com/Manish06097/DpsChallenge_AI/assets/73208573/f56191f1-3032-4d0c-9ab2-acb8722e0ea9)

<br />

### Number of accidents per Accident Type:

![image](https://github.com/Manish06097/DpsChallenge_AI/assets/73208573/e520467e-ca87-45e1-9a03-27a8639feaf0)

<br />

### Number of accidents per Accident Type:

![image](https://github.com/Manish06097/DpsChallenge_AI/assets/73208573/68307e67-2721-449c-84fc-669438b2a0c8)


Result Accuracy

```
MAE(Mean Absolute Error ) : 54.5
```

```
R2 Score :0.98
```













<br />


