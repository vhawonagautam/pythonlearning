def main():
    name = input("Enter a word :")
    for i in range(len(name)):
        print(name[:i+1])

main()
