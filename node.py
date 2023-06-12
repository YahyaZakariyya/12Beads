class node:
    __pointers = None
    __player = False
    __opponent = False
    __position_x = 0
    __position_y = 0

    def set_data(self, data, position_x, position_y):
        self.__pointers = data
        self.__position_x = position_x
        self.__position_y = position_y

    def get_data(self):
        return self.__pointers
    
    def set_player(self, player):
        self.__player = player

    def set_opponent(self, opponent):
        self.__opponent = opponent

    def get_player(self):
        return self.__player

    def get_opponent(self):
        return self.__opponent

    def get_position(self):
        return self.__position_x, self.__position_y

    def get_position_x(self):
        return self.__position_x

    def get_position_y(self):
        return self.__position_y