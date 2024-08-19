from pprint import pprint


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for name in self.file_names:
            with open(name, 'r', encoding='utf-8') as file:
                line = file.read().lower()
                for punctuation in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    line = line.replace(punctuation, '')
                words = line.split()
                all_words[name] = words
        return all_words

    def find(self, word):
        a = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                a[name] = words.index(word.lower()) + 1
        return a

    def count(self, word):
        b = {}
        for name, words in self.get_all_words().items():
            b[name] = words.count(word.lower())
        return b


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего