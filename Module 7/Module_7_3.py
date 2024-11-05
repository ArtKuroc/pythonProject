class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = file_names

    def del_sign(self, str_f):
        sign = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for x in sign:
            str_f = str_f.replace(x, '')
        return str_f

    def get_all_words(self):
        all_words = {}
        for name in self.file_names:
            with open(name, 'r', encoding='utf-8') as file:
                str_f = file.read().lower()
                str_rezult = self.del_sign(str_f)
                sub_words = str_rezult.split()
                all_words[name] = sub_words
        return all_words

    def find(self, word):
        find_word = {}
        word = word.lower()
        all_words = self.get_all_words()
        for name, sub_words in all_words.items():
            if word in sub_words:
                index = sub_words.index(word) + 1
                find_word[name] = index
        return find_word

    def count(self, word):
        count_word = {}
        word = word.lower()
        all_words = self.get_all_words()
        for name, sub_words in all_words.items():
            count = sub_words.count(word)
            if count > 0:
                count_word[name] = count
            else:
                print('Искомого слова в словаре нет!')
                return ''
        return count_word

finder2 = WordsFinder('test_files.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего