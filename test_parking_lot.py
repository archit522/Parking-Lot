import unittest
import sys
from ParkingLot import ParkingLot
from StringCodes import StringCodes

class ParkingLotTests(unittest.TestCase):
    
    def test_initiateLot(self):
        parkingLot = ParkingLot()
        result = parkingLot.initiateLot(10)
        self.assertEqual(result, 10)
    
    def test_parkNewCar(self):
        parkingLot = ParkingLot()
        size = parkingLot.initiateLot(1)
        result = parkingLot.parkNewCar("ASD53T", "WHITE")
        self.assertEqual(result, 1)
        result = parkingLot.parkNewCar("WESRT1", "BLUE")
        self.assertEqual(result, StringCodes.OVERFLOW)
    
    def test_removeCar(self):
        parkingLot = ParkingLot()
        size = parkingLot.initiateLot(10)
        slot = parkingLot.parkNewCar("4GHF31", "WHITE")
        result = parkingLot.removeCar(slot - 1)
        self.assertEqual(result, StringCodes.SUCCESS)
    
    def test_allSlotsWithColor(self):
        parkingLot = ParkingLot()
        size = parkingLot.initiateLot(10)
        slotsOfWhiteCars = []
        slotsOfWhiteCars.append(parkingLot.parkNewCar("4GHF31", "VIOLET"))
        slotsOfWhiteCars.append(parkingLot.parkNewCar("FDERTY", "VIOLET"))
        result = parkingLot.allSlotsWithColor("VIOLET")
        self.assertEqual(slotsOfWhiteCars, result)
    
    def test_allCarsWithColor(self):
        parkingLot = ParkingLot()
        size = parkingLot.initiateLot(10)
        parkingLot.parkNewCar("4GHF31", "RED")
        parkingLot.parkNewCar("FDERTY", "RED")
        result = parkingLot.allCarsWithColor("RED")
        self.assertIn("4GHF31", result)
        self.assertIn("FDERTY", result)
    
    def test_slotNumberForId(self):
        parkingLot = ParkingLot()
        size = parkingLot.initiateLot(10)
        parkingLot.parkNewCar("4GHF31", "RED")
        parkingLot.parkNewCar("FDERTY", "RED")
        result = parkingLot.findSlotIdForUniqueId("FDERTY")
        self.assertEqual(2, result)
    
if __name__ == '__main__':
	unittest.main()