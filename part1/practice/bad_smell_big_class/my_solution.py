class Warrior:
    def defense(self):
        pass

    def attack(self):
        pass

    def move(self):
        pass


class Healer:
    def defense(self):
        pass

    def heal(self):
        pass

    def move(self):
        pass


class Tree:
    def defense(self):
        pass

    def on_fire(self):
        pass


class Trap:
    def trap_attack(self):
        print("Ловушка!")


if __name__ == '__main__':
    unit = Warrior()
    healer = Healer()
    tree = Tree()
    trap = Trap()
