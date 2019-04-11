from flask import Flask, url_for, request, json, jsonify
from client import Client
from product import Product
from sale import Sale

app = Flask(__name__)
myClient = []
myProduct = []
mySale = []

@app.route('/')
def api_root():
    return 'Seja bem-vindo!!!'


@app.route('/creatclient')
def api_creatclient():
    global myClient
    myClient.append(Client(1, "Joao"))
    myClient.append(Client(2, "Pedro"))
    myClient.append(Client(3, "Antonio"))
    res = {'status': 'ok'}
    return jsonify(res)

@app.route('/addClient', methods = ['POST'])
def api_newclient():
    global myClient
    req_data = request.get_json()

    id = req_data['id']
    nome = req_data['nome']

    new_client = Client(id, nome)
    myClient.append(new_client)
    res = {'status':'ok'}
    return jsonify(res)

@app.route('/addProduct', methods = ['POST'])
def api_newProduct():
    global myProduct
    req_data = request.get_json()

    id = req_data['id']
    nome = req_data['nome']
    price = req_data['price']

    new_product = Product(id,nome,price)
    myProduct.append(new_product)
    res = {'status':'ok'}
    return jsonify(res)

 
@app.route('/sale', methods = ['POST'])
def api_newSale():
    global mySale

    req_data = request.get_json()

    idClient = req_data['idClient']
    idProduct = req_data['idProduct']
    amount = req_data['amount']
    #price = req_data['price']
    #total = req_data['total']
    price = 0
    total = 0
    for elem in myProduct:
        if idProduct == elem.getProductId():
            price = elem.getProductPrice()
            total = int(amount)*int(price)
        else:
            print("Produto não esta cadastrado!!")
            break
    
    #total = int(amount)*int(price)
    #total2 = str(total)

    new_sale = Sale(idClient,idProduct,amount,price,str(total))
    mySale.append(new_sale)
    res = {'status':'ok'}
    return jsonify(res)


@app.route('/vendacliente/<id_client>', methods = ['GET'])
def api_vendaCliente(id_client):
    client = id_client
    payload = []
    content = {}

    for elem in mySale:
        if client == elem.getClientId():
            content = {'idCliente': str(elem.getClientId()),'[idProduto]': str(elem.getProductId()),
            '[amount]': elem.getSaleAmount(), '[total]': elem.getSaleTotal()}
            payload.append(content)
            content = {}
    
    res = json.dumps(payload)
    return jsonify(SaleList=res)
    
@app.route('/totalvendacliente/<id_client>', methods = ['GET'])
def api_totalvendaCliente(id_client):
    client = id_client
    payload = []
    content = {}
    total = 0

    for elem in mySale:
        if client == elem.getClientId():
            total = total + int(elem.getSaleTotal())
            content = {'idCliente': str(elem.getClientId()),'[totalGasto]': str(total)}
            payload.append(content)
            content = {}
            

    res = json.dumps(payload)
    return jsonify(SaleList=res)

@app.route('/listClients', methods = ['GET'])
def api_listClients():
    payload = []
    content = {}

    for elem in myClient:
        content = {'id': str(elem.getClientId()), '[nome]':elem.getClientNome()}
        payload.append(content)
        content = {}

    res = json.dumps(payload)

    return jsonify(ClientList=res)

if __name__ == '__main__':
    app.run()

