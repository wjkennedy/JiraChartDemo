import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt

# Simulating Jira data
projects = ['Project A', 'Project B', 'Project C', 'Project D', 'Project E']
statuses = ['To Do', 'In Progress', 'In Review', 'Done']
np.random.seed(42)
data = np.random.randint(0, 100, size=(len(projects), len(statuses)))

# Creating a DataFrame
df = pd.DataFrame(data, columns=statuses, index=projects)

# Radar Chart using Plotly
def radar_chart(df):
    fig = px.line_polar(df.reset_index().melt(id_vars='index'),
                        r='value', theta='variable',
                        color='index', line_close=True,
                        template='plotly_dark')
    fig.update_traces(fill='toself')
    return fig

st.title("Chart Types Demo with Simulated Jira Data")

st.header("Radar Chart - Project Completion States")
st.plotly_chart(radar_chart(df))

# Placeholder for more charts
st.header("More Chart Types Coming Soon...")

