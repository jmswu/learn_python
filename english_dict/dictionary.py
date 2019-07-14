import json

from dict_source import DictResource


# dictionary object
class Dictionary:

    def __init__(self, src=DictResource.normal):
        """
        load data from the dictionary file into python dictionary
        """
        self.dict_data = json.load(open(src, 'r'))

    def translate(self, word):
        """
        lookup the key from the dictionary and return the matching data
        :param word: word to be translate
        :return: meaning of the word
        """
        return self.dict_data[word]
