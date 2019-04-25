from sqlalchemy import create_engine


class DbUtils:
    db_string = "postgresql+psycopg2://postgres:1234@localhost/asa"
    db_query = ""

    def createTable(self):
        db = create_engine(self.db_string)
        self.db_query = "CREATE TABLE cadastro.usuarios(id_usuario SERIAL PRIMARY KEY, nome VARCHAR(60), idade INT, cidade VARCHAR(40));"
        try:
            db.execute(self.db_query)
            res = True
        except:
            print("Problemas ao criar a tabela\n")
            res = False
        return res

    def addFornecedores(self, cnpj, razaoSocial, telefone, endereco, contato, fg_ativo):
        db = create_engine(self.db_string)
        try:
            db.execute("INSERT INTO sistema.tb_fornecedores(cnpj, razaosocial, telefone, endereco, contato, fg_ativo ) VALUES (%s, %s, %s, %s, %s, %s)", cnpj, razaoSocial, telefone, endereco, contato, fg_ativo)
            res = True
        except:
            print("Problemas ao inserir na tabela usuário\n")
            res = False
        return res


    def addCategoria(self, titulocategoria, descricaocategoria, fg_ativo):
        db = create_engine(self.db_string)
        try:
            db.execute("INSERT INTO sistema.tb_categorias(titulocategoria, descricaocategoria, fg_ativo ) VALUES (%s, %s, %s)", titulocategoria, descricaocategoria, fg_ativo)
            res = True
        except:
            print("Problemas ao inserir na tabela usuário\n")
            res = False
        return res

    def addProduto(self, id_fornecedor, id_categoria, nomeproduto, descricaoproduto, valor_unitario, quantidade, quantidademinima, fg_ativo):
        db = create_engine(self.db_string)
        try:
            db.execute("INSERT INTO sistema.tb_produtos(id_fornecedor, id_categoria, nomeproduto, descricaoproduto, valor_unitario, quantidade, quantidademinima, fg_ativo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", id_fornecedor, id_categoria, nomeproduto, descricaoproduto, valor_unitario, quantidade, quantidademinima, fg_ativo)
            res = True
        except:
            print("Problemas ao inserir na tabela usuário\n")
            res = False
        return res
    
    
    def addNovoUsuario(self, nome, idade, cidade):
        db = create_engine(self.db_string)
        try:
            db.execute("INSERT INTO cadastro.usuarios(nome, idade, cidade) VALUES (%s,%s,%s)", nome, idade, cidade)
            res = True
        except:
            print("Problemas ao inserir na tabela usuário\n")
            res = False
        return res

    def addVendedores(self, cpf, nome, carteiratrabalho, telefone, dataadmissao, fg_ativo):
        db = create_engine(self.db_string)
        try:
            db.execute("INSERT INTO sistema.tb_vendedores(cpf, nome, carteiratrabalho, telefone, dataadmissao, fg_ativo) VALUES (%s,%s,%s,%s,%s,%s)", cpf, nome, carteiratrabalho, telefone, dataadmissao, fg_ativo)
            res = True
        except:
            print("Problemas ao inserir na tabela usuário\n")
            res = False
        return res

    def addVenda(self, id_vendedor, id_categoria, id_produto, datavenda, valortotal, quantidade, fg_ativo):
        db = create_engine(self.db_string)
        try:
            db.execute("INSERT INTO sistema.tb_vendas(id_vendedor, id_categoria, id_produto, datavenda, valortotal, quantidade, fg_ativo) VALUES (%s,%s,%s,%s,%s,%s,%s)", id_vendedor, id_categoria, id_produto, datavenda, valortotal, quantidade, fg_ativo)
            res = True
        except:
            print("Problemas ao inserir na tabela usuário\n")
            res = False
        return res

    def addCompra(self, id_fornecedor, id_produto, id_categoria, datacompra, valortotal, quantidade, fg_ativo):
        db = create_engine(self.db_string)
        try:
            db.execute("INSERT INTO sistema.tb_compras(id_fornecedor, id_produto, id_categoria, datacompra, valortotal, quantidade, fg_ativo) VALUES (%s,%s,%s,%s,%s,%s,%s)", id_fornecedor, id_produto, id_categoria, datacompra, valortotal, quantidade, fg_ativo)
            res = True
        except:
            print("Problemas ao inserir na tabela.\n")
            res = False
        return res


    def getUsuario(self):
        db = create_engine(self.db_string)
        usuario = db.execute("SELECT * FROM cadastro.usuarios")
        return usuario 

    def getFornecedor(self):
        db = create_engine(self.db_string)
        fornecedores = db.execute("SELECT * FROM sistema.tb_fornecedores")
        return fornecedores

    def getCategorias(self):
        db = create_engine(self.db_string)
        categorias = db.execute("SELECT * FROM sistema.tb_categorias")
        return categorias

    def getProdutos(self):
        db = create_engine(self.db_string)
        produtos = db.execute("SELECT * FROM sistema.tb_produtos")
        return produtos

    def getVendedores(self):
        db = create_engine(self.db_string)
        vendedores = db.execute("SELECT * FROM sistema.tb_vendedores")
        return vendedores

    def getVendas(self):
        db = create_engine(self.db_string)
        vendas = db.execute("SELECT * FROM sistema.tb_vendas")
        return vendas

    def getCompras(self):
        db = create_engine(self.db_string)
        compras = db.execute("SELECT * FROM sistema.tb_compras")
        return compras

    



