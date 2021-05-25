class Man:
    def __init__(self):
        pass

    def help(self):
        print("man helping...")

class Woman:
    def __init__(self):
        pass

    def help(self):
        print("woman helping...")

class Elephant:
    def __init(self):
        pass

    def help(self):
        print("elephant helping...")

class Fox:
    def __init__(self):
        pass


def seekHelp(helper):
    # python won't check if it's a method or field ):
    if ("help" in dir(helper)):
        helper.help()
    else:
        print("Are you kidding...")

def main():
    bob = Man()
    sarah = Woman()
    hathi = Elephant()
    fox = Fox()
    seekHelp(bob)
    seekHelp(sarah)
    seekHelp(hathi)
    seekHelp(fox)


main()