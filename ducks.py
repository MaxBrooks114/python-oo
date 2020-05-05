class Wing:
    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("I'm flying")
        elif self.ratio == 1:
            print("I'm sort of flying")

        else:
            print("Can't fly")



class Duck(object):

    def __init__(self):
        self._wing = Wing(1.8)

    def walk(self):
        print("waddle")

    def swim(self):
        print("SWIMMING")

    def quack(self):
        print("quack")

    def fly(self):
        self._wing.fly()


class Penguin(object):

    def walk(self):
        print("waddle but like a penguin")

    def swim(self):
        print("SWIMMING but like a penguin")

    def quack(self):
        print("quack")
#
# def test_duck(duck):
#     duck.walk()
#     duck.swim()
#     duck.quack()

if __name__ == "__main__":
    donald = Duck()
    donald.fly()


    #
    # penny = Penguin()
    # test_duck(penny)



