from abc import ABC, abstractmethod


class Hero:
    def __init__(self):
        self.positive_effects = []
        self.negative_effects = []
        self.stats = {
            "HP": 128,  # health points
            "MP": 42,  # magic points,
            "SP": 100,  # skill points
            "Strength": 15,  # сила
            "Perception": 4,  # восприятие
            "Endurance": 8,  # выносливость
            "Charisma": 2,  # харизма
            "Intelligence": 3,  # интеллект
            "Agility": 8,  # ловкость
            "Luck": 1  # удача
        }

    def get_positive_effects(self):
        return self.positive_effects.copy()

    def get_negative_effects(self):
        return self.negative_effects.copy()

    def get_stats(self):
        return self.stats.copy()


class AbstractEffect(Hero, ABC):
    def __init__(self, base, effect_name):
        super().__init__()
        self.effect_name = effect_name
        self.base = base

    def get_positive_effects(self):
        return self.base.get_positive_effects()

    def get_negative_effects(self):
        return self.base.get_negative_effects()

    def get_stats(self):
        self.stats = self.base.get_stats()
        self._change_stats()
        return self.stats.copy()

    @abstractmethod
    def _add_effect(self):
        pass

    @abstractmethod
    def _change_stats(self):
        pass


class AbstractPositive(AbstractEffect, ABC):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @abstractmethod
    def _change_stats(self):
        pass

    def _add_effect(self):
        self.positive_effects.append(self.effect_name)

    def get_positive_effects(self):
        self.positive_effects = self.base.get_positive_effects()
        self._add_effect()
        return self.positive_effects.copy()


class AbstractNegative(AbstractEffect, ABC):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @abstractmethod
    def _change_stats(self):
        pass

    def _add_effect(self):
        self.negative_effects.append(self.effect_name)

    def get_negative_effects(self):
        self.negative_effects = self.base.get_negative_effects()
        self._add_effect()
        return self.negative_effects.copy()


class Berserk(AbstractPositive):
    def __init__(self, *args, **kwargs):
        super().__init__(effect_name="Berserk", *args, **kwargs)

    def _change_stats(self):
        self.stats["Strength"] += 7
        self.stats["Endurance"] += 7
        self.stats["Agility"] += 7
        self.stats["Luck"] += 7
        self.stats["Perception"] -= 3
        self.stats["Charisma"] -= 3
        self.stats["Intelligence"] -= 3
        self.stats["HP"] += 50


class Blessing(AbstractPositive):
    def __init__(self, *args, **kwargs):
        super().__init__(effect_name="Blessing", *args, **kwargs)

    def _change_stats(self):
        self.stats["Strength"] += 2
        self.stats["Endurance"] += 2
        self.stats["Agility"] += 2
        self.stats["Luck"] += 2
        self.stats["Perception"] += 2
        self.stats["Charisma"] += 2
        self.stats["Intelligence"] += 2


class Weakness(AbstractNegative):
    def __init__(self, *args, **kwargs):
        super().__init__(effect_name="Weakness", *args, **kwargs)

    def _change_stats(self):
        self.stats["Strength"] -= 4
        self.stats["Endurance"] -= 4
        self.stats["Agility"] -= 4


class EvilEye(AbstractNegative):
    def __init__(self, *args, **kwargs):
        super().__init__(effect_name="EvilEye", *args, **kwargs)

    def _change_stats(self):
        self.stats["Luck"] -= 10


class Curse(AbstractNegative):
    def __init__(self, *args, **kwargs):
        super().__init__(effect_name="Curse", *args, **kwargs)

    def _change_stats(self):
        self.stats["Strength"] -= 2
        self.stats["Endurance"] -= 2
        self.stats["Agility"] -= 2
        self.stats["Luck"] -= 2
        self.stats["Perception"] -= 2
        self.stats["Charisma"] -= 2
        self.stats["Intelligence"] -= 2


if __name__ == "__main__":
    hero = Hero()
    print(hero.get_stats())
    print(hero.stats)
    print(hero.get_positive_effects())
    print(hero.get_negative_effects())
    print("Berserk")
    brs1 = Berserk(hero)
    print(brs1.get_stats())
    print(brs1.get_positive_effects())
    print(brs1.get_negative_effects())
    print("Berserk-Berserk-Curse")
    brs2 = Berserk(brs1)
    cur1 = Curse(brs2)
    print(cur1.get_stats())
    print(cur1.get_positive_effects())
    print(cur1.get_negative_effects())
    print("Снимаем эффект")
    cur1.base = brs1
    print(cur1.get_stats())
    print(cur1.get_positive_effects())
    print(cur1.get_negative_effects())

