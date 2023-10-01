
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
user = os.getenv('MONGO_USER')
password = os.getenv('MONGO_PASSWORD')


uri = f"mongodb+srv://{user}:{password}@cluster0.pqm6abd.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

client .get_database('prueba').get_collection('BJ').insert_one(document={"Ciudad":"Quito","Velocidad viento":"16"})

client .get_database('prueba').get_collection('BJ').insert_one(document={"Tiempo":"soleado","Estación":"Verano"})