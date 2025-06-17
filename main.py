from stats import get_book_text, count_words, count_characters  # Import the necessary functions

def main():
    filepath = './books/frankenstein.txt'
    try:
        book_text = get_book_text(filepath)  # Get the text from the book
        word_count = count_words(book_text)  # Count the words in the text
        print(f"{word_count} words found in the document")  # Print the word count
        
        char_count = count_characters(book_text)  # Count the characters in the text
        print(char_count)  # Print the dictionary of character counts

    except FileNotFoundError:
        print(f"Alas, the book at {filepath} could not be found!")
    # You could add other except blocks here for other potential errors
 
if __name__ == "__main__":
    main()
