
from Graph import Graph 
from Intepreter import Intepreter
import json


if __name__ == '__main__':

    i = Intepreter("all_the_loads.json" , "all_input_requests.json")
    g = Graph(i.loadFile)
    g.createGraph()
     
    for key , value in g.graph.items() :
        print(key , "   ",value)
    

    
