class File:
    def __init__(self, txt):
        self.txt = txt

class WordFile(File):
    def __init__(self, txt):
        super().__init__(txt)
    def visit(self, fileVisitor):
        fileVisitor.visitWord(self)
    def __str__(self):
        return self.txt

class PictureFile(File):
    def __init__(self, txt):
        super().__init__(txt)
    def visit(self, fileVisitor):
        fileVisitor.visitPicture(self)
    def __str__(self):
        return self.txt

class FileVisitor:
    pass

class PrintVisitor(FileVisitor):
    def visitWord(self, wordFile):
        print(wordFile)

    def visitPicture(self, pictureFile):
        print(pictureFile)

class InfoVisitor(FileVisitor):
    def visitWord(self, wordFile):
        print("Info Visitor ", wordFile)

    def visitPicture(self, pictureFile):
        print("InfoVisitor ", pictureFile)

l = list()
l.append(WordFile("wordFile"))
l.append(PictureFile("pictireFile"))

visitor = PrintVisitor()
for f in l:
    f.visit(visitor)

visitor = InfoVisitor()
for f in l:
    f.visit(visitor)
