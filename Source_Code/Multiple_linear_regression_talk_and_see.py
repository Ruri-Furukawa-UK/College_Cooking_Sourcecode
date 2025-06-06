# Investigate the influence of frequency of talking about cooking on the frequency of cooking
# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from mpl_toolkits.mplot3d import Axes3D

# Upload a dataset
from google.colab import files
uploaded = files.upload()

# Convert into a DataFrame
excel_file_path = 'Cooking.xlsx'
df = pd.read_excel(excel_file_path)

# Recode categorical variables into numerical ones
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

def howtalk(value):
    if isinstance(value, str):
        if 'often' in value:
            return 3
        elif 'sometimes' in value:
            return 2
        elif 'rarely' in value:
            return 2
        else:
            return 0

df['Howoften_dorm'] = df['あなたの自炊を行う頻度 について教えてください/ How often do you cook for yourself in a week?'].apply(howoften)
df['Howoften_alone'] = df['あなたの自炊を行う頻度 について教えてください/ How often do you cook for yourself in a week?.1'].apply(howoften)
df['Howoften_home'] = df['あなたの自炊を行う頻度 について教えてください/ How often do you cook for yourself in a week?.2'].apply(howoften)

df['Howtalk_dorm'] = df['仲の良い友達や家族と自炊についての話をしますか / Do you often talk with your close friends or your family about cooking?'].apply(howtalk)
df['Howtalk_alone'] = df['周りの人とよく自炊についての話をしますか / Do you often talk with others about cooking?'].apply(howtalk)
df['Howtalk_home'] = df['周りの人とよく自炊についての話をしますか / Do you often talk with others about cooking?.1'].apply(howtalk)

df['Howlook_dorm'] = df['他の寮生が自炊するのをよく見ますか/ How often do you see other residents cooking in the kitchen?'].apply(howtalk)
df['Howlook_alone'] = df['周りの人は自炊していますか / Do other people around you cook for themselves?'].apply(howtalk)
df['Howlook_home'] = df['周りの人は自炊していますか / Do other people around you cook for themselves?.1'].apply(howtalk)

# Investigation of students in dormitories
df_dorm = df[df['現在の居住状況について / Current living condition'].str.contains('寮')]

# Define explanatory and response variables
X = df_dorm[['Howtalk_dorm', 'Howlook_dorm']]
y = df_dorm['Howoften_dorm']

# Fit a linear regression model
model_dorm = LinearRegression()
model_dorm.fit(X, y)

# Compute regression coefficients
coefficients = np.append(model_dorm.intercept_, model_dorm.coef_)
estimated_intercept = coefficients[0]
estimated_coefficients = coefficients[1:]

# Show the equation
equation = f"y = {estimated_intercept:.2f} + {estimated_coefficients[0]:.2f} * x1 + {estimated_coefficients[1]:.2f} * x2"
print(equation)

# Investigation of students living alone
df_alone= df[df['現在の居住状況について / Current living condition'].str.contains('一人')]

# Define explanatory and response variables
X = df_alone[['Howtalk_alone', 'Howlook_alone']]
y = df_alone['Howoften_alone']

# Fit a linear regression model
model_alone = LinearRegression()
model_alone.fit(X, y)

# Compute regression coefficients
coefficients = np.append(model_alone.intercept_, model_alone.coef_)
estimated_intercept = coefficients[0]
estimated_coefficients = coefficients[1:]

# Show the equation
equation = f"y = {estimated_intercept:.2f} + {estimated_coefficients[0]:.2f} * x1 + {estimated_coefficients[1]:.2f} * x2"
print(equation)

# Investigation of students living with their family
df_home= df[df['現在の居住状況について / Current living condition'].str.contains('実家')]

# Define explanatory and response variables
X = df_home1[['Howtalk_home', 'Howlook_home']]
y = df_home1['Howoften_home']

# Fit a linear regression model
model_home = LinearRegression()
model_home.fit(X, y)

# Compute regression coefficients
coefficients = np.append(model_home.intercept_, model_home.coef_)
estimated_intercept = coefficients[0]
estimated_coefficients = coefficients[1:]

# Show the equation
equation = f"y = {estimated_intercept:.2f} + {estimated_coefficients[0]:.2f} * x1 + {estimated_coefficients[1]:.2f} * x2"
print(equation)
