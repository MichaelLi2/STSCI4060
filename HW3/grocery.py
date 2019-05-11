import time

class Grocery:
    #part a, init makes an empty dictionary
    def __init__(self):
        self.dic = {}
    #part b, updates and adds to the dictinary
    def buildInventory(self, diction):
        for key in diction.keys():
            self.dic[key] = diction[key]
    #part c, prints the inventory
    def viewInventory(self):
        if self.dic == {}:
            print 'The inventory is empty. Put an order ASAP.\n'
        else:
            print str(self.dic) + '\n'
    #part d, provides an interactive interface for the customers to buy things
    def checkOut(self):
        cart = {} #key: names, value:list of quantity, price, and Subtotal
        invoice = '\n'
        inputYN = raw_input('Do you want to buy something? ')
        if inputYN == 'Yes' or inputYN == 'yes' or inputYN == 'Y' or inputYN == 'y':
            invoice = invoice + 'Item\t\tQuantity\tPrice\tSubtotal\n-------------------------------------\n'
        while inputYN == 'Yes' or inputYN == 'yes' or inputYN == 'Y' or inputYN == 'y':
            input_item = raw_input('Enter an item to buy: ')
            if not input_item in self.dic or self.dic[input_item][0] == 0:
                print 'Wrong item name or out of stock.'
                inputYN = raw_input('Do you still want to buy something? ')
            else:
                input_num = input('How many do you want? ')
                if input_num > self.dic[input_item][0]:
                    print 'Not enough in stock; we can only sell you ' + str(self.dic[input_item][0]) + ' item(s).'
                else:
                    self.dic[input_item][0] = self.dic[input_item][0] - input_num
                    if not input_item in cart:
                        #Quanitiy, price, and subtotal
                        cart[input_item] = [input_num, self.dic[input_item][1], input_num * self.dic[input_item][1]]
                    else:
                        cart[input_item][0] = cart[input_item][0] + input_num #Quantity
                        cart[input_item][2] = cart[input_item][2] + input_num * cart[input_item][1] #Subtotal
                inputYN = raw_input('Do you still want to buy something? ')
        #find total and print invoice
        if cart != {}:
            total = 0
            for k in cart.keys():
                invoice = invoice + k  + '\t\t' + str(cart[k][0]) + '\t\t' + str(cart[k][1]) + '\t' + str(cart[k][2]) + '\n'
                total = total + cart[k][2]
            invoice = invoice + '-------------------------------------\nPlease pay $' + str(total) + '\n\n'

        print invoice + 'Goodbye.\t' + time.ctime() + '\n'
