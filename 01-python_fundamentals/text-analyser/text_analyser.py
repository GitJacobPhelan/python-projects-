"""A program that analyses text entered by the user."""

def text_analyser():
    """Analyse user-provided text."""
    while True:
        sentence = input("Enter your sentence: ")

        if not sentence.strip():
            print("No text provided.")
        else:
            break


    characters = len(sentence)
    print(f"Characters: {characters}")

    word_count = len(sentence.split())
    print(f"Word Count: {word_count}")

    sentence_count = sentence.count(".") + sentence.count("!") + sentence.count("?")
    print(f"Sentence Count: {sentence_count}")

    words = sentence.lower().split()
    word_frequencies = {}

    for word in words:
        if word in word_frequencies:
            word_frequencies[word] += 1
        else:
            word_frequencies[word] = 1

    most_common_word = max(word_frequencies, key=word_frequencies.get)

    print(f"Most common word: {most_common_word}")
    print(f"Occurences: {word_frequencies[most_common_word]}")



text_analyser()
