from stats import get_book_text, count_words, count_characters, generate_report # Import the necessary functions
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    
    try:
        book_text = get_book_text(filepath)  # Get the text from the book
        word_count = count_words(book_text)  # Count the words in the text
        char_count = count_characters(book_text)
        report_data = generate_report(char_count)
       # Print the report
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {filepath}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")

        # Iterate through the sorted list and print character counts
        for entry in report_data:
            print(f"{entry['char']}: {entry['num']}")

        print("============= END ===============")

    except FileNotFoundError:
        print(f"Alas, the book at {filepath} could not be found!")
    # You could add other except blocks here for other potential errors
 
if __name__ == "__main__":
    main()
