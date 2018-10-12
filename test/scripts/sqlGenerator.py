import json
tags = []
temp_tags = []
infile = open('data/sock.json', 'r')
data = json.load(infile, encoding='UTF-8')
infile.close()
fp = open("data/dump1.sql", 'w')
fp.truncate()
# loop to insert values into sock table
for sock in data:
    sid = sock['id']
    name = sock['name']
    desc = sock['description']
    price = str(sock['price'])
    count = str(sock['count'])
    url1 = sock['imageUrl'][0]
    url2 = sock['imageUrl'][1]
    temp_tags = temp_tags+sock['tag']
    fp.write("INSERT INTO sock VALUES (\""+sid+"\",\""+name+"\",\""+desc+"\","+price+","+count+",\""+url1+"\","+"\""+url2+"\");"+'\n')
# remove duplicated tag from temp_tags array
for tag in temp_tags:
    if tag not in tags:
        tags.append(tag)
# loop to insert tag values into tag table
for tag in tags:
    fp.write("INSERT INTO tag(name) VALUES (\"" + tag + "\");" + '\n')

# loop to insert values into sock_tag table
for sock in data:
    sid=sock['id']
    for tag in sock['tag']:
        tid = str(tags.index(tag)+1)
        fp.write("INSERT INTO sock_tag VALUES (\""+sid+"\",\""+tid+"\");"+'\n')

fp.close()
