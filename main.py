def find_word_count(string):
    return len(string.split())

def find_occurrences_of_each_character(string):
    character_occurrences = {}
    for c in string:
        char = c.lower()
        character_occurrences[char] = character_occurrences[char] + 1 if char in character_occurrences else 1
    return character_occurrences

def sort_character_occurrences(char_dict):
    result = []
    for key in char_dict:
        if key.isalpha():
            result.append({"key": key, "value": char_dict[key]})
    result.sort(reverse=True, key=lambda d: d["value"])
    return result

def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        words_in_text = find_word_count(file_contents)
        report = "--- Begin report of books/frankenstein.txt ---\n"
        report += f"{words_in_text} words found in the document\n\n"

        characters = find_occurrences_of_each_character(file_contents)
        sorted = sort_character_occurrences(characters)
        for i in sorted:
            report += f"The {i['key']} character was found {i["value"]} times\n"

        report += "--- End Report --- "
        print(report)

main()
