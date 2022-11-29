class RandomizedSet:
    def __init__(self):
        self.indices = {}
        self.arr = []
    def insert(self, val: int) -> bool:
        if val in self.indices: return False
        self.arr.append(val)
        self.indices[val] = len(self.arr)-1
        return True  
    def remove(self, val: int) -> bool:
        if val not in self.indices: return False
        i = self.indices[val]
        self.indices[self.arr[-1]] = i
        self.arr[i] = self.arr[-1]
        self.indices.pop(val)
        self.arr.pop() 
        return True
    def getRandom(self) -> int:
        return random.choice(self.arr)
