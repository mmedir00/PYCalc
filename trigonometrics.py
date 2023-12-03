import math

class trigonometrics:
    def processor(self, string):
        print(type(string), string)
        for i in range(len(string)):
            if str(string[i:i+5]) == "acos{":
                for j in range(len(string)):
                    if string[j] == "}":
                        return self.acos(string[i+5:j])

            elif string[i:i+5] == "asin{":
                for j in range(len(string)):
                    if string[j] == "}":
                        return self.asin(string[i+5:j])

            elif string[i:i+5] == "atan{":
                for j in range(len(string)):
                    if string[j] == "}":
                        return self.atan(string[i+5:j])

            elif string[i:i+4] in ["cos{"]:
                for j in range(len(string)):
                    if string[j] == "}":
                        print(string[i+4:j])
                        return self.cos(math.radians(int(string[i+4:j])))
           
            elif string[i:i+4] == "sen{":
                for j in range(len(string)):
                    if string[j] == "}":
                        return self.sen(math.radians(int(string[i+4:j])))
           
            elif string[i:i+4] == "tan{":
                for j in range(len(string)):
                    if string[j] == "}":
                        return self.tan(math.radians(int(string[i+4:j])))
        
    def cos(self, angle):
        return math.cos(float(angle))
    
    def sin(self, angle):
        return math.sin(int(angle))
    
    def tan(self, angle):
        return math.tan(angle)
    
    def acos(self, angle):
        return math.acos(angle)
    
    def asin(self, angle):
        return math.asin(angle)
    
    def atan(self, angle):
        return math.atan(angle)