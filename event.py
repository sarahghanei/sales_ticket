class Event:
    def __init__(self, id_event, name_event, date_event, time_event, place_event, cost_event, total_capacity,
                 mod_total_capacity, flag_event=1):
        self.id_event = id_event
        self.name_event = name_event
        self.date_event = date_event
        self.time_event = time_event
        self.place_event=place_event
        self.cost_event=cost_event
        self.total_capacity = total_capacity
        self.mod_total_capacity = mod_total_capacity
        self.flag_event = flag_event
    def create_event(self):

# this library is for work by csv file
import csv
# this library is for import correct date and time to csv file
from datetime import datetime

# this library is read a csv file in dataframe format
import pandas as pd
# use this library for colored code
from termcolor import colored

# we have a csv file at first and csv file have 2 static record that dont delete this first row is my attribute
# and second row is set first id and add them in future record
# load csv file
file_name = "events.csv"
# exception handling
try:
    df_events = pd.read_csv(file_name)
    # set id_event for index in csv file
    df_events_indexed = df_events.set_index("id_event", drop=True)
    # get info of one event from admin and add to csv file
    name_event = input("Enter title of event: ")
    # this while is for that we input correct answer to dataset
    while True:
        try:
            date_event = str(datetime.strptime(input('Enter date of event with this format 1399/08/26 : '),
                                               "%Y/%m/%d")).split()[0]
            break
        except ValueError:
            print("your date event is not valid please input with this format: 1399/08/26")
    while True:
        try:
            time_event = str(datetime.strptime(input('Enter time of event with this format 20:00 : '),
                                               "%H:%M")).split()[1]
            break
        except ValueError:
            print("your time event is not valid please input with this format", colored("20:00", "red"))
    place_event = input("Enter place of event: ")
    cost_event = input("Enter cost of event in Rial: ")
    total_capacity = input("Enter total capacity of event: ")
    # add data to csv file
    row = [[df_events_indexed.index[-1] + 1, name_event, date_event, time_event, place_event, cost_event,
            total_capacity, total_capacity, 1]]
    with open(file_name, 'a', newline='') as csv_events:
        # creating a csv writer object
        csv_writer = csv.writer(csv_events)
        # writing the data row
        csv_writer.writerows(row)
# if file not fount
except FileNotFoundError:
    print("you have not this file please create a file with name events.csv and set first "
          "row with this items (id_event,Name_event,Date_event,Time_event,"
          "place_event,Cost_event,Total_capacity,Mod_total_capacity,Flag_event)"
          "and second row with this item (0,) without parenthesis ")
print("yes")