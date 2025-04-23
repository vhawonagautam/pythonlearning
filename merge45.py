def main():
    number = input("Enter any number:")
    for i in range(4):
        print(number[(3-i):(5+i)])
    
    for i in range(5):
        print(number[(4-i):(5+i)])
           
        
main()