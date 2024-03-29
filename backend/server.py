from flask import Flask, request, jsonify
import products_dao
from mysql_connection import get_db_connection

app = Flask(__name__)

connection = get_db_connection()

@app.route("/getProducts", methods=["GET"])
def get_products():
    products = products_dao.get_all_products(connection)
    response = jsonify(products)
    response.headers.add("Access-Control-Allow-Origin", "*")

    return response


@app.route("/deleteProduct", methods=["POST"])
def delete_product():
    return_id = products_dao.delete_product(connection, request.form["product_id"])
    response = jsonify({
        "product_id": return_id,
    })
    response.headers.add("Access-Control-Allow-Origin", "*")

    return response









if __name__ == "__main__":
    print("Start flask server")
    app.run(port=5000)