from Interpreter import Interpreter

i = Interpreter("all_the_loads1.json" , "all_input_requests.json")

lookUpTable = {}
for loadInfo in i.loadFile:
    lookUpTable[(loadInfo["origin_latitude"],loadInfo["origin_longitude"],loadInfo["origin_city"] + " " + loadInfo["origin_state"])] = loadInfo["origin"] = (loadInfo["destination_latitude"],loadInfo["destination_longitude"],loadInfo["destination_city"] + " " + loadInfo["destination_state"],loadInfo["load_id"],loadInfo["amount"],loadInfo["pickup_date_time"]) 


for key, value in lookUpTable.items():
    print(key, " -> " ,value)
    print("\n")

