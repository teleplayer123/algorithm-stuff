from random import random

class Perceptron(object):

    def __init__(self, x, y, learn_rate=0.1, epochs=6):
        self.x = x
        self.y = y
        self.learn_rate = learn_rate
        self.epochs = epochs
    
    def init_weights(self):
        self.weights = [[random()] for _ in range(len(self.x[0])+1)]

    def init_bias(self):
        for row in range(len(self.x)):
            self.x[row].append(-1)

    def train(self):
        for _ in range(self.epochs):
            a = self.activate(self.x) 
            e = self.calc_error(a, self.y)
            self.update_weights(transpose(self.x), e)
        return a

    def update_weights(self, x, e):
        res = [[0] for _ in range(len(self.x))]
        for d in range(len(x)):
            for n in range(len(e[0])):
                for m in range(len(x[0])):
                    res[m][n] += x[d][m] * e[m][n]
                    self.weights[d][n] -= self.learn_rate * res[m][n]

    def calc_error(self, a, y):
        e = [[None] for _ in range(len(self.x))]
        for n in range(len(a)):
            for m in range(len(a[0])):
                e[n][m] = a[n][m] - y[n][m]
        return e 
                    
    def activate(self, x):
        a = [[0] for _ in range(len(self.x))] 
        for d in range(len(x)):
            for n in range(len(self.y[0])):
                for m in range(len(x[0])):
                    a[d][n] += self.weights[m][n] * x[d][m]
                if a[d][n] > 0:
                    a[d][n] = 1
                else:
                    a[d][n] = 0
        return a

    def predict(self, x):
        a = [[0] for _ in range(len(x))] 
        for d in range(len(x)):
            for n in range(len(self.y[0])):
                for m in range(len(x[0])):
                    a[d][n] += self.weights[m][n] * x[d][m]
                a[d][n] = int(a[d][n] > 0)
        return a

def transpose(matrix):
    return [[matrix[y][x] for y in range(len(matrix))] for x in range(len(matrix[0]))]

x = [[0,0],[0,1],[1,0],[1,1]]
y = [[0], [0], [0], [1]]
p = Perceptron(x, y)
p.init_weights()
p.init_bias()
res = p.train()
print(p.predict(x))
print(res)