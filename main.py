nested_list = [['a', 'b', 'c'],['d', 'e', 'f', 'h', False],[1, 2, None]]

#1

class FlatIterator:
    def __init__(self, nested_list):
        self.nested_list = nested_list
        self.value = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.value += 1
        res_list = [item for items in self.nested_list for item in items]
        if self.value >= len(res_list):
            raise StopIteration
        else:
            result = res_list[self.value]
            return result

for item in FlatIterator(nested_list):
    print(item)

flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)

#2

def FlatIterator(nested_list):
    for items in range(len(nested_list)):
        for item in nested_list[items]:
            yield item

for item in  FlatIterator(nested_list):
	print(item)

