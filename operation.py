from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'


# http://127.0.0.1:5000/world

@app.route('/world')
def world():
    return 'Весной природа прекрасна! Все расцветает, и появляются первые насекомые.'


@app.route('/<str:number_one>/<str:number_two>/add')
def add(number_one, number_two):
    number_one,number_two = float(number_one), float(number_two)
    return f'{number_one} + {number_two} = {number_one + number_two}'


@app.route('/<str:number_one>/<str:number_two>/sub')
def sub(number_one, number_two):
    number_one,number_two = float(number_one), float(number_two)
    return f'{number_one} - {number_two} = {number_one - number_two}'


@app.route('/<str:number_one>/<str:number_two>/multi')
def multi(number_one, number_two):
    number_one,number_two = float(number_one), float(number_two)
    return f'{number_one} * {number_two} = {number_one * number_two}'


@app.route('/<str:number_one>/<str:number_two>/div')
def div(number_one, number_two):
    number_one,number_two = float(number_one), float(number_two)
    if number_two == 0:
        return 'Деление на 0 невозможно'
    return f'{number_one} : {number_two} = {number_one / number_two}'


if __name__ == '__main__':
    app.run()
