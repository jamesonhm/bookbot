def main():
    path = "books/frankenstein.txt"
    text = get_text(path)
    print(word_count(text))
    print(letter_count(text))
    print_report(path)

def get_text(path):
    with open(path) as f:
        return f.read()

def word_count(text):
    return len(text.split())

def letter_count(text):
    letter_counts = {}
    for c in text:
        c = c.lower()
        if c in letter_counts:
            letter_counts[c] += 1
        else:
            letter_counts[c] = 1
    return letter_counts

def print_report(path):
    print(f"*** Begin Report of {path} ***")
    text = get_text(path)
    print(f"{word_count(text)} words found in the book")
    print()
    counts = letter_count(text)
    chars = list(counts.keys())
    chars.sort()
    for c in chars:
        if c.isalpha():
            print(f"The '{c}' char was found {counts[c]} times")
    return None

main()

