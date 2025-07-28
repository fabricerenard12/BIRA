from label import lab

import string

def string_to_label(sentence: str) -> int:
    """
    Converts a sentence into a label based on predefined English or French values.

    Args:
        sentence (str): The input sentence to be processed and analyzed.

    Returns:
        int: The key corresponding to the recognized object, or 80 if no match is found.
    """
    sentence = sentence.strip(string.punctuation)
    words = sentence.lower().split()
    labels = []

    for word in words:
        for key, values in (lab()).items():
            if word in values:
                labels.append(key)
                print(f"Key of recognized object: {key} , {lab()[key]}")

    if len(labels) != 1:
        print("Erreur, il y a", len(labels), "objets.")
        return 80

    return labels[0]
