n = int(input())

words_and_synonyms = {}

for _ in range(n):
    word = input()
    synonym = input()

    if word not in words_and_synonyms.keys():
        words_and_synonyms[word] = []

    words_and_synonyms[word].append(synonym)

for key, value in words_and_synonyms.items():
    print(f"{key} - {', '.join(value)}")