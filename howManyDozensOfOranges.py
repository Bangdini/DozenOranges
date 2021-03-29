#priceOranges = 0.38 #price is calculated by average grams of oranges to the average price per pound
#print('How many dozens of oranges were purchased?')
#dozens = int(input())
#Total = print((priceOranges*12*dozens))
fruitStatsCredits = '\n \nPrices are calculated from the price to pound from statista.com \nand the average weight of oranges from reference.com \n Program by @Bangdini everywhere'
def orangeDozens():
    priceOranges = 0.38
    print('How many dozens of oranges were purchased?')
    dozens = int(input())
    Total = (round(+priceOranges*12*dozens,2))
    print('You would spend $'+str(Total)+' for '+str(dozens)+' dozen oranges')
    print(fruitStatsCredits)
orangeDozens()
