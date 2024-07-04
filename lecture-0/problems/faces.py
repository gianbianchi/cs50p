def main():
    text = input()

    convertedText = convert(text)

    print(convertedText)


def convert(emoticon: str) -> str:
    return emoticon.replace(":)", "🙂").replace(":(", "🙁")


main()
