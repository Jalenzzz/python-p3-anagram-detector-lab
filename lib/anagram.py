# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, possible_anagrams):
        sorted_word = sorted(self.word)
        
        return [candidate for candidate in possible_anagrams if sorted(candidate) == sorted_word]