import csv
import plotly.graph_objects as go 
import pandas as pd 

df=pd.read_csv("data.csv")
grouped=df.groupby("level")["attempt"].mean()
print(grouped)

fig=go.Figure(go.Scatter(x=grouped,y=["Level 1","Level 2","Level 3","Level 4"]))
fig.show()