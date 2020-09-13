
import pandas as pd 

data = pd.read_csv("it51org.csv",names=['fyear','tic','conm','at','revt']) 
data2 = pd.read_csv("it51org.csv")
list8=list()
print (data2)
year_,tic_,conm_,at_,revt_,tic_real=list(),list(),list(),list(),list(),list()
for i in data['tic']:
	tic_.append(i)
for i in range(len(tic_)-7):
	if tic_[i] == tic_[i+7]:
		tic_real.append(tic_[i])
tic_real=list(dict.fromkeys(tic_real))
for i in range(len(tic_real)):
	data3 = pd.read_csv("it51org.csv",names=['fyear'],index_row = [i]) 
	if data3['fyear'].count()<=7:
		pass
	else 
		list8.append(i)
export_csv = df.to_csv =(r'q2outout.csv')	
print (tic_real)
