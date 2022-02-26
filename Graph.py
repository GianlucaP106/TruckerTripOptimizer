from math import sqrt, pi, sin, cos, atan2


class Graph:

    
    def __init__(self, loadFile):
        self.tripTuples = []
        self.graph = {}

        for i in range(len(loadFile)):
            id = loadFile[i]["load_id"]
            originLocation = loadFile[i]["origin_city"] + \
                " , " + loadFile[i]["origin_state"]
            originLat = loadFile[i]["origin_latitude"]
            originLong = loadFile[i]["origin_longitude"]
            destLocation = loadFile[i]["destination_city"] + \
                " , " + loadFile[i]["destination_state"]
            destLat = loadFile[i]["destination_latitude"]
            destLong = loadFile[i]["destination_longitude"]
            amount = loadFile[i]["amount"]
            pickUpTime = loadFile[i]["pickup_date_time"]
            self.tripTuples.append(((originLocation, destLocation), id,
                                   originLat, originLong, destLat, destLong, amount, pickUpTime))


    def coordToDistance(self, lat1, long1, lat2, long2):
        R = 6371000
        φ1 = lat1 * pi/180
        φ2 = lat2 * pi/180
        Δφ = (lat2-lat1) * pi/180
        Δλ = (long2-long1) * pi/180

        a = sin(Δφ/2) * sin(Δφ/2) + cos(φ1) * \
            cos(φ2) * sin(Δλ/2) * sin(Δλ/2)
        c = 2 * atan2(sqrt(a), sqrt(1-a))

        d = R * c  # meters

        return d

    def metricConverter(self, d):
        km = float(d/1000)
        conversion_ratio = 0.621371
        miles = float(km * conversion_ratio)
        return miles

    def profitCalc(self, amount, distance):
        return float(amount - float(distance * 0.40))
    def createGraph(self):
        index = 0
        while True: # self.tripTuples.append(((originLocation, destLocation), id, originLat, originLong, destLat, destLong, amount, pickUpTime))
            if (index > len(self.tripTuples) - 1):
                break
            start = self.tripTuples[index][0][0]
            end = self.tripTuples[index][0][1]
            temp = self.tripTuples[index]
            meters = self.coordToDistance(temp[2], temp[3], temp[4], temp[5])
            miles = self.metricConverter(meters)

            if start not in self.graph:
                self.graph[start] = [(end, miles)]
                
                        

            else:
                temp = 0
                for i in range(len(self.graph[start])):
                    if end == self.graph[start][i][0]:
                        temp +=1
                        
                if temp == 0:
                    self.graph[start].append((end , miles)) 

            index += 1
    
        