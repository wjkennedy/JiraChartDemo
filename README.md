# Jira Chart Demo

## Because you have options in Python and EazyBI isn't synonomous with Easy ROI.

Sure, here's a detailed README for the Streamlit app that you can use to highlight the benefits of using Python for charting Jira data compared to paid marketplace add-ons.

## Overview

This Streamlit application demonstrates various chart types using Plotly and Matplotlib, leveraging simulated Jira data. The goal is to showcase the capabilities of the zero-cost, highly capable Python application stack for visualizing project data, as opposed to investing in expensive marketplace add-ons with limited ROI.

## Features

- **Radar Chart**: Visualizes the state of completion for various projects.
- **Bar Chart**: Displays project completion states.
- **Pie Chart**: Shows total task distribution across different statuses.
- **Line Chart**: Plots task distribution over statuses.
- **Scatter Plot**: Illustrates task distribution across projects and statuses.
- **Heatmap**: Represents task distribution in a heatmap format.
- **Histogram**: Displays the frequency of task counts.
- **Box Plot**: Shows the distribution of task counts.
- **Area Chart**: Visualizes task counts over projects.
- **Violin Plot**: Represents task distribution with a violin plot.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repository/jira-data-visualization.git
   cd jira-data-visualization
   ```

2. **Install the required packages**:
   ```bash
   pip install streamlit plotly matplotlib pandas numpy
   ```

## Running the Application

1. **Save the script**: Ensure the `demo3.py` file is in your working directory.
2. **Run the Streamlit app**:
   ```bash
   streamlit run demo3.py
   ```

## Simulated Jira Data

The application simulates Jira data for various projects with different statuses. The data is generated randomly for demonstration purposes.

## Code Structure

- **Data Simulation**: Generates random data for projects and their statuses.
- **Chart Functions**: Contains functions to create various chart types using Plotly and Matplotlib.
- **Streamlit App**: Integrates all charts into a Streamlit application for interactive visualization.

## Usage

1. **Radar Chart**: Visualizes the state of completion for various projects.
2. **Bar Chart**: Displays project completion states in a bar format.
3. **Pie Chart**: Shows the total distribution of tasks across different statuses.
4. **Line Chart**: Plots the distribution of tasks over different statuses.
5. **Scatter Plot**: Illustrates the distribution of tasks across projects and statuses.
6. **Heatmap**: Represents task distribution as a heatmap.
7. **Histogram**: Displays the frequency distribution of task counts.
8. **Box Plot**: Shows the distribution of task counts.
9. **Area Chart**: Visualizes task counts over different projects.
10. **Violin Plot**: Represents the distribution of task counts with a violin plot.

## Advantages

- **Cost-effective**: Utilize the powerful Python ecosystem without incurring additional costs for marketplace add-ons.
- **Highly Capable**: Leverage advanced charting libraries like Plotly and Matplotlib.
- **Customizable**: Tailor the visualizations to meet specific needs and requirements.
- **Interactive**: Benefit from Streamlit's interactive capabilities to explore data in real-time.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
