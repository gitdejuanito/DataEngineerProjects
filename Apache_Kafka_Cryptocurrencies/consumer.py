from confluent_kafka import Consumer
import csv
import json
import time

#kafka consumer configuration
topic_name = 'cryptodata'
group_id = 'grupocrypto'

consumer_conf = {'bootstrap.servers': 'localhost:9092', 'group.id': group_id, 'auto.offset.reset': 'earliest'}
consumer = Consumer(consumer_conf)
consumer.subscribe([topic_name])

#CSV file name
csv_file_path = 'crypto_precios.csv'


with open(csv_file_path, 'w', newline='') as csv_file:
    # create an object with DictWriter
    writer = csv.DictWriter(csv_file, fieldnames=['timestamp',  'name', 'symbol', 'price'])

    #  write column names if the file does not exist
    if not csv_file.tell():
        writer.writeheader()
 
    #consume kafka messages and write them in the CSV file
    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                print('Error: {}'.format(msg.error()))
                continue

            row = json.loads(msg.value())
            writer.writerow(row)
            print(f"DATA RECEIVED AND LOADED IN THE FILE {csv_file_path}")


    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()
        print("Consumer closed. |Final data loaded in the csv file")
        time.sleep(2)
    