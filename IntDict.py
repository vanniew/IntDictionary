import json
from difflib import get_close_matches


def translate(word, dictionary):
    word = word.lower()
    if word in dictionary:
        return word.capitalize()+" has one of the following meanings:\n"+'\n'.join(dictionary[word])
    elif get_close_matches(word,dictionary.keys()):
        return 'Did you mean one of the following: '+' '.join(get_close_matches(word, dictionary.keys()))
    else:
        return 'I don''t know that word!'


def main():
    dictionary = json.load(open("data.json"))
    while True:
        word = input("Type a word for which you want to know the meaning : ")
        print(translate(word, dictionary))


main()