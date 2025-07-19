from label import lab, validLabel

import string

def string_to_label(sentence: str) -> int:
    """
    Converts a sentence into a label based on predefined English or French values.

    This function processes the input sentence by stripping punctuation, converting it to lowercase,
    and splitting it into words. It then checks each word against a predefined dictionary (obtained
    from the `lab` function) to find a matching English or French value. If a match is found, it returns
    the corresponding key from the dictionary. If no match is found, it returns 80.

    Args:
        sentence (str): The input sentence to be processed and analyzed.

    Returns:
        int: The key corresponding to the recognized object, or 80 if no match is found.
    """
    sentence = sentence.strip(string.punctuation)
    words = sentence.lower().split()  # Convert sentence to lowercase and split into words
    labels = []
    for word in words:
        # Check if the word matches any English or French value in the dictionary
        for key, values in (lab()).items():
            if word in values:
                if key in validLabel(True):
                    labels.append(key)
                    print(f"Key of recognized object: {key} , {lab()[key]}")

                

    if len(labels) > 1 or len(labels) == 0:  # Utilise len() pour obtenir la longueur de la liste
        print("Erreur, il y a", len(labels), "objets.")
        return 80


    # If no object is found, return 80
    return labels[0]

