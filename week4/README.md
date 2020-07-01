## Паттерн Цепочка обязанностей (Chain of responsibility)

Паттерн относится к классу поведенческих. 

Условия применения Chain of Responsibility:
* Присутствуют типизированные сообщения
* Все сообщения должны быть обработаны хотя бы один раз
* Работа с сообщением: делай сам или передай другому

Пример реализации: 

```python
QUEST_SPEAK, QUEST_HUNT, QUEST_CARRY = "QSPEAK", "QHUNT", "QCARRY"


class Character:
    def __init__(self):
        self.name = "Nagibator"
        self.xp = 0
        self. passed_quests = set()
        self. taken_quests = set()


class Event:

    def __init__(self, kind):
        self.kind = kind


class NullHandler:
    def __init__(self, successor=None):
        self.__successor = successor

    def handle(self, char, event):
        if self.__successor is not None:
            self.__successor.handle(char, event)


class HandleQSpeak(NullHandler):
    def handle(self, char, event):
        if event.kind == QUEST_SPEAK:
            quest_name = "Поговорить с фермером"
            xp = 100
            if event.kind not in (char.passed_quests | char.taken_quests):
                print(f"Квест получен: \"{quest_name}\"")
                char.taken_quests.add(event.kind)
            elif event.kind in char.taken_quests:
                print(f"Квест сдан: \"{quest_name}\"")
                char.passed_quests.add(event.kind)
                char.taken_quests.remove(event.kind)
                char.xp += xp
        else:
            print("Передаю обработку дальше")
            super().handle(char, event)


class HandleQHunt(NullHandler):
    def handle(self, char, event):
        if event.kind == QUEST_HUNT:
            xp = 300
            quest_name = "Охота на крыс"
            if event.kind not in (char.passed_quests | char.taken_quests):
                print(f"Квест получен: \"{quest_name}\"")
                char.taken_quests.add(event.kind)
            elif event.kind in char.taken_quests:
                print(f"Квест сдан: \"{quest_name}\"")
                char.passed_quests.add(event.kind)
                char.taken_quests.remove(event.kind)
                char.xp += xp
        else:
            print("Передаю обработку дальше")
            super().handle(char, event)


class HandleQCarry(NullHandler):
    def handle(self, char, event):
        if event.kind == QUEST_CARRY:
            xp = 200
            quest_name = "Принести доски из сарая"
            if event.kind not in (char.passed_quests | char.taken_quests):
                print(f"Квест получен: \"{quest_name}\"")
                char.taken_quests.add(event.kind)
            elif event.kind in char.taken_quests:
                print(f"Квест сдан: \"{quest_name}\"")
                char.passed_quests.add(event.kind)
                char.taken_quests.remove(event.kind)
                char.xp += xp
        else:
            print("Передаю обработку дальше ")
            super().handle(char, event)


class QuestGiver:
    def __init__(self):
        self.handlers = HandleQSpeak(HandleQHunt(HandleQCarry(NullHandler)))
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def handle_quests(self, character):
        for event in self.events:
            self.handlers.handle(character, event)


if __name__ == "__main__":
    events = [Event(QUEST_SPEAK), Event(QUEST_HUNT), Event(QUEST_CARRY)]
    quest_giver = QuestGiver()
    for event in events:
        quest_giver.add_event(event)

    player = Character()
    quest_giver.handle_quests(player)
    print()
    player.taken_quests = {QUEST_CARRY, QUEST_SPEAK}
    quest_giver.handle_quests(player)
    print()
    quest_giver.handle_quests(player)

```

## Паттерн Абстрактная фабрика (Abstract Factory)

Для программы не имеет значения, как создаются компоненты. Необходима лишь "фабрика", производящая компоненты, 
умеющие взаимодействовать друг с другом. 

### Реализация шаблона Абстрактная фабрика
**Этап проектирования приложения**
* Работа с **абстрактной фабрикой** - класс с описанием всех создаваемых объектов без реализации
**Этап выполнения**
* Передается **реальная фабрика** - класс с реализацией создания всех компонент

### Пример реализации

```python
class HeroFactory:
    @classmethod
    def create_hero(cls, name):
        return cls.Hero(name)

    @classmethod
    def create_spell(cls):
        return cls.Spell()

    @classmethod
    def create_weapon(cls):
        return cls.Weapon()


class WarriorFactory(HeroFactory):

    class Hero:
        def __init__(self, name):
            self.name = name
            self.spell = None
            self.weapon = None

        def add_weapon(self, weapon):
            self.weapon = weapon

        def add_spell(self, spell):
            self.spell = spell

        def hit(self):
            print(f"Warrior {self.name} hits with {self.weapon.hit()}")

        def cast(self):
            print(f"Warrior {self.name} casts {self.spell.cast()}")

    class Weapon:

        def hit(self):
            return "Claymore"

    class Spell:
        def cast(self):
            return "Power"


def create_hero(factory):
    hero = factory.create_hero("Nagibator")

    weapon = factory.create_weapon()
    spell = factory.create_spell()

    hero.add_weapon(weapon)
    hero.add_spell(spell)

    return hero


if __name__ == "__main__":
    player = create_hero(WarriorFactory())
    player.hit()
    player.cast()

```

## Конфигурирование через YAML
Пример реализации: 
```python
import yaml


hero_yaml = """
--- !Character
factory: 
    !factory warrior
name:
    Nagibator
"""


class HeroFactory:
    @classmethod
    def create_hero(cls, name):
        return cls.Hero(name)

    @classmethod
    def create_spell(cls):
        return cls.Spell()

    @classmethod
    def create_weapon(cls):
        return cls.Weapon()


class WarriorFactory(HeroFactory):

    class Hero:
        def __init__(self, name):
            self.name = name
            self.spell = None
            self.weapon = None

        def add_weapon(self, weapon):
            self.weapon = weapon

        def add_spell(self, spell):
            self.spell = spell

        def hit(self):
            print(f"Warrior {self.name} hits with {self.weapon.hit()}")

        def cast(self):
            print(f"Warrior {self.name} casts {self.spell.cast()}")

    class Weapon:

        def hit(self):
            return "Claymore"

    class Spell:
        def cast(self):
            return "Power"


def factory_constructor(loader, node):
    data = loader.construct_scalar(node)
    if data == "warrior":
        return WarriorFactory


class Character(yaml.YAMLObject):
    yaml_tag = "!Character"

    def create_hero(self):
        hero = self.factory.create_hero(self.name)

        weapon = self.factory.create_weapon()
        spell = self.factory.create_spell()

        hero.add_weapon(weapon)
        hero.add_spell(spell)

        return hero


if __name__ == "__main__":
    loader = yaml.Loader
    loader.add_constructor("!factory", factory_constructor)
    hero = yaml.load(hero_yaml, loader).create_hero()
    hero.hit()
    hero.cast()

```