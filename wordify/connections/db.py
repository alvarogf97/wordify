import json


class Connection:
    
    def __init__(self):
        pass


    def read_db(self):
        with open('resources/db.json', 'r') as file:
            self.data = json.load(file)
            return self.data
    

    def write_db(self, username, phrase):
        self.data = self.read_db()
        if username in self.data.keys():
            for i in self.data[username]:
                if phrase in i["data"]:
                    return True
                else:
                    y = {"id": len(self.data[username]), "data": phrase}
                    self.data[username].append(y)
                    self.write_json(self.data)
                    return True
        else:
            y = [{"id": '0', "data": phrase}]
            self.data[username] = y
            self.write_json(self.data)
            return True


    def write_json(self, data):
        with open('resources/db.json', 'w') as f: 
            json.dump(data, f, indent=4)
            return True
