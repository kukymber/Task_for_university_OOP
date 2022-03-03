class main:
    def __init__(self, some_string):
        self.some_string = some_string

    def PrintResult(self):
        return print(self.some_string)


class FindMidElement(main):
    def __init__(self, some_string):
        super().__init__(some_string)

    def find(self):
        string_length = len(self.some_string)
        mid_elem = self.some_string[len(self.some_string) // 2]
        index_right_word = self.some_string[string_length // 2 + 1::].index(' ')  # слово справа от центр. элемента
        index_left_word = self.some_string[string_length // 2 - 1:: -1].index(' ')  # слово слева от центр. элемента
        index_end_word = self.some_string[string_length // 2::].index(' ')  # правая часть от центр. элемента
        index_start_word = self.some_string[string_length // 2::-1].index(' ') - 1  # левая часть от центр. элемента
        if len(self.some_string.split(' ')) == 2 or len(self.some_string.split(' ')) == 1:  # Если слов меньшеравно двух
            print(self.some_string)
        elif len(self.some_string.split(' ')) > 2 and mid_elem != ' ':  # центр. элемент символ
            print(f"Если центральный элемент строки находится посередине слова "
                  f"{self.some_string[string_length // 2 - index_start_word:string_length // 2]}{mid_elem}"
                  f"{self.some_string[string_length // 2 + 1:string_length // 2 + index_end_word]}")
        elif mid_elem == ' ':  # центр. элемент пробел
            input_right_word = self.some_string[string_length // 2:string_length // 2 + index_right_word + 1]
            input_left_word = self.some_string[string_length // 2 - index_left_word:string_length // 2:]
            print(f'Если центральный элемент пробел, то два слова по краям {input_left_word}{input_right_word}')


print_result_form_parents = FindMidElement('карл у клары украл кораллы')
print_result_form_parents.find()
print_result_form_parents.PrintResult()
