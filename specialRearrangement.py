# the concept of this is to create a function that have a list of nbs 
# as a parameter , we take it and arrange the even nbs aside then the 
# odd ones after them and preserve the original relative order 
# first we must create a loop to search for the even then the odd 
# next we must put them in order 

list_of_integrs = [3,2,1,10,19,5,7]

def relative_order(array:any ) :
    #creating a function that put numbers in order ,taking the list as parameter
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
#returning the arranged array

def special_arrangement(list_of_integrs):
  #creating a function that take lists as parameter , it specifies the even nb and the odd nbs 

  new_list = [] 
  #creating list to add the two other lists(even and odd) at last 
  even_list = [] 
  #creating list for storing even nbs 
  odd_list  = []
  #creating list for storing odd nbs

  for i in range(len(list_of_integrs)-1):
      #creating or loop for checking the list
      if list_of_integrs[i] % 2 == 0:
         #checking if the content of the index is even
         even_list.append(list_of_integrs[i])
         #if even its going to be stored in the even list
      else:
         #else it is going to store the value as odd nb in the odd list
         odd_list.append(list_of_integrs[i])

  relative_order(even_list)
  #applying funtion relative order to order the nbs in the even_list in relative order 
  relative_order(odd_list)
  #applying funtion relative order to order the nbs in the odd_list in relative order 
  new_list = even_list + odd_list 
  #adding the two lists in one list

  return new_list
#returning the list 

print(special_arrangement(list_of_integrs))



















