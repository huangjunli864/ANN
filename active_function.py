# coding:utf8

class ActiveFunction:
    #x 为输入
    def sigmoid(self, x):
        res = 1/2 + (1/4)*x + (1/48)*(x**3) + (1/480)*(x**5) + (17/80640)*(x**7) + (31/1451520)*(x**9) + (691/319334400)*(x**11)
        return res