# -*- coding: utf-8 -*-

from redis import Redis
from shorten import shorten
redis = Redis()

KEEP = 6

def fetch(url):
    key = 'u:%s' % url
    res = redis.get(key)
    if res is not None:
        return res
    else:
        hashed = shorten(url)[:KEEP]
        redis.set(key, hashed)
        return hashed
