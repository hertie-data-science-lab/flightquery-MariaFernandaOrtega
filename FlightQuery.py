from SortedTableMap import *

class FlightQuery(SortedTableMap):
    '''An application of SortedTableMap, used to query tickets of expected period'''

    class Key:
        __slots__ = "_origin", "_dest", "_date", "_time"

        def __init__(self, origin, dest, date, time):
            self._origin = origin
            self._dest = dest
            self._date = date
            self._time = time

        def __lt__(self, other):
            if self._date < other._date:
                return True
            elif self._date == other._date and self._time < other._time:
                return True
            elif self._date == other._date and self._time == other._time and self._origin < other._origin:
                return True
            elif self._date == other._date and self._time == other._time and self._origin == other._origin and self._dest < other._dest:
                return True
            else:
                return False

        def __le__(self, other):
            if self._date < other._date:
                return True
            elif self._date == other._date and self._time <= other._time:
                return True
            elif self._date == other._date and self._time == other._time and self._origin <= other._origin:
                return True
            elif self._date == other._date and self._time == other._time and self._origin == other._origin and self._dest <= other._dest:
                return True
            else:
                return False

        def __eq__(self, other):
            return self._date == other._date and self._time == other._time and self._origin == other._origin and self._dest == other._dest

        def __str__(self):
            return f"{self._origin}-{self._dest} {self._date} {self._time}"

    def query(self, k1, k2):
        result = []
        for item in self._table:
            key = item._key
            if k1 <= key <= k2:
                result.append(item._value)
        return result

a = FlightQuery()
s = [("A", "B", 622, 1200, "No1"), ("A", "B", 622, 1230, "No2"), ("A", "B", 622, 1300, "No3")]
for each in s:
    key = a.Key(each[0], each[1], each[2], each[3])
    value = each[4]
    a[key] = value

print(len(a))
k1 = a.Key("A", "B", 622, 1200)
k2 = a.Key("A", "B", 622, 1300)
print(a.query(k1, k2))  # output: ['No1', 'No2', 'No3']

