#!/usr/bin/python
def reverse_words(mystr):
    length = len(mystr);
    start = 0 ;
    end = length - 1;
    str_list = list(mystr);
    while start < end:
        index_of_next_space = mystr.find(" ", start, end)
        if(index_of_next_space == -1) :
            reverse_sublist(start, end, str_list)
            break 
        else:
            reverse_sublist(start, index_of_next_space - 1, str_list)
        start = index_of_next_space + 1
        
    mystr = "".join(str_list)
    return mystr 
        
        
def reverse_sublist(begin, end, str_list):
    while (begin < end):
        tmp = str_list[begin]
        str_list[begin] = str_list[end]
        str_list[end] = tmp
        begin += 1
        end -= 1

def main():
    #Accept String
    print "Please Enter the string: "
    mystr = raw_input()
    mystr = reverse_words(mystr)
    print "Reversed Words:", mystr;


if __name__ == "__main__":
    main()

