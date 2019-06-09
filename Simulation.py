Req = 1000000
N_tries4 = []
import numpy as np
import pandas as pd
from statistics import mode
for i in range(Req):
	N_tries = []
	
	v = 0
	while v != 4:
		v = np.random.randint(1,7)
		N_tries.append(v)
	N_tries4.append(len(N_tries))

print('mean is',sum(N_tries4)/Req)
print('number of tries is',mode(N_tries4))
df = pd.DataFrame(N_tries4)
print(max(df.groupby([0]).groups),'\n',df.groupby(0).size().sort_values(ascending=True))
all=df.groupby(0).size().sort_values(ascending=False)
print((sum(all[0:4])/Req)*100)
