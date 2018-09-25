def repeated_word(paragraph):
    split_words = paragraph.split()
    word_dict = {}

    for word in split_words:
        if word not in word_dict:
            word_dict[word] = 1
        elif word in word_dict:
            word_dict[word] += 1

    max = ''

    for k,v in word_dict.items():
        if not max:
           max = [k, v]
        elif v > max[1]:
            max = [k, v]

    if max[1] == 1:
        return "No repeated words"
    else:
        return max[0]
