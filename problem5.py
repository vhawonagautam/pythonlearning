def main():
    number = input("Enter any number:")
    length = len(number)
    mid = length // 2
    

    for i in range(mid+1):
        line = number[(mid-i):(mid + i +1)]
        
        spaces = ' ' * (mid - i) 
        
        print(spaces + line)   
         
main()