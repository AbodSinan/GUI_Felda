__author__ = 'HotShot'
import pyrebase
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

config = {
    'apiKey' : 'AIzaSyC6AVSfidmgJtRioSQBgvP4nvv-qzy5XtU',
    "authDomain": "feldamobile-app.firebaseapp.com",
    "databaseURL": "https://feldamobile-app.firebaseio.com",
    "storageBucket": "feldamobile-app.appspot.com"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()
df= db.child('userProfile').get().val()

costs = []
item_costs = []
item_names = []
item_emails = []
item_dates = []
revenue = []
dates = []
emails = []
#getting list of events
for users,user_info in df.items():
    for user_key in user_info:
        for events, event_info in user_info['eventList'].items():
            emails.append(user_info['email'])
            costs.append(event_info['cost'])
            revenue.append(event_info['revenue'])
            dates.append(event_info['date'])
            if "itemList" in event_info:
                for item, item_info in event_info['itemList'].items():
                    item_costs.append(item_info['price'])
                    item_emails.append(user_info['email'])
                    item_names.append(item_info['name'])
                    item_dates.append(event_info['date'])

event_data = pd.DataFrame(
    {'email': emails,
     'cost': costs,
     'date': dates,
     'revenue': revenue
    })
item_data = pd.DataFrame(
    {'name': item_names,
     'cost': item_costs,
     'date': item_dates,
     'email': item_emails
    })
print(event_data.index)

item_data = item_data.sort_values(by='date')

p1 = plt.bar(event_data['date'], event_data['cost'])
p2 = plt.bar(event_data['date'], event_data['revenue'])
plt.show()