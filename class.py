#コード05
#データ4つとメソッド（関数）1つをカプセル化
class Tokuten_data:
    def __init__(self):
        self.name = ''
        self.kokugo = 0
        self.sansuu = 0
        self.heikin = 0.0
         
    def heikin_cal(self):
        self.heikin = (self.kokugo + self.sansuu) / 2
 
#変数taroに、データ4つとメソッド（関数）1つをカプセル化したオブジェクトを代入
taro = Tokuten_data()
taro.name = '太郎'   #nameに'太郎'を代入
taro.kokugo = 50     #kokugoに50を代入
taro.sansuu = 45     #sansuuに45を代入
taro.heikin_cal()  #メソッドheikin_cal()の実行
 
#変数hanakoに、データ4つとメソッド（関数）1つをカプセル化したオブジェクトを代入
hanako = Tokuten_data()
hanako.name = '花子'   #nameに'花子'を代入
hanako.kokugo = 90     #kokugoに90を代入
hanako.sansuu = 85     #sansuuに85を代入
hanako.heikin_cal()  #メソッドheikin_cal()の実行
 
print(taro.name, 'の平均点：', taro.heikin)
print(hanako.name, 'の平均点：', hanako.heikin)