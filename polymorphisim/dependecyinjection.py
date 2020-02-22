class flight:
    def __init__(self,engine):
        self.engine=engine

    def startEngine(self):
        self.engine.start()

class AirbusEngine:
    def start(self):
        print("Starting Airbus Engine")


class BoeingEngine:
    def start(self):
        print("Starting Boeing Engine")

ae=AirbusEngine()
f=flight(ae)
f.startEngine()