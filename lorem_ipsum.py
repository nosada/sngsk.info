import argparse
import random


class LoremIpsum(object):
    def __init__(self, word_source_file):
        with open(word_source_file, 'r') as f:
            self.word_source = f.read().split('\n')
        self.punctuations = [' ', ',', ':', ';']
        self.base_param = 80
        self.rate_sentence = self.base_param + random.randint(1, 10)
        self.rate_paragraph = self.base_param + random.randint(1, 10)
        self.rate_text = self.base_param + random.randint(1, 10)

    def stop_generation(self, limit):
        if random.randint(1, 100) > limit:
            return True
        else:
            return False

    def choose_punctuation(self):
        random_number = random.randint(1, 100)
        if random_number < 90:
            return self.punctuations[0]
        elif 90 <= random_number < 97:
            return self.punctuations[1] + ' '
        elif 97 <= random_number <= 100:
            return random.choice(self.punctuations[2:]) + ' '

    def generate_sentence(self):
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
        sentences = set()
        while True:
            sentences.add(self.generate_sentence())
            if self.stop_generation(self.rate_paragraph):
                break
        return ' '.join(sentences)

    def generate_text(self):
        paragraphs = set()
        while True:
            paragraphs.add(self.generate_paragraph())
            if self.stop_generation(self.rate_text):
                break
        return '\n\n'.join(paragraphs)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
            description="Generates random pseudo-sentences like Lorem ipsum.")
    parser.add_argument(
        "word_source",
        metavar="<word source>",
        type=str,
        help="list of words for generating pseudo-sentences")
    args = parser.parse_args()

    word_source = args.word_source
    li = LoremIpsum(word_source)
    text = li.generate_text()
    print(text)
