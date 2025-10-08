from flask import Flask #Importa a classe Flask do módulo flask

#__name__ = '__main__'
app = Flask(__name__) #Cria uma instância do aplicativo Flask

@app.route("/") #Rota para a página inicial
def hello_world(): # Define a função para a rota /
    return "Hello, World!" # Retorna uma string simples


@app.route("/about") #Rota para a página "Sobre"
def about(): #  Define a função para a rota /about
    return "About Page" # Retorna uma string simples

if __name__ == "__main__": #Executa o aplicativo Flask
    app.run(debug=True) #Modo de depuração ativado