"""
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
from packages import transition,row_column,oneD_to_twoD,convert_array,reduce,print_array,display_triangle

#Here I get the argument from user
for arg in sys.argv:
    stream=arg
#Reverse the input, as a result the left part has lowest value
rev=stream[::-1]
print(stream)


if (stream == len(stream) * stream[0]):
    print(stream[0])
else:
    while(True):
        row, column = row_column(len(stream))
        array = oneD_to_twoD(stream[::-1], row)
        array, segments = convert_array(array, row,len(stream)/4)
        #print_array(array[::-1])
        #print(segments)
        if segments==0:
            stream = ""
            for i in array:
                for j in i:
                    stream+=str(j)
        else:
            stream=""
            #print(array)
            print_array(array)
            for i in reduce(array,row):
                for j in i:
                    stream+=str(j)

        if(len(stream)==1):
            print(stream)
            break
        if(stream == len(stream) * str(stream[0])):
            print(stream[0])
            break
        stream=stream[::-1]
        print(stream)