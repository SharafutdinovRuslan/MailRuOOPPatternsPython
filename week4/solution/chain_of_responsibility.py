class SomeObject:
    def __init__(self):
        self.integer_field = 0
        self.float_field = 0.0
        self.string_field = ""


class EventGet:
    def __init__(self, type):
        self.type = type
        self.event_type = "get"


class EventSet:
    def __init__(self, value):
        self.value = value
        self.event_type = "set"


class NullHandler:
    def __init__(self, successer=None):
        self.__successer = successer

    def handle(self, object, event):
        if self.__successer is not None:
            return self.__successer.handle(object, event)


class IntHandler(NullHandler):
    def handle(self, object, event):
        if event.event_type == "get":
            if event.type == int:
                return object.integer_field
            return super().handle(object, event)
        elif event.event_type == "set":
            if isinstance(event.value, int):
                object.integer_field = event.value
            else:
                super().handle(object, event)
        else:
            raise ValueError(f"Event type {event.event_type} is not supported")


class FloatHandler(NullHandler):
    def handle(self, object, event):
        if event.event_type == "get":
            if event.type == float:
                return object.float_field
            return super().handle(object, event)
        elif event.event_type == "set":
            if isinstance(event.value, float):
                object.float_field = event.value
            else:
                super().handle(object, event)
        else:
            raise ValueError(f"Event type {event.event_type} is not supported")


class StrHandler(NullHandler):
    def handle(self, object, event):
        if event.event_type == "get":
            if event.type == str:
                return object.string_field
            return super().handle(object, event)
        elif event.event_type == "set":
            if isinstance(event.value, str):
                object.string_field = event.value
            else:
                super().handle(object, event)
        else:
            raise ValueError(f"Event type {event.event_type} is not supported")


if __name__ == "__main__":
    obj = SomeObject()
    obj.integer_field = 42
    obj.float_field = 3.14
    obj.string_field = "some text"
    chain = IntHandler(FloatHandler(StrHandler(NullHandler)))
    print(chain.handle(obj, EventGet(int)))
    print(chain.handle(obj, EventGet(float)))
    print(chain.handle(obj, EventGet(str)))
    chain.handle(obj, EventSet(100))
    print(chain.handle(obj, EventGet(int)))
    chain.handle(obj, EventSet(0.5))
    print(chain.handle(obj, EventGet(float)))
    chain.handle(obj, EventSet('new text'))
    print(chain.handle(obj, EventGet(str)))
