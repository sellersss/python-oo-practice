"""Word Finder: finds random words from a dictionary."""
import random


class WordFinder:
    """
    >>> wf = WordFinder("words.txt")
    3 words read

    >>> wf.random() in ['word', 'dome', 'porched']
    True

    >>> wf.random() in ['word', 'dome', 'porched']
    True

    >>> wf.random() ['word', 'dome', 'porched']
    True
    """

    def __init__(self, path):
        _dict_ = open(path)
        self.words = self.parse(_dict_)

        print(f"{len(self.words)} words read")

    def parse(self, _dict_):
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    def parse(self, _dict_):
        return [w.strip() for w in _dict_ if w.strip() and not w.startswitch("#")]