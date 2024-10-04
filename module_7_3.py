class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = [*file_names]

    def get_all_words(self):
        all_words = {}
        except_symbols = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                f = file.read().lower().split()
                words = []
                for word in f:
                    for symbol in except_symbols:
                        word = word.replace(symbol, "")
                    words.append(word.replace(symbol, ''))
            all_words[file_name] = words
        return all_words

    def find(self, word):
        find_word = {}

        for file_name, file_word in self.get_all_words().items():
            num_word = 0
            for w in file_word:
                num_word += 1
                if w == word.lower():
                    find_word[file_name] = num_word
                    break
        return find_word

    def count(self, word):
        find_word = {}
        for file_name, file_word in self.get_all_words().items():
            count_word = 0
            for w in file_word:
                if w == word.lower():
                    count_word += 1
            find_word[file_name] = count_word
        return find_word


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
# print()
# print('Дополнительные материалы:')
# finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
#                       'Rudyard Kipling - If.txt',
#                       'Mother Goose - Monday’s Child.txt')
# print(finder1.get_all_words())
# print(finder1.find('the'))
# print(finder1.count('the'))
