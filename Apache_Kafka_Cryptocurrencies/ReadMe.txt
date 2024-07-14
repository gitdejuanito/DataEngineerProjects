Cryptocurrencies 


Hi ! This is a small Project using Apache Kafka and Power BI, to visualize in real time the Price of some of the most important cryptocurrencies.

I used some of the basic concepts of Apache Kafka using a PRODUCER and CONSUMER scripts to extract the Price of the cryptocurrencies EVERY 30 seconds, due to the free API of Coincap just return the prices every 30 seconds, and then load the records into a CSV file.

Here are the links of the Price sources:
https://coincap.io/
https://docs.coincap.io/


Finally, I used PowerBi to have a table and a visualization of the prices. I load the CSV file to PowerBI and every 30 seconds you can refresh the data and the prices will change.


NOTE: For refreshing the data, everytime we need to run producer and consumer scripts
