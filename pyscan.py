#!/usr/bin/env python3

# Module
import socket, subprocess ,sys, time
from collections import deque

# Colorama
import colorama
colorama.init()

# Klasse mit Eigenschaften, Eingabe, Ausgabe und Zeitberechnung
class PortScanner_Init:

    # Methoden
    def __init__(self):

        # Zeitmessung
        self.lt = time.localtime()
        self.jahr, self.monat, self.tag = self.lt[0:3]
        self.stunde, self.minute, self.sekunde = self.lt[3:6]

        # Erfassung von Zeitwerten
        self.zeitbeginn = bytes()
        self.zeitende = bytes()

        # Werte für die Berechnung von Differenzen
        self.time_diff_sek = bytes()
        self.time_diff_min = bytes()
        self.time_diff_std = bytes()

        # Zieldaten des Hosts
        self.remoteServer = []
        self.remoteServerIP = bytes()

        # Verbose Modus
        self.verbose = False

        # Anzahl der offenen Ports wird hier gespeichert
        self.count = 0

        # Alle offenen Ports werden in dieser Liste gespeichert
        self.portlist = deque([])

    # Ausgabe
    def __str__(self):

        return "-" * 60 + "\n" \
               + "Please wait, Starting to scan remote Host: " + self.remoteServerIP \
               + "\n" + "-" * 60

    def ausgabe(self, x):

        if x == 0:
            print(f"Date: {self.tag:02d}.{self.monat:02d}.{self.jahr:4d}")
            print(f"Time: {self.stunde:02d}:{self.minute:02d}:{self.sekunde:02d}")
            print()
            time.sleep(1)
            print(self.__str__())
            time.sleep(3)

        elif x == 1:
            print()
            print("Time Consumetion:")
            print("-" * 60)
            print("Scanning Completed in: ", self.time_diff_std, "Hours", self.time_diff_min, "Minutes", self.time_diff_sek, "Seconds")
            print(f"Date: {self.tag:02d}.{self.monat:02d}.{self.jahr:4d}")
            print(f"Time: {self.stunde:02d}:{self.minute:02d}:{self.sekunde:02d}")

        elif x == 2:
            print()
            print(colorama.Fore.RED + "Scanner Closed!")

    # Eingabe
    def eingabe(self):

        # Terminal leeren, Leere Datei erzeugen
        subprocess.call('clear', shell=True)
        subprocess.call('touch results.txt', shell=True)

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
                    print("Scan:", self.remoteServer, "IP:", self.remoteServerIP, "Press [y] to start and [n] to abort")
                    self.frage = input()
                    if "y" in self.frage:
                        self.inputs = 0
                        self.frageschleife = 0
                        # Frage ob verbose mode aktiviert werden soll
                        while self.frageschleife != 1:
                            print()
                            print("Verbose mode on [y] or off [n]")
                            self.frage = input()
                            if "y" in self.frage:
                                print()
                                print("Verbose Activated!")
                                print()
                                self.verbose = True
                                self.frageschleife = 1
                            elif "n" in self.frage:
                                print()
                                print("Verbose Deactivated")
                                print()
                                self.frageschleife = 1
                            elif "y" or "n" not in self.frage:
                                print()
                                print("Wrong Value, Try Again!")
                                print()
                                self.frageschleife = 0
                                continue
                        self.frageschleife = 0
                    elif "n" in self.frage:
                        print()
                        print("Aborted!")
                        sys.exit()
                    elif "y" or "n" not in self.frage:
                        print("Wrong Value, Try Again!")
                        print()
                        continue

            # Fehlerbehandlung
            except KeyboardInterrupt:
                print()
                print(colorama.Fore.RED + "You presses Ctrl+C")
                sys.exit()
            except RuntimeError:
                print()
                print(colorama.Fore.RED + "Wrong Statement")
                sys.exit()
            except ValueError:
                print()
                print(colorama.Fore.RED + "You must enter a valid Host")
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
            self.time_diff_sek = self.zeitende - self.zeitbeginn
            self.time_diff_min = self.time_diff_sek/60
            self.time_diff_std = self.time_diff_min/60

    # Banner
    def banner(self):
        print(colorama.Fore.RED + "-" * 60)
        print(colorama.Fore.CYAN + "Python Portscanner", "\n" + "Author: Pierelucas")
        print(colorama.Fore.RED + "-" * 60)
        print(colorama.Style.RESET_ALL)

    def results(self, x):
        if x == 0:
            # Öffnen und Header der Textdatei
            self.file = open('results.txt', 'wt')
            self.file.write("Python Portscanner by PiereLucas")
            self.file.write("\n")
            self.file.write("Results ==>")
            self.file.write("\n")
            self.file.write("Host: ")
            self.file.write(self.remoteServer)
            self.file.write("\n")
            self.file.write("IP: ")
            self.file.write(self.remoteServerIP)
            self.file.write("\n")
            self.file.write("-" * 60)
            self.file.write("\n")
        # Offene Ports in der Textdatei
        elif x == 1:
            self.file.write("\n")
            self.file.write("Nr: ")
            self.file.write(self.count)
            self.file.write("\n Port: ")
            self.file.write(self.port)
            self.file.write("\n")
            self.file.write("-" * 60)
        # Schließen der Textdatei
        elif x == 2:
            self.file.close()


    # Hauptfunktion
    def scan(self):

        self.results(0)

        try:
            # Portscan der Ports 1 - 35535
            for self.port in range(1, 35536):
                # Teste ob verbose modus aktiviert wurde
                if self.verbose:
                    time.sleep(0.01)
                # Teste ob der Port geöffnet ist
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.resultscan = self.sock.connect_ex((self.remoteServerIP, self.port))

                # Wenn offener Port gefunden wurde
                if self.resultscan == 0:
                    print("<-")
                    print("Port {}: 	 Open".format(self.port))
                    print("->")
                    # Erhöhe Zähler für offene Ports
                    self.count += 1
                    # Schreibe in Datei
                    self.results(1)
                    # Füge offenen Port an die Liste der offenen Ports an
                    self.portlist.append(self.port)

                # Ausgabe über offene Ports wenn Port 35535 erreicht
                if self.port == 35535:
                    self.banner()
                    print()
                    print("Results:", colorama.Fore.RED + self.count + colorama.Style.RESET_ALL, "Open Ports found")
                    print("-" * 60)
                    print(colorama.Fore.CYAN + "Port/s Open: {}".format(self.portlist) + colorama.Style.RESET_ALL)
                # Port der zuletzt gescannt wurde
                else:
                    print("Scanning Port: ", self.port)

                self.sock.close()

            self.results(2)

        # Fehlerbehandlung bei start und während des Scans
        except KeyboardInterrupt:
            print()
            print(colorama.Fore.RED + "You presses Ctrl+C")
            sys.exit()

        except socket.gaierror:
            print()
            print(colorama.Fore.RED + "Hostname could not be resolved. Exiting")
            sys.exit()

        except socket.error:
            print()
            print(colorama.Fore.RED + "Couldn't connect to server")
            sys.exit()

# Programm
# ->

# Instanzobjekte
portscanner_init = PortScanner_Init()

# Eingabe
portscanner_init.eingabe()

# Ausgabe über laufenden Scan
portscanner_init.ausgabe(0)

# Prüfe wann der Scan startet
portscanner_init.zeit(1)

# Hauptfunktion
portscanner_init.scan()

# Prüfe die Zeit nochmal
portscanner_init.zeit(2)

# Berechne die Zeitspanne
portscanner_init.zeit(3)

# Gebe die Zeitinformation aus
portscanner_init.ausgabe(1)

# Sicheres Beenden
portscanner_init.ausgabe(2)
sys.exit()
