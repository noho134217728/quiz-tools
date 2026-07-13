# 無機化学小テスト：各論編

印刷して使うことを前提にした、無機化学の各論編向け小テスト生成器です。

問題文から化学反応式を書き、元素・物質の所属を記号で回答します。
所属記号は複数回答できます。

## ファイル構成

```text
inorganic-kakuron-quiz/
  index.html
  reactions.csv
  reactions.json
  csv_to_json.py
  README.md
```

## 起動方法

```bash
cd inorganic-kakuron-quiz
python csv_to_json.py
python -m http.server 8000
```

ブラウザで次を開きます。

```text
http://localhost:8000
```

`index.html` をブラウザで直接開いた場合、ブラウザの制限で `reactions.json` を自動読み込みできないことがあります。その場合は画面上の「データ読み込み」から `reactions.csv` または `reactions.json` を選択してください。

## 所属記号群

```text
(ア) アルカリ金属元素
(イ) 2族元素
(ウ) 両性元素
(エ) 遷移元素
(オ) 14族元素
(カ) 15族元素
(キ) 16族元素
(ク) 17族元素
```

## CSV形式

`reactions.csv` は次の形式です。

```csv
id,unit,chapter,statement,equation,affiliations,note,level
001,第1章,アルカリ金属元素,ナトリウムを水に入れる。,2Na + 2H_2O -> 2NaOH + H_2↑,ア,ナトリウムはアルカリ金属元素。,1
```

### 各列の意味

| 列名 | 内容 |
|---|---|
| `id` | 問題ID |
| `unit` | 大分類 |
| `chapter` | 単元名 |
| `statement` | 問題文 |
| `equation` | 模範解答の化学反応式 |
| `affiliations` | 所属記号。複数の場合は `ア;イ` のようにセミコロン区切り |
| `note` | 解答欄の備考 |
| `level` | 難易度。任意 |

## 化学式の書き方

下付き数字は `_` を使って書けます。

```text
H_2O
SO_4^2-
CaCO_3
```

沈殿と気体発生は次のように書けます。

```text
AgCl↓
CO_2↑
```

画面表示では MathJax + mhchem により、化学式として組版されます。

## 問題を増やす手順

1. `reactions.csv` に行を追加する。
2. ターミナルで次を実行する。

```bash
python csv_to_json.py
```

3. ブラウザを再読み込みする。

## 印刷

画面上の「印刷」ボタンからPDF化できます。
問題用紙と解答用紙はページ分けされます。
