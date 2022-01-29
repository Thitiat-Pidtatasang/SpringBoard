"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """
     >>> wf = WordFinder("simple.txt")
    3 words read

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    """

    def __intit__(self, path):
        dict_file = open(path)

        self.words = self.parse(dict_file)

        print(f"{len(self.word)} word read")

    def parse(self, dict_file):
        return [w.strip() for w in dict_file]

    def random(self):
        return random.choice(self.words)

    class SpecialWordFinder(WordFinder):
        """
        >>> swf = SpecialWordFinder("complex.txt")

        >>> swf.random() in ["pear", "carrot", "kale"]

        >>> swf.random() in ["pear", "carrot", "kale"]

        >>> swf.random() in ["pear", "carrot", "kale"]
        """

        def parse(self, dict_file):
            return [w.strip() for w in dict_file
                    if w.stri() and not w.startswith("#")]