import json
def delete_from_dict(li,di):
    for i in li:
        di.pop(i)
    return di

def search_startswith(parse,event_di,category,search):
    li = []
    for event in event_di.keys():
        for string in search:
            if event.lower().startswith(string):
                parse[event] = category
                if len(li)==0 or li[-1] != event:
                    li.append(event)
    event_di = delete_from_dict(li,event_di)
    return (parse,event_di)

def search_contains(parse,event_di,category,search):
    li = []
    for event in event_di.keys():
        for string in search:
            if string in event.lower():
                parse[event] = category
                if len(li)==0 or li[-1] != event:
                    li.append(event)
    delete_from_dict(li,event_di)
    return (parse,event_di)

event_di = {}
parse = {}
starts_with_di = {
    'CreateObject': ['create','copy','run','purchase'],
    'ModifyExistingResource': ['modify','update','set','tag','deregister','Deprecate','un','reject','register'],
    'ListResources' : ['list'],
    'Download/UploadObjects': ['getobjects','upload'],
    'GetInfo': ['describe','get','search'],
    'AssociateResources' : ['associate','put'],
    'Login' : ['assume','login','switch','RenewRole','RenewDelegate'],

}

contains_di = {
    'Delete': ['delet','terminate','revoke'] ,
    'DisableObjects': ['disabl','stop','cancel','unlink','suspend'],
    'EnableObjects': ['enabl','start','invoke'],
    'SensitiveInfo': ['accesskey','secretkey','token','invite','exportapi'],
    'Logout': ['exit'],
    'CreateObject': ['create','copy'],
    'ModifyExistingResource': ['detach','modify','update','set','tag','deregister','Deprecate','attach','upgrade','wipe','transfer','validate','publish'],
    'ListResources' : ['list'],
    'Download/UploadObjects': ['getobjects','upload'],
    'GetInfo': ['describe','get','view'],
    'AssociateResources' : ['associate','put'],
    'Login' : ['assume','login'],

}
with open("event_names.py","r") as f:
    line = f.readline()
    while line:
        event_di[line.replace('\n','')] = ""
        line = f.readline()

print(len(event_di))
for key,value in starts_with_di.items():
    parse,event_di = search_startswith(parse,event_di,key,value)
for key,value in contains_di.items():
    parse,event_di = search_contains(parse,event_di,key,value)

with open('event_category.json','w') as f:
    json.dump(parse, f)
print(len(event_di))
print(event_di)