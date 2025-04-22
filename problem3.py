def main():
    number = input("Enter any number:")
    for i in range(len(number)):
        print(number[-(i+1):])
        
        
    for i in range(1,len(number)):
        print(number[i:])
        
        
        
main()