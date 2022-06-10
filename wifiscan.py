## Under construction

from random import randint, shuffle
import sys
import time
from traceback import print_tb
import pyfiglet
import socket
from datetime import datetime

from pystyle import *

banner1 = r'''
  ___         _     ___                            
 | _ \___ _ _| |_  / __| __ __ _ _ _  _ _  ___ _ _ 
 |  _/ _ \ '_|  _| \__ \/ _/ _` | ' \| ' \/ -_) '_|
 |_| \___/_|  \__| |___/\__\__,_|_||_|_||_\___|_|  
                                                   '''[1:]

yellow = Col.StaticMIX([Col.blue, Col.yellow])

def stage(text: str, symbol: str = '...') -> str:
    yyellow = yellow if symbol == '...' else Col.light_blue
    return f""" {Col.Symbol(symbol, yyellow, Col.blue)} {yyellow}{text}{Col.reset}"""
    

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid amount of Argument")
    print("Syntax (linux): python3 wifiscan.py <ip>")
    print("Syntax (windows): py wifiscan.py <ip>")
    exit()
try:
    System.Size(150, 40)
    System.Title("Port Scanner")
    print(Colorate.Diagonal(Colors.purple_to_blue, Center.XCenter(banner1 + '\n\n')))
    print(stage("Scanning " + target , '-'))
    print(stage(f"Scan started at {str(datetime.now())}"))
    time.sleep(1)
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.04)
        result = s.connect_ex((target,port))
        if result ==0:
            print(stage(Col.green + "Port " + str(port) + f" is open on {target}" + Col.reset))
        s.close()
    print('\n')
    print(stage("Scanning complete!", '-'))
    print(stage("Scan ended at " + str(datetime.now())))
    input(stage("\nPress Enter to exit..."))
    
except KeyboardInterrupt:
        print("\n")
        print(f""" {Col.Symbol('!', Col.light_red, Col.blue)} {Col.light_red}KeyboardInterrupt Detected!{Col.reset}""")
        time.sleep(1)
        print(f""" {Col.Symbol('!', Col.light_red, Col.blue)} {Col.light_red}Exiting...{Col.reset}""")
        sys.exit()
except socket.gaierror:
        print("\n Hostname Could Not Be Resolved !!!!")
        sys.exit()
except socket.error:
        print("\ Server not responding !!!!")
        sys.exit()

