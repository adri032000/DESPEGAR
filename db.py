from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

class MongoDriver:
    def _init_(self):

        user = os.getenv('MONGO_USER')
        password = os.getenv('MONGO_PASSWORD')
        hostname = os.getenv('MONGO_HOSTNAME')

        uri = f"mongodb+srv://{user}:{password}@{hostname}/?retryWrites=true&w=majority"

        # Create a new client and connect to the server
        self.client = MongoClient(uri, server_api=ServerApi('1'))
        # Send a ping to confirm a successful connection

    def insert_record(self, record: dict, username: str):
        self.client.get_database('db_ADRIANA').get_collection(f'{username}_Raquetas').insert_one(record)


    def test_connection(self):
        try:
            self.client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)


if __name__ == "_main_":
    mi_base_de_datos = MongoDriver()
    mi_base_de_datos.insert_record(record={
        "Marca": "Babolat",
        "Detalles": {
            "Serie":"Nadal",
            "Fechayhora": datetime.now(),
            "Incidencias":[
                "Rota una cuerda",
                "Tape del mango desgastado"
            ]
        },
        "Precio": 100,
        "Cuerdas": "Negras"}, username="Adriana")