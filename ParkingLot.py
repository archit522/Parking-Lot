from enum import Enum
import Car

class StringCodes(Enum):
    OVERFLOW = -1
    UNDERFLOW = -2
    SUCCESS = 1

class ParkingLot:
    def __init__(self):
        self.totalSlots = 0
        self.slotId = 0
        self.occupied = 0
    
    def initiateLot(self, totalSlots):
        self.totalSlots = totalSlots
        self.eachSlotInfo = [0]*totalSlots
        return self.totalSlots
    
    def parkNewCar(self, uniqueId, color):
        if self.occupied >= self.totalSlots:
            return StringCodes.OVERFLOW
        
        for i in range(self.totalSlots):
            if self.eachSlotInfo[i] == 0:
                self.eachSlotInfo[i] = Car(uniqueId, color)
                self.occupied += 1
                self.slotId += 1
                return self.slotId
    
    def removeCar(self, slotId):
        if(self.eachSlotInfo[slotId] == 0){
            return StringCodes.UNDERFLOW
        }
        self.eachSlotInfo[slotId] = 0
        self.occupied -= 1
        return StringCodes.SUCCESS
        