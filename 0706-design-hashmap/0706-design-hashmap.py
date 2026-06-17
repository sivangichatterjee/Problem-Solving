class MyHashMap:

    def __init__(self):
        self.size=1000
        self.map=[[] for _ in range(self.size)]

    def hash(self, key):
        return key%self.size

        
    def put(self, key: int, value: int) -> None:
        map_key=self.map[self.hash(key)]
        for i, (k,v) in enumerate(map_key):
            if k==key:
                map_key[i]=(key,value)
                return
        map_key.append((key,value))
        

    def get(self, key: int) -> int:
        map_key=self.map[self.hash(key)]
        for k,v in map_key:
            if k==key:
                return v
        return -1
        

    def remove(self, key: int) -> None:
        map_key=self.map[self.hash(key)]
        for i, (k,v) in enumerate(map_key):
            if k==key:
                map_key.pop(i) #removes by index.. #.remove removes by value
                return

        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)