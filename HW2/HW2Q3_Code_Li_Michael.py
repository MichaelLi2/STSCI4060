import ast

def matrixMultiplication():
    #handling input
    inputA = raw_input('Input two matrices A and B to multiply\nInput Matrix A: ')
    inputB = raw_input('Input Matrix B: ')
    matrixA = ast.literal_eval(inputA)
    matrixB = ast.literal_eval(inputB)
    print '\nMatrix A is:'
    for a in range(len(matrixA)):
        print matrixA[a]
    print '\nMatrix B is:'
    for b in range(len(matrixB)):
        print matrixB[b]

    #for i in check for all rows?
    if len(matrixA[0]) != len(matrixB):
        return True

    #initialize matrix C
    matrixC = []
    for c in range(len(matrixA)):
        temp = []
        for d in range(len(matrixB[0])):
            temp.append(0)
        matrixC.append(temp)
    #multiplication
    for i in range(len(matrixA)):
        for j in range(len(matrixB[0])):
            for k in range(len(matrixB)):
                matrixC[i][j] = matrixC[i][j] + matrixA[i][k] * matrixB[k][j]

    print '\nMatrix C = AB is:'
    for r in range(len(matrixC)):
        print matrixC[r]

def main():
    print "STSCI 4060 HW2"
    print "Name: Michael Li"
    print "NetID: mjl257"
    print '''\n****** Question 3 ********

This program multiplies two matrices.\n'''

    failed = matrixMultiplication()
    while failed:
        print 'Error, these two matrixes cannot be multiplied since their dimensions do not match.\n'
        failed = matrixMultiplication()

main()
