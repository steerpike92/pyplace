import random, sys, string
from collections import Counter, defaultdict


class PrettyDefaultDict(defaultdict):
    __repr__ = dict.__repr__


class PrettyCounter(Counter):
    __repr__ = dict.__repr__


class RandomStory:
    def __init__(self, filepath, n_gram=2):
        with open( filepath ) as f:
            self.source_words=self._process_words(f)
        self.n_gram = n_gram
        self.train()


    def _make_unigrams(self):
        dic = {(): self.source_words}
        return dic


    def _make_bigrams(self):
        dic = PrettyDefaultDict(list)
        for i in range(0, len(self.source_words)-1):
            word, next_word = self.source_words[i], self.source_words[i+1]
            dic[(word,)].append(next_word)
        return dic


    def _make_trigrams(self):
        dic = PrettyDefaultDict(list)
        for i in range(0, len(self.source_words) - 2):
            word1 = self.source_words[i]
            word2 = self.source_words[i + 1]
            word3 = self.source_words[i + 2]
            dic[(word1, word2)].append(word3)
        return dic


    def train(self):
        grams = {1: self._make_unigrams, 2: self._make_bigrams, 3: self._make_trigrams}
        self.dic=grams[self.n_gram]()


    def _process_words(self, f):
        p = string.punctuation
        words = []
        for line in f:
            new_words = line.split()
            words.extend(
                map(lambda word: word.lstrip(p).rstrip(p).lower(), new_words))
        return words


    def generate(self, n=200):
        random.seed('Is the looking-glass is half full or half-empty?')
        story_tuple = random.choice(self.dic.keys())
        for i in range(self.n_gram, n+1):
            key = story_tuple[i-self.n_gram:]
            choices = self.dic[key]
            story_tuple += (random.choice(choices),)
        story = ' '.join(story_tuple)
        return story

if __name__ == '__main__':
    r_story = RandomStory("../data/alice.txt", 3)
    story = r_story.generate()
    print story












#pad
