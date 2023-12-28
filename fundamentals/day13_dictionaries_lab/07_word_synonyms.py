pair_of_synonyms = int(input())
synonym_dict = {}

for pair in range(pair_of_synonyms):
    word = input()
    synonym = input()
    if word not in synonym_dict:
        synonym_dict[word] = [synonym]
    else:
        synonym_dict[word].append(synonym)

[(print(f"{word} - {', '.join(synonym)}")) for word, synonym in synonym_dict.items()]

