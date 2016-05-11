# -*-coding:UTF-8 -*

from webControler import *
from consoleControler import *
import sys


def printHelp():
    print("To launch the web server, type 'python3 main.py' or 'python3 main.py web'\n \
    To launch the console interface, type 'python3 main.py console'")

if __name__ == '__main__':
    if(len(sys.argv) > 1):
        if(sys.argv[1] in ["--help", "-help", "help"]):
            printHelp()
        elif(sys.argv[1] in ["--console", "-console", "console"]):
            myMain = ConsoleMenu()
        elif(sys.argv[1] in ["--web", "-web", "web"]):
            myMain = WebServer()
        else:
            print(sys.argv[1], " is not a proper command")
            printHelp()
    else:
        myMain = WebServer()
