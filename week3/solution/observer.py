from abc import ABC, abstractmethod


class Engine:
    pass


class ObservableEngine(Engine):
    def __init__(self):
        super().__init__()
        self.__subscribers = set()

    def subscribe(self, subscriber):
        self.__subscribers.add(subscriber)

    def unsubscribe(self, subscriber):
        self.__subscribers.remove(subscriber)

    def notify(self, message):
        for subscriber in self.__subscribers:
            subscriber.update(message)


class AbstractObserver(ABC):

    @abstractmethod
    def update(self, message):
        pass


class ShortNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = set()

    def update(self, message):
        self.achievements.add(message["title"])


class FullNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = []

    def update(self, message):
        if message not in self.achievements:
            self.achievements.append(message)


if __name__ == "__main__":
    short = ShortNotificationPrinter()
    full = FullNotificationPrinter()

    engine = ObservableEngine()
    engine.subscribe(short)
    engine.subscribe(full)

    engine.notify({'text': 'Пройти основной сюжет игры', 'title': 'Воитель'})
    engine.notify({'text': 'Пройти основной сюжет игры', 'title': 'Воитель'})
    print(short.achievements)
    print(full.achievements)

