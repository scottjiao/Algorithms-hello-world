# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 13:15:43 2018

@author: ziang
"""
'''
# =============================================================================
# #插入排序
# =============================================================================
'''
def insertSort(array):
    sortedArray=[]
    i=0
    while True:
        if i>=len(array):
            break
        newCard=array[i]
        #插入部分实现有改进空间(优化：二分插入)
        #print(sortedArray,newCard)
        insertElementSorted(sortedArray,newCard,0,len(sortedArray)-1)
        #print(sortedArray,newCard)
        i+=1
    return sortedArray
#测试
#insertSort(List)
'''    
# =============================================================================
# #堆排序
# =============================================================================
'''
class Heap(list):
    def __init__(self,List,heapsize=0):
        super(Heap,self).__init__(List)
        self.heapSize=heapsize
        
def maxHeapify(heap,i):
        i_strct=i+1
        left=2*i_strct-1
        right=2*i_strct+1-1
        if left<=heap.heapSize-1 and heap[left]>heap[i]:
            #print('left')
            largest=left
        else:
            largest=i                        
        if right<=heap.heapSize-1 and heap[right]>heap[largest]:
            #print('right')
            largest=right
        else:
            largest=largest            
        #print(heap,i,left,right)
        #print(largest,heap[i],heap[left],heap[right])
        #print(heap)        
        if largest!=i:
            temp=heap[i]
            heap[i]=heap[largest]
            heap[largest]=temp
            maxHeapify(heap,largest)
        else:
            pass
        return
#maxHeapify(Heap([1, 3, 1, 2, 2, 5],heapsize=6),0)

def buildMaxHeap(heap):
    for i in range(heap.heapSize,0,-1):        
        maxHeapify(heap,i-1)
        #print(heap,i-1)
#    return heap        
#buildMaxHeap(Heap([1,2,1,2,3,5],heapsize=6))        
        
def heapSort(array):
    heap=Heap(array,heapsize=len(array)) 
    buildMaxHeap(heap)   
    for i in range(len(array),0,-1):        
        
        #print(heap)
        heap.heapSize-=1        
        temp=heap[i-1]
        heap[i-1]=heap[0]
        heap[0]=temp
        maxHeapify(heap,0)
    return list(heap)        
#a=[6,1,2,1,2,3,5,2,3,1,9,3,1]
#heapSort(a)          
'''            
# =============================================================================
# #快速排序           
# =============================================================================
'''            
def partition(array,p,r):
    i=p-1
    j=p    
    while True:        
        if j >r:
            break
        if array[j]<=array[r]:
            #print(array,i,j)
            temp=array[j]
            array[j]=array[i+1]
            array[i+1]=temp
            i+=1
        j+=1    
    return i
        
def recurrsionQuick(array,p,r):
    #print(array,p,r)
    if p<r:
        parts=partition(array,p,r)
        #print(parts)
        recurrsionQuick(array,p,parts-1)
        recurrsionQuick(array,parts,r)
    
def quickSort(array):
    p=0
    r=len(array)-1
    #避免直接改变原数组
    copyArray=[0]*len(array)
    for i in range(len(array)):
        copyArray[i]=array[i]        
    recurrsionQuick(copyArray,p,r)
    return copyArray
        
#a=[1,2,1,2,3,5]
#d=quickSort(a)     
    
'''    
# =============================================================================
# #计数排序    
# =============================================================================
'''        
#先定义好最大值最小值搜寻算法
def minmax(array):
    Min=float("inf")
    Max=-float("inf")
    for i in range(int(len(array)/2)):
        left=array[2*i]
        right=array[2*i+1]        
        if left<right:
            if Min>left:
                Min=left
            if Max<right:
                Max=right
        else:
            if Min>right:
                Min=right
            if Max<left:
                Max=left    
    if 2*i+2<len(array):
        lastElement=array[2*i+2]
        if lastElement<Min:
            Min=lastElement
            return (Min,Max)
        if lastElement>Max:
            Max=lastElement
            return (Min,Max)
    return (Min,Max)        
#然后做计数排序    
def countSort(array):    
    minimal,maximal=minmax(array)
    #do it
    k=maximal-minimal+1    
    container=[0]*k
    for i in array:
        #check it
        if i!=int(i):
            raise ValueError('there exist non-integer')
            #非python环境
            #return 'there exist non-integer'
        container[i-minimal]+=1        
    sortedArray=[0]*len(array)    
    index=0
    for number in range(minimal,maximal+1):
        while container[number-minimal]:
            sortedArray[index]=number
            container[number-minimal]-=1
            index+=1
    return sortedArray        
#a=[1,2,1,2,3,5]
#countSort(a)        
'''    
# =============================================================================
# #基数排序    
# =============================================================================
'''        
def radixIntSort(array):
    copyArray=[]
    for i in range(len(array)):
        if i!=int(i):
            raise ValueError('there exist non-integer')
        else:            
            copyArray.append(str(array[i]))
    #print(copyArray)
    sortedArray=radixSort(copyArray)
    sortedIntArray=[int(i) for i in sortedArray]    
    return sortedIntArray

def radixSort(array):
    #预设数组中每个数都必须支持按位索引(可迭代对象)
    #并且被索引出来的元素都支持比较
    Max=-float('inf')
    for i in array:            
        if len(i)>Max:
            Max=len(i)    
    dimension=Max   
    for d in range(1,dimension+1):
        array=dimensionSort(array,d)
    #to do
    return array

def dimensionSort(array,d):
    #在这个基数上使用计数排序
    containers=[]
    for i in range(10):
        containers.append([])
    #containers=[[]]*10有坑慎用    
    #容器中每一个是一个栈（队列也可），用以存放该位相同的所有数
    for item in array:
        if len(item)<d:
            number=0
        else:
            number=int(item[-d])
        #print(number,item)
        containers[number].append(item)
        #print(containers)
    sortedArray=[]    
    for i in range(len(containers)):
        while True:
            if containers[i]==[]:
                break            
            #print(containers)
            item=containers[i].pop(0)
            sortedArray.append(item)
    return sortedArray
            
#a=[1,2,1,2,3,5]
#t=radixIntSort(a)                        
        
'''    
# =============================================================================
# #桶排序    
# =============================================================================
'''        
def insertElementSorted(sortedArray,element,p,r):
    #二分插入法
    #print(p,r)
    #末尾索引等于长度减一的想法并不完全正确，当长度为零时会发生错误（此时长度等于末尾索引）
    if p<r:
        left=p+int((r-p)/2)
        right=left+1
        #print(right,left)
        if sortedArray[left]<=element and element<=sortedArray[right]:
            sortedArray.insert(right,element)
        elif sortedArray[left]>element:
            insertElementSorted(sortedArray,element,p,left)
        elif sortedArray[right]<element:
            insertElementSorted(sortedArray,element,right,r)
    elif p==r:
        if element>sortedArray[p]:
            sortedArray.insert(p+1,element)
        else:
            sortedArray.insert(p,element)
    elif r==-1:
        #一定是空集的时候
        assert p==0
        sortedArray.insert(0,element)
    
def bucketSort(array):
    #假设数组是0-1分布的实数
    containers=[]
    for i in range(10):
        containers.append([])
    for element in array:
        if element>1:
            raise ValueError('greater than 1.0 !')
        elif element==1:
            index=9
        else:
            index=int(element/0.1)
        #print(element,index)
        insertElementSorted(containers[index],element,0,len(containers[index])-1)
    #print(containers)
    sortedArray=[]    
    for i in range(len(containers)):
        while True:
            if containers[i]==[]:
                break            
            #print(containers)
            item=containers[i].pop(0)
            sortedArray.append(item)
    return sortedArray   

#b=[0.33,0.43,0.53,0.66,0.12]
#t=bucketSort(b)  
    
'''    
# =============================================================================
# #测试  
# =============================================================================
'''        

import time

def timeCount(sortFunc,array):
    start=time.time()
    print('start {} now, {} is the length of array.'.format(sortFunc.__name__,len(array)))
    sortedArray=sortFunc(array)
    end=time.time()
    print('end {} now, {}s is the time we cost.'.format(sortFunc.__name__,end-start))
    return end-start
    
    
import numpy as np
from matplotlib import pyplot as plt
#List=list(np.random.choice(range(100000),100000)) 
'''   
sortedArray=timeCount(insertSort,List)    
sortedArray=timeCount(heapSort,List) 
sortedArray=timeCount(quickSort,List) 
sortedArray=timeCount(countSort,List) 
sortedArray=timeCount(radixIntSort,List) 
sortedArray=timeCount(sorted,List)
'''

tryList=[insertSort,heapSort,quickSort,countSort,radixIntSort,sorted]
valueList=[]
for function in tryList:
    valueList.append([])
    for number in range(1,11):
        List=list(np.random.choice(range(10000*number),10000*number)) 
        value=timeCount(function,List)
        valueList[-1].append(value)
for (Values,i) in zip(valueList,range(len(valueList))):
    plt.plot([n*10000 for n in range(1,11)],Values,label=tryList[i].__name__)
plt.legend()
plt.title('dense')
plt.show()

valueList=[]
for function in tryList:
    valueList.append([])
    for number in range(1,11):
        List=list(np.random.choice(range(100000*number),10000*number)) 
        value=timeCount(function,List)
        valueList[-1].append(value)
for (Values,i) in zip(valueList,range(len(valueList))):
    plt.plot([n*10000 for n in range(1,11)],Values,label=tryList[i].__name__)
plt.legend()
plt.title('sparse')
plt.show()

valueList=[]
for function in tryList:
    valueList.append([])
    for number in range(1,11):
        List=list(np.random.choice(range(500*number),10000*number,replace=True)) 
        value=timeCount(function,List)
        valueList[-1].append(value)
for (Values,i) in zip(valueList,range(len(valueList))):
    plt.plot([n*10000 for n in range(1,11)],Values,label=tryList[i].__name__)
plt.legend()
plt.title('very dense')
plt.show()
