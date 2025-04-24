def main():
    number = int(input("Enter a number: "))
    i = 1
    num = 1


    while num < number:
        for j in range(i):
            if num > number:
                break
            print(num, end=' ')
            num += 1
        print()
        i += 1

main()
