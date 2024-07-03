def main():
    text: str = input()

    splittedText = text.split(" ")

    print(*splittedText, sep="...")


main()
