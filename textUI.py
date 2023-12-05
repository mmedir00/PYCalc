from numberProcessor import *

import os

class textUI:
    def __init__(self):
        self.ans = 0

    def init(self):
        self.clear()
        print("Welcome to PyCalc!\nWrite the operation. \"exit\" to exit.\n")
        while True:
            string = str(input(">>> "))
            if string.lower() in ["exit"]:
                break
            else:
                try:
                    string = self.ansReplace(string)
                    self.ans = numberProcessor.process(string)
                    print(f"<<< {self.ans}\n")
                except NameError:
                    print("<<< Sintaxis Error.\n")
                except ZeroDivisionError:
                    print("<<< Math Error (zero division).\n")

    def clear(self):    
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    def ansReplace (self, string):
        string = string.replace("Ans", str(self.ans))
        string = string.replace("ans", str(self.ans))
        return string
    
            