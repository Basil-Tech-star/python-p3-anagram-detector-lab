# your code goes here!
from collections import Counter


class Anagram:
    def __init__(self, word):
        self.word = word
        self.word_count = Counter(word)

    def match(self, word_list):
        return [word for word in word_list if Counter(word) == self.word_count and word != self.word]
    
    def __repr__(self):
        return f"Anagram('{self.word}')"
    
    