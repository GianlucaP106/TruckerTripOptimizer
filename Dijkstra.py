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
from EndNode import EndNode
from Graph import Graph
from ConvertDistance import coordToDistance
from SecondsBetween import SecondsBetween

COST_PER_METRE = 0.4 / 1609.344 # $/mile / metres/mile = $/metre
METRE_PER_HOUR = 55 * 1609.344 # miles/hour * metres/mile = metres/hour
COST_PER_SECOND = COST_PER_METRE * METRE_PER_HOUR / 3600 # $/metre * metres/hour * hour/seconds
load_list = []
input_list = []
all_nodes = []
profit_list = []

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
    all_nodes = list(end_node_set) + input_list + list(start_node_set)
    g = Graph(len(start_node_set)+len(end_node_set)+len(input_list))
    for start_node in start_node_set:
        node = load_list[[node.start_node for node in load_list].index(start_node)] # current node, this has node.load_earning
        for input_node in input_list:
            time_duration_start_input = (coordToDistance(start_node.origin_latitude,start_node.origin_longitude, input_node.start_latitude, input_node.start_longitude)/METRE_PER_HOUR) * 3600 # to seconds
            # if statement here to eliminate nodes that exceed the maximum alloted time
            if (time_duration_start_input < SecondsBetween(input_node.max_destination_time,input_node.start_time)): # input to start
                g.add_edge(all_nodes.index(input_node), all_nodes.index(start_node), time_duration_start_input, 0, 'input')
        for end_node in end_node_set:
            time_duration_end_start = coordToDistance(start_node.origin_latitude,start_node.origin_longitude, end_node.destination_latitude, end_node.destination_longitude)/METRE_PER_HOUR * 3600 # to seconds
            if (time_duration_end_start < SecondsBetween(input_node.max_destination_time,input_node.start_time)): # end to start
                g.add_edge(all_nodes.index(end_node),all_nodes.index(start_node), time_duration_end_start, node.load_earning, 'end')
    start_node_index = all_nodes.index(input_list[0])
    start_node = all_nodes[start_node_index]
    D = Graph.dijkstra(g, start_node_index)
    for vertex in range(len(D)):
        if(isinstance(all_nodes[vertex], EndNode)):
            profit_list.append(D[vertex][1] - D[vertex][0]*COST_PER_SECOND)
    max_profit_index = profit_list.index(max(profit_list))
    print("Time from vertex {} and {} to {} and {} is {} and load earning of trip {} net profit is {}.".format(start_node.start_latitude, start_node.start_longitude,all_nodes[max_profit_index].destination_latitude, all_nodes[max_profit_index].destination_longitude,D[max_profit_index][0],D[max_profit_index][1], D[max_profit_index][1] - D[max_profit_index][0]*COST_PER_SECOND))
