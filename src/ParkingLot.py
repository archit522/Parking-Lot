import argparse
import sys
from Car import Car
from TypeChecker import TypeChecker
from StringCodes import StringCodes

class ParkingLot:
    def __init__(self):
        self.totalSlots = 0
        self.occupied = 0
        self.isInitiated = False
    
    #Initiate Parking Lot with space = totalSlots
    def initiateLot(self, totalSlots):
        self.totalSlots = totalSlots
        self.eachSlotInfo = [0]*totalSlots
        self.occupied = 0
        self.isInitiated = True
        return self.totalSlots
    
    #Park New Car and return slot no.
    def parkNewCar(self, uniqueId, color):
        if self.occupied >= self.totalSlots:
            return StringCodes.OVERFLOW
        
        for i in range(self.totalSlots):
            if self.eachSlotInfo[i] == 0:
                self.eachSlotInfo[i] = Car(uniqueId, color)
                self.occupied += 1
                return i+1
    
    #Leave car from the slotId if found
    def removeCar(self, slotId):
        if slotId >= self.totalSlots:
            return StringCodes.INVALID_INPUT
        
        if self.eachSlotInfo[slotId] == 0:
            return StringCodes.NOT_PRESENT
        
        self.eachSlotInfo[slotId] = 0
        self.occupied -= 1
        return StringCodes.SUCCESS
    
    #Return list of all slots containing car with given color
    def allSlotsWithColor(self, color):
        slots = []
        for i in range(self.totalSlots):
            if self.eachSlotInfo[i] != 0 and self.eachSlotInfo[i].color == color:
                slots.append(i+1)
        return slots
    
    #Return list of all cars parked in parking lot with given color
    def allCarsWithColor(self, color):
        ids = []
        for i in range(self.totalSlots):
            if self.eachSlotInfo[i] != 0 and self.eachSlotInfo[i].color == color:
                ids.append(self.eachSlotInfo[i].uniqueId)
        
        return ids
    
    #Print array seperated by comma
    def printArrayByComma(self, arr):
        n = len(arr)
        for i in range(n):
                print(arr[i], end='')
                if i != n - 1:
                    print(", ", end='')
        print("\n", end='')
    
    #Return slotId for car with given uniqueId
    def findSlotIdForUniqueId(self, uniqueId):
        for i in range(self.totalSlots):
            if self.eachSlotInfo[i] != 0 and self.eachSlotInfo[i].uniqueId == uniqueId:
                return i+1
        
        return StringCodes.NOT_PRESENT
    
    #Print status of parking lot
    def parkingLotStatus(self):
        print("Slot No.\tID\t\tColor")
        for i in range(self.totalSlots):
            if self.eachSlotInfo[i] != 0:
                print(str(i+1) + "\t\t" + self.eachSlotInfo[i].uniqueId + "\t\t" + self.eachSlotInfo[i].color)
    
    #Check input sanity (digit -> slotId, alphanumeric -> car uniqueId)
    def checkInput(self, inputString, whichType):
        if whichType == TypeChecker.DIGIT:
            return inputString.isdigit()
        
        elif whichType == TypeChecker.ALPHANUMERIC:
            return inputString.isalnum()
    
    #Process each line of command input through file or command line
    def processEachCommand(self, command):
        if command.startswith("create_parking_lot"):
            temp = command.split(" ")
            if(len(temp) != 2 or self.checkInput(temp[1], TypeChecker.DIGIT) == False or int(temp[1]) < 0):
                print("Invalid Input")
                return
            size = int(temp[1])
            self.initiateLot(size)
            print("Created a parking lot with %s slots" % size)

        elif command.startswith("park"):
            temp = command.split(" ")
            if(len(temp) != 3 or len(temp[1]) != 6 or self.checkInput(temp[1], TypeChecker.ALPHANUMERIC) == False or self.isInitiated == False):
                print("Invalid Input")
                return
            result = self.parkNewCar(temp[1], temp[2])
            if result == StringCodes.OVERFLOW:
                print("Sorry, parking lot is full")
            else:
                print("Allocated slot number: %s" % result)
        
        elif command.startswith("leave"):
            temp = command.split(" ")
            if(len(temp) != 2 or self.checkInput(temp[1], TypeChecker.DIGIT) == False or self.isInitiated == False):
                print("Invalid Input")
                return
            result = self.removeCar(int(temp[1]) - 1)
            if result == StringCodes.NOT_PRESENT:
                print("No car found at this slot")
            elif result == StringCodes.INVALID_INPUT:
                print("Invalid Input")
            else:
                print("Slot number %s is free" % temp[1])
        
        elif command.startswith("status"):
            if (self.isInitiated == False):
                print("Invalid Input")
                return
            self.parkingLotStatus()
        
        elif command.startswith("ids_for_cars_with_color"):
            temp = command.split(" ")
            if (len(temp) != 2 or self.isInitiated == False):
                print("Invalid Input")
                return
            ids = self.allCarsWithColor(temp[1])
            if len(ids) == 0:
                print("No car found with color: %s" % temp[1])
            else:
                self.printArrayByComma(ids)
            
        elif command.startswith("slot_numbers_for_cars_with_color"):
            temp = command.split(" ")
            if (len(temp) != 2 or self.isInitiated == False):
                print("Invalid Input")
                return
            slots = self.allSlotsWithColor(temp[1])
            if len(slots) == 0:
                print("No car found with color: %s" % temp[1])
            self.printArrayByComma(slots)
        
        elif command.startswith("slot_number_for_id"):
            temp = command.split(" ")
            if(len(temp) != 2 or self.checkInput(temp[1], TypeChecker.ALPHANUMERIC) == False or self.isInitiated == False):
                print("Invalid Input")
                return
            result = self.findSlotIdForUniqueId(temp[1])
            if result == StringCodes.NOT_PRESENT:
                print("Not found")
            else:
                print(result)
        
        else:
            print("Invalid Command")

def main():
    #create class obj
    parkingLot = ParkingLot()
    
    #Command line parser
    parseObj = argparse.ArgumentParser(description="Parking Lot Application")
    parseObj.add_argument("-f", dest = "fileName", required=False, action='store')
    
    #check if fileName is provided
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

if __name__ == "__main__":
    main()