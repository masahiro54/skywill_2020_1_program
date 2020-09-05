# -*- coding: utf-8 -*-
import MeCab
import csv
import chardet

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



row = u"立川駅から15分程、西国立駅からだと数分。身体に優しいアットホームな中華のお店カウンターもあり、お一人様にもやさしい。そして料理はこんな中華もあるんだ！ってくらい優しい＆奥深い味で美味。強すぎない、でも満足出来るスパイス使いに一つ一つ感動します。ランチでしか利用したことがなかったのですが今回はお店を貸し切っての宴会に呼んで貰って初の夜利用。5000円で飲み放題付き。飲み放題はビール、サワーの他紹興酒やワインもあって◎料理は普段あんまり食べれない物をリクエストしてくれたそうで....正式名称は分からないものの(ちゃんと教えてくれたのですが飲兵衛の記憶からは....)前菜～揚げチャーシュー、青菜炒め、そして魚、肉！！普段食べるエビチリ～とか酢豚～とかじゃない、初めて食べる中華がたくさん！どれも和風とは違う、でも油っぽくない、優しい味でほんとに美味しい。味わい奥深く、山椒等、随所にスパイスがしっかり効いていて◎付け合わせの人参の飾り切りが素晴らし過ぎてついつい集めてしまいました。追加で餡かけ炒飯なんかも注文してお腹いっぱい。心も満足◎◎やっぱり美味しい、そして味も雰囲気も優しい、また来たい！ゆるりさん、さすがです。,レビュアーさん絶賛の中華料理屋さんにやっと行けました(^^)店内は薄暗くカウンターとテーブルで中華と言うよりカフェみたいな雰囲気で落ち着きました。ランチのBコース980円を注文。ご飯、メイン2つ、小皿、デザート、ドリンクがそれぞれ選べて薬膳滋養スープと本日のお野菜も付きます。◆選べるご飯類はうるおいチャーハン◆メインは七色豚とチーズのミルフィーユ酢豚と完熟トマトのエビチリ◆小皿はパリパリ五目春巻き◆デザートはバニラアイスのバルサミコアップルがけどれも美味しそうで悩みました。ご飯類は3種類、メインは10種類、小皿は5種類、デザートは10種類から選べるので毎日来ても飽きなさそう(^^)10分程揚げたり炒めたりする音を聞きながら待ちました。丁寧に自分のために作ってくれている感じ悪くないです。この音も食欲をそそります～出てきたセットは色々な物を少しずつ....と女性には嬉しい感じ。がっつり食べたい男性にはちょっと物足りないかな？くらいの量です。まずは薬膳滋養スープ。身体にすっと入っていく感じで漢方みたいな味がするかと思いきやそんなことはなく、優しい味でした。お代わりしたい～♪チャーハンは油っこくなくて塩コショウも最低限、麦の食感が良く一般的な中華のチャーハンと違う味でしたが飽きがこずお茶碗一杯ペロリでした。酢豚は私には味が濃いめでしたが、ごろっとしたさつま芋と千切りドライさつま芋が上に乗っていたのが印象的。こちらも油控えめでもたれなさそう。丁寧な盛り付けだと思いました。エビチリはトマトの酸味と後からのピリ辛を楽しめる一品でした。エビは小ぶりでしたがぷりっと美味しい～後ひく美味しさでした。バニラアイスのバルサミコアップルがけは初めての味。アイスに酢という発想がなかったのでどうなの？と思いましたが甘さがさっぱりとした後味になって有りです。自分でもやってみよう～と思いました。バルサミコは別に提供されたので苦手な方はアイスのみで食べられます。最後はドリンクのマンゴージュースで一息。何から何まで揃って980円というCPの良さ！総じて油が控えめでもったりしないので毎日でも食べたくなる中華でした。また１つ１つが丁寧に作られていてよくある街の中華の大雑把に早くがっつり！と言うのと全く違う中華でした。西国立は中々来ないので理由をつけて行こうと思います(^^)ごちそうさまでした！"
# chardet.detect(row)

print(wakati_text(row))