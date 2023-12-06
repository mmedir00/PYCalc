class numberProcessor:

    def process(string):
        result = string
        result = result.replace("x", "*")
        result = result.replace("^","**")
        result = eval(result)
        return result