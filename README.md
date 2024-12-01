Character & Word Frequency Analyzer

This Python project analyzes a text file, providing a detailed report of the word count and frequency of each character
in the document. Designed to work with plain text files, it offers insights into text composition and can serve as a
foundation for more advanced text analysis.

Features

	•	Word Count: Calculates the total number of words in the document.
	•	Character Frequency: Counts how often each character appears, case-insensitive.
	•	Sorted Output: Displays characters sorted by frequency in descending order.
	•	Customizable Input: Specify the path to any .txt file for analysis.
	•	Robust Error Handling: Provides clear feedback if the input file is missing or unreadable.

Installation

	1.	Clone the Repository:

git clone https://github.com/Shramkoweb/bookbot.git
cd character-word-analyzer

	2.	Ensure Python is Installed:

This script requires Python 3.6 or later. Check your version:

python3 --version

	3.	Prepare the Input File:
	•	Place the .txt file you want to analyze in the books/ directory.
	•	Update the book_path variable in the main() function if using a different directory.

Usage

	1.	Run the script:

python3 main.py

	2.	The script will:
	•	Read the text file specified in the book_path variable.
	•	Display a report of the word count and character frequencies.

Example Output

For a file frankenstein.txt:

--- Begin report of books/frankenstein.txt ---
75045 words found in the document

The 'e' character was found 57000 times
The 't' character was found 43000 times
The 'a' character was found 32000 times
...
The 'z' character was found 500 times

--- End report ---

Customization

	1.	Analyzing a Different File:

Modify the book_path variable in the main() function:

book_path = "path/to/your/textfile.txt"

	2.	Filtering Characters:

By default, the script excludes non-alphabetic characters from the report. To include all characters, remove the
isalpha() check in main():

if item['char'].isalpha():  # Remove this condition

Troubleshooting

	•	File Not Found:

Ensure the file path is correct and that the file exists. The default path is books/frankenstein.txt.
• Encoding Issues:
If your text file uses a non-UTF-8 encoding, update the get_book_text() function:

with open(path, "r", encoding="your-encoding") as f:

Contact

For issues, suggestions, or questions, feel free to reach out:
• Author: Serhii Shramko    
• Email: shramko.dev@gmail.com
• GitHub: shramkoweb

Enjoy analyzing text with ease! 🚀