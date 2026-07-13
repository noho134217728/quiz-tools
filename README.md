# 無機化学 小テスト生成器

無機化学の小テストを、印刷用に生成するためのツールです。

## 小テストへのリンク

- [トップページ](https://<GitHubユーザー名>.github.io/<リポジトリ名>/)
- [無機化学 化学反応式小テスト](https://<GitHubユーザー名>.github.io/<リポジトリ名>/chem-quiz/)
- [無機化学小テスト：各論編](https://<GitHubユーザー名>.github.io/<リポジトリ名>/inorganic-kakuron-quiz/)

---

## 概要

このリポジトリには、以下の2種類の小テスト生成器が入っています。

```text
chem-quiz/
  無機化学 化学反応式小テスト

inorganic-kakuron-quiz/
  無機化学小テスト：各論編
```

どちらも基本的な使い方は同じです。

1. GitHub上で `reactions.csv` を編集する
2. 保存すると GitHub Actions が自動で `reactions.json` を生成する
3. GitHub Pages 上の小テストに反映される
4. ブラウザで小テストを生成し、印刷またはPDF化する

---

## フォルダ構成

```text
.
├─ index.html
├─ chem-quiz/
│  ├─ index.html
│  ├─ reactions.csv
│  ├─ reactions.json
│  ├─ csv_to_json.py
│  └─ README.md
├─ inorganic-kakuron-quiz/
│  ├─ index.html
│  ├─ reactions.csv
│  ├─ reactions.json
│  ├─ csv_to_json.py
│  └─ README.md
└─ .github/
   └─ workflows/
      └─ deploy-pages.yml
```

---

## 2つの小テストの違い

### 1. 無機化学 化学反応式小テスト

フォルダ：

```text
chem-quiz/
```

問題文を見て、以下を回答する形式です。

- 化学反応式
- 反応の分類記号

分類記号は以下です。

```text
(ア) 酸塩基反応：酸化物と水の反応
(イ) 酸塩基反応：中和反応
(ウ) 酸塩基反応：遊離反応
(エ) 酸化還元反応
(オ) 熱分解反応
(カ) 沈殿生成反応
(キ) 錯体生成反応
```

---

### 2. 無機化学小テスト：各論編

フォルダ：

```text
inorganic-kakuron-quiz/
```

問題文を見て、以下を回答する形式です。

- 化学反応式
- 元素・単元の所属記号

所属記号は以下です。

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

---

## GitHub上で問題を編集する方法

基本的に編集するのは `reactions.csv` だけです。

反応分類編を編集する場合：

```text
chem-quiz/reactions.csv
```

各論編を編集する場合：

```text
inorganic-kakuron-quiz/reactions.csv
```

GitHub上での操作は以下です。

```text
1. 編集したい reactions.csv を開く
2. 右上の鉛筆アイコンを押す
3. CSVを編集する
4. Commit changes を押す
5. GitHub Actions が自動で実行される
6. 数十秒〜数分後に GitHub Pages に反映される
```

`reactions.json` は自動生成されるファイルなので、基本的には直接編集しません。

---

## CSVの書き方

CSVは以下の形式です。

```csv
id,unit,chapter,statement,equation,categories,note,level
```

各列の意味は以下です。

| 列名 | 内容 |
|---|---|
| `id` | 問題ID。重複しない番号や名前をつける |
| `unit` | 部・大分類 |
| `chapter` | 章・単元 |
| `statement` | 問題文 |
| `equation` | 模範解答の化学反応式 |
| `categories` | 分類記号または所属記号 |
| `note` | 備考 |
| `level` | 難易度。数字で管理する |

---

## CSVの記入例：反応分類編

`chem-quiz/reactions.csv` の例です。

```csv
id,unit,chapter,statement,equation,categories,note,level
001,第I部,酸化物と水の反応,酸化ナトリウムに水を加える。,Na_2O + H_2O -> 2NaOH,ア,塩基性酸化物と水の反応,1
002,第I部,酸化物と水の反応,三酸化硫黄に水を加える。,SO_3 + H_2O -> H_2SO_4,ア,酸性酸化物と水の反応,1
003,第I部,中和反応,二酸化炭素が水酸化ナトリウムに吸収される。,2NaOH + CO_2 -> Na_2CO_3 + H_2O,イ,酸性酸化物と塩基の中和,2
004,第II部,沈殿生成反応,硝酸銀水溶液に塩化ナトリウム水溶液を加える。,AgNO_3 + NaCl -> AgCl↓ + NaNO_3,カ,塩化銀の白色沈殿,1
005,第II部,錯体生成反応,水酸化亜鉛に過剰のアンモニア水を加える。,Zn(OH)_2 + 4NH_3 -> [Zn(NH_3)_4]^2+ + 2OH^-,キ,テトラアンミン亜鉛(II)イオンの生成,2
```

複数分類にしたい場合は、セミコロンで区切ります。

```csv
006,第I部,中和・沈殿,石灰水に二酸化炭素を少量通じる。,Ca(OH)_2 + CO_2 -> CaCO_3↓ + H_2O,イ;カ,中和と沈殿生成,2
```

---

## CSVの記入例：各論編

`inorganic-kakuron-quiz/reactions.csv` の例です。

```csv
id,unit,chapter,statement,equation,categories,note,level
001,1 アルカリ金属元素,ナトリウム,ナトリウムを水に入れる。,2Na + 2H_2O -> 2NaOH + H_2↑,ア,ナトリウムと水の反応,1
002,2 2族元素,カルシウム,酸化カルシウムに水を加える。,CaO + H_2O -> Ca(OH)_2,イ,生石灰と水の反応,1
003,3 両性元素,アルミニウム,アルミニウムに塩酸を加える。,2Al + 6HCl -> 2AlCl_3 + 3H_2↑,ウ,両性元素Alの反応,2
004,4 遷移元素,鉄,鉄に希塩酸を加える。,Fe + 2HCl -> FeCl_2 + H_2↑,エ,鉄の酸との反応,1
005,8 17族元素,塩素,塩素を水に溶かす。,Cl_2 + H_2O <=> HCl + HClO,ク,塩素水,2
```

複数の所属にまたがる問題を作る場合も、セミコロンで区切ります。

```csv
006,総合問題,両性元素と錯体,水酸化アルミニウムに過剰の水酸化ナトリウム水溶液を加える。,Al(OH)_3 + OH^- -> [Al(OH)_4]^-,ウ;ア,両性元素とアルカリ金属水酸化物,2
```

---

## 化学式の書き方

化学式は、CSVでは以下のように書きます。

```text
H_2O
SO_4^2-
AgCl↓
CO_2↑
[Zn(NH_3)_4]^2+
```

画面上では、化学式として整形されて表示されます。

よく使う記法は以下です。

| 書きたいもの | CSVでの書き方 |
|---|---|
| 水 | `H_2O` |
| 硫酸イオン | `SO_4^2-` |
| アンモニウムイオン | `NH_4^+` |
| 沈殿 | `AgCl↓` |
| 気体発生 | `H_2↑` |
| 反応矢印 | `->` |
| 可逆反応 | `<=>` |
| 錯イオン | `[Zn(NH_3)_4]^2+` |

---

## GitHub Pagesへの反映

このリポジトリでは、CSVを編集して保存すると GitHub Actions が自動で実行されます。

処理の流れは以下です。

```text
chem-quiz/reactions.csv
↓
chem-quiz/reactions.json
↓
chem-quiz/index.html が読み込む

inorganic-kakuron-quiz/reactions.csv
↓
inorganic-kakuron-quiz/reactions.json
↓
inorganic-kakuron-quiz/index.html が読み込む
```

2つの小テストは別フォルダで管理されているため、データが混ざることはありません。

---

## ローカルで確認する方法

GitHubにアップロードする前に、自分のPC上で確認することもできます。

### 反応分類編

```bash
cd chem-quiz
python csv_to_json.py
python -m http.server 8000
```

ブラウザで以下を開きます。

```text
http://localhost:8000
```

### 各論編

```bash
cd inorganic-kakuron-quiz
python csv_to_json.py
python -m http.server 8000
```

ブラウザで以下を開きます。

```text
http://localhost:8000
```

---

## よくあるトラブル

### GitHub上でCSVを編集したのに反映されない

GitHub Actions の実行が終わっていない可能性があります。

リポジトリ上部の `Actions` タブを開き、最新の処理が成功しているか確認してください。

---

### CSVを編集したら小テストが表示されなくなった

CSVの書式が崩れている可能性があります。

特に以下に注意してください。

- 1行目の列名を消さない
- カンマの数を崩さない
- 文章中にカンマを入れる場合は `"..."` で囲む
- 分類記号・所属記号は定義済みのものを使う
- 複数記号は `イ;カ` のようにセミコロンで区切る

文章中にカンマを含める場合の例です。

```csv
007,第II部,沈殿生成反応,"硫酸銅(II), 水酸化ナトリウム水溶液を混合する。",CuSO_4 + 2NaOH -> Cu(OH)_2↓ + Na_2SO_4,カ,青白色沈殿,2
```

---

### ブラウザで直接 `index.html` を開くと読み込めない

ブラウザの仕様により、直接ファイルを開くと `reactions.json` を読み込めないことがあります。

その場合は、以下のように簡易サーバーを起動してください。

```bash
python -m http.server 8000
```

または、画面上の「データ読み込み」から `reactions.csv` または `reactions.json` を手動で読み込んでください。

---

## 編集方針

- 問題データの正本は `reactions.csv`
- `reactions.json` は自動生成用
- 小テストの見た目や機能を変える場合は `index.html`
- CSVからJSONへの変換仕様を変える場合は `csv_to_json.py`
- 2つの小テストは別フォルダで独立管理する

---

## ライセンス・利用範囲

授業・自習・演習プリント作成など、個人利用または教育目的で使用することを想定しています。
