import multiprocessing as mp


class Multi:
    def __init__(self):
        self.a = 1
        self.b = 2

    def A(self):
        self.a = self.a*5
        print(self.a)

    def B(self):
        self.b = self.b*5
        print(self.b)

    def p(self):
        p1 = mp.Process(target=self.A)
        p2 = mp.Process(target=self.B)
        p1.start()
        p2.start()
        p1.join()
        p2.join()


if __name__ == '__main__':
    m = Multi()
    m.p()