#import modules
from mysql_connection import get_db_connection

#####
#functions

def get_all_products(connection):
    
    cursor = connection.cursor()
    
    query = """
            SELECT
                pr.product_id,
                pr.name,
                pr.uom_id,
                uom.uom_name,
                pr.price_per_unit
            FROM products as pr
            INNER JOIN units_of_measure as uom ON uom.uom_id = pr.uom_id
            """

    cursor.execute(query)
    
    response = []
    
    for (product_id, name, uom_id, uom_name, price_per_unit) in cursor:
        response.append(
            {
                "product_id": product_id,
                "name": name,
                "uom_id": uom_id,
                "uom_name": uom_name,
                "price_per_unit": price_per_unit,
            }
        )
    
    return response


def insert_new_product(connection, product):
    
    cursor = connection.cursor()
    
    query = """
            INSERT INTO
                products (name, uom_id, price_per_unit)
                VALUES (%s, %s, %s)
            """
    data = (product["product_name"], product["uom_id"], product["price_per_unit"])
    
    cursor.execute(query, data)
    connection.commit()
    
    return cursor.lastrowid


def delete_product(connection, product_id):
    
    cursor = connection.cursor()
    
    query = (
                """
                DELETE FROM products
                WHERE product_id = 
                """
                + str(product_id)
    )

    cursor.execute(query)
    connection.commit()
    
    return cursor.lastrowid


def insert_new_customer(connection, customer):
    
    cursor = connection.cursor()
    
    query = """
            INSERT INTO
                customers (customer_name, phone_number, email)
                VALUES (%s, %s, %s)
            """
    data = (customer["customer_name"], customer["phone_number"], customer["email"])
    
    cursor.execute(query, data)
    connection.commit()
    
    return cursor.lastrowid


if __name__ == "__main__":
    connection = get_db_connection()
    
    #print(delete_product(connection, 7))
    
    #print(insert_new_product(connection, {
    #    "product_name": "dupa",
    #    "uom_id": "1",
    #    "price_per_unit": "14.55",
    #}))

    #print(insert_new_customer(connection, {
    #    "customer_name": "Stach",
    #    "phone_number": "888574598",
    #    "email": "abw123@cba.pl",
    #}))