class stack:
    __capacity = 0
    __position = ()
    __tos = 0
    def __init__(self, positions):
        self.__capacity = 12
        self.__tos = -1
        self.__position = positions

    def isFull(self):
        if self.__tos == self.__capacity - 1:
            return True
        return False

    def isEmpty(self):
        if self.__tos == -1:
            return True
        return False

    def push(self):
        if not self.isFull():
            self.__tos += 1

    def get_position(self):
        return self.__position[:self.__tos+1]