import numpy as np

# mse    ----- mean of squared error        

actual=np.array([[1,2,3]])
predicted=np.array([[8,9,10]])

def mse(actual,predicted):
    np.mean((actual-predicted)**2)

print(mse(actual,predicted))
