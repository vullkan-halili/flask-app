class BestSeller():
    def __init__(self, bestseller_collection):
        # Injecting the collection dependency into the constructor
        # So that we can later test it using mock objects.
        self.bestseller_collection = bestseller_collection

    def get_product(self, product_id):
        best_seller = self.bestseller_collection.find_one(
            {'productID': product_id}
        )

        return self.make_best_seller_object(best_seller)

    def make_best_seller_object(self, best_seller_obj=None):
        best_seller = {
            'productID': None,
            'totalSold': None,
            'category': None
        }
        if best_seller_obj:
            best_seller['productID'] = best_seller_obj['productID']
            best_seller['totalSold'] = best_seller_obj['counts']
            best_seller['category'] = best_seller_obj['category']

        return best_seller
