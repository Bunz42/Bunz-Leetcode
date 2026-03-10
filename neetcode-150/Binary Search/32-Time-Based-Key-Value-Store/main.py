class TimeMap:

    def __init__(self):
        self.time_map = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""

        values = self.time_map[key]

        l, r = 0, len(values) - 1
        res = ""

        while l <= r:
            mid = (l + r) // 2

            mid_stamp = values[mid][1]
            mid_value = values[mid][0]

            if mid_stamp <= timestamp:
                res = mid_value
                l = mid + 1
            else:
                r = mid - 1
        
        return res

