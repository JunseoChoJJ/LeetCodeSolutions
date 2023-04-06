class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        # first find out which is one the biggest numberofunitesperbox is. what about switch?
        # switch the elements inside 
        
        
        boxTypes.sort(key=lambda x: -x[1])
        boxes = 0
        for box, units in boxTypes:
            if truckSize > box:
                truckSize -= box
                boxes += box * units
            else:
                boxes += truckSize * units
                return boxes
        return boxes    
