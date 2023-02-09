from unittest import TestCase, main
from hero.project.hero import Hero


class TestHero(TestCase):
    def setUp(self) -> None:
        self.hero = Hero("Hero", 2, 10.5, 5.5)
        self.enemy = Hero("Enemy", 1, 8.5, 2.5)

    def test__initialising(self):
        self.assertEqual("Hero", self.hero.username)
        self.assertEqual(2, self.hero.level)
        self.assertEqual(10.5, self.hero.health)
        self.assertEqual(5.5, self.hero.damage)

    def test__battle__hero_and_enemy_equality(self):
        self.enemy.username = self.hero.username
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test__battle__hero_health_zero_or_less(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test__battle__enemy_health_zero_or_less(self):
        self.enemy.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)
        self.assertEqual("You cannot fight Enemy. He needs to rest", str(ve.exception))

    def test__battle__hero_health(self):
        self.hero.battle(self.enemy)
        self.assertEqual(13.0, self.hero.health)

    def test__battle__enemy_health(self):
        self.hero.battle(self.enemy)
        self.assertEqual(-2.5, self.enemy.health)

    def test__battle__draw(self):
        self.hero.level, self.hero.damage, self.hero.health = 1, 1, 1
        self.enemy.level, self.enemy.damage, self.enemy.health = 1, 1, 1
        result = self.hero.battle(self.enemy)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(0, self.hero.health)
        self.assertEqual(0, self.enemy.health)
        self.assertEqual('Draw', result)

    def test__battle__hero_win(self):
        self.hero.level, self.hero.damage, self.hero.health = 2, 2, 2
        self.enemy.level, self.enemy.damage, self.enemy.health = 1, 1, 1
        result = self.hero.battle(self.enemy)
        self.assertEqual(3, self.hero.level)
        self.assertEqual(1, self.enemy.level)
        self.assertEqual(6, self.hero.health)
        self.assertLessEqual(self.enemy.health, 0)
        self.assertEqual("You win", result)

    def test__battle__hero_lose(self):
        self.hero.level, self.hero.damage, self.hero.health = 1, 1, 1
        self.enemy.level, self.enemy.damage, self.enemy.health = 2, 2, 2
        result = self.hero.battle(self.enemy)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(3, self.enemy.level)
        self.assertEqual(6, self.enemy.health)
        self.assertLessEqual(self.hero.health, 0)
        self.assertEqual("You lose", result)

    def test__str__output(self):
        expected = "Hero Hero: 2 lvl\n" \
                   "Health: 10.5\n" \
                   "Damage: 5.5\n"
        self.assertEqual(expected, self.hero.__str__())


if __name__ == '__main__':
    main()
