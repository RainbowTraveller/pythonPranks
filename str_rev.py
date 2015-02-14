#!/usr/bin/python

def reverse(mystr):
    #Get the length
    length = len(mystr);
    if(length > 0):
        str_list = list(mystr);
        begin = 0;
        end = length -1;
        while (begin < end):
            tmp = str_list[begin]
            str_list[begin] = str_list[end]
            str_list[end] = tmp
            begin += 1
            end -= 1
        mystr = "".join(str_list)
        print "Reversed String : ", mystr
    else:
            print "Please enter a valid string"

def main():
    #Accept String
    print "Please Enter the string: "
    mystr = raw_input()
    reverse(mystr)

if __name__ == "__main__":
    main()

