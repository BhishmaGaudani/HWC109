import random
from tracemalloc import start
from unicodedata import name
from unittest import result
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import csv
import pandas as pd

df=pd.read_csv("data.csv")
MathScore_list=df["math score"].tolist()
ReadingScore_list=df["reading score"].tolist()

mean=statistics.mean(ReadingScore_list)
mode=statistics.mode(ReadingScore_list)
median=statistics.median(ReadingScore_list)
SD=statistics.stdev(ReadingScore_list)

SD1_start,SD1_ends=mean-SD,mean+SD
SD2_start,SD2_ends=mean-(2*SD),mean+(2*SD)
SD3_start,SD3_ends=mean-(3*SD),mean+(3*SD)

print("mean :",mean ,
"mode :",mode ,
"median :",median ,
"Standard deviatation :",SD)

list_of_data_in_oneSD=[result for result in ReadingScore_list if result>SD1_start and result<SD1_ends]
list_of_data_in_twoSD=[result for result in ReadingScore_list if result>SD2_start and result<SD2_ends]
list_of_data_in_thirdSD=[result for result in ReadingScore_list if result>SD3_start and result<SD3_ends]
print("{}% of data lies between 1 standard deviaiton ".format(len(list_of_data_in_oneSD)*(100)/len(ReadingScore_list)))
print("{}% of data lies between 3 standard deviaiton ".format(len(list_of_data_in_twoSD)*(100)/len(ReadingScore_list)))
print("{}% of data lies between 3 standard deviaiton ".format(len(list_of_data_in_thirdSD)*(100)/len(ReadingScore_list)))

fig=ff.create_distplot([ReadingScore_list],["result"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[SD1_start,SD1_start],y=[0,0.17],mode="lines",name="STANDARD DEVIATATION 1"))
fig.add_trace(go.Scatter(x=[SD2_start,SD2_start],y=[0,0.17],mode="lines",name="STANDARD DEVIATATION 2"))
fig.add_trace(go.Scatter(x=[SD3_start,SD3_start],y=[0,0.17],mode="lines",name="STANDARD DEVIATATION 3"))

fig.add_trace(go.Scatter(x=[SD1_ends,SD1_ends],y=[0,0.17],mode="lines",name="STANDARD DEVIATATION 1"))
fig.add_trace(go.Scatter(x=[SD2_ends,SD2_ends],y=[0,0.17],mode="lines",name="STANDARD DEVIATATION 2"))
fig.add_trace(go.Scatter(x=[SD3_ends,SD3_ends],y=[0,0.17],mode="lines",name="STANDARD DEVIATATION 3"))
fig.show()
