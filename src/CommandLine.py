import sys

class CommandLine:

    _args = None
    _instance = None
    _parameters = None
    __computer = int()

    def __init__(self, args):
        self._args = args

    def run(self):
        if len(self._args) != 3:
            print("Usage: python ", self._args[0], " <Computer-Number> <MDVRP-instance>")
            sys.exit(1)

        self.__computer = int(self._args[1])
        self._instance = self._args[2]

    def instance(self):
        return self._instance

    def computer(self):
        return self.__computer
