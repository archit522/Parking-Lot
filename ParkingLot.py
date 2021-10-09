from enum import Enum
import Car
import argparse
import sys

class StringCodes(Enum):
    OVERFLOW = -1
    NOT_PRESENT = -2
    SUCCESS = -3

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
            return StringCodes.NOT_PRESENT
        }
        self.eachSlotInfo[slotId] = 0
        self.occupied -= 1
        return StringCodes.SUCCESS
    
    def allSlotsWithColor(self, color):
        slots = []
        for i in range(self.totalSlots):
            if self.eachSlotInfo[i] != 0 and self.eachSlotInfo[i].color == color:
                slots.append(i+1)
        return slots
    
    def allCarsWithColor(self, color):
        ids = []
        for i in range(self.totalSlots):
            if(self.eachSlotInfo[i] != 0 and self.eachSlotInfo[i].color == color):
                ids.append(self.eachSlotInfo[i].uniqueId)
        
        return ids
    
    def printArrayByComma(self, arr):
        n = len(arr)
        for i in range(n):
                print(arr[i])
                if(i != n - 1):
                    print(", ")
        print("\n")
    
    def findSlotIdForUniqueId(self, uniqueId):
        for i in range(self.totalSlots):
            if(self.eachSlotInfo[i] != 0 and self.eachSlotInfo[i].uniqueId == uniqueId):
                return i+1
        
        return StringCodes.NOT_PRESENT
    
    def parkingLotStatus(self):
        print("Slot No.\tID\tColor")
        for i in range(self.totalSlots):
            if(self.eachSlotInfo[i] != 0):
                print(i + "\t" + self.eachSlotInfo[i].uniqueId + "\t" + self.eachSlotInfo[i].color)
    
    def processEachCommand(self, command):
        if(command.startswith("create_parking_lot")):
            temp = command.split(" ")
            size = int(temp[1])
            self.initiateLot(size)
            print("Created a parking lot with %s slots" % size)

        elif(command.startswith("park")):
            temp = command.split(" ")
            result = self.parkNewCar(temp[1], int(temp[2]))
            if(result == StringCodes.OVERFLOW):
                print("Sorry, parking lot is full")
            else:
                print("Allocated slot number: %s" % result)
        
        elif(command.startswith("leave")):
            temp = command.split(" ")
            result = self.removeCar(int(temp[1]))
            if(result == StringCodes.NOT_PRESENT):
                print("No car found at this slot")
            else:
                print("Slot number %s is free" % temp[1])
        
        elif(command.startswith("status")):
            self.parkingLotStatus()
        
        elif(command.startswith("ids_for_cars_with_color")):
            temp = command.split(" ")
            ids = self.allCarsWithColor(temp[1])
            if(len(ids) == 0):
                print("No car found with color: %s" % temp[1])
            else:
                self.printArrayByComma(ids)
            
        elif(command.startswith("slot_numbers_for_cars_with_color")):
            temp = command.split(" ")
            slots = self.allSlotsWithColor(temp[1])
            self.printArrayByComma(slots)
        
        elif(command.startswith("slot_number_for_id")):
            temp = command.split(" ")
            result = self.findSlotIdForUniqueId(temp[i])
            if(result == StringCodes.NOT_PRESENT):
                print("Not found")
            else:
                print(result)

def main():
    parkingLot = ParkingLot()
    parseObj = argparse.ArgumentParser(description="Parking Lot Application")
    parseObj.add_argument("-f", dest = "fileName", action='store_const')
    if parseObj.parse_args().fileName:
        commands = []
        with open(parseObj.parse_args().fileName, 'r') as f:
            commands = f.readlines()
        
        for command in commands:
            parkingLot.processEachCommand(command.rstrip())
    else:
        for command in sys.stdin:
            if "exit" == command.rstrip():
                break
            parkingLot.processEachCommand(command.rstrip())

if __init__ == "__main__":
    main()
    
    
    
        