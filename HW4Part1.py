def my_function(some_list):
     i=0
     output=some_list
     n=len(some_list)-1
     while (i <= n-1):
       print(output[i],end=", ")
       i=i+1
     while (i == n):
       print('and', output[i], end='.')
       i=i+1
     
     return output
 

vegetables = ['carrot', 'lettuce', 'onion', 'radish']
output = my_function(vegetables)
