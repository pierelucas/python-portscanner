# Author: PiereLucas (Julian Huch)
# MIT License - for futher information read LICENSE
# Creation: 20.10.2019
# Last update: 20.10.2019

# Module
import socket
import sys
import time
from colorama import Fore
from argparse import ArgumentParser

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
    def __init__(self, *, target_addr, target_port, start_port, end_port):
        # Details
        self.addr = target_addr
        self.port = target_port
        self.start_port = start_port
        self.end_port = end_port

    def check_port(self):
        pass

    def write_file(self):
        pass

    def make_thread(self):
        pass

    def run(self):

class Controller():

    def __init__(self):
        # Time
        self.lt = time.localtime()
        self.year, self.month, self.day = self.lt[0:3]
        self.hour, self.minute, self.second = self.lt[3:6]

        # Banner
        self.banner = "PASS"

        # Details
        self.target_addr = ""
        self.target_port = 0

    def argum(self):
        parser = ArgumentParser(description=self.banner)
        parser.add_argument("-t", "--target", dest="target_addr", required=True, metavar="Target Address")
        parser.add_argument("-p", "--port-range", dest="port_ran", required=True, metavar="Port Range")
        args = parser.parse_args()
        if self.check_argum(args=args):
            return
        else:
            print("Wrong Arguments")
            sys.exit(0)

    def check_argum(self, *, args):
        pass

    def out(self):
        pass

    def ports(self, port_range):
        # make list
        ports = port_range.split("-")
        start_port = ports[0]
        end_port = ports[1]
        return start_port, end_port

    def run(self):
        pass


if __name__ == "__main__":
    pass
