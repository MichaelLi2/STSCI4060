import random

def main():
    print "STSCI 4060 HW2"
    print "Name: Michael Li"
    print "NetID: mjl257"

    samp = []
    for i in range(59):
        samp.append(i+1)
    nums = random.sample(samp,5)
    print nums
    num1 = nums[0]
    num2 = nums[1]
    num3 = nums[2]
    num4 = nums[3]
    num5 = nums[4]
    num6 = random.randint(1,35)

    print '''\n****** Question 1 ********

This program is an immitation of the Powerball lottery game.\n'''
    r = raw_input('Play a Powerball game by pressing <Enter>. Good luck!\n')
    print ('Your Powerball game result is:\n\n ' + str(num1) + ' '+ str(num2) +
    ' '+ str(num3) + ' '+ str(num4) + ' '+ str(num5) + ' '+ str(num6) + '\n')

main()
