import math
import xlwt 
from xlwt import Workbook

wb = Workbook()
sheet1=wb.add_sheet('Sheet 1')



def fi(eta, m):
    cfi=((math.pow(eta,5/3))*(math.pow((1+m*eta),5/3)))/(math.pow((1 + 2*math.sqrt(1+m*m)*eta),2/3))
    return cfi
    

def frange(start, stop, step):
    while start <= stop:
        yield start
        start += step


sheet1.write(0,0,'eta')

sheet1.write(0,1,'m=0')
sheet1.write(0,2,'m=1')
sheet1.write(0,3,'m=1.5')
sheet1.write(0,4,'m=2')
sheet1.write(0,5,'m=2.5')


indexofrow=1

for i in frange (0.1, 2, 0.005):
    
    sheet1.write(indexofrow,0,float(i))
    sheet1.write(indexofrow,1,fi(float(i),0))
    sheet1.write(indexofrow,2,fi(float(i),1))
    sheet1.write(indexofrow,3,fi(float(i),1.5))
    sheet1.write(indexofrow,4,fi(float(i),2))
    sheet1.write(indexofrow,5,fi(float(i),2.5))
    indexofrow=indexofrow+1


wb.save('values.xls')