import threading

class LoadData (threading.Thread):
    def __init__(self, data):
        threading.Thread.__init__(self)
        self.data = data
    def run(self):
        self.__return = _trainModel()
    def join(self):
        threading.Thread.joinn(self)
        return self.__return