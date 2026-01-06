from flask import Flask
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

#Mapeamento da porta a ser utilizada para acessar o "site"
@app.route('/')
def main():
    return 'Hello World'

