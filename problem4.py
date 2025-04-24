def main():
    number = input("Enter any number:")
    length = len(number)
    mid = length // 2
    

    for i in range(mid):
        line = number[(mid-i-1):(mid + i +1)]
        
        spaces = ' ' * (mid - i -1) 
        
        print(spaces + line)   
         
main()