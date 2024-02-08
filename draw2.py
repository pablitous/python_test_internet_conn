import pandas as pd
import plotly.express as px

# Set the working folder
working_folder = "F:/desarrollo/python_test_internet_conn/"
file_name = "internet_connection_data.csv"  # Replace with your actual file name
file_path = working_folder + file_name

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(file_path, header=None, names=['timestamp', 'internet_status'])

# Convert the timestamp column to datetime format
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Map colors to True/False values
color_map = {True: 'Up', False: 'Down'}
df['status'] = df['internet_status'].map(color_map)

freq = '1H'

df_grouped = df.groupby([pd.Grouper(key='timestamp', freq=freq), 'status']).size().unstack(fill_value=0)

# Plot the stacked bar graph using Plotly
fig = px.bar(df_grouped, x=df_grouped.index, y=['Up', 'Down'],
             color_discrete_map={'Up': 'green', 'Down': 'red'},
             title=f'Internet Connection Status Every {freq}',
             labels={'timestamp': 'Time', 'value': 'Connection Count', 'variable': 'Connection Status'},
             width=1600, height=800,
             )


# Show the plot
fig.show()
