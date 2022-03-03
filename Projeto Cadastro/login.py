from PyQt5 import uic,QtWidgets



def funçao_login():
   usuario = login.linhaUsuario.text()
   senha = login.linhaSenha.text()
   
   if usuario == "Guga" and senha == "1234":
       login.close()
       cadastro.show()

   

   




app=QtWidgets.QApplication([])
login=uic.loadUi("tela_login.ui")
cadastro=uic.loadUi("Cadastro_clientes.ui")
login.btnLogin.clicked.connect(funçao_login)


login.show()
app.exec()