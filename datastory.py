import plotly.express as px
import pandas as pd
import csv

from google.colab import files
dataToLoad = files.upload()

df = pd.read_csv("data.csv")
fig = px.scatter(df, y = "quant_saved", title = "Qty of Money($) saved by women", color = "female")
fig.show()

import csv

with open('data.csv', newline="") as f:
  reader = csv.reader(f)
  savingsData = list(reader)

savingsData.pop(0)

totalPeople = len(savingsData)
reminderCounter = 0
for i in savingsData:
  if int(i[3]) == 1:
    reminderCounter += 1

import plotly.graph_objects as go

fig = go.Figure(go.Bar(x=["Reminded", "Not Reminded"], y=[reminderCounter, (totalPeople - reminderCounter)]))

fig.show()

import seaborn as sns

sns.boxplot(data = df, x = df["quant_saved"])

q1 = df["quant_saved"].quantile(0.25)
q2 = df["quant_saved"].quantile(0.75)
IQR = q2 - q1

print(f"Q1 - {q1}")
print(f"Q2 - {q2}")
print(f"IQR - {IQR}")

lowerValue = q1 - (1.5 * IQR)
higherValue = q2 + (1.5 * IQR)

print(f"The lower half is - {lowerValue}")
print(f"The higher half is - {higherValue}")

newDataSet = df[df["quant_saved"] < higherValue]

import statistics
import plotly.figure_factory as ff

savingsData = newDataSet["quant_saved"].tolist()

Mean = statistics.mean(savingsData)
Median = statistics.median(savingsData)
Mode = statistics.mode(savingsData)
StdDev = statistics.stdev(savingsData)

print("The Mean of the Data Set is:", Mean)
print("The Median of the Data Set is:", Median)
print("The Mode of the Data Set is:", Mode)
print("The Standard Deviation of the Data Set is:", StdDev)

fig = ff.create_distplot([savingsData], ["Savings"], show_hist = False)
fig.show()

import random 
import plotly.graph_objects as go

samplingMean = []

for i in range(0,1000):
  tempList = []
  for j in range(0,100):
    tempList.append(random.choice(savingsData)) 
  samplingMean.append(statistics.mean(tempList))

meanSampling = statistics.mean(samplingMean)

print("The mean sampling is: ", meanSampling)

fig = ff.create_distplot([samplingMean] , ["Savings"] , show_hist = False)
fig.add_trace(go.Scatter(x = [meanSampling, meanSampling], y = [0,0.1], mode = "lines", name = "MEAN"))
fig.show()