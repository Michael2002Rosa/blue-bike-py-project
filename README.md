🚲 Boston Blue Bikes Data Analysis
============

This interactive Streamlit web app analyzes and visualizes Boston's Blue Bikes (formerly Hubway) trip data. Built as a final project for CS230 (Programming with Python), it enables users to explore trends in bike usage across the city using real trip and station data.

![BlueBikeProjectDemo](https://github.com/user-attachments/assets/e424caa2-442f-4f5d-95d5-51d65352de92)


---
## Technologies Used

- Python

- Streamlit – for building the interactive web app

- Pandas – for data wrangling

- Matplotlib & Seaborn – for visualizations

- CSV Datasets – trip and station data from Blue Bikes/Hubway

---

## Features
- Station Selector: Choose a specific start station to explore ride statistics.
- Trip Duration Stats: Calculates average, shortest, and longest ride durations for a selected station.
- Histogram: Visualizes the distribution of trip durations using Matplotlib.
- Time Series Analysis: Daily line chart showing total rides and average duration over time.
- Geospatial Map: Displays current Blue Bikes station locations on an interactive map.
- Top 5 Stations: Lists the most popular starting stations.
- Weekly Trends: Visual bar chart of average trip durations by day of the week.


![User Features](https://i.imgur.com/owfBYkp.png)

![User Features 2](https://i.imgur.com/Z05ZthZ.png)


---

## Setup
1. Clone this repo:
```bash
git clone https://github.com/Michael2002Rosa/blue-bike-py-project
```

2. Install Dependencies:
```bash
pip install streamlit pandas matplotlib seaborn
```

3. Run Streamlit:
```bash
run streamlit PythonFinal.py
```


