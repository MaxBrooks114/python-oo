from enemy import Enemy, Troll, Vampire

ugly_troll = Troll("Pug")
print("Ugly troll -{}".format(ugly_troll))


another_troll = Troll("Ug")
print("Another troll -{}".format(another_troll))

brother = Troll("Ugr")
print(brother)
ugly_troll.grunt()

brother.take_damage(4)
print(brother)

dracula = Vampire("Dracula")

dracula.take_damage(3)

print(dracula)


while dracula.alive:
    dracula.take_damage(3)

