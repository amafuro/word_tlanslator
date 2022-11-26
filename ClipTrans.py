# 選択範囲を翻訳する。

from googletrans import Translator
import pyautogui
import pyperclip

# 元のアプリに切り替える
pyautogui.hotkey('alt', 'tab')

# 選択範囲をコピーする
pyautogui.hotkey('ctrl', 'c')

# クリップボードの5000文字を取り出す。
OrgTEXT = pyperclip.paste()[:5000]

# GoogleTransで翻訳
# 翻訳元の言語種類srcは自動判断されるようなので(信用できれば)省略可能
# 翻訳先の言語種類destはデフォルトで英語(en)なので、
# 翻訳先の言語種類を変更する場合は明示する
tr = Translator()
if OrgTEXT.isascii()==True:
  NewTEXT = tr.translate(OrgTEXT, dest="ja", src="en").text
else:
  NewTEXT = tr.translate(OrgTEXT, dest="en", src="ja").text

# 結果をクリップボードにコピー
pyperclip.copy(NewTEXT)

# 選択範囲に貼り付ける
pyautogui.hotkey('ctrl', 'v')