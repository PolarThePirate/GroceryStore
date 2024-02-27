import mysql.connector
# global variable
__cnx = None


def get_db_connection():
    global __cnx
    if __cnx is None:
        __cnx = mysql.connector.connect(user='root', password='singer6-enrich-unvaried-poplar',
                                        host='127.0.0.1',
                                        database='grocery_store')
    return __cnx

if __name__ == "__main__":
    get_db_connection()