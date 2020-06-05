
class OutStream(object):
    def __init__(self, task):
        self.task = task
        self._handle = 0
        self._task = 0
