f = open("input.txt", "r")


class Module:
    def __init__(self, receivers):
        self.receivers = receivers


class Broadcaster(Module):
    def receive(self, pulse):
        for receiver in self.receivers:
            receiver.receive(pulse)

class FlipFlop(Module):
    pass




broadcaster = Broadcaster()
flip_flops = dict()
conjuctions = dict()

for line in f:
    if "broadcaster" in line:
        broadcaster += [i.strip() for i in line.split("->")[1].split(",")]
    elif "%" in line:
        flip_flops[line.split("->")[0].strip().removeprefix("%")] = (
            [i.strip() for i in line.split("->")[1].split(",")])
    elif "&" in line:
        conjuctions[line.split("->")[0].strip().removeprefix("%")] = (
            [i.strip() for i in line.split("->")[1].split(",")])
