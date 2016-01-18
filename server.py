# -*- coding: utf-8 -*-

from lib import db
from flask import Flask, request, redirect

app = Flask(__name__)


@app.route('/shorten', methods=['GET', 'POST'])
def url2hash():
    url = request.args.get('url')
    if url is None:
        return ''
    else:
        if not url.startswith('http://'):
            url = 'http://' + url
        return db.save(url)


@app.route('/<hashed>')
def hash2url(hashed):
    url = db.fetch(hashed)
    if url is None:
        return 'not found'
    return redirect(url, code=302)

if __name__ == '__main__':
    app.run(debug=True)
