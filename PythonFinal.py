"""
Class: CS230--Section 3
Name: Michael Rosa
Description: Final Project
I pledge that I have completed the programming assignment 
independently. 
I have not copied the code from a student or any source.
I have not given my code to any student.
"""
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
trip_data = pd.read_csv('201501-hubway-tripdata.csv')
station_data = pd.read_csv('current_bluebikes_stations.csv', skiprows=1)  # Skip the first row

# Convert 'starttime' and 'stoptime' columns to datetime objects
trip_data['starttime'] = pd.to_datetime(trip_data['starttime'])
trip_data['stoptime'] = pd.to_datetime(trip_data['stoptime'])

# Streamlit Layout
st.title("Boston Blue Bikes Data Analysis")

# Dropdown for station selection
station_list = trip_data['start station name'].unique()
selected_station = st.selectbox("Select a Station", station_list)

# Function to calculate average, shortest, and longest trip duration
def calculate_duration_stats(station_name):
    relevant_trips = trip_data[trip_data['start station name'] == station_name]

    
    
    avg_duration = relevant_trips['tripduration'].mean()
    shortest_duration = relevant_trips['tripduration'].min()
    longest_duration = relevant_trips['tripduration'].max()
    
    return avg_duration, shortest_duration, longest_duration, relevant_trips
   




# Displaying the average, shortest, and longest duration
if st.button("Calculate Duration Stats"):
    result = calculate_duration_stats(selected_station)
    
    if result:
        avg_duration, shortest_duration, longest_duration, relevant_trips = result

        
        
       
        st.write(f"Average Duration for {selected_station}: {avg_duration:.2f} seconds")
        st.write(f"Shortest Duration for {selected_station}: {shortest_duration:.2f} seconds")
        st.write(f"Longest Duration for {selected_station}: {longest_duration:.2f} seconds")
    

# Visualization 1: Histogram of Trip Durations
st.subheader("Distribution of Trip Durations")

# Check if relevant_trips is defined
if 'relevant_trips' in locals():
    # Use Matplotlib to create the histogram
    plt.figure(figsize=(10, 6))
    plt.hist(relevant_trips['tripduration'], bins=50, color='skyblue', density=False, cumulative=False)
    plt.xlabel('Trip Duration (seconds)')
    plt.ylabel('Frequency')
    st.pyplot()
else:
    st.warning("Please calculate duration stats before attempting to visualize the distribution.")

# Visualization 2: Daily Rides Line Chart
st.subheader("Daily Rides Over Time")
trip_data['start_time'] = pd.to_datetime(trip_data['starttime'])

if not trip_data.empty:
    daily_rides = trip_data.resample('D', on='start_time').agg({
        'tripduration': 'count',
        'start station name': lambda x: x.mode().iloc[0] if not x.empty else None  # Most common start station
    })

    # Calculate average trip duration per day
    avg_duration_by_day = trip_data.groupby(trip_data['start_time'].dt.date)['tripduration'].mean()

    # Plotting the line chart
    fig, ax1 = plt.subplots(figsize=(10, 6))

    color = 'tab:red'
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Number of Rides', color=color)
    ax1.plot(daily_rides.index, daily_rides['tripduration'], color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
    color = 'tab:blue'
    ax2.set_ylabel('Average Trip Duration (seconds)', color=color)
    ax2.plot(avg_duration_by_day.index, avg_duration_by_day, color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()  # ensure no overlapping of the plots
    st.pyplot()

    # Display most common start station for each day
    st.subheader("Most Common Start Station by Day")
    st.table(daily_rides[['start station name']])
else:
    st.warning("No data available for visualization.")


# Map: Station Locations
station_data.rename(columns={'Latitude': 'LAT'}, inplace=True)
station_data.rename(columns={'Longitude': 'LON'}, inplace=True)

st.subheader("Station Locations")
st.map(station_data[['LAT', 'LON']])

# Data Analytics Capability: Top 5 Stations by Rides
st.subheader("Top 5 Stations by Number of Rides")
top_stations = trip_data['start station name'].value_counts().head(5)
st.table(top_stations)

# Data Analytics Capability: Average Trip Duration by Day of Week
st.subheader("Average Trip Duration by Day of Week")
trip_data['day_of_week'] = trip_data['start_time'].dt.day_name()
avg_duration_by_day = trip_data.groupby('day_of_week')['tripduration'].mean()
st.bar_chart(avg_duration_by_day)