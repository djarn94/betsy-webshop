import models
import os

"""
Use this file to create/delete a database for testing your functions in main.py.
Be sure to delete the database before running wincpy check.
Alternatively you can use :memory: in models.py to prevent wincpy from using your database.
"""


def main():
    """
    Comment out the fuction you are not using and run the file.
    """
    setup_data()
    #delete_database()


def setup_data():
    """
    Creates the database and fills it with data.
    """
    models.db.connect()
    models.db.create_tables(
        [
            models.User,
            models.Product,
            models.Transaction,
        ]
    )

    user_data = [
        (#name, address data, billing info
            ("Noraly", "longstreet 10", 'rabo001'),
            [#products owned
                ("papercards", 'handmade cards',['paper', 'handmade', 'card'], 3.5, 100),
                ("facemask", 'green camo face mask',['green','camo','facemask'], 10, 250),
            ],
        ),
        (
            ("Oi", "trollstreet 37", 'oink017'),
            [
                ("shovel", "handmade survival shovel",['handmade','survival','shovel'], 8 , 50),
                ("iron lock", 'homemade iron lock with key',['homemade','lock','iron'], 10, 25),
            ],
        ),
        (
            ("Errol","romanalley 102", 'ing117'),
            [
                ("wooden table", 'homemade wooden table',['homemade','wood','table'], 250, 30),
                ("deer horn", 'a handmade deer horn',['handmade','deer','wildlife','horn'], 35, 20),
            ],
        ),
        (
            ("Jara","riverroad 44", 'tour223'),
            [
                ("black sweater", 'Medium sized black coloured sweater',['medium','black','sweater'], 25, 150),
                ("mini cat statue", 'mini cat statues made from stone',['mini','statue','cat','stone'], 75, 10),
            ],
        ),
    ]

    for user, products in user_data:
        user2 = models.User.create(
            name=user[0],
            address=user[1],
            billing=user[2],
        )
        for product_data in products:
            product_source = models.Product.create(
                product =product_data[0],
                description = product_data[1],
                tags = product_data[2],
                price= product_data[3],
                amount = product_data[4],
                user_id = user2
            )

def delete_database():
    """
    Delete the database.
    """
    cwd = os.getcwd()
    database_path = os.path.join(cwd, "database.db")
    if os.path.exists(database_path):
        os.remove(database_path)


if __name__ == "__main__":
    main()
