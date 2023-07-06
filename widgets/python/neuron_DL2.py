#!/usr/bin/python3

# ## {R2D2919B742E} ##
# ###########################################################################
# What if magic existed?
# What if a place existed where your every thought and dream come to life.
# There is only one catch: it has to be written down.
# Such a place exists, it is called programming.
#    - Scott Taylor Reph, RightThumb.com
# ###########################################################################
# ## {C3P0D40fAe8B} ##

import numpy as np


X = np.array([ [0,0,1],[0,1,1],[1,0,1],[1,1,1] ])
y = np.array([[0,1,1,0]]).T
syn0 = 2*np.random.random((3,4)) - 1
syn1 = 2*np.random.random((4,1)) - 1
for j in range(60000):
	# print(j)
	l1 = 1/(1+np.exp(-(np.dot(X,syn0))))
	l2 = 1/(1+np.exp(-(np.dot(l1,syn1))))
	l2_delta = (y - l2)*(l2*(1-l2))
	l1_delta = l2_delta.dot(syn1.T) * (l1 * (1-l1))
	syn1 += l1.T.dot(l2_delta)
	syn0 += X.T.dot(l1_delta)
	# if j%1000==0:
	#     print(syn0)
	#     print(syn1)
	#     print()

