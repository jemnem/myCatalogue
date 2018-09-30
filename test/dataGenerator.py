import json
infile=open('data/sock.json','r')
data=json.load(infile,encoding='UTF-8')
infile.close()
fp = open("data/dump.sql",'w')
fp.truncate()
tags=[]
for dict in data:
    id=dict['id']
    name=dict['name']
    desc=dict['description']
    price=str(dict['price'])
    count=str(dict['count'])
    url1=dict['imageUrl'][0]
    url2 = dict['imageUrl'][1]
    tags=tags+dict['tag']
    fp.write("INSERT INTO sock VALUES (\""+id+"\",\""+name+"\",\""+desc+"\","+price+","+count+",\""+url1+"\","+"\""+url2+"\");"+'\n')


new_tags = []
for tag in tags:
    if tag not in new_tags:
        new_tags.append(tag)
print(new_tags)
for tag in new_tags:
    fp.write("INSERT INTO tag VALUES (\"" + tag + "\");" + '\n')

fp.close()