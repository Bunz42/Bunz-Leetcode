class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse=True)

        fleets = []

        for p, s in cars:
            time = (target - p)/s
            if not fleets or time > fleets[-1]:
                fleets.append(time)

        return len(fleets)
