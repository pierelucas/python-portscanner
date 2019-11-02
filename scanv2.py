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


class Scanner():

    def scan_port(self, *, target_addr, target_port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.2)
            result = sock.connect_ex((target_addr, target_port))
            if result == 0:
                return True
            else:
                return False

    def time_str(self):
        lt = time.localtime()
        year, month, day = lt[0:3]
        today = f"{year:02d}_{month:02d}_{day:02d}_"
        return today

    def write_file(self, addr, port):
        str_addr = addr.replace(".", "-")
        file_name = "time{}+addr{}.txt".format(self.time_str(), str_addr)
        with open(file_name, 'a+') as f:
            f.write("[+] OPEN        [{}]:[{}]".format(addr, port))


class Controller(Scanner):

    def __init__(self):

        # Banner
        self.banner = CYAN + "Python Portscanner by PiereLucas (Julian Huch)" + RESET

        # Details
        self.target_addr = ""
        self.target_port = 0
        self.start_port = 0
        self.end_port = 0

    def argum(self):
        parser = ArgumentParser(description=self.banner)
        parser.add_argument("-t", "--target", dest="target_addr", metavar=GREEN + "Target Address" + RESET, help=CYAN + "Define Target Host" + RESET)
        parser.add_argument("-p", "--port-range", dest="port_ran", metavar=GREEN + "Port Range" + RESET, help=CYAN + "Define Port Range [N-N]" + RESET)
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
        count = 0
        print(CYAN + "Connected to [{}]".format(self.target_addr) + RESET)
        for port in range(self.start_port, self.end_port+1):
            self.target_port = port
            port_open = self.scan_port(target_addr=str(self.target_addr), target_port=int(self.target_port))
            if port_open:
                count += 1
                self.write_file(self.target_addr, port)
                print(GREEN + "[+] OPEN        [{}]:[{}]".format(self.target_addr, port) + RESET)
            else:
                print(RED + "[-] CLOSED      [{}]:[{}]".format(self.target_addr, port) + RESET)
            continue
        print(CYAN + "Sucessfully scanned host [{}] and found [{}] open ports".format(self.target_addr, count) + RESET)
        sys.exit(0)


if __name__ == "__main__":
    cc = Controller()
    cc.argum()
    cc.action()
