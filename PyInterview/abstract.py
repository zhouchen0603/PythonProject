

class CopyBase(object):
    def save(self):
        raise NotImplementedError


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

"""
copy_question = CopyQuestion()
copy_question.save()
"""