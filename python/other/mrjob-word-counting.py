# https://github.com/Yelp/mrjob/tree/master/mrjob
from mrjob.job import MRJob

class MRWordFrequencyCount(MRJob):
    def mapper(self, _, line):
        yield "chars", len(line)
        yield "words", len(line.split())
        yield "lines", 1

    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == '__main__': MRWordFrequencyCount.run()

# $ python word-counting-with-mrjob.py text.txt
# "words"   234
# "lines"   35
# "chars"   1057