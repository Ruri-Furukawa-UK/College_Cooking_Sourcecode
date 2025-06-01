# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

# Upload a dataset of an Excel file
from google.colab import files
uploaded = files.upload()
excel_file_path = '学生の食生活についての調査（回答） (1).xlsx'
df = pd.read_excel(excel_file_path)

# Define a function to convert a categorical variable into numerical one
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

# Recode the original data
df['Howoften_dorm'] = df['あなたの自炊を行う頻度 について教えてください/ How often do you cook for yourself in a week?'].apply(howoften)
df['Howoften_alone'] = df['あなたの自炊を行う頻度 について教えてください/ How often do you cook for yourself in a week?.1'].apply(howoften)
df['Howoften_home'] = df['あなたの自炊を行う頻度 について教えてください/ How often do you cook for yourself in a week?.2'].apply(howoften)

# Extract data with the frequency of cooking
filtered_data = df[df['現在の居住状況について / Current living condition'] == '寮生活 / living in the dorm']['Howoften_dorm']
filtered_data2 = df[df['現在の居住状況について / Current living condition'] == '一人暮らし/ living alone']['Howoften_alone']
filtered_data3 = df[df['現在の居住状況について / Current living condition'] == '実家暮らし/ living with family']['Howoften_home']

# Define a function to conduct t-test
def ttest(group1, group2):

    # Conduct t-test
    t_statistic, p_value = ttest_ind(group1, group2)

    # Set the significance level
    alpha = 0.05

    # Conclude t-test
    if p_value < alpha:
        print("We reject the null hypothesis that there is no statistically significant difference.")
    else:
        print("We fail to reject the null hypothesis that there is no statistically significant difference.")

# Implement t-test for each combination of data
ttest(filtered_data, filtered_data2)
ttest(filtered_data, filtered_data3)
ttest(filtered_data2, filtered_data3)
