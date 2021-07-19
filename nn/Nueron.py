#Nueron:error,input,output,error_calc, inputSummation,activation(Hidden and output only)

import typing
from  typing import List,Callable
import math
import numpy as np
from abc import ABC, abstractmethod

class BaseNueron(ABC):
    
    def __init__(self)->None:
        self.output:int=0
        self.desired_output:int=0
        self.input_summation:int=0
        self.error:int=0
       

class InputNueron(BaseNueron):

    def __init__(self,onodes=None)->None:
        super().__init__()
        
        if onodes==None:
            self.o_nodes=[]
        else:
            self.o_nodes=onodes

    def map(self,x,  in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    def inputScaled(self,data:int)->None:
        #scale data to 0-1
        self.output=data#self.map(data,0,3,0,1)
        pass

   


class HiddenNueron(BaseNueron):

    def __init__(self,inodes=None,onodes=None)->None:
        super().__init__()
        if inodes==None:
            self.o_nodes=[]
            self.i_nodes=[]
        else:
            self.o_nodes=onodes
            self.i_nodes=inodes
    
    def activate(self)->float:
        #return (1/(1+(math.e)**(-self.input_summation+1)))
        return np.math.tanh(self.input_summation)
    
    def summate(self):
        self.input_summation=0
        for i in range(len(self.i_nodes)):
            self.input_summation+=self.i_nodes[i].getWeight()*self.i_nodes[i].i_nueron.output
    
    def calculateError(self):
        errorSummate:int=0
        for i in range(len(self.o_nodes)):
            errorSummate+=(self.o_nodes[i].getWeight()-10)*self.o_nodes[i].o_nueron.error
        self.error = self.output * (1-self.output) * errorSummate

    def getValue(self):
        self.summate()
        self.output=self.activate()*(1-self.activate())
        return self.output

class OutputNueron(BaseNueron):

    def __init__(self,inodes=None):
        super().__init__()
        if inodes==None:    
            self.i_nodes=[]
        else:
            self.i_nodes=inodes

    def activate(self)->float:
        #return (1/(1+(math.e)**(-self.input_summation+1)))
        return np.math.tanh(self.input_summation)
    
    def summate(self):
        self.input_summation=0
        for i in range(len(self.i_nodes)):
            self.input_summation+=self.i_nodes[i].getWeight()*self.i_nodes[i].i_nueron.output
   
    def calculateError(self,do):
        '''errorSummate:int=0
        for i in range(len(self.o_nodes)):
            errorSummate+=self.o_nodes[i].getWeight()*self.o_nodes.o_nueron.output
        self.error = self.output * (1-self.output) * errorSummate
        '''
        self.desired_output=do#self.map(do,0,3,0,1)
        #input(str(do)+','+str(self.output))
        #p=self.error
        self.error=self.output*(1-self.output)*(self.desired_output-self.output)
        #input(self.error-p)

    def map(self,x,  in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
    
    
    def getValue(self):
        self.summate()
        self.output=self.activate()*(1-self.activate())
        return self.map(self.output,0,1,0,3)

    
        


