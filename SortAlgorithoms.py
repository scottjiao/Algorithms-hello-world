# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 13:15:43 2018

@author: admin
"""
'''
# =============================================================================
# #插入排序
# =============================================================================
'''
def insertSort(array):
    sortedArray=[0]*len(array)
    i=0
    while True:
        if array==[]:
            break
        newCard=array.pop()
        
        #插入部分实现有改进空间
        #case1 用数组来实现(将sortedArray视作基本数据结构)
        for j in range(i):
            if newCard<sortedArray[i-j]:
                sortedArray[i-j+1]=sortedArray[i-j]
                
            else:
                sortedArray[i-j+1]=newCard
                i+=1
                break
        
        
        
    return sortedArray

#测试
#insertSort([2,3,4,1,2,3])
        
    
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
    
    
    for i in range(len(array),0,-1):
        
        buildMaxHeap(heap)
        #print(heap)
        heap.heapSize-=1
        
        temp=heap[i-1]
        heap[i-1]=heap[0]
        heap[0]=temp
    return list(heap)
        
#a=[1,2,1,2,3,5]
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
            
            copyArray.append(str(i))
    sortedArray=radixSort(copyArray)


def radixSort(array):
    #预设数组中每个数都必须支持按位索引(可迭代对象)
    #并且被索引出来的元素都支持比较
    Max=-float('inf')
    for i in array:
            
        if len(i)>Max:
            Max=len(i)
    
    dimension=Max
    
    for d in range(dimension):
        dimensionSort(array,d)
            
                    
    
    
    #to do
    return array



'''    
# =============================================================================
# #桶排序    
# =============================================================================
'''        

def bucketSort(array):
    #to do
    return


















