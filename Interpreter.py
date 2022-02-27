
import json


class Interpreter:
    def __init__(self ,loadFile ,inputFile):
        file = open(loadFile , "r")
        self.loadFile = json.load(file)
        file = open(inputFile , "r")
        self.inputFile = json.load(file)
        
        
        


