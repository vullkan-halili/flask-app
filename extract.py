from src import ExtractProducts
from pymongo import MongoClient
import configparser

client = MongoClient()
config = configparser.RawConfigParser()
config.read('config/application.cfg')


def extract_top_sold_products():
    db_name = config.get('main', 'DB_NAME')
    db = client[db_name]
    checkout_collection = db.checkout
    bestseller_collection = db.bestseller
    extract_products = ExtractProducts(
        checkout_collection,
        bestseller_collection
    )
    extract_products.extract_most_sold_products()


extract_top_sold_products()
