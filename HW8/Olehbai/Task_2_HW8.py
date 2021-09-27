class Car:
    def __init__(self, name, kind, model):
        self.name = name
        self.kind = kind
        self.model = model

    def start(self):
        print(f"\nYou start the engine of {self.name} {self.kind} {self.model}\n")
    def stop(self):
        print(f"You turned off the engine of {self.name} {self.kind} {self.model}")

Audi = Car("Audi", "RS", "7")
Audi.start()
Audi.stop()
