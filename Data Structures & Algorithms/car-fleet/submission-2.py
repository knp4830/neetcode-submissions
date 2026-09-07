class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Iteration
        # Get the cars in reverse order
        pair = []
        for i in range(len(position)):
            pair.append([position[i], speed[i]])
        
        pair.sort(reverse = True)
        fleets = 1
        prevTime = (target - pair[0][0]) / pair[0][1]
        for i in range(1, len(pair)):
            currCar = pair[i]
            currTime = (target - currCar[0]) / currCar[1]
            
            if currTime > prevTime:
                fleets += 1
                prevTime = currTime
        
        return fleets