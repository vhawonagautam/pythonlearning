def main():
    number = input("Enter any number:")
    length = len(number)
    mid = length // 2
    if length % 2 == 0: 
        for i in range(mid):
         line = number[(mid-i-1):(mid + i +1)]
        
         spaces = ' ' * (mid - i -1) 
        
         print(spaces + line)  
         
    else: 
    
      for i in range(mid+1):
         line = number[(mid-i):(mid + i +1)]
        
         spaces = ' ' * (mid - i) 
        
         print(spaces + line)  
           
        
main()