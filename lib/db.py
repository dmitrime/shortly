# -*- coding: utf-8 -*-

from redis import Redis
from shorten import shorten
redis = Redis()

MINLEN         = 4
REDIS_URL_FMT  = 'u:{}'
REDIS_HASH_FMT = 'h:{}'

def save_shortest(url, hashed):
    '''
    Start from MINLEN and add one extra character from the hash until there are no more collisions.
    '''
    i = 0
    while redis.get(hashed[:MINLEN+i]) is not None:
        if MINLEN+i >= len(hashed):
            raise 'This is so unlikely, it should never happen!'
        i += 1

    hashed = hashed[:MINLEN+i]
    redis.set(REDIS_URL_FMT.format(url), hashed)
    redis.set(REDIS_HASH_FMT.format(hashed), url)
    return hashed

def save(url):
    res = redis.get(REDIS_URL_FMT.format(url))
    if res is not None:
        return res
    else:
        return save_shortest(url, shorten(url))

def fetch(hashed):
    return redis.get(REDIS_HASH_FMT.format(hashed))
