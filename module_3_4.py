def single_root_words (root_word='',*other_words):

    same_words = []
    word = str(root_word).lower()

    for i in range(len(other_words)):

        ltr = other_words[i].lower()

        if ltr in word :

            same_words.append(other_words[i])

        elif ltr.count(word) :

            same_words.append(other_words[i])

    return same_words

print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))
