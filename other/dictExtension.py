

"""

Example 1
methods = ['add', 'add' 'addToValues', 'get' ,addToKeys', 'get']
queries = [[2,4], [4,5] [2],[4],[1], [3]]

output - sum of gets
{
    2:4,
    4:5
}

{
    2:6,
    4:7
}

{
    3:6,
    5:7
}

output - 7+6

return 13

"""

def solution(methods, queries):
    
    mydict = {}
    sumResults = 0
    
    def addToDict(arr):
        nonlocal mydict
        
        mydict[arr[0]] = arr[1]
        
    def addToValues(value):
        nonlocal mydict
        for key in mydict:
            mydict[key] += value
            
    def addToKeys(valueToAdd):
        nonlocal mydict
        copy = {}
        for key, value in mydict.items():
            mykey, myvalue = key+valueToAdd, value
           
            copy[mykey] = myvalue
            
        mydict = copy
        
            
    def getValue(key):
        nonlocal sumResults
        
        sumResults += mydict[key]
        
    
    for i in range(len(methods)):
        if methods[i] == 'add':
            addToDict(queries[i])
            
            
        elif methods[i] == 'addToValues':
            addToValues(queries[i][0])
            
        elif methods[i] == 'addToKeys':
            addToKeys(queries[i][0])
            
        else:
            getValue(queries[i][0])
        
        # print(mydict)
        
    return sumResults
        
        

        
    

methods = ['add', 'add', 'addToValues', 'get' ,'addToKeys', 'get']
queries = [[2,4], [4,5], [2],[4], [1], [3]]

print(solution(methods, queries)) # output = 13

    
    
     