def tickets(people):
    cash_in_hand = 0 #Start with no cash
    for i in range(len(people)):
        print('Customer ' + str(i+1))
        print('Cash recieved: ' + str(people[i]))
        cash_in_hand = cash_in_hand + people[i] #Cash given
        print('Cash: ' + str(cash_in_hand))
        change = people[i] - 25 #Change calculated
        print('Change: ' + str(change))
        cash_in_hand = cash_in_hand - change #Change given
        print('Cash: ' + str(cash_in_hand))
        print('  ')
        if cash_in_hand < 0:
            return 'NO'
    return 'YES'

print(tickets([25, 25, 50, 50, 100]))