import ducks

flock = ducks.Flock()

donald = ducks.Duck()
daisy = ducks.Duck()
bart = ducks.Duck()
floeng = ducks.Duck()
groon = ducks.Duck()
percy = ducks.Penguin()


flock.add_duck(donald)
flock.add_duck(daisy)
flock.add_duck(bart)
flock.add_duck(floeng)
flock.add_duck(groon)
flock.add_duck(percy)

flock.migrate()



