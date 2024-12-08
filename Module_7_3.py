class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                text = file.read().lower()
                for i in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    text = text.replace(i, '')
                words = text.split()
                all_words[file.name] = words
        return all_words

    def find(self, word):
        all_words = self.get_all_words()
        result_words = {}
        for file_name, words in all_words.items():
            for i, w in enumerate(words, 1):
                if w == word.lower():
                    result_words[file_name] = i
                    break
        return result_words

    def count(self, word):
        all_words = self.get_all_words()
        result_words = {}
        for file_name, words in all_words.items():
            result_words[file_name] = words.count(word.lower())
        return result_words


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего




