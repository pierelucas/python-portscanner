# Author: PiereLucas (Julian Huch)
# MIT License - for futher information read LICENSE
# Creation: 20.10.2019
# Last update: 20.10.2019

# Module
import socket
from colorama import Fore

# Colors
CYAN = Fore.CYAN
RED = Fore.RED
GREEN = Fore.GREEN
RESET = Fore.RESET

class SuperScan(socket):
    def __init__(self, fam, typ):
        super(SuperScan, self).__init__(family=fam, type=typ)

    def __str__(self):
        return GREEN + "SuperScan loaded  ..." + RESET

class Scanner():
    def __init__(self):
        pass

    def inp(self):
        pass

    def out(self):
        pass

    def check_port(self):
        pass

    def write_file(self):
        pass

    def make_thread(self):
        pass

    def run(self):


if __name__ == "__main__":
    s = Scanner()
    s.run()
