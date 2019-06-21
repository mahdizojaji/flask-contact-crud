from config import *
from errors import *
from models import Contact
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/contact', methods=['POST'])
def create():
    try:
        print(dict(request.form))
        name = request.form['name']
        phone = request.form['phone']
        Contact.create(name=name, phone=phone).save()
        result = jsonify({'name': name, 'phone': phone})
        return result
    except Exception:
        raise InvalidUsage('Invalid arguments', status_code=400)


if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=DEBUG)
