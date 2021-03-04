class User():

    def __init__(self, name, phrases):
        self.name = name
        self.phrases = phrases

    def get_name(self):
        return self.name

    def get_phrases(self):
        return self.phrases

    def get_id_phrase(self, id):
        return self.phrases[id]
    
    def set_name(self, name):
        self.name = name

    def add_phrase(self, phrase):
        new_id =len(self.phrases)
        new_phrase={"id":new_id, "data":phrase}
        self.phrases.append(new_phrase)