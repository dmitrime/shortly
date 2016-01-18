# -*- coding: utf-8 -*-

from lib import db
from flask import Flask, request

app = Flask(__name__)

@app.route('/shorten', methods=['GET', 'POST'])
def url2hash():
    url = request.args.get('url')
    if url is None:
        return ''
    else:
        return db.fetch(url)

if __name__ == '__main__':
    app.run(debug=True)

