def main():
    print "STSCI 4060 HW1"
    print "Name: Michael Li"
    print "NetID: mjl257"
    print '''\n****** Question 1 ********

This program is to manipulate a string using a format string, string methods, and a tuple.

A. Define a string variable, story, to hold the content of the story including its layout.\n'''
    #Q1 part a
    story = '''Once upon a time, deep in an ancient
jungle, there lived a tiger. This tiger
liked to eat fish, but the jungle had
very little fish to offer. One day, an
explorer found the tiger and discovered
it liked fish. The explorer took the
tiger back to NYC, where it could
eat as much fish as it wanted. However,
the tiger became homesick, so the
explorer brought it back to the jungle,
leaving a large supply of fish.

-- The End of the Story --'''
    print story
    #q1 part b
    print '''\nB. Change the content of the story into a format string by replacing the
words "tiger" and "fish" with a format symbol with the replace() string method.\n'''
    story = story.replace('tiger', '%s')
    story = story.replace('fish', '%s')
    print story
    #q1 part c
    print '''\nC. Create a tuple called "t1" to hold the words of "tiger" and "fish" so
that the tuple can be used to restore the story to its original condition by using a
string format operator (%).\n'''
    t1 = ('tiger','tiger','fish','fish','tiger','fish','tiger','fish','tiger','fish')
    story = story%(t1)
    print story
    #q1 part d
    print '''\nD. Now programmatically create a different version of the story by changing
the animal and its food from "tiger" and "fish" to "monkey" and "bananas".\n'''
    story = story.replace('tiger', '%s')
    story = story.replace('fish', '%s')
    t2 = ('monkey','monkey','bananas','bananas','monkey','bananas','monkey','bananas','monkey','bananas')
    story = story%(t2)
    print story

    #question 2
    print '''\n****** Question 2 ********

This program is to manipulate a string using a format string and dictionary.

A. Using the replace() method, replace the word "monkey" with "%(animal)s", "bananas" with
"%(food)s", and NYC with "%(city)s".\n'''
    #q2 part a
    story = story.replace('monkey', '%(animal)s')
    story = story.replace('bananas', '%(food)s')
    story = story.replace('NYC', '%(city)s')
    print story
    #q2 part b
    print '''\nB. Define a dictionary, myDict, to hold the following keys and values. The
keys are animal, food, and city and the values are cat, mice and Beijing respectively.
Then, use the string format operator and apply the dictionary to the format string.\n'''
    myDict = {'animal':'cat', 'food':'mice', 'city':'Beijing'}
    print "The dictionary is:"
    print myDict
    story = story%(myDict)
    print "\n" + story
    #q2 part c
    print '''\nC. Using assignment statements ONLY, update the dictionary values with the
values of "fox", "rabbits", and "London" respectively\n'''
    story = story.replace('cat', '%(animal)s')
    story = story.replace('mice', '%(food)s')
    story = story.replace('Beijing', '%(city)s')
    myDict['animal'] = 'fox'
    myDict['food'] = 'rabbits'
    myDict['city'] = 'London'
    print "The dictionary is:"
    print myDict
    story = story%(myDict)
    print "\n" + story

    #Question 3
    print '''\n****** Question 3 ********

This program is to calculate the dot product of two vectors\n'''
    u = [[10],[-2],[3],[44]]
    v = [[20],[3],[-2],[11]]
    print "The list representation of vector u is:"
    print u
    print "The list representation of vector v is:"
    print v
    dot_product = u[0][0]*v[0][0] + u[1][0]*v[1][0] + u[2][0]*v[2][0] + u[3][0]*v[3][0]
    print "The dot product of u and v is: " + str(dot_product)


main()
