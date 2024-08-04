import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
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

# Bar Chart using Plotly
def bar_chart(df):
    fig = px.bar(df.reset_index().melt(id_vars='index'),
                 x='index', y='value', color='variable',
                 barmode='group',
                 template='plotly_dark')
    return fig

# Pie Chart using Plotly
def pie_chart(df):
    total_statuses = df.sum().reset_index()
    total_statuses.columns = ['Status', 'Count']
    fig = px.pie(total_statuses, names='Status', values='Count', template='plotly_dark')
    return fig

# Line Chart using Plotly
def line_chart(df):
    fig = px.line(df.T, template='plotly_dark')
    return fig

# Scatter Plot using Plotly
def scatter_plot(df):
    fig = px.scatter(df.reset_index().melt(id_vars='index'),
                     x='variable', y='value', color='index',
                     template='plotly_dark')
    return fig

# Heatmap using Plotly
def heatmap(df):
    fig = px.imshow(df, text_auto=True, aspect="auto", template='plotly_dark')
    return fig

# Histogram using Matplotlib
def histogram(df):
    plt.figure(figsize=(10, 6))
    df.plot(kind='hist', alpha=0.7)
    plt.title('Histogram of Task Counts')
    plt.xlabel('Task Counts')
    plt.ylabel('Frequency')
    st.pyplot(plt)

# Box Plot using Plotly
def box_plot(df):
    fig = px.box(df.reset_index().melt(id_vars='index'),
                 x='variable', y='value', color='index',
                 template='plotly_dark')
    return fig

# Area Chart using Matplotlib
def area_chart(df):
    plt.figure(figsize=(10, 6))
    df.plot(kind='area', alpha=0.4)
    plt.title('Area Chart of Task Counts')
    plt.xlabel('Project')
    plt.ylabel('Task Counts')
    st.pyplot(plt)

# Violin Plot using Plotly
def violin_plot(df):
    fig = px.violin(df.reset_index().melt(id_vars='index'),
                    y='value', x='variable', color='index',
                    box=True, points='all',
                    template='plotly_dark')
    return fig

st.title("Chart Types Demo with Simulated Jira Data")

st.header("Radar Chart - Project Completion States")
st.plotly_chart(radar_chart(df))

st.header("Bar Chart - Project Completion States")
st.plotly_chart(bar_chart(df))

st.header("Pie Chart - Total Task Distribution")
st.plotly_chart(pie_chart(df))

st.header("Line Chart - Task Distribution Over Statuses")
st.plotly_chart(line_chart(df))

st.header("Scatter Plot - Task Distribution")
st.plotly_chart(scatter_plot(df))

st.header("Heatmap - Task Distribution")
st.plotly_chart(heatmap(df))

st.header("Histogram - Task Counts")
histogram(df)

st.header("Box Plot - Task Distribution")
st.plotly_chart(box_plot(df))

st.header("Area Chart - Task Counts Over Projects")
area_chart(df)

st.header("Violin Plot - Task Distribution")
st.plotly_chart(violin_plot(df))

