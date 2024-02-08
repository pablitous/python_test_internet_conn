import time
import datetime
import csv
from ping3 import ping, verbose_ping


working_folder = "F:/desarrollo/python_test_internet_conn/"

def check_internet():
    target_host = '8.8.8.8'  # Use a reliable IP address, like Google's DNS server
    response = ping(target_host)
    return response is not None

def save_data(data):
    with open(f'{working_folder}internet_connection_data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

while True:
    internet_status = check_internet()
    current_time = datetime.datetime.now()
    data_to_save = [current_time, internet_status]
    save_data(data_to_save)
    time.sleep(5)
