class UndergroundSystem:
    def __init__(self):
        self.check_ins = {}
        self.travel_times = {}

    def checkIn(self, id, stationName, t):
        self.check_ins[id] = (stationName, t)

    def checkOut(self, id, stationName, t):
        start_station, check_in_time = self.check_ins[id]
        end_station = stationName
        travel_time = t - check_in_time

        
        key = (start_station, end_station)
        if key not in self.travel_times:
            self.travel_times[key] = [travel_time, 1]
        else:
            self.travel_times[key][0] += travel_time
            self.travel_times[key][1] += 1

    def getAverageTime(self, startStation, endStation):
        key = (startStation, endStation)
        total_time, num_trips = self.travel_times[key]
        return total_time / num_trips