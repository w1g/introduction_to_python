import json
import functools

def to_json(func):
    @functools.wraps(func)
    def inner(*argv, **kwargv):
        result = func(*argv, **kwargv)
        return json.dumps(result)
    return inner