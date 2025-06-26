import json
import string
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

class StemPhraseProcessor:
    def __init__(self, pg_mgr, language='english', databaseType='postgres'):
        self.pg = pg_mgr
        self.language = language
        self.databaseType = databaseType
        self.stemmer = PorterStemmer()
        self.stopwords = set(stopwords.words(language))


    def clean_and_stem(self, text):
        text_clean = text.translate(str.maketrans('', '', string.punctuation))
        words = word_tokenize(text_clean)
        stems = [self.stemmer.stem(w.lower()) for w in words if w.isalpha()]
        return stems

    def trim_omit_words(self, stems):
        left = 0
        right = len(stems)

        while left < right and stems[left] in self.stopwords:
            left += 1
        while right > left and stems[right - 1] in self.stopwords:
            right -= 1

        return stems[left:right]

    def get_or_create_stem_ids(self, stems):
        stem_id_map = {}
        for stem in stems:
            self.pg.update_or_insert('stems', {'stem': stem}, {'stem': stem})
            res = self.pg.read('stems', {'stem': stem})
            if res:
                stem_id_map[stem] = res[0]['id']
        return stem_id_map

    # def save(self, text):
    #     original_stems = self.clean_and_stem(text)
    #     if not original_stems:
    #         return []

    #     trimmed_stems = self.trim_omit_words(original_stems)
    #     if not trimmed_stems:
    #         return []

    #     stem_id_map = self.get_or_create_stem_ids(trimmed_stems)
    #     stem_ids = [stem_id_map[s] for s in trimmed_stems if s in stem_id_map]
    #     if not stem_ids:
    #         return []

    #     # Step 1: Save bigrams
    #     for i in range(len(trimmed_stems) - 1):
    #         id1, id2 = stem_id_map[trimmed_stems[i]], stem_id_map[trimmed_stems[i + 1]]
    #         self.pg.update_or_insert(
    #             'stem_bigrams',
    #             {'id1': id1, 'id2': id2},
    #             {'id1': id1, 'id2': id2}
    #         )

    #     phrase_text = ' '.join(trimmed_stems)
    #     phrase_data = []

    #     res = self.pg.read('phrases', {'stem_ids': stem_ids})
    #     if res:
    #         phrase_id = res[0]['id']
    #         self.pg.sql('UPDATE phrases SET frequency = frequency + 1 WHERE id = %s', (phrase_id,))
    #         phrase_data.append({'id': phrase_id, 'phrase_text': phrase_text})
    #     else:
    #         insert_sql = '''
    #             INSERT INTO phrases (stem_ids, phrase_text, frequency)
    #             VALUES (%s, %s, 1)
    #             RETURNING id
    #         '''
    #         self.pg.cursor.execute(insert_sql, (stem_ids, phrase_text))
    #         phrase_id = self.pg.cursor.fetchone()['id']
    #         phrase_data.append({'id': phrase_id, 'phrase_text': phrase_text})

    #         # Step 2: Save phrase_stems
    #         for pos, sid in enumerate(stem_ids):
    #             self.pg.update_or_insert(
    #                 'phrase_stems',
    #                 {'phrase_id': phrase_id, 'position': pos},
    #                 {'phrase_id': phrase_id, 'position': pos, 'stem_id': sid}
    #             )

    #     return phrase_data



    def save(self, text):
        original_stems = self.clean_and_stem(text)
        if not original_stems:
            return []

        trimmed_stems = self.trim_omit_words(original_stems)
        if not trimmed_stems:
            return []

        stem_id_map = self.get_or_create_stem_ids(trimmed_stems)
        stem_ids = [stem_id_map[s] for s in trimmed_stems if s in stem_id_map]
        if not stem_ids:
            return []

        # Step 1: Save bigrams
        for i in range(len(trimmed_stems) - 1):
            id1, id2 = stem_id_map[trimmed_stems[i]], stem_id_map[trimmed_stems[i + 1]]
            self.pg.update_or_insert(
                'stem_bigrams',
                {'id1': id1, 'id2': id2},
                {'id1': id1, 'id2': id2}
            )

        phrase_text = ' '.join(trimmed_stems)
        phrase_data = []

        res = self.pg.read('phrases', {'stem_ids': stem_ids})
        if res:
            phrase_id = res[0]['id']

            if self.databaseType == 'postgres':
                self.pg.sql('UPDATE phrases SET frequency = frequency + 1 WHERE id = %s', (phrase_id,))
            else:
                self.pg.sql('UPDATE phrases SET frequency = frequency + 1 WHERE id = ?', (phrase_id,))

            phrase_data.append({'id': phrase_id, 'phrase_text': phrase_text})
        else:
            if self.databaseType == 'postgres':
                insert_sql = '''
                    INSERT INTO phrases (stem_ids, phrase_text, frequency)
                    VALUES (%s, %s, 1)
                    RETURNING id
                '''
                self.pg.cursor.execute(insert_sql, (stem_ids, phrase_text))
                phrase_id = self.pg.cursor.fetchone()['id']
            else:
                insert_sql = '''
                    INSERT INTO phrases (stem_ids, phrase_text, frequency)
                    VALUES (?, ?, 1)
                '''
                self.pg.cursor.execute(insert_sql, (json.dumps(stem_ids), phrase_text))
                phrase_id = self.pg.cursor.lastrowid

            phrase_data.append({'id': phrase_id, 'phrase_text': phrase_text})

            # Step 2: Save phrase_stems
            for pos, sid in enumerate(stem_ids):
                self.pg.update_or_insert(
                    'phrase_stems',
                    {'phrase_id': phrase_id, 'position': pos},
                    {'phrase_id': phrase_id, 'position': pos, 'stem_id': sid}
                )

        return phrase_data
