from array import array #Library import

# declare an object of array type
myArray = array('i', [1,2,3,4,5,6,7,8,9,10]) # Declare and initialize myArray object
print(myArray)

# Methods
# append(self,v,/)
myArray.append(11)
print(myArray)
myArray = array('i', [1,2,3,4,5,6,7,8,9,10,9,8,7,7,6,5,4,3,2,1]) # Re-initializer
print(myArray.buffer_info())

# count(self, v, /)
var1 = myArray.count(1)
print(var1)

# extend(self, bb, /) # list, tuple - collection
list1 = [8,4,5,6]
tup1 = (1,2,3,4,5)
set1 = {2,3,4,5,6}
tmp_array = array('i', [5,6,7,8])
myArray.extend(list1)
myArray.extend(tup1)
myArray.extend(set1)
myArray.extend(tmp_array)
print(myArray)