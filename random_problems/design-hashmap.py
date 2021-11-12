# Design a HashMap without using any built-in hash table libraries.

# Implement the MyHashMap class:

# MyHashMap() initializes the object with an empty map.
# void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
# int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
# void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.

class MyHashMap:
    

    def __init__(self):
        self.hashmap = []

    def put(self, key: int, value: int) -> None:
        
        for entries in self.hashmap:
            if key == entries.key:
                entries.value = value
                return None 

        new_entry  = myhashmap(key,value)
        
        self.hashmap.append(new_entry)

    def get(self, key: int) -> int:
        for entries in self.hashmap:
            if key == entries.key:
                return entries.value 
        return -1 

    def remove(self, key: int) -> None:

        for i in range(len(self.hashmap)):
            if key == self.hashmap[i].key:
                self.hashmap.pop(i)
                return None

        
class myhashmap:
	def __init__(self,inkey,invalue):
		self.key = inkey 
		self.value = invalue 


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)