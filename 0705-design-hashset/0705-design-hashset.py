class MyHashSet:

    def __init__(self):
        self.size=10000
        self.bucket=[[] for _ in range(self.size)]

    def hash(self,key):
        return key%self.size
        

    def add(self, key: int) -> None:
        bucket_key=self.bucket[self.hash(key)]
        if key not in bucket_key:
            bucket_key.append(key)
        

    def remove(self, key: int) -> None:
        bucket_key=self.bucket[self.hash(key)]
        if key in bucket_key:
            bucket_key.remove(key)
        
    def contains(self, key: int) -> bool:
        bucket_key=self.bucket[self.hash(key)]
        return key in bucket_key
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)