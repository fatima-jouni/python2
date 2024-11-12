# the concept of this program to move ll all the zeros found in a list 
# to the end of the list while preserving the order of the nbs in the list 
#  created a counter that counts the nbs of zeros , and created a new list to append 
# the numbers found in the previous list without the zeros ,at last i fill the list by zeros 
# according to the counter 

def move_zeros(my_list :list):
  #creating a function to do this 
  count = 0
  #creating a counter that counts the nb of zeros found in the list
  new_list = []
  #new list to take the nbs not zero from the previuos one while preserving the order
  for i in range (len(my_list)):
    #for loop tocheck the nb of zeros found 
    if my_list[i] == 0:
        count +=1
        #counting the zeros and saving the value in the count variable
    else:
        #for other nbs they are going to be appended to a new list
        new_list.append(my_list[i])
 
  for i in range (count):
   #at the end,we are going to fill the lsit by the zeros that we removed 
   new_list.append(0)

  print("old list is ",my_list)
  #print the old list
  print("new list is ",new_list)
  #print the new one moving the zeros to the end

#Example1:  
my_list = [2,7,5,0,4,2,0]
move_zeros(my_list) 
print() 

#Example2:
array = [0,5,9,7,0,1,0]
move_zeros(array)
print() 
