def pig_latin(word: str) -> str:
    vowels = "aeiouAEIOU"
    first_letter = word[0]
    return f"{word}ay" if first_letter in vowels else word[1:] + first_letter + "ay"


if __name__ == "__main__":
    word = input("Enter the word to convert : ").lower()
    print(f"{word} -> {pig_latin(word)}")
