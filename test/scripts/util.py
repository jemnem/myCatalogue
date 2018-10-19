import json
import sys

class Util:
    def get_size(self):
        infile_path = 'data/sock.json'
        infile = open(infile_path, 'r')
        data = json.load(infile, encoding='UTF-8')
        infile.close()
        return len(data)

    def set_size(self):
        infile_path = '../postman/catalogue_environment.json'
        outfile_path = 'data/environment.json'
        size = self.get_size()
        infile = open(infile_path, 'r')
        data = json.load(infile, encoding='UTF-8')
        infile.close()
        for value in data['values']:
            if value['key'] == 'size':
                value['value'] = size
        outfile = open(outfile_path, 'w')
        outfile.write(json.dumps(data))
        outfile.close()

    def set_sql(self):
        tags = []
        temp_tags = []
        infile_path = 'data/sock.json'
        outfile_path = 'data/dump1.sql'
        infile = open(infile_path, 'r')
        data = json.load(infile, encoding='UTF-8')
        infile.close()
        outfile = open(outfile_path, 'w')
        outfile.truncate()
        # loop to insert values into sock table
        for sock in data:
            sid = sock['id']
            name = sock['name']
            desc = sock['description']
            price = str(sock['price'])
            count = str(sock['count'])
            url1 = sock['imageUrl'][0]
            url2 = sock['imageUrl'][1]
            temp_tags = temp_tags + sock['tag']
            outfile.write(
                "INSERT INTO sock VALUES (\"" + sid + "\",\"" + name + "\",\"" + desc + "\"," + price + "," + count + ",\"" + url1 + "\"," + "\"" + url2 + "\");" + '\n')
        # remove duplicated tag from temp_tags array
        for tag in temp_tags:
            if tag not in tags:
                tags.append(tag)
        # loop to insert tag values into tag table
        for tag in tags:
            outfile.write("INSERT INTO tag(name) VALUES (\"" + tag + "\");" + '\n')

        # loop to insert values into sock_tag table
        for sock in data:
            sid = sock['id']
            for tag in sock['tag']:
                tid = str(tags.index(tag) + 1)
                outfile.write("INSERT INTO sock_tag VALUES (\"" + sid + "\",\"" + tid + "\");" + '\n')

        outfile.close()


if __name__ == '__main__':
    util = Util()
    arg = sys.argv[1]
    getattr(util, arg)()
