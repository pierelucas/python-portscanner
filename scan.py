# Author: PiereLucas (Julian Huch)
# MIT License - for futher information read LICENSE
# Creation: 20.10.2019
# Last update: 20.10.2019

# Module
import socket
import sys
import string
import random
import time
from colorama import Fore
from argparse import ArgumentParser

# Colors
CYAN = Fore.CYAN
RED = Fore.RED
GREEN = Fore.GREEN
RESET = Fore.RESET

class Scanner():

    def scan_port(self, *, target_addr, target_port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            result = sock.connect_ex((target_addr, target_port))
        if result == 0:
            return True

    def rnd_str(self):
        letters = string.ascii_lowercase + string.digits
        return "".join(random.choice(letters) for i in range(4))

    def time_str(self):
        lt = time.localtime()
        year, month, day = lt[3-6]
        today = f"{year:4d}_{month:02d}_{day:02d}_"
        return today

    def write_file(self, id, target_port):
        if id == "":
            id = self.rnd_str()
            file_name = self.time_str() + id
        else:
            file_name = self.time_str() + id
        with open(file_name, 'a+') as f:
            f.write("OPEN      {}".format(target_port))
        return id

class Controller(Scanner):

    def __init__(self):

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
        id = ""
        for port in range(self.start_port, self.end_port+1):
            self.target_port = port
            port_open = self.scan_port(target_addr=self.target_addr, target_port=self.target_port)
            if port_open:
                print("[+] OPEN:      {}".format(port))
                id = self.write_file(id, port)
            continue

    def run(self):
        # Start time
        self.argum()
        self.action()


if __name__ == "__main__":
    pass
