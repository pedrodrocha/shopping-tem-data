import json

with open('raw-data/eldorado.json', encoding="utf8") as user_file:
  file_contents = user_file.read()
  
parsed_json = json.loads(file_contents)

print(parsed_json['data'][0])