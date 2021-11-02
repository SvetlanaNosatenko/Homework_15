from flask import Flask, jsonify, abort
from base_animals import *


app = Flask(__name__)


@app.route('/<int:itemid>')
def animal_fin(itemid: int):
    """По запросу /<itemid> возвращает информацию об одном объекте"""
    if itemid:
        return jsonify(base_animal(itemid))
    abort(404)


@app.errorhandler(404)
def not_found_handler(request):
    return jsonify({'error': '404 Not Found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
