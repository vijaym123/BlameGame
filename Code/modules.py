from os import listdir
from os.path import isfile, join

class readFiles:
    def __init__(self, folder='../NewsLetters/'):
        self.folder = folder
        self.newsLetters = [ f for f in listdir(folder) if isfile(join(folder,f)) ]
        self.i = 0
        self.n = len(self.newsLetters)
        if self.newsLetters.count(".DS_Store"):
            self.newsLetters.remove(".DS_Store")

    def __iter__(self):
        return self

    def next(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return (self.newsLetters[i], file(self.folder+"/"+self.newsLetters[i],"r").read())
        else:
            raise StopIteration()
