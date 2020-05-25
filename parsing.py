import json

r = json.loads('')

print(type(r))
for key, value in r.items():
  print("{0}: {1}".format(key, value))
