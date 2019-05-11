def main():
    print "STSCI 4060 HW2"
    print "Name: Michael Li"
    print "NetID: mjl257"
    print '''\n****** Question 4 ********

This program creates a dictionary from stock.txt and lists stocks that increased in price\n'''
    infile = file('./stock.txt','r') #using / for mac
    contents = infile.read()
    contents = contents.replace('\r','')

    #creating lists
    names = []
    dates = []
    openPrices = []
    closePrices = []

    listContents = contents.split('\n')
    for i in range(len(listContents)):
        listContents[i] = listContents[i].split('\t')
        names.append(listContents[i][0])
        dates.append(listContents[i][1])
        openPrices.append(listContents[i][2])
        closePrices.append(listContents[i][5])

    print 'The list names is:\n' + str(names) + '\n'
    print 'The list dates is:\n' + str(dates) + '\n'
    print 'The list openPrices is:\n' + str(openPrices) + '\n'
    print 'The list closePrices is:\n' + str(closePrices) + '\n'

    #creating dictionary
    stockDict = {'names':names, 'dates':dates, 'openPrices':openPrices, 'closePrices':closePrices}
    print 'Dictionary:\n' + str(stockDict)
    #creating list of stocks that increased prices
    increasedStocks = []
    for j in range(len(names)):
        if stockDict['openPrices'][j] < stockDict['closePrices'][j]:
            increasedStocks.append(stockDict['names'][j])
    stocklist = ''
    for k in increasedStocks:
        stocklist = stocklist + k + ", "
    stocklist = stocklist[0:-2] + '.\n'
    print '\nThe stocks that increased their prices are ' + stocklist

main()
