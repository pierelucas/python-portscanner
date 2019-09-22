#!/usr/bin/env python3

# Module
import socket
import subprocess
import sys
import time

# Klasse
class PortScanner_Init():

    # Methoden
    def __init__(self):

        # Zeitmessung
        self.lt = time.localtime()
        self.jahr, self.monat, self.tag = self.lt[0:3]
        self.stunde, self.minute, self.sekunde = self.lt[3:6]

        #
        self.zeitbeginn = bytes()
        self.zeitende = bytes()

        self.time_diff_sek = bytes()
        self.time_diff_min = bytes()
        self.time_diff_std = bytes()

        # Daten
        self.remoteServer = []
        self.remoteServerIP = bytes()

        # Zähler
        self.count = 0

    # Ausgabe
    def __str__(self):

        return "-" * 60 + "\n" \
               + "Please wait, scanning remote Host: " + self.remoteServerIP \
               + "\n" + "-" * 60

    def ausgabe(self, x):

        if x == 0:
            print(f"Date: {self.tag:02d}.{self.monat:02d}.{self.jahr:4d}")
            print(f"Time: {self.stunde:02d}:{self.minute:02d}:{self.sekunde:02d}")
            self.__str__()

        elif x == 1:
            print()
            print("Time Consumetion:")
            print("-" * 60)
            print("Scanning Completed in: ", self.time_diff_std, "Hours", self.time_diff_min, "Minutes", self.time_diff_sek, "Seconds")
            print(f"Date: {self.tag:02d}.{self.monat:02d}.{self.jahr:4d}")
            print(f"Time: {self.stunde:02d}:{self.minute:02d}:{self.sekunde:02d}")

    # Eingabe
    def eingabe(self):

        # Terminal leeren
        subprocess.call('clear', shell=True)

        # Banneraufruf
        self.banner()

        # Schleifeninitialisierung
        self.inputs = 1
        self.frageschleife = 1

        # Eingabeschleife
        while self.inputs != 0:
            try:
                print()
                self.remoteServer = input("Enter a remote host to scan: ")
                self.remoteServerIP = socket.gethostbyname(self.remoteServer)

                # Eingabebestätigung
                while self.frageschleife != 0:
                    print("Scan:", self.remoteServer, "IP:", self.remoteServerIP, "Press [Y] to start and [N] to abort")
                    self.frage = input()
                    if "y" in self.frage:
                        self.inputs = 0
                        self.frageschleife = 0
                    elif "n" in self.frage:
                        print("Aborted!")
                        sys.exit()
                    elif "y" or "n" not in self.frage:
                        print("Wrong Value, Try Again!")
                        continue

            # Fehlerbehandlung
            except KeyboardInterrupt:
                print()
                print("You presses Ctrl+C")
                sys.exit()
            except RuntimeError:
                print()
                print("Wrong Statement")
                sys.exit()
            except ValueError:
                print()
                print("You must enter a valid Host")
                sys.exit()

    # Methode zur Ermittlung von Zeitwerten
    def zeit(self, x):

        if x == 1:
            self.zeitbeginn = time.localtime()
        elif x == 2:
            self.zeitende = time.localtime()

        # Berechnung von Zeitspannen
        elif x == 3:
            self.zeitbeginn = time.mktime(self.zeitbeginn)
            self.zeitende = time.mktime(self.zeitende)
            self.time_diff_sek = self.zeitbeginn - self.zeitende
            self.time_diff_min = self.time_diff_sek/60
            self.time_diff_std = self.time_diff_min/60

    # Banner
    def banner(self):
        print("-" * 60)
        print("Python Portscanner")
        print("Author: PiereLucas")
        print("-" * 60)


class PortScanner(PortScanner_Init):

    def __init__(self):

        # Init der Basisklasse, Eigenschaften werden übernommen
        PortScanner_Init.__init__(self)

        # Offenner Ports wird hier gespeichert
        self.open = 0

        # Anzahl der offenen Ports wird hier gespeichert
        self.count = 0

        # Alle offenen Ports werden in dieser Liste gespeichert
        self.portlist = []

    def __str__(self):

        pass

    # Hauptprogramm
    def scan(self):

        try:
            # Portscan der Ports 1 - 35535
            for self.port in range(1, 35536):
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.result = self.sock.connect_ex((self.remoteServerIP, self.port))
                if self.result == 0:
                    print("<-")
                    print("Port {}: 	 Open".format(self.port))
                    print("->")
                    self.count += 1
                    self.open = self.port
                    self.portlist.append(self.port)

                # Gebe Ports wieder
                else:
                    print("Scanning Port: ", self.port)

                # Ausgabe über offene Ports
                if self.port == 35535:
                    print()
                    print("Results:", self.count, "Open Ports found")
                    print("-" * 60)
                    print("Port {}: 	 Open".format(self.portlist))
                self.sock.close()

        # Fehlerbehandlung während des Scans
        except KeyboardInterrupt:
            print()
            print("You presses Ctrl+C")
            sys.exit()

        except socket.gaierror:
            print()
            print("Hostname could not be resolved. Exiting")
            sys.exit()

        except socket.error:
            print()
            print("Couldn't connect to server")
            sys.exit()


# Instanzobjekte
portscanner_init = PortScanner_Init()
portscanner = PortScanner()

# Eingabe
portscanner_init.eingabe()

# Ausgabe über laufenden Scan
portscanner_init.ausgabe(0)

# Prüfe wann der Scan startet
portscanner_init.zeit(1)

# Hauptfunktion
portscanner.scan()

# Prüfe die Zeit nochmal
portscanner_init.zeit(2)

# Berechne die Zeitspanne
portscanner_init.zeit(3)

# Gebe die Zeitinformation aus
portscanner_init.ausgabe(1)
