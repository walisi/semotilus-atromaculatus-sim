import math

def getBestLake(day):
    raise NotImplementedError()

def longitude(degrees, minutes, seconds):
    #Return longitude in seconds
    return (((degrees * 60) + minutes) * 60) + seconds;
    
class WaterBody:
    def __init__(self, name, pos, temperature_model):
        self.name = name
        self.pos = pos
        self.temperature_model = temperature_model

class Temperature:
    #Daily temperature model as a cosinus curve over a period of one year.
    #For exemple (1.5 , 5, 50) specifies a range of temperature from 3.5 to
    #6.5, where the 50th day, February 19, is the coldest day.
    K = math.pi / 182.5

    def __init__(self, amplitude, center, coldestDay):
        self.A = amplitude
        self.D = center
        self.coldestDay = coldestDay

    def getTemperature(self, day):
        #day is in the range 1 to 365. Nevermind gap years.
        if day < 1:
            day = 1
        if day > 365:
            day = 365
        return math.cos(self.K * (day - self.coldestDay) + math.pi) * self.A + self.D
