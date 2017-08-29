def is_isogram(string):

    size = len(string)

    print size
    for i in range(size):
        for j in range(size):
            if (i!=j):
                if(string[i].lower()==string[j].lower()):
                    return False
	    print i,j

    return True

print is_isogram('eleven')
