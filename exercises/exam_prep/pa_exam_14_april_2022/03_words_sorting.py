
def words_sorting(*key):
    word_dict = {}
    for word in key:
        sum_chars = 0
        for char in word:
            sum_chars += ord(char)
        if word not in word_dict:
            word_dict[word] = sum_chars #създаваме си value към думичката, която сме сумирали
        else:
            word_dict[word] += sum_chars #добавяме си стойностите към вече съществуващите такива

    is_odd = True if sum(word_dict.values()) % 2 != 0 else False

    if is_odd:
        sorted_words = sorted(word_dict.items(), key=lambda x: -x[1])
    else:
        sorted_words = sorted(word_dict.items(), key=lambda x: x[0])

    print_result = ''
    for k, v in sorted_words:
        print_result += f'{k} - {v}\n'

    return print_result


print(
    words_sorting(
        'cacophony',
        'accolade'
  ))

