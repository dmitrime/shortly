import sys
import redis
from mock import patch, Mock
from pytest import fixture

sys.path.append('.')
sys.path.append('..')

from lib import db
from lib.shorten import shorten


@patch('redis.Redis.get')
def test_fetch(get, hashed):
    db.fetch(hashed)
    get.assert_called()

@patch('redis.Redis.get')
@patch('redis.Redis.set')
def test_save(set, get):
    db.save(url)
    set.assert_called()
    get.assert_called()

@fixture
def hashed(url):
    return shorten(url)
    
@fixture
def url():
    return 'http://www.google.com'
