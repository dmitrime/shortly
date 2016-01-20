# -*- coding: utf-8 -*-

from lib import db
from flask import Flask, request, redirect, render_template

app = Flask(__name__)


@app.route('/shorten', methods=['GET', 'POST'])
def url2hash():
    url = request.values.get('url')
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


@app.route('/')
def landing():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
