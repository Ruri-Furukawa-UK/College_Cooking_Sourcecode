# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import statsmodels.api as sm

# Create a DataFrame from the Excel file
from google.colab import files
uploaded = files.upload()
excel_file_path ='学生の食生活についての調査（回答）.xlsx'
df = pd.read_excel(excel_file_path)

# Define functions to convert categorical data
def howoften(value):
    if isinstance(value, str):
        if 'everyday' in value:
            return 4
        elif '週4~6' in value:
            return 3
        elif '週2~3' in value:
            return 2
        elif 'rarely' in value:
            return 1
        else:
            return 0

def whycook(value):
    if isinstance(value, str):
        if 'save' in value:
            return 1
        else:
            return 0
def whycook2(value):
    if isinstance(value, str):
        if 'health' in value:
            return 1
        else:
            return 0

def whycook3(value):
    if isinstance(value, str):
        if 'delicious' in value:
            return 1
        else:
            return 0

def whycook4(value):
    if isinstance(value, str):
        if 'skills' in value:
            return 1
        else:
            return 0

def whycook5(value):
    if isinstance(value, str):
        if 'other' in value:
            return 1
        else:
            return 0

# Recode the original DataFrame
df['Howoften_dorm'] = df['あなたの自炊を行う頻度 について教えてください/ How often do you cook for yourself in a week?'].apply(howoften)
df['Howoften_alone'] = df['あなたの自炊を行う頻度 について教えてください/ How often do you cook for yourself in a week?.1'].apply(howoften)
df['Howoften_home'] = df['あなたの自炊を行う頻度 について教えてください/ How often do you cook for yourself in a week?.2'].apply(howoften)

# Investigation of dorm students
df_dorm = df[df['現在の居住状況について / Current living condition'].str.contains('寮')]

# Recode the original dataset
df_dorm['Savemoney'] = df_dorm['【自炊を行う】理由 / The reasons why you cook for yourself'].apply(whycook)
df_dorm['Forhealth'] = df_dorm['【自炊を行う】理由 / The reasons why you cook for yourself'].apply(whycook2)
df_dorm['Delicious'] = df_dorm['【自炊を行う】理由 / The reasons why you cook for yourself'].apply(whycook3)
df_dorm['Skills'] = df_dorm['【自炊を行う】理由 / The reasons why you cook for yourself'].apply(whycook4)
df_dorm['OtherResidents'] = df_dorm['【自炊を行う】理由 / The reasons why you cook for yourself'].apply(whycook5)

# Fill in the missing values
df_dorm=df_dorm.fillna(0)

# Define the explanatory and response variables
X_mul = df_dorm[['Savemoney', 'Forhealth', 'Delicious','Skills','OtherResidents']]
y_mul = df_dorm['Howoften_dorm']
X_mul0 = sm.add_constant(X_mul) # Add a constant

# Fit the linear regression model and show regression coefficients
model_dorm2 = sm.OLS(y_mul, X_mul0.fillna(0)).fit()
coefficients_dorm = model_dorm2.params
print(coefficients_dorm)

# Investigation of students living alone
df_alone= df[df['現在の居住状況について / Current living condition'].str.contains('一人')]

# Recode the original dataset
df_alone['Savemoney'] = df_alone['【自炊を行う】理由 / The reasons why you cook for yourself.1'].apply(whycook)
df_alone['Forhealth'] = df_alone['【自炊を行う】理由 / The reasons why you cook for yourself.1'].apply(whycook2)
df_alone['Delicious'] = df_alone['【自炊を行う】理由 / The reasons why you cook for yourself.1'].apply(whycook3)
df_alone['Skills'] = df_alone['【自炊を行う】理由 / The reasons why you cook for yourself.1'].apply(whycook4)

# Define the explanatory and response variables
X_mul1 = df_alone[['Savemoney', 'Forhealth', 'Delicious','Skills']]
y_mul1 = df_alone['Howoften_alone']
X_mul01 = sm.add_constant(X_mul1) # Add a constant

# Fit the linear regression model and show regression coefficients
model_alone2 = sm.OLS(y_mul1, X_mul01.fillna(0)).fit()
coefficients_alone = model_alone2.params
print(coefficients_alone)

# Investigation of students living with their family
df_home= df[df['現在の居住状況について / Current living condition'].str.contains('実家')]

# Define additional functions to convert categorical variables unique in students living with their family
def whycook7(value):
    if isinstance(value, str):
        if '味付け' in value:
            return 1
        else:
            return 0

def whycook8(value):
    if isinstance(value, str):
        if '家族' in value:
            return 1
        else:
            return 0

# Recode the original dataset
df_home['Savemoney'] = df_home['【自炊を行う】理由 / The reasons why you cook for yourself.2'].apply(whycook)
df_home['Forhealth'] = df_home['【自炊を行う】理由 / The reasons why you cook for yourself.2'].apply(whycook2)
df_home['Delicious'] = df_home['【自炊を行う】理由 / The reasons why you cook for yourself.2'].apply(whycook3)
df_home['Skills'] = df_home['【自炊を行う】理由 / The reasons why you cook for yourself.2'].apply(whycook4)
df_home['Taste'] = df_home['【自炊を行う】理由 / The reasons why you cook for yourself.2'].apply(whycook7)
df_home['OtherFamily'] = df_home['【自炊を行う】理由 / The reasons why you cook for yourself.2'].apply(whycook8)

# Define the explanatory and response variables
X_mul2 = df_home[['Savemoney', 'Forhealth', 'Delicious','Skills','OtherFamily','Taste']]
y_mul2 = df_home['Howoften_home']
X_mul02 = sm.add_constant(X_mul2) # Add a constant

# Fit the linear regression model and show regression coefficients
model_alone3 = sm.OLS(y_mul2, X_mul02.fillna(0)).fit()
coefficients_home = model_alone3.params
coefficients_home
