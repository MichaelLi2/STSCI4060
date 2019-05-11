def main():
    print "STSCI 4060 HW2"
    print "Name: Michael Li"
    print "NetID: mjl257"
    print '''\n****** Question 2 ********

This program finds the number of lines, words, characters, and paragraphs in AboutCornell.txt.\n'''
    infile = file('./AboutCornell.txt','r') #using / for mac
    contents = infile.read()
    #print repr(contents)
    
    numlines = 1
    numwords = 1
    numchars = 0
    numpar = 1
    i = 0
    while i<len(contents):
        if contents[i] == '\r':
            None
        elif contents[i] == '\n':
            numlines += 1
            if contents[i+2] != '\n':
                numwords += 1
            else:
                numpar += 1
        elif contents[i] == ' ':
            if contents[i+2] != '\n':
                numwords += 1
        else:
            numchars += 1
        i+=1
    print ('In the article there are ' + str(numlines) + ' lines, ' + str(numwords)
    + ' words, ' + str(numchars) + ' characters\n(excluding whitespaces), and ' +
    str(numpar) + ' paragraphs.\n')


main()
