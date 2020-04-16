from Productcheck import check
def buy(product,num,price):
    if check (product,num):
        print('You bought %s and spent %s' %(product,num*price))
    else:
        print('Sorry! We are out of this product.')

        
def main():
    product=input('Product: ')
    num= int(input('Number: '))
    price=int(input('Price: '))
    buy (product,num,price)
if __name__=='__main__':
    main()
  