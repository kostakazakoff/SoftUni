class Weapon:
    def __init__(self, bullets):
        self.bullets = bullets
        self.charger = bullets

    def __repr__(self):
        return f'Remaining bullets: {self.charger}'

    def shoot(self):
        if self.charger == 0:
            return 'no bullets left'
        self.charger -= 1
        return 'shooting...'


weapon = Weapon(5)
print(weapon.shoot())
print(weapon.shoot())
print(weapon)
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon)