from pysword.modules import SwordModules
from pysword.bible import SwordBible
from pysword.books import BookStructure
import random


class Verser:
    def __init__(self) -> None:
        self.translations = SwordModules("/usr/share/sword/")
        self.bible = self.get_bible()
        self.bibstruc = self.bible.get_structure()
        self.bookstruc = self.get_bookstruc()


    def get_bible(self) -> SwordBible:
        transinits_iter = self.translations.parse_modules().keys()  # translation initials (e.g. "KJV")
        self.transinits = random.choice(list(transinits_iter))
        return self.translations.get_bible_from_module(self.transinits)


    def get_bookstruc(self) -> BookStructure:
        bookstrucs = self.bibstruc.get_books()
        self.testament = random.choice(list(bookstrucs.keys()))
        return random.choice(bookstrucs[self.testament])


    def get_passage(self):
        return self.bible.get(self.book, self.chapter, self.verse)


    def get_passage_slow(self):
        bibiter = self.bible.get_iter()
        j = i = 0
        ri = random.randint(1, j)
        passage = None
        for _ in bibiter:
            j += 1
        while i < ri:
            passage = next(bibiter)
            i += 1
        return passage


    def print_passage(self, slow=False):
        if slow:
            passage = self.get_passage_slow()
        else:
            passage = self.get_passage()
        print(self.transinits, self.testament, self.bookstruc.name, self.chapter, self.verse)
        print(passage)


    def set_query_keys(self):
        self.book = self.bookstruc.preferred_abbreviation
        self.chapter = random.randint(1, self.bookstruc.num_chapters)
        numverses = self.bookstruc.chapter_lengths[self.chapter - 1]
        self.verse = random.randint(1, numverses)


v = Verser()
v.set_query_keys()
v.print_passage()
