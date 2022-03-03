from PyQt5 import uic,QtWidgets
import mysql.connector


banco= mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="cadastro_clientes",
)

def funçao_login():
    usuario = login.lineEditLogin.text()
    senha = login.lineEditSenha.text()
    login.lineEditLogin.setText("")
    login.lineEditSenha.setText("")
    if usuario == "Guga" and senha == "1234":
        login.close()
        cadastro.show()
    else :
        login.labelError.setText("Usuário ou Senha Incorretos!")

def funçao_principal():
    linha1 = cadastro.lineEdit.text()
    linha2 = cadastro.lineEdit_2.text()
    linha3 = cadastro.lineEdit_3.text()
    linha4 = cadastro.lineEdit_4.text()
    linha5 = cadastro.lineEdit_5.text()

    print ("Nome: ", linha1 )
    print ("Sobrenome: ", linha2)
    print ("Endereço: ", linha3)
    print ("Numero: ", linha4)
    print ("Telefone: ", linha4)

    cursor=banco.cursor()
    comando_SQL = "INSERT INTO clientes (nome, sobrenome, endereco, numero, telefone) VALUES (%s,%s,%s,%s,%s)"
    dados = (str(linha1), str(linha2), str(linha3),str(linha4),str(linha5))
    cursor.execute(comando_SQL,dados)
    banco.commit()

    cadastro.lineEdit.setText("")
    cadastro.lineEdit_2.setText("")
    cadastro.lineEdit_3.setText("")
    cadastro.lineEdit_4.setText("")
    cadastro.lineEdit_5.setText("")

def open_listaclientes():
    lista_clientes.show()
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM clientes"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()

    
    
app=QtWidgets.QApplication([])
cadastro=uic.loadUi("Cadastro_clientes.ui")
login=uic.loadUi("tela_login.ui")
lista_clientes=uic.loadUi("lista_clientes.ui")
login.btnLogin.clicked.connect(funçao_login)
cadastro.btnCadastrar.clicked.connect(funçao_principal)
cadastro.btnCancelar.clicked.connect(open_listaclientes)
login.lineEditSenha.setEchoMode(QtWidgets.QLineEdit.Password)


login.show()
app.exec()

