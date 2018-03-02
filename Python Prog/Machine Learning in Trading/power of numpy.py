


import numpy as np

def test_run():
	print np.array([1,2,3])
	print np.array([(1,2,3),(4,5,6)])

	print np.empty(5) # create emapty 1 d array of size 5
	print np,empty((2,3)) # 2 d array of size 2*3
	print np,empty((2,3,4)) # default value is the stored value in that location of the computer

	# array of 1s
	print np.ones((5,4))

	# specfying the datatype # default of np is flaot
	print np.ones((5,4), dtype=np.int)

	# generate an array full of random numbers, uniformly sampled from [0.0, 1.0)
	print np.random.random((5,4)) # tuple argument
	print np.random.rand(5,4) # funtion argument , and not a tuple

	# sample numbers from a Gaussian (normal) distrubution
	print np.random.normal(size=(2,3)) # standard normal mean = 0, standard deviation = 1
	print np.random.normal(50,10, size=(2,3)) # changed mean = 50, standard deviation = 10

	# random integers
	print np.random.randint(10) # a single integer in [0,10)
	print np.random.randint(0,10) # same  as above, specfying [low,high) explictly
	print np.random.randint(0,10,size=5) # 5 random integers as a 1D array
	print np.random.randint(0,10, size=(2,3)) # 2*3 array of random integers

	# array attributes
	a =  np.random.random((5,4))
	print a.shape # 5,4
	print a.shape[0],a.shape[1]
	print len(a.shape)  # gives the dimension i.e 2 2D array
	print a.size # no of elements i.e 20
	print a.dtype # float64 ..type of the array elem

	# Operation on ndarray :stastics min,max,mean(across row,column and overall)
	np.random.seed(693)
	a = np.random.randint(o,10, size=(5,4))  # 5*4 random integer in [0,10)
	print 'min of each column', a.min(axix=0).. #i.e iterate over row
	print 'max of each row', a.max(axix=1).. #i.e iterate over column
	print 'mean of all elem ', a.mean().. #i.e can provide axix=0/1

	# Find the maximum and its index in array
    print "Maximum value:", a.max()
    print "Index of max.:", a.argmax() # print amx elem adn its index

    # Assigning a single value to an entire row
    a = np.random.rand(5,4)
    a[0, :] = 2
    a[0,0] = 1
    a[:, 3] = [1,2,3,4,5] # assigning a list to a column in a array. length must be same

    # numpy index
    a = np.random.rand(5)
    indices = np.array([1,1,2,3])
    print a[indices] # print elem in arrray at index 1,1,2,3

    # numpy masking
    a = np.array([(20,25,23,26,32,10,5,0),(0,2,50,0,1,28,5,0)])

    mean = a.mean()

    # masking
    a[a<mean] = mean # all values in array which are less than mean is assinned mean value

    # Arithmetic Operation
    # after each operation a new array is created and the original array remain intact
    a = np.array([(1,2,3,4,5),(10,20,30,40,50)])
    b = np.array([(100,200,300,400,500),(1,2,3,4,5)])
    print 2*a
    print a/2  # integer divison result a/2.0 = float diviion of the elem of the array

    # multiply a and b 2D array.. this is elem by elem multiplicatin and not matrix multiplication
    print a*b
    print a/b


if __name__ == "__main__":
	test_run()

























