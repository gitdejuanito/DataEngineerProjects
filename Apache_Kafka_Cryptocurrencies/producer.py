#libreries
from confluent_kafka import Producer
import requests
import json
import time
from datetime import datetime



#Which crypto we are going to follow
cryptos_to_track = ['bitcoin', 'ethereum', 'ripple', 'litecoin', 'bnb', 'solana', 'stellar', 'eos', 'tron', 'avalanche']

#URL OF THE COINCAP API
api_url = 'https://api.coincap.io/v2/assets'

# KAFKA CONFIGURATION
producer_conf = {'bootstrap.servers': 'localhost:9092'}
producer = Producer(producer_conf)
topic_name = 'cryptodata'

while True:
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        # VERIFY THE RESPONSE
        if 'data' in data and isinstance(data['data'], list):
            #CREATE A LIST OF DICTIONARIES WITH THE INFORMATION
            rows = [{'timestamp': datetime.fromtimestamp(int(time.time())).strftime('%Y-%m-%d %H:%M:%S'), 
                     'name': crypto['name'], 
                     'symbol': crypto['symbol'], 
                     'price': crypto['priceUsd']} 
                     for crypto in data['data'] if crypto['id'] in cryptos_to_track]
            
            # SEND DATA TO KAFKA
            for row in rows:
                producer.produce(topic_name, value=json.dumps(row))

            producer.flush()

            print(" Data send successfully")
        
        else:
            print("RESPONSE NOT CORRECT ")
        
    else:
        print(f"FAILURE TO CONNECT WITH THE API. FAILURE CODE: {response.status_code}")

    time.sleep(30)