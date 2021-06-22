import numpy as np
# data = np.array([[1, 2, 3], [10, 20, 30]])
# print(data)
# print(data.shape)
# print(data.size)
# print(data.ndim)
# print(data.dtype)
# print(data.nbytes)

# data1 = np.array([1, 2, 3, 4, 5])
# print(data1)
# print(data1.shape)
#
# data2 = np.array([[[1, 2, 3], [1, 2, 3], [1, 2, 3]], [[1, 2, 3], [1, 2, 3], [1, 2, 3]], [[1, 2, 3], [1, 2, 3], [1, 2, 3]], [[1, 2, 3], [1, 2, 3], [1, 2, 3]]])
# print(data2.shape)
# print(data2)
# data3 = np.array((1, 2,3))
# print(data3)
#
# data4 = np.array(range(10))
# print(data4)

# zeroarray = np.zeros((2, 3))
# print(zeroarray)
# zeroarray2 = np.zeros((2, 3), dtype=int)
# print(zeroarray2)

# one_array = np.ones((3, 5))
# print(one_array)

# empty_array = np.empty((3, 3))
# print(empty_array)
# empty_array.fill(50)
# print(empty_array)

# single_step = np.full(10, 5)
# print(single_step)

# xaxis = np.array(range(0, 11, 2))
# xaxis = np.arange(0, 11, 2)
# print(xaxis)
# yaxis = np.linspace(0, 10, 6)
# print(yaxis)
# logx = np.logspace(0,10,6)
# print(logx)

# data_1d = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(data_1d[5])
# print(data_1d[-4])
# print(data_1d[2:5])
# print(data_1d[:6])
# print(data_1d[6:])
# print(data_1d[-1::-1])
# print(data_1d[::-1])
# print(data_1d[:])

# data_test = np.array([[1, 2, 3, 4], [10, 20, 30, 40],
#                       [100, 200, 300, 400], [110, 210, 310, 410]])
# print(data_test)
# print(data_test[2,1])
# print(data_test[2:,1:])
# print(data_test[1:3,1:3])
# print(data_test[2,:])
# print(data_test[:,3])

# one_d = np.arange(12)
# print(one_d)
# rshapec = np.reshape(one_d,(3,4))
# print(rshapec)
#
# rshaper = np.reshape(one_d,(3,4), order='F')
# print(rshaper)
#
# rshape2 = np.reshape(rshapec, (6,2), order='F')
# print(rshape2)
#
# one_d_again = np.ndarray.flatten(rshape2)
# print(one_d_again)
# # print(rshape2.flatten())
# print(type(one_d))

# data_new = np.array([[1, 2, 3 ],[3, 9, 5],[-2, 0, 7],[0.8, 10, 3]])
# print(data_new)
#
# # sorted_array = np.sort(data_new)
# print(np.sort(data_new))
# print(np.sort(data_new, axis=1))
# print(np.sort(data_new, axis=0))
# print("*"*25)
# print(np.sum(data_new))
# print(np.sum(data_new, axis=0))
# print(np.sum(data_new, axis=1))

