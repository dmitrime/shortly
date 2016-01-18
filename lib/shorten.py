# -*- coding: utf-8 -*-

from hashlib import sha256

def shorten(url):
    return sha256(url).hexdigest()
