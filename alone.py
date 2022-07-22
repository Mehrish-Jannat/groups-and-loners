import pandas as pd
import plotly.graph_objects as go
data = pd.read_csv("https://raw.githubusercontent.com/whitehatjr/Data-Analysis-by-visualisation/master/data.csv")
student = data.loc[data["student_id"]=="TRL_zet"]
print(student.groupby("level")["attempt"].mean())
graph = go.Figure(go.Bar(x = student.groupby("level")["attempt"].mean(), y = ["Level 1","Level 2","Level 3","Level 4"],orientation = "h"))
graph.show()