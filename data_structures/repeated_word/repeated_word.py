def repeated_word(paragraph):
    split_words = paragraph.split()
    word_dict = {}

    for word in split_words:
        if word not in word_dict:
            word_dict[word] = 1
        elif word in word_dict:
            word_dict[word] += 1

    maximum = ''

    for k,v in word_dict.items():
        if not maximum:
           maximum = [k, v]
        elif v > maximum[1]:
            maximum = [k, v]

    if maximum[1] == 1:
        return "No repeated words"
    else:
        return maximum[0]
