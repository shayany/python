def space_maker(numberOfspace):
    """
    This function return a line that contain n spaces
    :param numberOfspace:
    :return temp:
    """
    temp=""
    for i in range(numberOfspace):
        temp+=" "
    return temp


def display_triangle(array,column):
    """
            This function display an 2D array in triangular shape
    :param array:
    :param column:
    :return:
    """
    space=column+1
    for row in array:
        if (len(row)==1):
            line = ""
            print(space_maker(space)+"^")
            space-=1
            line += "/"
            line += row[0]
            line += "\\"
            print(space_maker(space)+line)
            space-=1
            print(space_maker(space)+"*---*")
            space-=1
        else:
            j=0
            line = ""
            underline=""
            while(j<len(row)):
                if (j % 2 == 0):
                    line+="/"
                    line+=row[j]
                    line+="\\"
                    underline+="*---"
                else:
                    line+=row[j]
                j+=1
            underline+="*"
            print(space_maker(space)+line)
            space-=1
            print(space_maker(space)+underline)
            space-=1


def transition(bits):
    """
        This function apply the transition on input
    :param bits:
    """
    if (bits == "0000"):
        return "0000"
    elif (bits == "0001"):
        return "1000"
    elif (bits == "0010"):
        return "0001"
    elif (bits == "0011"):
        return "0010"
    elif (bits == "0100"):
        return "0000"
    elif (bits == "0101"):
        return "0010"
    elif (bits == "0110"):
        return "1011"
    elif (bits == "0111"):
        return "1011"
    elif (bits == "1000"):
        return "0100"
    elif (bits == "1001"):
        return "0101"
    elif (bits == "1010"):
        return "0111"
    elif (bits == "1011"):
        return "1111"
    elif (bits == "1100"):
        return "1101"
    elif (bits == "1101"):
        return "1110"
    elif (bits == "1110"):
        return "0111"
    elif (bits == "1111"):
        return "1111"


def row_column(length):
    """
    Compute how many rows and columns needed for keeping the solution in 2D array
    :param length:
    :return:
    """
    counter=0
    row=0
    column=1

    if (length == 1):
        return 1,1

    while(counter < length):
        for i in range(column):
            counter+=1
        row+=1
        column+=2
    return row,column-2


def oneD_to_twoD(stream,row):
    """
    Convert string of data into 2D array
    :param stream:
    :param row:
    :return:
    """
    counter=0
    column=1
    array=[]
    for i in range(row):
        temp=[]
        for i in range(column):
            temp.append(stream[counter])
            counter+=1
        array.append(temp)
        column+=2
    return array


def reduce(array,row):
    """
    Apply reduction
    :param array:
    :param row:
    :return:
    """
    column = 0
    i = 0
    groupC = 0
    reduce_array=[]
    while (i < row):
        l=[]
        for j in range(column+1):
            if(j % 4 == 0):
                l.append(array[i][j])
            else:
                groupC += 1
                if (groupC == 3):
                    groupC=0
                    l.append(array[i][j])
        i += 2
        column+=4
        reduce_array.append(l)
    return reduce_array


def print_array(array):
    """
    Printing an 2D array as a string
    :param array:
    :return:
    """
    stream=""
    for i in array:
        for j in i:
            stream+=str(j)
    print(stream[::-1])


def convert_array(array,row,totalItem):
    """
    Apply the transition rules on 2D array
    :param array:
    :param row:
    :return:
    """
    segments=0
    column = 0
    i = 0
    groupC = 0
    while (i < row):
        l=[]
        for j in range(column+1):
            if(j % 4 == 0):
                bits = []
                bits.append(array[i][j])
                for t in range(3):
                    bits.append(array[i + 1][j + t])
                bits = bits[::-1]
                bits = list(transition("".join(bits)))

                if (bits == ['0', '0', '0', '0'] or bits == ['1', '1', '1', '1']):
                    segments+=1
                else:
                    segments=0

                counter = 3
                array[i][j] = bits[counter]
                for t in range(3):
                    counter -= 1
                    array[i + 1][j + t] = bits[counter]
            else:
                groupC += 1
                if (groupC == 3):
                    groupC=0
                    bits = []
                    bits.append(array[i + 1][j])
                    for t in range(j - 2, j + 1):
                        bits.append(array[i][t])
                    bits = bits[::-1]
                    bits = list(transition("".join(bits)))
                    if (bits == ['0', '0', '0', '0'] or bits == ['1', '1', '1', '1']):
                        segments += 1
                    else:
                        segments = 0

                    counter = 3
                    array[i + 1][j] = bits[counter]
                    for t in range(j - 2, j + 1):
                        counter -= 1
                        array[i][t] = bits[counter]
        i += 2
        column+=4
    #print("Total:{} Segments:{}".format(totalItem,segments))
    if totalItem==segments:
        return array,1
    else:
        return array,0

