import MeCab
import csv

# 取り出したい品詞
select_conditions = ['動詞', '形容詞', '名詞']

# 分かち書きオブジェクト
tagger = MeCab.Tagger('')

# Neologdの指定版 最新語に対応する
# tagger = MeCab.Tagger('-d /usr/lib64/mecab/dic/mecab-ipadic-neologd')

tagger.parse('')


def wakati_text(row):
    """
    文書textを分かち書きして、半角スペース区切りの単語文字列に変換する

    Parameters
    ----------
    text: str
        文書

    Returns
    -------
    text_result: str
        分かち書きされた文書

    """

    # 分けてノードごとにする
    node = tagger.parseToNode(row)
    #空の配列を作る
    terms = []

    while node:

        # 単語
        term = node.surface

        # 品詞
        pos = node.feature.split(',')[0]

        # もし品詞が条件と一致してたら
        if pos in select_conditions:
            terms.append(term)

        node = node.next

    # 連結おじさん
    text_result = terms
    return text_result


# text = "私はプログラミングが苦手です"


cnt = 0
box = []
# print(cnt)
with open('wktgaki.csv', 'w',encoding="utf-8_sig",newline='') as x:
  writer = csv.writer(x,lineterminator='\n')
  with open('C:\\Users\owner\\Desktop\\skywill_2020_1_program\\review_marge_after\\review_all.csv',encoding="utf-8_sig") as f:
      reader = csv.reader(f)
      for row in reader:
          cnt =+1
          # print(row)
          # print(' '.join(row))
          row_2 = ' '.join(row)
          # print(row.replace("　"," "))
          # print(wakati_text(row_2))
        #   box.append(wakati_text(row_2))

          writer.writerow(wakati_text(row_2))
f.close
x.close

# print(box)