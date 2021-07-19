#Nueron:error,input,output,weight_update,error_calc,desired_output,inputSummation,activation(HIdden and OUTPUT only),predict
#Node: weight,input_nueron,actual_value,predicted,input_nueron_id,output_nueron_id
#Layer:Nuerons[],error gradient,layer_bias(optional)
#Network: learning_rate
#
#Output Nueron Error:E=y(1-y)(d-y)[E=error,y=output,d=desired_output]
#Hidden Nueron Error:E=y(1-y) ([sum k=1->n]w*output_error)
#Node weight_update: old_weight+learningRate*InputNueron[summation]*error_of_OutputNueron
#weightupdate=old_weight-learningRate(inputSummation*(predicted/calculated[y])-actual[actual y]))
#
import numpy as np
import random
import matplotlib.pyplot as plt
import math
#plt.axis([0, 10, 0, 1])
fig = plt.figure()
ax = fig.add_subplot(111)
x = np.linspace(0, 30, 100)
y=np.sin(x)
line1, = ax.plot(x, y, 'b-')
for i in np.linspace(0,5,100):
    y = random.uniform(-1,1)
    #plt.scatter(i, y)
    line1.set_ydata(y)
    fig.canvas.draw()
    plt.pause(0.05)

plt.show()