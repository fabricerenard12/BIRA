from label import lab
import string

def stringtoLabel(sentence: str) -> int:
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
    
    for word in words:
        # Check if the word matches any English or French value in the dictionary
        for key, values in (lab()).items():
            if word in values:
                print(f"Key of recognized object: {key} , {lab()[key]}")
                return key
    # If no object is found, return 80
    print("Erreur, il n'y a pas d'objet.")
    return 80

