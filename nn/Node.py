#Node: weight,input_nueron/output,error
import typing
import random
from nn.Nueron import BaseNueron

class Node:

    def __init__(self,i:BaseNueron,o:BaseNueron,weight=0):
        
        #Assign Random weight initially
        random.seed(13)
        self.weight=random.uniform(0.1,.9) if weight==0 else weight
        self.i_nueron=i
        self.o_nueron=o

        #error of output nueron
        self.error=0
    
    def getError(self):
        return self.error
    def setError(self,error:int):
        self.error=error

    def setWeight(self,value:int):
        self.weight=value
    def getWeight(self):
        return self.weight

    def updateWeight(self,learningRate):
        self.weight+=learningRate*self.o_nueron.input_summation*self.o_nueron.error


    



if __name__=="__main__":
    print("Node")