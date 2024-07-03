def main():
    hello()

    # Ask user for their name
    name: str = input("What's your name? ")

    # Removes whitespace from str and capitalize user's name
    name = name.strip().title()

    # Say hello to user
    hello(name)


def hello(to: str = "World") -> None:
    print(f"Hello, {to}")


main()
