"""A program that analyses text entered by the user."""

def text_analyser():
    """Analyse user-provided text."""
    sentence = input("Enter your sentence: ")

    characters = len(sentence)
    print(f"Characters: {characters}")

    word_count = len(sentence.split())
    print(f"Word Count: {word_count}")

    sentence_count = sentence.count(".") + sentence.count("!") + sentence.count("?")
    print(f"Sentence Count: {sentence_count}")

text_analyser()
