#file to store moves classes and assoicated objects

#attack class 
class Attack:
    #constructor for pokemon attack moves
    def __init__(self, name, typ, category, power, accuracy, pp):
        self.name = name
        self.typ = typ
        self.category = category
        self.power = power
        self.accuracy = accuracy
        self.pp = pp

#list of attack type moves

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

swift = Attack('Swift', 'normal', 'special', 60, 100, 20)

thunder = Attack('Thunder', 'electric', 'special', 110, 70, 15)

headbutt = Attack('Headbutt', 'normal', 'physical', 70, 100, 15)

body_slam = Attack('Body Slam', 'normal', 'physical', 85, 100, 15)

double_edge = Attack('Double-Edge', 'normal', 'physical', 120, 100, 15)

hyper_beam = Attack('Hyper Beam', 'normal', 'special', 150, 90, 5)

splash = Attack('Splash', 'normal', 'special', 0, 100, 40)




#potions class
class Potion:
    def __init__(self, name, price, effect):
        self.name = name
        self.price = price
        self.effect = effect

potion = Potion('Potion', 300, 20)

super_potion = Potion('Super Potion', 700, 50)

hyper_potion = Potion('Hyper Potion', 1200, 200)

max_potion = Potion('Max Potion', 2500, 'full')