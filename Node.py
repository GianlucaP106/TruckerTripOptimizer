from StartNode import StartNode
from EndNode import EndNode
from ConvertDistance import coordToDistance

class Node:
    def __init__(self, node_id, origin_latitude, origin_longitude, destination_latitude, destination_longitude, load_earning, pick_up_time):
        self.node_id = node_id
        self.start_node = StartNode(origin_latitude,origin_longitude)
        self.end_node = EndNode(destination_latitude,destination_longitude)
        self.load_earning = load_earning
        self.pick_up_time = pick_up_time
        self.distance = coordToDistance(origin_latitude,origin_longitude,destination_latitude,destination_longitude)