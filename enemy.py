import random
class Enemy:

    def __init__(self, name="Enemy", hit_points=0, lives=1):
        self._name = name
        self._hit_points = hit_points
        self._lives = lives
        self._alive = True

    def take_damage(self, damage):
        remaining_points = self._hit_points - damage
        if remaining_points >= 0:
            self._hit_points = remaining_points
            print("Ouuch, I was hit for {} damage and {} life left.".format(damage, self._hit_points))
        else:
            self._lives -= 1
            if self._lives > 0:
                print("{0._name} lost a life, and has {0._lives} lives left".format(self))
            else:
                print("{0._name} is dead".format(self))
                self._alive = False

    def __str__(self):
        return "Name: {0._name}, Lives: {0._lives}, Hit points: {0._hit_points}".format(self)


class Troll(Enemy):

    def __init__(self, name):
        super().__init__(name=name, lives=1, hit_points=23)

    def grunt(self):
        print("Me {0._name}, me stomp you".format(self))


class Vampire(Enemy):

    def __init__(self, name):
        super().__init__(name=name, lives=3, hit_points=12)


    def dodges(self):
        if random.randint(1,3) == 3:
            print("{0._name} dodged your blow!".format(self))
            return True
        else:
            return False

    def take_damage(self, damage):
        if not self.dodges():
            super().take_damage(damage=damage)


class VampireKing(Vampire):

    def __init__(self, name):
        super().__init__(name)
        self._hit_points = 140

    def take_damage(self, damage):
        super().take_damage(damage//4)

