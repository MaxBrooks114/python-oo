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

    def __init__(self):
        self.fly = self.aviate

    def walk(self):
        print("waddle but like a penguin")

    def swim(self):
        print("SWIMMING but like a penguin")

    def quack(self):
        print("quack")

    def aviate(self):
        print("I won the lottery and bought a lear jet")



class Mallard(Duck):
    pass


class Flock:

    def __init__(self):
        self.flock = []

    def add_duck(self, duck: Duck) -> None:
        fly_method = getattr(duck, 'fly', None)
        # if isinstance(duck, Duck):
        if callable(fly_method):
            self.flock.append(duck)
        else:
            raise TypeError("Cannot add duck, it is a " + str(type(duck).__name__))

    def migrate(self):
        problem = None
        for duck in self.flock:
            try:
                duck.fly()
                raise AttributeError("Testing exception handler in migrate") #TODO remove this before release
            except AttributeError as e:
                print("one duck didn't make it")
                problem = e

        if problem:
            raise problem

if __name__ == "__main__":
    donald = Duck()
    donald.fly()


    #
    # penny = Penguin()
    # test_duck(penny)



