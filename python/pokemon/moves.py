#file to store moves classes and assoicated objects

#attack class 
class Attack:
    #constructor for pokemon attack moves
    def __init__(self, name, type, category, power, accuracy, pp):
        self.name = name
        self.typ = typ
        self.category = category
        self.power = power
        self.accuracy = accuracy
        self.pp = pp

#list of Normal type moves
#16, moves.swift: 26, moves.thunder: 43})

tackle = Attack('Tackle', 'normal', 'physical', 40, 100, 35)

vine_whip = Attack('Vine Whip', 'grass', 'physical', 45, 100, 25)

razor_leaf = Attack('Razor Leaf', 'grass', 'physical', 55, 95, 25)

solar_beam = Attack('Solar Beam', 'grass', 'special', 120, 100, 10)

scratch = Attack('Scratch', 'Normal', 'physical', 40, 100, 35)

ember = Attack('Ember', 'Fire', 'Special', 40, 100, 25)

rage = Attack('Rage', 'Normal', 'Physical', 20, 100, 20)

slash = Attack('Slash', 'Normal', 'Physical', 70, 100, 20)

flamethrower = Attack('Flamethrower', 'Fire', 'Special', 90, 100, 15)

fire_spin = Attack('Fire Spin', 'Fire', 'Special', 35, 85, 15)

bubble = Attack('Bubble', 'water', 'special', 40, 100, 30)

water_gun = Attack('Water Gun', 'water', 'special', 40, 100, 25)

bite = Attack('Bite', 'dark', 'physical', 60, 100, 25)
 
skull_bash = Attack('Skull Bash', 'normal', 'physical', 130, 100, 10)

hydro_pump = Attack('Hydro Pump', 'water', 'special', 110, 80, 5)

thunder_shock = Attack('Thunder Shock', 'electric', 'special', 40, 100, 30)

quick_attack = Attack('Quick Attack', 'normal', 'physical', 40, 100, 30)

swift = Attack('Swift', 'normal', 'special', 60, 100, 30)

