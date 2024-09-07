import streamlit as st
import pandas as pd
import time
from datetime import datetime
from streamlit_autorefresh import st_autorefresh
import os

# Get the current timestamp
ts = time.time()
date = datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
timestamp = datetime.fromtimestamp(ts).strftime("%H:%M-%S")

# Auto-refresh FizzBuzz counter
count = st_autorefresh(interval=2000, limit=100, key="fizzbuzzcounter")

if count == 0:
    st.write("Count is zero")
elif count % 3 == 0 and count % 5 == 0:
    st.write("FizzBuzz")
elif count % 3 == 0:
    st.write("Fizz")
elif count % 5 == 0:
    st.write("Buzz")
else:
    st.write(f"Count: {count}")

# Define the path to the attendance CSV file
csv_path = f"Attendance/Attendance_{date}.csv"

# Check if the CSV file exists before attempting to read it
if os.path.exists(csv_path):
    df = pd.read_csv(csv_path)
    st.dataframe(df.style.highlight_max(axis=0))
else:
    st.write(f"No attendance file found for {date}.")
