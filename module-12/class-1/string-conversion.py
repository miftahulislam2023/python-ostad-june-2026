"""
PYTHON TYPE CONVERSIONS
String <-> List, Tuple, Set, Dictionary (And Vice Versa)
"""

import json
import ast
from collections import Counter

# 1. STRING <-> LIST CONVERSION

# 1. Character-by-character conversion using list()
text = "Python"
char_list = list(text)
print(f"Original String: '{text}'")
print(f"1. list(text) -> {char_list}")

# 2. Split by whitespace (default) using .split()
sentence = "Learning Python is fun and easy"
word_list = sentence.split()
print(f"\nOriginal String: '{sentence}'")
print(f"2. sentence.split() -> {word_list}")

# 3. Split by specific delimiter (comma, dash, etc.)
csv_data = "apple,banana,cherry,date"
fruit_list = csv_data.split(",")
print(f"\nOriginal String: '{csv_data}'")
print(f"3. csv_data.split(',') -> {fruit_list}")

# 1. Join list of strings with empty separator
letters = ['P', 'y', 't', 'h', 'o', 'n']
combined_word = "".join(letters)
print(f"Original List: {letters}")
print(f"1. ''.join(letters) -> '{combined_word}'")

# 2. Join list of words with space separator
words = ["Python", "is", "awesome"]
joined_sentence = " ".join(words)
print(f"\nOriginal List: {words}")
print(f"2. ' '.join(words) -> '{joined_sentence}'")

# 3. Join with custom delimiter (comma, hyphen, newline, etc.)
items = ["HTML", "CSS", "JavaScript", "Python"]
comma_separated = ", ".join(items)
print(f"\nOriginal List: {items}")
print(f"3. ', '.join(items) -> '{comma_separated}'")

# 2. STRING <-> TUPLE CONVERSION

# 1. Character-by-character conversion using tuple()
word = "Code"
char_tuple = tuple(word)
print(f"Original String: '{word}'")
print(f"1. tuple(word) -> {char_tuple}")

# 2. Delimited string to tuple using .split() + tuple()
point_str = "10,20,30"
coordinates = tuple(map(int, point_str.split(",")))
print(f"\nOriginal String: '{point_str}'")
print(f"2. tuple(map(int, point_str.split(','))) -> {coordinates}")

# 3. Tuple from words
quote = "Stay hungry stay foolish"
words_tuple = tuple(quote.split())
print(f"\nOriginal String: '{quote}'")
print(f"3. tuple(quote.split()) -> {words_tuple}")

# 1. Join string tuple elements
rgb_names = ("Red", "Green", "Blue")
rgb_str = " -> ".join(rgb_names)
print(f"Original Tuple: {rgb_names}")
print(f"1. ' -> '.join(rgb_names) -> '{rgb_str}'")

# 3. STRING <-> SET CONVERSION

# 1. Unique characters using set()
# Note: Sets are unordered and store unique elements only
sample = "mississippi"
unique_chars = set(sample)
print(f"Original String: '{sample}'")
print(f"1. set(sample) -> {unique_chars} (Duplicates removed, unordered)")

# 2. Unique words from a string
paragraph = "apple orange banana apple banana grapes orange"
unique_words = set(paragraph.split())
print(f"\nOriginal String: '{paragraph}'")
print(f"2. set(paragraph.split()) -> {unique_words}")

# 1. Join set elements
tags = {"python", "django", "backend", "api"}
tags_string = ", ".join(tags)
print(f"Original Set: {tags}")
print(f"1. ', '.join(tags) -> '{tags_string}' (Order may vary)")