import math

class specialsDetector:
    def __init__(self, string):
        self.string = string
        self.dict = {"e": math.e,
                    "pi": math.pi,
                    }

        self.operators = ["cos", "sin", "tan", "acs", "asn", "atg"]

    def process(self):
        last = 0
        for i in range(len(self.string)):
            if self.string[i] == "{":
                last = i
            elif self.string[i] == "}":
                if self.string[last + 1 : i] in self.dict:
                    self.string = self.string.replace(self.string[last : i + 1], str(self.dict[self.string[last + 1 : i]]))
                    last = 0
                elif self.string[last + 1 : last + 4] in self.operators:
                    self.string = self.string.replace(self.string[last : i + 1], str(self.operator(self.string[last + 1 : i])))
                    last = 0
        if "{" in self.string and "}" in self.string:
            self.string = self.process()
        elif "{" in self.string or "}" in self.string:
            raise NameError("Sintaxis Error. Missing \"}\" or \"{\"")
        return self.string


    def operator(self, string):
        result = ""
        if string[0:3] == "cos":
            result = str(math.cos(math.radians(float(eval(string[3:])))))
        
        elif string[0:3] == "sin":
            result = str(math.sin(math.radians(float(eval(string[3:])))))
        
        elif string[0:3] == "tan":
            result = str(math.tan(math.radians(float(eval(string[3:])))))
        
        elif string[0:3] == "acs":
            result = str(math.acos(float(eval(string[3:]))))
            result = math.degrees(float(result))
        
        elif string[0:3] == "asn":
            result = str(math.asin(float(eval(string[3:]))))
            result = math.degrees(float(result))
        
        elif string[0:3] == "atg":
            result = str(math.atan(float(eval(string[3:]))))
            result = math.degrees(float(result))
        
        return str(round(float(result), 5))