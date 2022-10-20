#  ACTIVIDAD REST API
#David Sanchez - Ficha: 2502640

from flask import Flask, jsonify, request

app = Flask(__name__)

from items import items

@app.route('/items')
def getitems():
    return jsonify(items)


@app.route('/items/<string:product_name>')
def getProduct(product_name):
    itemsFound = [product for product in items if product['name'] == product_name]

    if (len(itemsFound) > 0):
        return jsonify({"product": itemsFound[0]})
    return jsonify({"Message": "Product not found"}) 

@app.route('/items', methods=['POST'])
def addProduct():
    new_product = {
        "name": request.json['name'],
        "price": request.json['price'],
        "quantity": request.json['quantity']
    }
    items.append(new_product)
    return jsonify({'message': "product added succesfully", "items":items})

@app.route('/items/<string:product_name>', methods=['PUT'])
def updateProduct(product_name):
    productFound = [product for product in items if product['name'] == product_name]
    if (len(productFound) > 0):
        productFound[0]['name'] = request.json['name']
        productFound[0]['price'] = request.json['price']
        productFound[0]['quantity'] = request.json['quantity']
        return jsonify({
            "message": "Product Updated",
            "product": productFound[0]
        })
    return jsonify({"message": "Product Not Found"})

@app.route('/items/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
    itemsFound=[product for product in items if product['name'] == product_name]
    if len(itemsFound) > 0:
        items.remove(itemsFound[0])
        return jsonify({
            "message": "Product deleted succesfully",
            "items": items
        })
    return jsonify({"message": "product not found"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=4000)