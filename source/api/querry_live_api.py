"""
Creator: Mateus Goldbarg
Date: May 23 2022
Script that POSTS to the API using the requests 
module and returns both the result of 
model inference and the status code
"""
import requests
import json
# import pprint

person = {
        "Pregnancies": 0,
        "Glucose": 137,
        "BloodPressure": 40,
        "SkinThickness": 35,
        "Insulin": 168,
        "BMI": 43.1,
        "DiabetesPedigreeFunction": 2.288,
        "Age": 33
    }

url = "http://127.0.0.1:8000"
#url = "https://high-income-app.herokuapp.com"
response = requests.post(f"{url}/predict",
                         json=person)

print(f"Request: {url}/predict")
print(f"Person: \n Pregnancies: {person['Pregnancies']}\n Glucose: {person['Glucose']}\n"\
      f" BloodPressure: {person['BloodPressure']}\n SkinThickness: {person['SkinThickness']}\n"\
      f" Insulin: {person['Insulin']}\n"\
      f" BMI: {person['BMI']}\n"\
      f" DiabetesPedigreeFunction: {person['DiabetesPedigreeFunction']}\n"\
      f" Age: {person['Age']}\n"
     )
print(f"Result of model inference: {response.json()}")
print(f"Status code: {response.status_code}")