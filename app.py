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


@app.route('/contact/', defaults={'_id': None}, methods=['GET'])
@app.route('/contact/<int:_id>', methods=['GET'])
def read(_id):
    if _id is None:
        result = [{'_id': contact._id, 'name': contact.name, 'phone': contact.phone} for contact in Contact.select()]

        return jsonify(result) if result else 'No Contact Found'
    else:
        result = [
            {'_id': contact._id, 'name': contact.name, 'phone': contact.phone}
            for contact in Contact.select().where(Contact._id == _id)
        ]
        if result:
            return jsonify(result[-1])
        else:
            raise InvalidUsage('User Not Found', status_code=404)


@app.route('/contact/<int:_id>', methods=['PUT'])
def update(_id):
    try:
        data = dict(request.form)
        name = data.get('name')
        phone = data.get('phone')
        assert name or phone
    except Exception:
        raise InvalidUsage('Invalid arguments', status_code=400)
    try:
        contact = Contact.select().where(Contact._id == _id).get()
        contact.name = name or contact.name
        contact.phone = phone or contact.phone
        contact.save()
        return jsonify({'_id': contact._id, 'name': contact.name, 'phone': contact.phone})
    except Exception:
        raise InvalidUsage('User Not Found', status_code=404)


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=DEBUG)
