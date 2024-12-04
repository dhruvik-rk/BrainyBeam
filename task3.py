# Create a pandas DataFrame from a JSON object with nested structures.


#import necessary libraries:
import pandas as pd

#json data
json_data = [
    {
        "id": 1,
        "name": "Sagar Jasani",
        "address": {
            "street": "123 Abc St",
            "city": "Ahmedabad",
            "zipcode": "300001"
        },
        "orders": [
            {
                "order_id": 101,
                "amount": 250,
                "date": "2024-11-10"
            },
            {
                "order_id": 102,
                "amount": 150,
                "date": "2024-11-12"
            }
        ],
        "contacts": [
            {
                "type": "email",
                "value": "sagarjasani@brainybeam.com"
            },
            {
                "type": "phone",
                "value": "01234-56789"
            }
        ]
    },
    {
        "id": 2,
        "name": "Harry Patel",
        "address": {
            "street": "456 Def St",
            "city": "Rajkot",
            "zipcode": "300002"
        },
        "orders": [
            {
                "order_id": 103,
                "amount": 250,
                "date": "2024-11-13"
            },
            {
                "order_id": 104,
                "amount": 150,
                "date": "2024-11-15"
            }
        ],
        "contacts": [
            {
                "type": "email",
                "value": "harrypatel@infotech.com"
            }
        ]
    },
    {
        "id": 3,
        "name": "Priyesh Kansara",
        "address": {
            "street": "789 Ghi St",
            "city": "Surat",
            "zipcode": "300003"
        },
        "orders": [
            {
                "order_id": 105,
                "amount": 250,
                "date": "2024-11-17"
            }
        ],
        "contacts": [
            {
                "type": "phone",
                "value": "98765-43210"
            }
        ]
    }
]

#normalize address, orders, contacts
df_address = pd.json_normalize(json_data)[['id', 'name', 'address.street', 'address.city', 'address.zipcode']]
df_orders = pd.json_normalize(json_data, 'orders', ['id', 'name'])
df_contacts = pd.json_normalize(json_data, 'contacts', ['id', 'name'])
        #concate value of email and contact in contact dataframe
df_contacts_combined = df_contacts.groupby(['id', 'name'])['value'].apply('|'.join)

#combine dataframes and print it
df_combined = df_orders.merge(df_address, on=['id', 'name']).merge(df_contacts_combined, on=['id', 'name'])
print(df_combined)