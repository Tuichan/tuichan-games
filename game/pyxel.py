import pyxel

pyxel.init(128, 128)

# ビットマップフォントの読み込み
font = pyxel.Font("umplus_j10r.bdf")

# フォントを指定してテキスト表示
pyxel.text(10,10,"日本語の表示",7,font)

pyxel.show()
