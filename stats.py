def count_words(book_text):
    num_words = len(book_text.split())
    return num_words

def count_characters(book_text: str) -> dict:
    """Counts the occurrences of each character in the given text."""
    char_count = {}
    for char in book_text.lower():  # Convert to lowercase
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

# Assuming get_book_text now looks something like this (without catching FileNotFoundError):
def get_book_text(filepath: str) -> str:
    # Reads a text file and returns its contents as a string."""
    with open(filepath) as f: # If file isn't found, FileNotFoundError happens here
        return f.read() 
    
def generate_report(char_count):
      
    report_data = [{"char": char, "num": count} for char, count in char_count.items() if char.isalpha()]
    # Sort the list by character count in descending order
    report_data.sort(key=lambda x: x['num'], reverse=True)
    return report_data
    