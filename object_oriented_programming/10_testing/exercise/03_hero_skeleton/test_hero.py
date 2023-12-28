from unittest import TestCase, main
from hero import Hero


class TestHero(TestCase):

    def setUp(self):
        self.mage = Hero("Merlin", 9000, 9999.0, 9999.0)
        self.enemy_hero = Hero("Badguy", 9000, 9999.0, 9999.0)

    def test_initializing(self):
        self.assertEqual("Merlin", self.mage.username)
        self.assertEqual(9000, self.mage.level)
        self.assertEqual(9999.0, self.mage.health)
        self.assertEqual(9999.0, self.mage.damage)

    def test_attributes_types(self):
        self.assertIsInstance(self.mage.username, str)
        self.assertIsInstance(self.mage.level, int)
        self.assertIsInstance(self.mage.health, float)
        self.assertIsInstance(self.mage.damage, float)

    def test_method_battle_against_hero_with_same_username_raises_error(self):
        self.enemy_hero.username = "Merlin"
        with self.assertRaises(Exception) as ex:
            self.mage.battle(self.enemy_hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_method_battle_while_hero_has_no_health_raises_error(self):
        self.mage.health = 0
        with self.assertRaises(ValueError) as ve:
            self.mage.battle(self.enemy_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_method_battle_while_enemy_has_no_health_raises_error(self):
        self.enemy_hero.health = 0
        with self.assertRaises(ValueError) as ve:
            self.mage.battle(self.enemy_hero)
        self.assertEqual(f"You cannot fight {self.enemy_hero.username}. He needs to rest", str(ve.exception))

    def test_method_battle_result_with_draw(self):
        result = self.mage.battle(self.enemy_hero)
        self.assertEqual("Draw", result)

    def test_method_battle_result_with_win(self):
        self.enemy_hero.damage = 1
        result = self.mage.battle(self.enemy_hero)
        self.assertEqual("You win", result)
        self.assertEqual(9001, self.mage.level)
        self.assertEqual(1004.0, self.mage.health)
        self.assertEqual(10004.0, self.mage.damage)

    def test_method_battle_result_with_lose(self):
        self.mage.damage = 1
        result = self.mage.battle(self.enemy_hero)
        self.assertEqual("You lose", result)
        self.assertEqual(9001, self.enemy_hero.level)
        self.assertEqual(1004.0, self.enemy_hero.health)
        self.assertEqual(10004.0, self.enemy_hero.damage)

    def test_successfully_using_str_method(self):
        expected_return = f"Hero {self.mage.username}: {self.mage.level} lvl\n" \
               f"Health: {self.mage.health}\n" \
               f"Damage: {self.mage.damage}\n"
        self.assertEqual(expected_return, str(self.mage))


if __name__ == "__main__":
    main()