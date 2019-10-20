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
    def __init__(self, *, target_addr, target_port):
        # Details
        self.addr = target_addr
        self.port = target_port

    def scan_port(self):
        pass

    def write_file(self):
        pass

    def make_thread(self):
        pass

    def run(self):
        pass

class Controller(Scanner):

    def __init__(self):
        # Super Constructor
        super(Controller, self).__init__(target_addr=self.target_addr, target_port=self.target_port)

        # Time
        self.lt = time.localtime()
        self.year, self.month, self.day = self.lt[0:3]
        self.hour, self.minute, self.second = self.lt[3:6]

        # Banner
        self.banner = "PASS"

        # Details
        self.target_addr = ""
        self.target_port = 0
        self.start_port = 0
        self.end_port = 0

    def argum(self):
        parser = ArgumentParser(description=self.banner)
        parser.add_argument("-t", "--target", dest="target_addr", required=True, metavar="Target Address")
        parser.add_argument("-p", "--port-range", dest="port_ran", required=True, metavar="Port Range")
        args = parser.parse_args()
        if self.check_argum(args=args):
            return

    def check_argum(self, *, args):
        if args.target_addr and args.port_ran:
            self.target_addr = args.target_addr
            self.start_port, self.end_port = self.ports(args.port_ran)
            return True
        elif args.target_addr:
            print("No Port Range defined")
            sys.exit(0)
        elif args.port_ran:
            print("No target address defined")
            sys.exit(0)
        else:
            print("Use -h or --help")
            sys.exit(0)

    def ports(self, port_range):
        # make list
        try:
            ports = port_range.split("-")
            start_port = int(ports[0])
            end_port = int(ports[1])
        except Exception:
            print("please define port range in format [1-x]")
            sys.exit(0)
        else:
            return start_port, end_port

    def action(self):
        for port in range(self.start_port, self.end_port+1):



    def run(self):
        # Start time
        self.argum()



if __name__ == "__main__":
    pass
