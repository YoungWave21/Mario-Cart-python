import random

items = ["Banana", "Green Shell", "Star", "Golden Mushroom", "Bullet Bill"]


class Player:
    def __init__(self, position):
        self.position = position
        self.totals = {"Banana": 0, "Green Shell": 0, "Star": 0, "Golden Mushroom": 0, "Bullet Bill": 0}
        self.probability = {"Banana": 0.05, "Green Shell": 0.1, "Star": 0.35, "Golden Mushroom": 0.7, "Bullet Bill": 1}

    def Set_Position(self):
        p = input("Where would you like to start?: ")
        if p.isnumeric() and 0 < int(p) < 13:
            self.position = int(p)
            if 0 < self.position <= 6:
                self.probability["Banana"] = 0.45
                self.probability["Green Shell"] = 0.8
                self.probability["Star"] = 0.95
                self.probability["Golden Mushroom"] = 0.99
                self.probability["Bullet Bill"] = 1
            elif 6 < self.position <= 12:
                self.probability["Banana"] = 0.05
                self.probability["Green Shell"] = 0.1
                self.probability["Star"] = 0.35
                self.probability["Golden Mushroom"] = 0.7
                self.probability["Bullet Bill"] = 1
        else:
            print("The posiont you have selected is not between 1 and 12. Please try again!")
            self.Set_Position()
        print("Position set successful!")

    def Run_Simulation(self, times):
        for i in range(times):
            for n in range(5):
                chance = random.random()
                if chance <= self.probability[items[n]]:
                    self.totals[items[n]] += 1
                    break

    def Run_n_Times(self):
        times = input("How many times would you like to run the simmulation? (max 1000): ")
        if times.isnumeric() and int(times) < 1000:
            self.Run_Simulation(int(times))
            print("Run successful!")
        else:
            print("The number you enterd is not between 0 and 1000")
            self.Run_n_Times()

    def Run_Once(self):
        self.Run_Simulation(1)
        print("Run successful!")

    def until_ten_Bullet(self):
        while self.totals["Bullet Bill"] < 10:
            self.Run_Simulation(1)
        print("Run successful!")

    def Reset_Totals(self):
        for i in range(len(items)):
            self.totals[items[i]] = 0
        print("Reset successful!")

    def Display_Totals(self):
        for i in range(len(items)):
            print(f'{items[i]}: {self.totals[items[i]]}')


def main():
    person = Player(12)
    while True:
        print("______________________________")
        print(f"Main Menu (Current position: {person.position})")
        print("    1. Set Position")
        print("    2. Run Simulation Once")
        print("    3. Run Simulation ‘n’ Times")
        print("    4. Run Simulation until 10 Bullet Bills")
        print("    5. Display Totals")
        print("    6. Reset Totals")
        print("    7. Exit")
        print("______________________________")
        choice = input("Your choice: ")
        if choice.isnumeric() and 0 < int(choice) < 8:
            options = {
                1: person.Set_Position,
                2: person.Run_Once,
                3: person.Run_n_Times,
                4: person.until_ten_Bullet,
                5: person.Display_Totals,
                6: person.Reset_Totals,
                7: exit,
            }
            options[int(choice)]()
        else:
            print("The option you have selected does not exist!")


main()
