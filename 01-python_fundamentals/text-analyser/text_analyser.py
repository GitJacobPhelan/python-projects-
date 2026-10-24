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

    sentence_count = sentence.count(".") + sentence.count("!") + sentence.count("?")
    print(f"Sentence Count: {sentence_count}")

    words = sentence.lower().split()
    word_frequencies = {}

    for word in words:
        clean_word = word.strip(".,!?;:\"'()[]{}")
        if clean_word == '':
            continue
        if clean_word in word_frequencies:
            word_frequencies[clean_word] += 1
        else:
            word_frequencies[clean_word] = 1

    most_common_word = max(word_frequencies, key=word_frequencies.get)
    print(f"Most common word: {most_common_word}")

    top_five_words = sorted (
        word_frequencies.items(),
        key=lambda item: item[1],
        reverse=True
    ) [:5]

    print("Top five most common words:")

    for word, frequency in top_five_words:
        print(f"{word}: {frequency}")

    word_count = sum(word_frequencies.values())
    print(f"Word Count: {word_count}")

    print(f"Occurences: {word_frequencies[most_common_word]}")



text_analyser()
