from node import node
class adjacency_list:
    __n = []
    def __init__(self):
        for i in range(25):
            self.__n.append(node())
        pointers = ((None,None,self.__n[1],self.__n[6],self.__n[5],None,None,None),
        (None,None,self.__n[2],None,self.__n[6],None,self.__n[0],None),
        (None,None,self.__n[3],self.__n[8],self.__n[7],self.__n[6],self.__n[1],None),
        (None,None,self.__n[4],None,self.__n[8],None,self.__n[2],None),
        (None,None,None,None,self.__n[9],self.__n[8],self.__n[3],None),
        (self.__n[0],None,self.__n[6],None,self.__n[10],None,None,None),
        (self.__n[1],self.__n[2],self.__n[7],self.__n[12],self.__n[11],self.__n[10],self.__n[5],self.__n[0]),
        (self.__n[2],None,self.__n[8],None,self.__n[12],None,self.__n[6],None),
        (self.__n[3],self.__n[4],self.__n[9],self.__n[14],self.__n[13],self.__n[12],self.__n[7],self.__n[2]),
        (self.__n[4],None,None,None,self.__n[14],None,self.__n[8],None),
        (self.__n[5],self.__n[6],self.__n[11],self.__n[16],self.__n[15],None,None,None),
        (self.__n[6],None,self.__n[12],None,self.__n[16],None,self.__n[10],None),
        (self.__n[7],self.__n[8],self.__n[13],self.__n[18],self.__n[17],self.__n[16],self.__n[11],self.__n[6]),
        (self.__n[8],None,self.__n[14],None,self.__n[18],None,self.__n[12],None),
        (self.__n[9],None,None,None,self.__n[19],self.__n[18],self.__n[13],self.__n[8]),
        (self.__n[10],None,self.__n[16],None,self.__n[20],None,None,None),
        (self.__n[11],self.__n[12],self.__n[17],self.__n[22],self.__n[21],self.__n[20],self.__n[15],self.__n[10]),
        (self.__n[12],None,self.__n[18],None,self.__n[22],None,self.__n[16],None),
        (self.__n[13],self.__n[14],self.__n[19],self.__n[24],self.__n[23],self.__n[22],self.__n[17],self.__n[12]),
        (self.__n[14],None,None,None,self.__n[24],None,self.__n[18],None),
        (self.__n[15],self.__n[16],self.__n[21],None,None,None,None,None),
        (self.__n[16],None,self.__n[22],None,None,None,self.__n[20],None),
        (self.__n[17],self.__n[18],self.__n[23],None,None,None,self.__n[21],self.__n[16]),
        (self.__n[18],None,self.__n[24],None,None,None,self.__n[22],None),
        (self.__n[19],None,None,None,None,None,self.__n[22],self.__n[23]))
        px = 180
        py = 80
        for i in range(len(self.__n)):
            self.__n[i].set_data(pointers[i], px, py)
            px += 100
            if px > 580:
                px = 180
                py += 100
    
    def get_method(self):
        return self.__n

    def clear_list(self):
        self.__n.clear()