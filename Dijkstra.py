# run Djikstra for shortest amount of time
    # create a vertice for each of our nodes
    # the edge's 'weight' will be the time
    # if weight time is > max_time ... continue
    # keep track of a sum for the time and the distance if any of them exceeds the max_time or max_distance ... continue
# sort them in increasing order
# GET RID OF THIS
    # iterate over them between 0 and max_time
    # see if the distance exceeds max distance
# calculate profit with the remaining nodes
# sort and take the last one

from Interpreter import Interpreter
from Node import Node
from InputNode import InputNode
from Graph import Graph
from ConvertDistance import coordToDistance

COST_PER_METRE = 0.4 / 1609.344 # $/mile / metres/mile
METRE_PER_HOUR = 55 * 1609.344 # miles/hour * metres/mile = metres/hour
load_list = []
input_list = []

def create_nodes(loadFile, inputFile):
        for i in range(len(loadFile)):
            load_id = loadFile[i]["load_id"]
            originLat = loadFile[i]["origin_latitude"]
            originLong = loadFile[i]["origin_longitude"]
            destLat = loadFile[i]["destination_latitude"]
            destLong = loadFile[i]["destination_longitude"]
            amount = loadFile[i]["amount"]
            pickUpTime = loadFile[i]["pickup_date_time"]
            load_list.append(Node(id, originLat, originLong, destLat, destLong, amount, pickUpTime))
        for j in range(len(inputFile)):
            input_trip_id = inputFile[j]["input_trip_id"]
            start_latitude = inputFile[j]["start_latitude"]
            start_longitude = inputFile[j]["start_longitude"]
            start_time = inputFile[j]["start_time"]
            max_destination_time = inputFile[j]["max_destination_time"]
            input_list.append(InputNode(input_trip_id, start_latitude, start_longitude, start_time, max_destination_time))

if __name__ == "__main__":
    i = Interpreter("all_the_loads.json" , "all_input_requests.json")
    # instantiate the nodes
    create_nodes(i.loadFile , i.inputFile)
    # read files
    # load_list and node_list are now populated
    # instantiate graph
    # create a set in python of the start_nodes and end_nodes
    start_node_set = set([node.start_node for node in load_list])
    end_node_set = set([node.end_node for node in load_list])
    g = Graph(len(start_node_set)+len(end_node_set)+len(input_list))
    for input_node in input_list:
        for start_node in start_node_set:
            time_duration = (coordToDistance(start_node.origin_latitude,start_node.origin_latitude, input_node.start_latitude, input_node.start_longitude)/METRE_PER_HOUR) * 3600 # to seconds
            # if statement here to eliminate nodes that exceed the maximum alloted time
            if (time_duration < seconds_between(max_destination_time,start_time)):
                g.add_edge(input_node, start_node, time_duration)
            for end_node in end_node_set:
                g.add_edge(start_node, end_node, coordToDistance(start_node.origin_latitude,start_node.origin_latitude, end_node.start_latitude, end_node.start_longitude)/METRE_PER_HOUR)

    D = dijkstra(g, input_list[0])
    print(D)

# g = Graph(9)
# g.add_edge(0, 1, 4)
# g.add_edge(0, 6, 7)
# g.add_edge(1, 6, 11)
# g.add_edge(1, 7, 20)
# g.add_edge(1, 2, 9)
# g.add_edge(2, 3, 6)
# g.add_edge(2, 4, 2)
# g.add_edge(3, 4, 10)
# g.add_edge(3, 5, 5)
# g.add_edge(4, 5, 15)
# g.add_edge(4, 7, 1)
# g.add_edge(4, 8, 5)
# g.add_edge(5, 8, 12)
# g.add_edge(6, 7, 1)
# g.add_edge(7, 8, 3) 

# D = dijkstra(g, 0)

# print(D)
