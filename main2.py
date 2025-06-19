def get_book_text(filepath: str) -> str:
    """Reads a text file and returns its contents as a string."""
    # ... rest of your function ...
    
    try:
        with open(filepath) as f:
            file_contents = f.read()
            # Do something with file_contents
    except FileNotFoundError:
            print(f"Alas, the file was not found at {filepath}!")
    except Exception as e: # Catch other potential errors
            print(f"An error occurred: {e}")

def main():
    filepath = './books/frankenstein.txt'
    book_text = get_book_text(filepath)
    print(book_text)

if __name__ == "__main__":
    main()


    ### bessere Version 
"""    
def main():
    filepath = './books/frankenstein.txt'
        try:
        book_text = get_book_text(filepath)
        print(book_text)
    except FileNotFoundError:
        print(f"Alas, the book at {filepath} could not be found!")
    # You could add other except blocks here for other potential errors

# Assuming get_book_text now looks something like this (without catching FileNotFoundError):
def get_book_text(filepath: str) -> str:
    """Reads a text file and returns its contents as a string."""
    with open(filepath) as f: # If file isn't found, FileNotFoundError happens here
        return f.read() 
        
if __name__ == "__main__":
    main()
        
        """