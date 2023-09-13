from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '¡Bienvenido!'

@app.route('/contacto')
def contacto():
    return 'Nuestro contacto.'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

