class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def print_table(self):
        for key, value in enumerate(self.data_map):
            print(f"key: {key}, value: {value}")

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []

        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)

        if self.data_map[index]:
            for i in self.data_map[index]:
                if i[0] == key:
                    return i[1]
            return None

    def keys(self):
        all_keys = []

        for i in range(len(self.data_map)):
            if self.data_map[i]:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])

        return all_keys



hash_table = HashTable()
hash_table.set_item('prem', 77807935)
hash_table.set_item('pravi', 8834904)
hash_table.set_item('rachel', 29303)
hash_table.set_item('mani', 428)
hash_table.set_item('saran', 4353)

print("get item: ", hash_table.get_item('saran'))
print("get item: ", hash_table.get_item('saranbitch'))
print("get keys: ", hash_table.keys())
# hash_table.print_table()
