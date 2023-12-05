import math

class specialsDetector:
    def __init__(self, string):
        self.string = string
        self.dict = {"e": math.e, 
                    "pi": math.pi,
                    }

        self.operators = {"cos": self.trigonometrics(),
                          "sin": self.trigonometrics(),
                          "tan": self.trigonometrics(),
                          "acs": self.trigonometrics(),
                          "asn": self.trigonometrics(),
                          "atg": self.trigonometrics(),
                          }
    
    def process(self):
        braces = self.getDict()
        operations = []
        for key, value in reversed(braces):
            if self.string[key:value] in self.dict:
                pass#TODO


        
    def trigonometrics(self):
        if self.string[0:3] == "cos":
            return math.cos(float(self.string[3:]))
        
        elif self.string[0:3] == "sin":
            return math.sin(float(self.string[3:]))
        
        elif self.string[0:3] == "tan":
            return math.tan(float(self.string[3:]))
        
        elif self.string[0:3] == "acs":
            return math.acos(float(self.string[3:]))
        
        elif self.string[0:3] == "asn":
            return math.asin(float(self.string[3:]))
        
        elif self.string[0:3] == "atg":
            return math.atan(float(self.string[3:]))

    def getDict(self):
        open = self.open()
        close = self.close()
        if len(open) == len(close) and len(open) > 0:
            dict = {}
            for i in range(len(open)):
                dict[open[i]] = close[0-(i+1)]
            return dict
        else:
            raise NameError("Sintax : Invalid string. Not matching braces.")

    def open(self):
        position = []
        for i, caracter in enumerate(self.string):
            if caracter == '{':
                position.append(i)
        return position
    
    def close(self):
        position = []
        for i, caracter in enumerate(self.string):
            if caracter == '}':
                position.append(i)
        return position


string = "hola {mundo} {que} tal"
specials = specialsDetector(string)
dict = specials.getDict()
print(dict)
for key, value in reversed(dict):
    print(string[int(key):int(value)])