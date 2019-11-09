from flask import jsonify, current_app as app
from . import bp
from .check_if_best_seller import BestSeller
from pymongo import MongoClient

# Connect to default local instance of mongo
client = MongoClient()


@bp.route('/', methods=['GET'])
def home():
    return 'home'


@bp.route('/checkifbestseller/<product_id>', methods=['GET'])
def checkifbestseller(product_id):
    db = client[app.config["DB_NAME"]]
    bestseller_collection = db.bestseller
    best_seller = BestSeller(bestseller_collection)
    best_seller_product = best_seller.get_product(product_id)

    return jsonify(best_seller_product)
