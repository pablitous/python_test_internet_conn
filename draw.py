import pandas as pd
import matplotlib.pyplot as plt

working_folder = "F:/desarrollo/python_test_internet_conn/"

df = pd.read_csv(f'{working_folder}internet_connection_data.csv', names=['Timestamp', 'InternetStatus'])
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

df['Minute'] = df['Timestamp'].dt.minute
df['Hour'] = df['Timestamp'].dt.hour
df['Day'] = df['Timestamp'].dt.day
df['Month'] = df['Timestamp'].dt.month
df['Year'] = df['Timestamp'].dt.year

paginate_hours = 18
# Plotting function with pagination
def plot_data(time_interval):
    if time_interval == 'Minute':
        grouped_data = df.groupby(['Year', 'Month', 'Day', 'Hour', 'Minute'])['InternetStatus'].value_counts().unstack().fillna(0)
    elif time_interval == 'Hour':
        grouped_data = df.groupby(['Year', 'Month', 'Day', 'Hour'])['InternetStatus'].value_counts().unstack().fillna(0)
    elif time_interval == 'Day':
        grouped_data = df.groupby(['Year', 'Month', 'Day'])['InternetStatus'].value_counts().unstack().fillna(0)
    else:
        grouped_data = df.groupby([time_interval])['InternetStatus'].value_counts().unstack().fillna(0)

    # Calculate the number of subplots needed for 48-hour intervals
    num_subplots = len(grouped_data) // paginate_hours + 1

    for i in range(num_subplots):
        start_idx = i * paginate_hours
        end_idx = (i + 1) * paginate_hours

        # Extract data for the current 48-hour interval
        subset_data = grouped_data.iloc[start_idx:end_idx]

        # Create a subplot
        plt.figure(figsize=(10, 6))
        subset_data.plot(kind='bar', stacked=True)
        
        plt.title(f'Internet Connectivity Status Grouped by {time_interval} - Hours {start_idx}-{end_idx}')
        plt.xlabel(time_interval)
        plt.ylabel('Connection Count')
        plt.show()

# Examples
#plot_data('Minute')
plot_data('Hour')
#plot_data('Day')
#plot_data('Month')
#plot_data('Year')
