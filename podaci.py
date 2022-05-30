class Podaci:
    def __init__(self,first_language,second_language,image):
        self.first_language=first_language
        self.second_language=second_language
        self.image=image
    def add_data(self):
        return (self.first_language,self.second_language,self.image)
        #return "({},{},{})".format(self.first_language,self.second_language,self.image)
