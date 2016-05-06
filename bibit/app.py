"""
(1 hour)
Warning: This code has been developed for Linux platfrom.

Requirements:
    Ubuntu 14.04
    Python 3.5.1

Developer: Shayan Yazdanmehr
E-mail: shayany@ifi.uio.no
Personal E-mail: shayan.yazdanmehr@gmail.com
Phone Number: +47 486 35 510
"""

#!/usr/bin/env python

import sys
from packages import transition,row_column,oneD_to_twoD,convert_array,reduce,print_array
#Here I get the argument from user
for arg in sys.argv:
    stream=arg
#Reverse the input, as a result the left part has lowest value
rev=stream[::-1]
print(stream)

if (stream == len(stream) * stream[0]): #If the input string is only contain zero or one return the answer without any furthur computation
    print(stream[0])
else:
    while(True):
        row, column = row_column(len(stream))  # Compute how many rows and columns we need for current input
        array = oneD_to_twoD(stream[::-1], row) # Based on the string we create an 2D array to keep the string (Easy to process)
        array, segments = convert_array(array, row,len(stream)/4)  #Apply the rules on the array

        if segments==0: # If segments is zero then we should not reduce to string
            stream = ""
            for i in array:
                for j in i:
                    stream+=str(j)
        else: #Reduce the string to smaller string (64 becomes 16, 16 becomes 4)
            stream=""
            print_array(array)
            for i in reduce(array,row):
                for j in i:
                    stream+=str(j)

        if(len(stream)==1): #If the length is 1 just return the result
            print(stream)
            break
        if(stream == len(stream) * str(stream[0])): #If the input string is only contain zero or one return the answer without any furthur computation
            print(stream[0])
            break
        stream=stream[::-1] #Reverse the string
        print(stream)