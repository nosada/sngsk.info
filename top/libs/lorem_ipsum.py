"""Generate Lorem Ipsum"""

import argparse
import random


class LoremIpsum(object):
    """Class for Lorem Ipsum generation"""

    def __init__(self, word_source_file, base_rate):
        """Constructor of LoremIpsum"""

        with open(word_source_file, 'r') as wsf:
            self.word_source = wsf.read().split('\n')
        if 0 < base_rate < 100:
            self.base_rate = base_rate
        else:
            raise ValueError("base_rate must be between 1 to 99")

        self.rate_sentence = self.base_rate + random.randint(1, 10)
        self.rate_paragraph = self.base_rate + random.randint(1, 10)
        self.rate_text = self.base_rate + random.randint(1, 10)

    @staticmethod
    def stop_generation(limit):
        """Decide to stop Lorem Ipsum generation randomly
        - args: 'limit' as int
                threshold of randam number between 1 to 100
        - returns: boolean
                   Return True if random.randint(1, 100) returns value bigger
                   than 'limit'.
                   Return False if otherwise."""

        return random.randint(1, 100) > limit

    @staticmethod
    def choose_punctuation():
        """Choose puctuation randomly
        - args: none
        - returns: punctuation either one of ', ', ': ', '; ', ' '
        """

        punctuations = [' ', ',', ':', ';', '!', '?']
        random_number = random.randint(1, 100)
        if random_number < 90:
            return punctuations[0]
        elif 90 <= random_number < 97:
            return punctuations[1] + ' '
        elif 97 <= random_number <= 100:
            return random.choice(punctuations[2:]) + ' '

    def generate_sentence(self):
        """Generate sentence using words in self.word_source
        - args: none
        - returns: sentence as str"""

        sentence = ''
        while True:
            word = random.choice(self.word_source)
            if len(word) > 3 and random.choice([True, False]):
                word = word[0].upper() + word[1:]
            sentence += word
            if self.stop_generation(self.rate_sentence):
                sentence += '.'
                break
            else:
                sentence += self.choose_punctuation()
        return sentence[0].upper() + sentence[1:]

    def generate_paragraph(self):
        """Generate paragraph using generated sentence by
        self.generate_sentence()
        - args: none
        - returns: paragraph as str"""

        sentences = set()
        while True:
            sentences.add(self.generate_sentence())
            if self.stop_generation(self.rate_paragraph):
                break
        return ' '.join(sentences)

    def generate_text(self):
        """Generate text using generated paragraph by
        self.generate_text()
        - args: none
        - returns: text as str"""

        paragraphs = set()
        while True:
            paragraphs.add(self.generate_paragraph())
            if self.stop_generation(self.rate_text):
                break
        return '\n\n'.join(paragraphs)


if __name__ == "__main__":
    PARSER = argparse.ArgumentParser(
        description="Generates random pseudo-sentences like Lorem ipsum.")
    PARSER.add_argument(
        "word_source",
        metavar="<word source>",
        type=str,
        help="list of words for generating pseudo-sentences")
    PARSER.add_argument(
        "base_rate",
        metavar="<base parameter>",
        type=int,
        help=("base rate between 1 to 99 used to generate"
              "Lorem Ipsum sentences, paragraphs and texts"))
    ARGS = PARSER.parse_args()

    WORD_SOURCE = ARGS.word_source
    BASE_RATE = ARGS.base_rate
    LI = LoremIpsum(WORD_SOURCE, BASE_RATE)
    TEXT = LI.generate_text()
    print(TEXT)
