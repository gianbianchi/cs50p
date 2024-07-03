def main():
    x: float = float(input("What's x? "))

    print(f"x squared is {power(x)}")


def power(n: float, s: float = 2) -> float:
    return n**s


main()
