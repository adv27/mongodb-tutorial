from pymongo import MongoClient
from bottle import route, run, template


@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)


@route('/')
def index():
    # connect to mongoDB
    connection = MongoClient('localhost', 27017)

    # attach to the database
    db = connection.test

    # get the names collection
    names = db.names

    # find a single document
    item = names.find_one()
    
    return '<b>Hello {name}</b>'.format(name=item['name'])


run(host='localhost', port=8080)
