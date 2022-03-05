import re
import unidecode
from classes.stopwords import stopwords


class Parser:
    """This class is allowed to parse the user's sentence/question and get the keyword
    """
    def __init__(self, question):
        self.question = question
        self.keywords = []

    def parse(self):
        """Function to get the cleaned sentence"""
        self.remove_upper_case()
        self.remove_ponctuation()
        self.remove_accents()
        self.remove_unless_word()

    def remove_unless_word(self):
        """This function uses stopwords list to remove unless words from user's question
        """
        for word in self.question.split():
            if word not in stopwords:
                self.keywords.append(word)
                # print(word)

    def remove_upper_case(self):
<<<<<<< HEAD
        self.question = self.question.lower()

    def remove_ponctuation(self):
=======
        """Function to remove upper cases from user's question"""
        self.question = self.question.lower()

    def remove_ponctuation(self):
        """Function to remove punctuation from user's question """
>>>>>>> afa3ce2cccc9609d925ed4674cfb213557abe24d
        self.question = re.sub(r"[^\w\s]", "", self.question)

    def remove_accents(self):
        """Function to remove any accent from user's question"""
        self.question = unidecode.unidecode(self.question)

    def get_keyword(self):
        """Function to add the keyword if exists in a list, if not exists, it returns None"""
        if len(self.keywords) != 0:
            return (" ").join(self.keywords)
        return None
<<<<<<< HEAD


"""
if __name__ == '__main__':
    parser = Parser(QUESTION)
    parser.parse()
    print(parser.get_keyword())
    #print(parser.remove_unless_word())"""
=======
>>>>>>> afa3ce2cccc9609d925ed4674cfb213557abe24d
