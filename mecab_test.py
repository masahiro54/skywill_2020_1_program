#課題　丸コピペだからソースの理解が必要。不明なポイントの整理を行う必要がある。
# あとはスクレイピングした文章を取り込んでやれるかといったところ。


import MeCab
# import csv
import pandas as pd
# import numpy as np
# m = MeCab.Tagger ("-Ochasen")
text = "渋谷で働くデータサイエンティスト"

class CustomMeCabTagger(MeCab.Tagger):
    print('1')
    COLUMNS = ['word', 'Part-of-speech', 'subclassification1', 'subclassification2', 'subclassification3', 'Practical', 'Inflectional', 'Original_form', 'reading', 'pronunciation']
    print('2')
    def parseToDataFrame(self, text: str) -> pd.DataFrame:
        """テキストを parse した結果を Pandas DataFrame として返す"""
        results = []
        print('3')
        for line in self.parse(text).split('\n'):
            if line == 'EOS':
                break
            surface, feature = line.split('\t')
            
            feature = [None if f == '*' else f for f in feature.split(',')]
            results.append([surface, *feature])
        return pd.DataFrame(results, columns=type(self).COLUMNS)

tagger = CustomMeCabTagger()
tagger.parseToDataFrame(text)
print(tagger.parseToDataFrame(text))
tagger.parseToDataFrame(text).to_csv("df.csv",index = False)