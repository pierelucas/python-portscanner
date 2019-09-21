#!/usr/bin/env python3

# Module
import socket
import subprocess
import sys
from datetime import datetime

# Klasse
class PortScanner_Init():

    # Methoden
    def __init__(self):

        # Zeitmessung
        self.zeitbeginn = bytes()
        self.zeitende = bytes()
        self.zeitgesamt = bytes()
        self.zeitallgemein = bytes()

        # Daten
        self.remoteServer = []
        self.remoteServerIP = bytes()

    # Ausgabe
    def __str__(self):
        return "-" * 60 + "\n" \
               + "Please wait, scanning remtoe host: " + self.remoteServerIP \
               + "\n" + "-" * 60

    # Eingabe
    def eingabe(self):

        subprocess.call('clear', shell=True)

        self.banner()

        inputs = 1
        while inputs != 0:
            try:
                self.remoteServer = input("Enter a remote host to scan: ")
                self.remoteServerIP = socket.gethostbyname(self.remoteServer)
                inputs = 0
            except KeyboardInterrupt:
                print("You presses Ctrl+C")
                sys.exit()
            except RuntimeError:
                print("Wrong Statement")
            except ValueError:
                print("You must enter a valid Host")

    # Methode zur Ermittlung von Zeitwerten
    def zeit(self, x):

        if x == 0:
            self.zeitallgemein = datetime.now()
        if x == 1:
            self.zeitbeginn = datetime.now()
        elif x == 2:
            self.zeitende = datetime.now()
        elif x == 3:
            self.zeitgesamt = self.zeitbeginn - self.zeitende

    def banner(self):
        print("-" * 60)
        print("Python Portscanner")
        print("-" * 60)


class PortScanner(PortScanner_Init):

    def __init__(self):

        PortScanner_Init.__init__(self)

        self.open = 0
        self.exit = 0

    def __str__(self):

        pass


    # Hauptprogramm
    def scan(self):

        try:
            # Portscan der Ports 1 - 35535
            for self.port in range(1, 1025):
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.result = self.sock.connect_ex((self.remoteServerIP, self.port))
                if self.result == 0:
                    print("Port {}: 	 Open".format(self.port))
                    self.open = self.port
                else:
                    print("Scanning Port: ", self.port)
                if self.port == 1024:
                    print("Port {}: 	 Open".format(self.open))
                self.sock.close()

        except KeyboardInterrupt:
            print("You presses Ctrl+C")
            sys.exit()

        except socket.gaierror:
            print("Hostname could not be resolved. Exiting")
            sys.exit()

        except socket.error:
            print("Couldn't connect to server")
            sys.exit()


# Klassenvariable
portscanner_init = PortScanner_Init()
portscanner = PortScanner()


# Eingabe
portscanner_init.eingabe()

# Ausgabe
portscanner_init.zeit(0)
print(portscanner_init.zeitallgemein)
print(portscanner_init)

# Prüfe wann der Scan startet
portscanner_init.zeit(1)

# Range Funktion zwischen 1 und 1024. Wird alle Ports zwischen 1 und 1024 Scannen
portscanner.scan()

# Prüfe die Zeit nochmal
portscanner_init.zeit(2)

# Berechne die Zeitspanne
portscanner_init.zeit(3)

# Gebe die Zeitinformation aus
print('Scanning Completed in: ', portscanner_init.zeitgesamt)
