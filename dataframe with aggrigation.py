import pandas as p
d=p.DataFrame([[2,5,6],
              [4,6,3],
              [5,7,8]],
              columns=["Maths","java","py"])
print(d)
c=d.agg(['sum','min','count','mean','std','size'])
print()
print(c)