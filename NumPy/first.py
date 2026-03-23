import numpy as np
a= np.array([1,2,3],dtype='float16')
print(a)
b=np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]],dtype='float64')
print(b)   
print(b.ndim)
print(b.shape)
print(b.dtype)
print(a.itemsize) #size of each element in the array in bytes
print(b.itemsize) #float64 is 8 bytes and float16 is 2 bytes
print(a.size) #total number of elements in the array or the total number of items in the array not elements in the array
print(a.nbytes) #total bytes consumed by the array or total bytes consumed by the elements of the array or size*itemsize

