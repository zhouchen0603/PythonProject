import abc

"""
https://www.cnblogs.com/FG123/p/9463673.html
"""

class CopyBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def save(self):
        pass


class CopyPaper(CopyBase):
    def __init__(self):
        pass

    def save(self):
        print("copy paper")


class CopyQuestion(CopyBase):
    def __init__(self):
        pass


copy_paper = CopyPaper()
copy_paper.save()
copy_question = CopyQuestion()
copy_question.save()