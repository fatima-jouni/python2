#steps to do this :
#sort the list
#for loop to check nb after nb
#in case its true then print the nb before i

def sorting_list(array) :
    for j in range (len(array)*len( array)):
       #for loop to compare all nbs with each other ,thats why the range is power 2 the length of array 
       for i in range (len(array)-1) :
           #for loop to compare each nb by the other nbs 
           if  array[i] >  array[i+1]:
               #in case a nb is greater than the other ,we're going to swap the nbs to have the right order
               temp = array[i]
               #assigning the previous value of array[i] in new variable to maintain the nb
               array[i] = array[i+1]
               #the second nb is replacing the first one ,since its smaller 
               array[i+1] = temp
               #setting the smaller index the value of temp(the new variable that took the smaller value )
    
    return array 

def first_missing_positive(array:list):
#creating a func that takes array as parameter
    sorting_list(array) 
    #sorting the list using the sorting method to ease the search process for the missing positive nb 
    for i in range(len(array) - 1):
        #ignoring the iterstion if the number is negative since we're interested in positive nbs only
        if array[i] <= 0:
            continue 
        # Check if the next number is not consecutive
        if array[i + 1] != array[i] + 1:
            print("The missing positive number in this array", array, "is", array[i] + 1)
            return 
    if array[i] > 0  :
    # If no missing number found in the loop, return the next positive number after the last element
     print("The missing positive number in this array", array, "is", (array[i]- 2))
    else:
      print("The missing positive number in this array", array, "is", array[-1] + 1)  

first_missing_positive([-1,1,3,2])
first_missing_positive([1,3,0])
first_missing_positive([2,3,4])
