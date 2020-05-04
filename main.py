from player import Player

tim = Player("Tim")

print(tim.name)
print(tim.lives)
tim.lives -= 1
print(tim.lives)
tim.lives -= 1
print(tim.lives)
tim.lives -= 1
print(tim.lives)
tim.lives -= 1
print(tim.lives)
print(tim)

tim._lives = 9
print(tim)
tim.level = 2
print(tim)
tim.level += 7
print(tim)
