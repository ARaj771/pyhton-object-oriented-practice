"""Word Finder: finds random words from a dictionary."""

import random
""" to be able to choose words randomly from a list."""

class WordFinder:
    ...
    """ Opens a file with a word per line and reads it into a list.
    uses the random method to print a random word from list."""

    def __init__(self,file_path):
        """Opens a file with the given file path,reads the file and displays the number of words in the file.
           Closes the file."""
    
        self.word_file = open(file_path)
        self.list_word_file()
        self.word_file.close()
        

    def list_word_file(self):
        " reads the file and creates the list.Displays the number of words in file."
       
        self.copy_of_words = [line.strip() for line in self.word_file]
        print(self.copy_of_words)
        print (f'{len(self.copy_of_words)} words read')

        
    def random(self):
        " Chooses a word randomly from file."
        print(random.choice(self.copy_of_words))

