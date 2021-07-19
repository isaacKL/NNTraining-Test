#STOCK Order of Operations
#TODO Soft run on which[Top 20] has highest predicted gain initially (run ~1 day)
#TODO Add total predict give each a share factor [1-100 (.01-1.0)]
#TODO distribute available profit based on share factor 
#TODO Let that sit for one week, simultaneously start a new
#TODO Remodel with medium investigation(run ~5 days), pull out lowest profits prediction reinvest in highs with new share factors
#TODO let sit for 2 weeks-month or longer(continous prediction pull prior to predict down fall)
#TODO Collect new options based on news and stock forecast
#TODO use ruew money to invest in news based (run for ~8 days) if uneventful pull


'''
DB Tables:
Tickers[ID,Symbol,Date Added]
Accounts[ID,Name,Ruew?,Amount]
Funds[ID,Account_ID,Name,Price](Ruew,Basic, Advance/Risk)
Assets[ID,Ticker_ID,Funds_ID,Value,Increase value since added, Increase percent since added, share factor,type(crypto/stock),New?,Ruew?, Date Last Checked,Next Date Check]
Queue[ID,Assets_ID,Date Added,Final Value,Final Increase,Queue Priotity,date to remove]

Functions:
Thread:1-Run Soft model (store in json)


Thread:2-Phase 1[Find suitable stocks](weekly)
getAvailableFunds()
establishAsset(ticker,init_value,default:0,default:0,share_factor,STOCK,Fund_ID)

Thread:3-Run medium model(store in json)


Thread:4-Phase 2[Narrow down stocks from prior week](biweekly, run through all long term stocks)
getEstablishedAssets()
checkPercent() [Compare it against it share factor lower decrease can be risk]

Thread 5: Daily Check
CheckAssests(prioritize reuw,long-term,basic in that order, queue lost cause[HIGH(after run),MEDIUM(end of day),LOW(end of week)])
CheckQueue()[Export done to json with profile]
SellSharesofEliminated()(in json)


'''
 
#Crypto Order of Operations
#TODO Same as STOCK Order of Operations but with different margins and api
from nn.NueralNetwork import *
import os,sys
import numpy as np
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import collections

if __name__=="__main__":
    
    os.system('cls')
    go=True
   
    y=collections.deque(np.zeros(10))
    fig=plt.figure()
    ax=fig.add_subplot(111)

    n=NueralNetwork(2,1,[2],1)
    
    while go:
        n.loadData('1,1,2\n1,1,2\n1,1,2')
        print(n.test([1,1],2))
        os.system('cls')
        x=n.run()
        n.saveState('test.state')
        
        y.append(n.test([1,1],2))
        ax.plot(y)
        
        #time.sleep(0.1)
        go=False if y.popleft()==2.0 else True
    plt.show()
''' 
import numpy

import matplotlib.pyplot as plt
numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))

myline = numpy.linspace(0, 6, 100)

plt.scatter(train_x, train_y)
plt.plot(myline, mymodel(myline))
plt.show()'''