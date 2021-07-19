from nn.Nueron import *
from nn.Node import *
import copy

class NueralNetwork():

    def __init__(self,inputs=0,outputs=0,hidden=[],learningRate=0.0,run=True,statefile='n/a',bias=0):
        self.nodes=[]
        self.bias=bias
        if statefile=='n/a':
            _input=[]
            _hidden=[]
            _output=[]
            for i in range(inputs):
                _input.append(InputNueron())
            for i in range(len(hidden)):
                temp=[]
                for j in range(hidden[i]):
                    temp.append(HiddenNueron())
                _hidden.append(temp)
            for i in range(outputs):
                _output.append(OutputNueron())

            self.inputs=_input
            self.runs=[run,0]
            self.outputs=_output
            self.hidden=_hidden
            self.hidden_layers=len(hidden)
            self.learning_rate=learningRate
            
            self.syncNodes([])
        else:
            self.loadState(statefile)
        
    
    def syncNodes(self,stateNodes=[]):
        sn= lambda x: x.pop() if x else 0
        for i in range(len(self.inputs)):
            for j in range(len(self.hidden[0])):
                temp=Node(self.inputs[i],self.hidden[0][j],sn(stateNodes))
                self.nodes.append(temp)
                self.inputs[i].o_nodes.append(temp)
                self.hidden[0][j].i_nodes.append(temp) 
        if self.hidden_layers>1:
            for i in range(self.hidden_layers-1):
                if (i+1)<self.hidden_layers:  
                    for j in range(len(self.hidden[i])):
                        for k in range(len(self.hidden[i+1])):
                            temp=Node(self.hidden[i][j],self.hidden[i+1][k],sn(stateNodes))
                            self.nodes.append(temp)
                            self.hidden[i][j].o_nodes.append(temp)
                            self.hidden[i+1][k].i_nodes.append(temp)
        for i in range(len(self.hidden[self.hidden_layers-1])):
            length=self.hidden_layers-1
            for j in range(len(self.outputs)):
                temp=Node(self.hidden[length][i],self.outputs[j],sn(stateNodes))
                self.nodes.append(temp)
                self.hidden[length][i].o_nodes.append(temp)
                self.outputs[j].i_nodes.append(temp) 

        

    def loadData(self,data):
        self.data=data.split('\n')
        for i in range(len(self.data)):
            self.data[i]=[int(j) for j in self.data[i].split(',')]
            #print(self.data[i])
        print("Data Loaded")
    
    def calculateErrors(self,dos):
        for i in range(len(self.outputs)):
            self.outputs[i].calculateError(dos[i])
        for i in range(self.hidden_layers):
            for j in self.hidden[i]:
                j.calculateError()
        self.updateWeights()
    
    def updateWeights(self):
        for i in self.nodes:
            i.updateWeight(self.learning_rate)

    def loadState(self,stateFile):
        _input=[]
        _hidden=[]
        _output=[]
        nodes=[]
        runs=False
        learningRate=0
        try:
            with open(stateFile) as fp:
                print('Loading old state')
                header=fp.readline().split(';')
                runs=[True if header[0].find("True")!=-1 else False,int(header[0].split(',')[1].replace(']',''))]
                learningRate=float(header[1])
                for i in range(int(header[2])):
                   
                    _input.append(InputNueron())
                header[4]=header[4].split(',')
                for i in range(int(header[3])):
                    temp=[]
                    for k in range(int(header[4][i])):
                        temp.append(HiddenNueron())
                    _hidden.append(temp)
                for i in range(int(header[5])):
                    _output.append(OutputNueron())
                Line=fp.readlines()
                for lines in Line:
                    nodes.append(float(lines.strip()))
                #nodes.reverse()
            self.inputs=_input
            
            self.runs=runs
            self.outputs=_output
            self.hidden=_hidden
            self.hidden_layers=len(_hidden)
            self.learning_rate=learningRate
            self.syncNodes(nodes)
        except IOError as e:
            print(e.msg())

    def saveState(self,stateFile):
        header=str(self.runs[0])+','+str(self.runs[1])+';'
        header+=str(self.learning_rate)+';'
        header+=str(len(self.inputs))+';'
        header+=str(self.hidden_layers)+';'
        layer_header=''
        for i in range(self.hidden_layers):
            layer_header+=str(len(self.hidden[i]))+','*(1 if i<self.hidden_layers-1 else 0)
        
        header+=layer_header+';'+str(len(self.outputs))+'\n'
        nodelines=''
        for i in self.nodes:
            nodelines+=str(i.getWeight())+'\n'
        with open(stateFile,'w') as fp:
            fp.write(header+nodelines)
        

                
    def run(self):
        i:int=0
        error_num=len(self.data[0])-1
        print(f'training... run:{self.runs[1]}')
        while[self.runs[0]] and i<len(self.data):
            for k in range(len(self.inputs)):
                f=self.inputs[k]
                
                f.inputScaled(int(self.data[i][k]))
            
            for k in range(self.hidden_layers):
                #print(f"Layer: {k+1}",end=': ')
                for l in self.hidden[k]:
                    l.getValue()
                    #print('{:.4f}'.format(l.getValue()),end=', ')
                    #print()
            #print('Outputs:',end=': ')
            for k in self.outputs:
                k.getValue()
                #print('{:.4f}'.format(k.getValue()),end=' ')
            #print()
            self.calculateErrors(self.data[i][error_num:])               
            i+=1
        self.runs[1]+=1
        return self.runs[1]
        
    
    def test(self,inp,o):
        a=[]
        for i in range(len(inp)):
            self.inputs[i].inputScaled(inp[i])
        for i in range(self.hidden_layers):
                #print(f"Layer: {k+1}",end=': ')
                for j in self.hidden[i]:
                    j.getValue()
        
        for i in self.outputs:
                a.append(i.getValue())
        self.calculateErrors([o])
        return a[0]
            
    