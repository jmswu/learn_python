import json
from difflib import get_close_matches

from dict_source import DictResource


# dictionary object
class Dictionary:

    def __init__(self, src=DictResource.normal, cut_off=0.7):
        """
        load data from the dictionary file into python dictionary
        """
        self.dict_data = json.load(open(src, 'r'))
        self.cut_off = cut_off

    def translate(self, word):
        """
        lookup the key from the dictionary and return the meaning
        if no match is found, it will try to find a close match
        :param word: word to be translate
        :return: meaning of the word, or nothing if the word doesn't exit
        """
        # change the word to lower case
        word = word.lower()
        # find a match
        if word in self.dict_data:
            return self.dict_data[word]
        elif word.title() in self.dict_data:
            return self.dict_data[word.title()]
        else:
            # get close match
            did_you_mean = get_close_matches(word, self.dict_data.keys(), cutoff=self.cut_off)
            if len(did_you_mean) > 0:
                return "Did you mean [%s]?\n" % (did_you_mean[0]) + self.dict_data[did_you_mean[0]]
            else:
                return "[%s] doesn't exit, please double check." % word

    def set_cut_off(self, cut_off):
        """
        set the cut off rate of a match
        :param cut_off: cut off rate, 0 to 1
        :return: void
        """
        self.cut_off = cut_off
