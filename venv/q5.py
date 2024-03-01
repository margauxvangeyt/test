 # Find all occurrences of a pattern starting with "b," having an unlimited number of letters, and ending with bob
# we are defining the function
def count_bob_pattern_occurrences(text):
    """
    :param text: the text to look into
    :return: the number of matches
    """
    punctuation = ",!?.\n"
    count = 0

    # Replace each punctuation mark with nothing
    for p in punctuation:
        text = text.replace(p, "")

    # Get the words in the text
    words = text.split(" ")

    # Check each word for the specified pattern
    for word in words:
        word_lower = word.lower()
        if word_lower.startswith("b") and "bob" in word_lower:
            count += 1

    return count

# we put it to test
text = "the bamazingbob because he works for BodCorpBob for himself. He sometimes gets called beincrediblebob"
results = count_bob_pattern_occurrences(text)
print(results)


