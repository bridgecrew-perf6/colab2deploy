"""
Creator: Ivanovitch Silva
Date: 18 April 2022
API testing
"""
from fastapi.testclient import TestClient
import os
import sys
import pathlib
from source.api.main import app

# Instantiate the testing client with our app.
client = TestClient(app)

# a unit test that tests the status code of the root path
def test_root():
    r = client.get("/")
    assert r.status_code == 200

# a unit test that tests the status code and response 
# for an instance with a low income
def test_get_inference_low_income():

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

    r = client.post("/predict", json=person)
    # print(r.json())
    assert r.status_code == 200
    assert r.json() == "Diabetic"

# a unit test that tests the status code and response 
# for an instance with a high income
def test_get_inference_high_income():

    person = {
        "Pregnancies": 1,
        "Glucose": 89,
        "BloodPressure": 66,
        "SkinThickness": 23,
        "Insulin": 94,
        "BMI": 28.1,
        "DiabetesPedigreeFunction": 0.167,
        "Age": 21
    }

    r = client.post("/predict", json=person)
    print(r.json())
    assert r.status_code == 200
    assert r.json() == "Healthy"