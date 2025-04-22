def main():
    number = input("Enter any number:")
    for i in range(len(number)):
        print(number[-(i+1):])
        
        
main()