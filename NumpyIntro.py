import numpy as np

#declare and print a list
list1 = [[1,2,3],[4,5,6]]
list1

#declare and print a numpy array
array1 = np.array([[1,2,3],[4,5,6]])
array1

#numpy array consumes less memory
import sys
#create a list with values 0 to 999
list1 = range(1000)
print("Size of each element of list in bytes: ",sys.getsizeof(list1))
print("Size of the whole list in bytes: ",sys.getsizeof(list1)*len(list1))

#create a numpy array with values 0 to 999
array1 = np.arange(1000)
print("Size of each element of the Numpy array in bytes: ",array1.itemsize)
print("Size of the whole Numpy array in bytes: ",array1.size*array1.itemsize)

#numpy arrays are faster than lists
import time
size=9999999
#create list1 and list2 with value 0 to size variable
list1 = range(size) 
list2 = range(size)

initialTime = time.time()

resultantList = [(a * b) for a, b in zip(list1, list2)] 

print("Time taken by Lists to perform multiplication:",  
      (time.time() - initialTime), 
      "seconds")

#create array1 and array2 with value 0 to size variable
array1 = np.arange(size)   
array2 = np.arange(size)
 
initialTime = time.time()
resultantArray = array1 * array2 

print("Time taken by NumPy Arrays to perform multiplication:", 
      (time.time() - initialTime), 
      "seconds") 

#numpy is convenient and element-wise operation is possible

#element wise operation is not possible in list and error is thrown
list1 =[1, 2, 3]
list1 = list1 + 1
list1

#elementwise operation is possible in numpy array making it convenient
array1 = np.array([1,2,3])
array1 = array1 + 1
array1
