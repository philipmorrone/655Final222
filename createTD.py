class TD:
    count = 0

    def __init__(self):
        TD.count += 1
        self.initTD = []

        self.ins1 = ["F", "D", "X", "M", "W"]
        self.ins2 = ["-", "F", "D", "X", "M", "W"]
        self.ins3 = ["-", "-", "F", "D", "X", "M", "W"]
        self.ins4 = ["-", "-", "-", "F", "D", "X", "M", "W"]

        self.initTD.append(self.ins1)
        self.initTD.append(self.ins2)
        self.initTD.append(self.ins3)
        self.initTD.append(self.ins4)

    def retIns(self):
        return self.ins1




