from os import walk
import json
 
# Opening JSON file

filenames = next(walk('.'), (None, None, []))[2]  # [] if no file
filenames.remove('my.py')
datas = []
for file in filenames:
    with open(file) as json_file:
        datas.append(json.load(json_file))

records = [list(rec.values())[0] for rec in datas]
li = []
for record in records:
    li = li + record
di = {
    "Records" : li
}

with open('attack2.json', 'w') as fp:
    json.dump(di, fp)