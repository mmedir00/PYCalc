from numberProcessor import *
from specialsDetector import *

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
                    if "{" in string:
                        specials = specialsDetector(string)
                        numbers = specials.process()
                    numbers = self.ansReplace(numbers)
                    self.ans = numberProcessor.process(numbers)
                    print(f"<<< {self.ans}\n")
                except NameError as e:
                    print(f"<<< Sintaxis Error. {e.args}\n")
                except ZeroDivisionError as e:
                    print(f"<<< Math Error (zero division).{e.args}\n")

    def clear(self):    
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    def ansReplace (self, string):
        string = str(string).replace("Ans", str(self.ans))
        string = str(string).replace("ans", str(self.ans))
        return string
    
            