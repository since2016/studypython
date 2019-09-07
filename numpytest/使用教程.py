# Array 数组
# rank 维度

import numpy as np
a = np.array([1,2,3])
type(a)
a.shape

a = a.reshape((1,-1))
a.shape

a = np.array([1,2,3,4,5,6,7,8])
a = a.reshape((-1,2))
print(a)