from flask import Flask, url_for, request, json, jsonify, abort
from user import User
from json import dumps
from dbUtils import DbUtils
#from bottle import response

app = Flask(__name__)
myUser = []

@app.route('/')
def api_root():
    return 'Seja bem-vindo!!!'


@app.route('/addfornecedor', methods = ['POST'])
def api_addfornecedor():
    if not request.json:
        abort(400)

    req_data = request.get_json()

    cnpj = req_data['cnpj']
    razaoSocial = req_data['razaosocial']
    telefone = req_data['telefone']
    endereco = req_data['endereco']
    contato = req_data['contato']
    fg_ativo = req_data['fg_ativo']
    
    dbUtils = DbUtils()

    if(dbUtils.addFornecedores(cnpj, razaoSocial, telefone, endereco, contato, fg_ativo)):
        result = {"result": "Fornecedor inserido com sucesso!!!"}
    else:
        result = {"result": "Problemas!!"}
    return jsonify(result)


@app.route('/getfornecedor')
def api_getfornecedordb():
    fornecedores = []
    dbUtils = DbUtils()
    fornecedoresData = dbUtils.getFornecedor()
    for r in fornecedoresData:
        a = {"id":r[0], "cnpj": r[1], "razão Social": r[2], "telefone":r[3], "endereço":r[4], "contato":r[5], "fg_ativo":r[6]}
        fornecedores.append(a)
    return jsonify(fornecedores)

@app.route('/addCategoria', methods = ['POST'])
def api_addCategoria():
    if not request.json:
        abort(400)

    req_data = request.get_json()

    titulocategoria = req_data['titulo']
    descricaocategoria = req_data['descricao']
    fg_ativo = req_data['fg_ativo']
    
    dbUtils = DbUtils()

    if(dbUtils.addCategoria(titulocategoria, descricaocategoria, fg_ativo)):
        result = {"result": "Categoria inserida com sucesso!!!"}
    else:
        result = {"result": "Problemas!!"}
    return jsonify(result)

@app.route('/getcategoria')
def api_getcategoria():
    categorias = []
    dbUtils = DbUtils()
    categoriaData = dbUtils.getCategorias()
    for r in categoriaData:
        a = {"id":r[0], "título": r[1], "descrição": r[2], "fg_ativo":r[3]}
        categorias.append(a)
    return jsonify(categorias)


@app.route('/addproduto', methods = ['POST'])
def api_addproduto():
    if not request.json:
        abort(400)

    req_data = request.get_json()

    id_fornecedor = req_data['id_fornecedor']
    id_categoria = req_data['id_categoria']
    nomeproduto = req_data['nome']
    descricaoproduto = req_data['descricao']
    valor_unitario = req_data['valor_unitario']
    quantidade = req_data['quantidade']
    quantidademinima = req_data['quantidade_minima']
    fg_ativo = req_data['fg_ativo']
    
    dbUtils = DbUtils()

    if(dbUtils.addProduto(id_fornecedor, id_categoria, nomeproduto, descricaoproduto, valor_unitario, quantidade, quantidademinima, fg_ativo)):
        result = {"result": "Produto inserido com sucesso!!!"}
    else:
        result = {"result": "Problemas!!"}
    return jsonify(result)


@app.route('/getprodutos')
def api_getprodutos():
    produtos = []
    dbUtils = DbUtils()
    produtosData = dbUtils.getProdutos()
    for r in produtosData:
        a = {"id":r[0], "id_fornecedor": r[1], "id_categoria": r[2], "nome": r[3], "descrição": r[4], "valor_unitário":r[5], "quantidade":r[6], "quantidade_minima":r[7], "fg_ativo":r[8]}
        produtos.append(a)
    return jsonify(produtos)


@app.route('/addvendedor', methods = ['POST'])
def api_addvendedor():
    if not request.json:
        abort(400)

    req_data = request.get_json()

    cpf = req_data['cpf']
    nome = req_data['nome']
    carteiratrabalho = req_data['carteiratrabalho']
    telefone = req_data['telefone']
    dataadmissao = req_data['data_admissao']
    fg_ativo = req_data['fg_ativo']

    dbUtils = DbUtils()

    if(dbUtils.addVendedores(cpf, nome, carteiratrabalho, telefone, dataadmissao, fg_ativo)):
        result = {"result": "Vendedor inserido com sucesso!!!"}
    else:
        result = {"result": "Problemas!!"}
    return jsonify(result)


@app.route('/getvendedor')
def api_getvendedor():
    vendedores = []
    dbUtils = DbUtils()
    vendedoresData = dbUtils.getVendedores()
    for r in vendedoresData:
        a = {"id":r[0], "cpf": r[1], "nome": r[2], "carteira_Trabalho":r[3], "telefone":r[4], "data_admissao":r[5], "fg_ativo":r[6]}
        vendedores.append(a)
    return jsonify(vendedores)


@app.route('/addvenda', methods = ['POST'])
def api_addvenda():
    if not request.json:
        abort(400)

    req_data = request.get_json()

    id_vendedor = req_data['id_vendedor']
    id_categoria = req_data['id_categoria']
    id_produto = req_data['id_produto']
    datavenda = req_data['data_venda']
    valortotal = req_data['valor_total']
    quantidade = req_data['quantidade']
    fg_ativo = req_data['fg_ativo']

    dbUtils = DbUtils()

    if(dbUtils.addVenda(id_vendedor, id_categoria, id_produto, datavenda, valortotal, quantidade, fg_ativo)):
        result = {"result": "Venda feita com sucesso!!!"}
    else:
        result = {"result": "Problemas!!"}
    return jsonify(result)


@app.route('/getvendas')
def api_getvendas():
    vendas = []
    dbUtils = DbUtils()
    vendasData = dbUtils.getVendas()
    for r in vendasData:
        a = {"id":r[0], "id_vendedor": r[1], "id_categoria": r[2], "id_produto":r[3], "datavenda":r[4], "valortotal":r[5], "quantidade":r[6], "fg_ativo":r[7]}
        vendas.append(a)
    return jsonify(vendas)

@app.route('/addcompra', methods = ['POST'])
def api_addcompra():
    if not request.json:
        abort(400)

    req_data = request.get_json()

    id_fornecedor = req_data['id_fornecedor']
    id_produto = req_data['id_produto']
    id_categoria = req_data['id_categoria']
    datacompra = req_data['data_compra']
    valortotal = req_data['valor_total']
    quantidade = req_data['quantidade']
    fg_ativo = req_data['fg_ativo']

    dbUtils = DbUtils()

    if(dbUtils.addCompra(id_fornecedor, id_produto, id_categoria, datacompra, valortotal, quantidade, fg_ativo)):
        result = {"result": "Compra feita com sucesso!!!"}
    else:
        result = {"result": "Problemas!!"}
    return jsonify(result)

@app.route('/getcompras')
def api_getcompras():
    compras = []
    dbUtils = DbUtils()
    comprasData = dbUtils.getCompras()
    for r in comprasData:
        a = {"id":r[0], "id_fornecedor": r[1], "id_produto": r[2], "id_categoria":r[3], "datacompra":r[4], "valortotal":r[5], "quantidade":r[6], "fg_ativo":r[7]}
        compras.append(a)
    return jsonify(compras)


if __name__ == '__main__':
    app.run()


