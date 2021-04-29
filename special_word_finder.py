""" Special word finder program. Returns the actual words but not comments or blank line"""
from wordfinder import WordFinder


class SpecialWordFinder(WordFinder):
    """ Specialized random wordFinder that does not read blank lines or words that start with #.
    
    >>> swf = SpecialWordFinder("desktop/python/python-oo-practice/complex.txt")
    4 words read
    >>> swf.random().startswith(#)
    False
    >>> swf.random() not = "\n"
    True
    """


    def list_word_file(self):
        " reads the file and creates the list.Displays the number of words in file."
        self.copy_of_words = []
        for line in self.word_file:
            if (line.strip() and not line.startswith('#')):
                self.copy_of_words.append(line)
        print (f'{len(self.copy_of_words)} words read')
        for line in self.copy_of_words:
            print(line)