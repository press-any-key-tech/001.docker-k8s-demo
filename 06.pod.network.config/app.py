import time
import os

import redis
from flask import Flask

greeting_message = os.environ.get('GREETING_MESSAGE')
greeting_secret = os.environ.get('GREETING_SECRET')

app = Flask(__name__)
cache = redis.Redis(
    host=os.environ.get('REDIS_SERVER'),
    port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return '{}! This is my secret message: {} and I have been seen [{}] times.\n'.format(
        greeting_message,
        greeting_secret,
        count
    )

