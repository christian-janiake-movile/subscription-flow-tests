import json
import digdag

def store_value(key, value):
  obj = json.loads(value)
  digdag.env.store(dict([(key, obj)]))

