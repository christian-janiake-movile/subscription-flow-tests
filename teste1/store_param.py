import json
import digdag

def store_send_mo_response(value):
  obj = json.loads(value)
  digdag.env.store({'send_mo_response': obj})

