#coding=UTF8
import numpy as np
import pandas as pd

# RMS Titanic data visualization code
# 数据可视化代码
from titanic_visualizations import survival_stats
from IPython.display import display
#%matplotlib inline

# Load the dataset
# 加载数据集
in_file = 'titanic_data.csv'
full_data = pd.read_csv(in_file)

# Store the 'Survived' feature in a new variable and remove it from the dataset
# 从数据集中移除 'Survived' 这个特征，并将它存储在一个新的变量中。
outcomes = full_data['Survived']
data = full_data.drop('Survived', axis = 1)

def accuracy_score(truth, pred):
    # 确保预测的数量与结果的数量一致
    if len(truth) == len(pred):
        # 计算预测准确率（百分比）
        return "Predictions have an accuracy of {:.2f}%.".format((truth == pred).mean() * 100)

    else:
        return "Number of predictions does not match number of outcomes!"

predictions = pd.Series(np.ones(5, dtype=int))
print accuracy_score(outcomes[:5], predictions)

def predictions_0(data):
    predictions = []
    for idx, passenger in data.iterrows():
        predictions.append(0)
    return pd.Series(predictions)

predictions = predictions_0(data)
print "predictions_0:"
print accuracy_score(outcomes, predictions)

def predictions_1(data):
    predictions = []
    for _, passenger in data.iterrows():
        if passenger['Sex'] == 'male':
            predictions.append(0)
        else:
            predictions.append(1)
    return pd.Series(predictions)

predictions = predictions_1(data)
print "predictions_1:"
print accuracy_score(outcomes, predictions)


def predictions_2(data):
    predictions = []
    for _, passenger in data.iterrows():
        if passenger['Sex'] == 'female':
            predictions.append(1)
        elif passenger['Age'] < 10:
            predictions.append(1)
        else:
            predictions.append(0)
    return pd.Series(predictions)

predictions = predictions_2(data)
print "predictions_2:"
print accuracy_score(outcomes, predictions)

def predictions_3(data):
    predictions = []
    for _, passenger in data.iterrows():
        if passenger['Pclass'] < 3:
            if passenger['Age'] < 16:
                predictions.append(1)
                continue
        if passenger['Sex'] == 'female':
            if passenger['Pclass'] == 3 and passenger["Parch"] > 3 and passenger["Age"] > 10 and passenger["SibSp"] == 0:
                predictions.append(0)
            else:
                predictions.append(1)
        elif passenger['Age'] < 7:
            predictions.append(1)
        else:
            predictions.append(0)
    return pd.Series(predictions)

predictions = predictions_3(data)
print "predictions_3:"
print accuracy_score(outcomes, predictions)