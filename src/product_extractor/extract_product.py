import pandas as pd
from pandas.io.json import json_normalize
import math
import json


class ExtractProducts():
    def __init__(self, checkout_collection, bestseller_collection):
        # Injecting the collection dependencies into the constructor
        # So that we can later test it using mock objects.
        self.checkout_collection = checkout_collection
        self.bestseller_collection = bestseller_collection

    def get_checkout_data(self):
        checkout_data = self.checkout_collection.aggregate([
            {'$unwind': '$cart'},
            {'$match': {
                'cart.productID': {
                    '$exists': True
                }
            }}
        ])
        return list(checkout_data)

    def extract_most_sold_products(self):
        self.bestseller_collection.remove({})
        checkout_data = self.get_checkout_data()
        checkout_df = pd.DataFrame(
            json_normalize(checkout_data, max_level=1)
        )

        # Rename columns.
        checkout_df.rename(
            columns={
                'cart.productID': 'productID',
                'cart.category': 'category'
            },
            inplace=True
        )

        # Drop null values
        checkout_df.dropna(subset=['productID', 'category'])

        # Group data by product ID and category
        products = checkout_df[['productID', 'category']].groupby(
            ['productID', 'category']
        ).size().reset_index(name='counts')

        sorted_products = products.sort_values('counts', ascending=False)

        # Get top 20% of most sold products.
        top_20_percent_most_sold_products = sorted_products.iloc[
            :int(len(sorted_products)*(20/100))
        ]
        top_sold_products = json.loads(
            top_20_percent_most_sold_products.T.to_json()
        ).values()

        self.bestseller_collection.insert(top_sold_products)
        return top_sold_products
