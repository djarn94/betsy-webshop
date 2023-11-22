# Do not modify these lines
__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

# Add your code after this line
from datetime import datetime
from peewee import *
from models import *
from typing import List

def search(term) -> Product:
    result = []
    try :
        for item in Product.select().where(Product.product.contains(term)) or Product.select().where(Product.description.contains(term)):
            result.append(item.product)
    except:
        return print("search cannot be blank try again")
    
    result.sort()
    return print(result)

def list_user_products(user_id):
    result = []
    try :
        for item in Product.select().where(Product.user_id == user_id):
            result.append(item.product)
    except:
        return print("no results found")
    return print(result)


def list_products_per_tag(tag_id):
    result = []
    try:
        for item in Product.select().where(Product.tags.contains(tag_id)):
            result.append(item.product)
    except:
        return print("no product found with given tag.")
    return print(result)
    


def add_product_to_catalog(user_id1, product):
    return Product.update(user_id = user_id1).where(Product.product == product).execute()
        
        

def update_stock(product_id, new_quantity):
    for product in Product.select():
        if product.id == product_id:
            return Product.update(amount = new_quantity).where(Product.product == product.product).execute()


def purchase_product(product_id, buyer_id, quantity):

    user_list = []
    date = datetime.today()
    for user in User.select():
        user_list.append(user.id)
        
    for product in Product.select():
            try:
                if buyer_id in user_list:
                    if product.id == product_id:
                        if product.amount >= quantity:
                            Transaction.insert(
                            {'buyer_id' : buyer_id,
                            'seller_id' : product.user_id,
                            'product_name' : product.product,
                            'amount' : quantity,
                            'transaction_date' : date
                            }).execute()
                            new_amount = product.amount - quantity
                            return Product.update(amount = new_amount).where(Product.product == product.product).execute()
                        else:
                            return print('not enough stock')
                else:
                    return print('buyer id does not exist.')

            except:
                return print('something went wrong please try again')




def remove_product(product_id):

    product_list = []
    for product in Product.select():
        product_list.append(product.id)

    try:
        if product_id in product_list:
            Product.update(user_id = "").where(Product.id == product_id).execute()
        else:
            return print('that product id does not exist try another please')
    except:
        return print("something went wrong, did you fill in a number?")

if __name__ == "__main__":
    search('andmade')
    list_user_products(4)
    list_products_per_tag('homemade')
    update_stock(1, 200)
    purchase_product(7,2,40)
    remove_product(8)
    add_product_to_catalog(3,'mini cat statue')
