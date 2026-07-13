# 無機化学小テスト生成器

無機化学の小テストをブラウザ上で生成し、印刷用PDFとして出力するためのリポジトリです。

## 小テストへのリンク

GitHub Pagesで公開している場合は、以下のリンクからアクセスできます。

> `ユーザー名` と `リポジトリ名` は、自分のGitHub PagesのURLに合わせて置き換えてください。

- [無機化学 化学反応式小テスト](https://noho134217728.github.io/quiz-tools/chem-quiz/)
- [無機化学小テスト：各論編](https://noho134217728.github.io/quiz-tools/inorganic-kakuron-quiz/)

リポジトリ直下のトップページを作成している場合は、以下からも選択できます。

- [小テスト生成器トップページ](https://ユーザー名.github.io/リポジトリ名/)

## 収録している小テスト

### 1. 無機化学 化学反応式小テスト

フォルダ：`chem-quiz/`

問題文を読み、以下の2つを回答する形式です。

- 化学反応式
- 化学反応の分類記号

分類記号は以下です。

| 記号 | 分類 |
|---|---|
| ア | 酸塩基反応：酸化物と水の反応 |
| イ | 酸塩基反応：中和反応 |
| ウ | 酸塩基反応：遊離反応 |
| エ | 酸化還元反応 |
| オ | 熱分解反応 |
| カ | 沈殿生成反応 |
| キ | 錯体生成反応 |

複数の分類に該当する場合は、`イ;カ` のようにセミコロンで区切って入力します。

### 2. 無機化学小テスト：各論編

フォルダ：`inorganic-kakuron-quiz/`

問題文を読み、以下の2つを回答する形式です。

- 化学反応式
- 元素・単元の所属記号

所属記号は以下です。

| 記号 | 所属 |
|---|---|
| ア | アルカリ金属元素 |
| イ | 2族元素 |
| ウ | 両性元素 |
| エ | 遷移元素 |
| オ | 14族元素 |
| カ | 15族元素 |
| キ | 16族元素 |
| ク | 17族元素 |

複数の所属に該当する場合は、`ウ;エ` のようにセミコロンで区切って入力します。

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

基本的には、問題データは各フォルダの `reactions.csv` を編集します。

```text
chem-quiz/reactions.csv
inorganic-kakuron-quiz/reactions.csv
```

`reactions.json` は、CSVから生成されるデータファイルです。通常は直接編集しません。

## GitHub上で問題を編集する方法

GitHub上で問題を追加・修正する場合は、以下の手順で編集します。

1. GitHubでこのリポジトリを開く。
2. 編集したい小テストのフォルダを開く。
3. `reactions.csv` を開く。
4. 右上の鉛筆アイコンを押す。
5. CSVを編集する。
6. 画面下部の `Commit changes` を押して保存する。
7. GitHub Actionsが自動で動く。
8. 数十秒〜数分後、GitHub Pages上の小テストに反映される。

編集するファイルは以下の通りです。

| 小テスト | 編集するCSV |
|---|---|
| 化学反応式小テスト | `chem-quiz/reactions.csv` |
| 各論編 | `inorganic-kakuron-quiz/reactions.csv` |

2つのCSVは別ファイルなので、データが勝手に混ざることはありません。

## CSVの書き方

CSVの列は以下です。

```csv
id,unit,chapter,statement,equation,categories,note,level
```

| 列名 | 内容 |
|---|---|
| `id` | 問題ID。重複しない値にする。 |
| `unit` | 部・大分類。例：`第I部`、`アルカリ金属元素`。 |
| `chapter` | 章・小分類。例：`中和反応`、`ナトリウム`。 |
| `statement` | 問題文。 |
| `equation` | 模範解答の化学反応式。 |
| `categories` | 分類記号または所属記号。複数の場合は `;` で区切る。 |
| `note` | 解答欄に表示する備考。空欄でもよい。 |
| `level` | 難易度。任意。例：`1`、`2`、`3`。 |

### 化学反応式小テストの例

```csv
id,unit,chapter,statement,equation,categories,note,level
001,第I部,中和反応,二酸化炭素が水酸化ナトリウムに吸収される。,2NaOH + CO_2 -> Na_2CO_3 + H_2O,イ,酸性酸化物と塩基の中和,2
002,第II部,沈殿生成反応,硝酸銀水溶液に塩化ナトリウム水溶液を加える。,AgNO_3 + NaCl -> AgCl↓ + NaNO_3,カ,塩化銀の白色沈殿,1
003,第I部,中和・沈殿,石灰水に二酸化炭素を少量通じる。,Ca(OH)_2 + CO_2 -> CaCO_3↓ + H_2O,イ;カ,中和と沈殿生成,2
```

### 各論編の例

```csv
id,unit,chapter,statement,equation,categories,note,level
001,アルカリ金属元素,ナトリウム,ナトリウムが水と反応する。,2Na + 2H_2O -> 2NaOH + H_2↑,ア,水素を発生し水酸化ナトリウムを生じる,1
002,両性元素,アルミニウム,アルミニウムが水酸化ナトリウム水溶液に溶ける。,2Al + 2NaOH + 6H_2O -> 2Na[Al(OH)_4] + 3H_2↑,ウ,両性金属の反応,2
003,17族元素,塩素,塩素が水酸化ナトリウム水溶液と反応する。,Cl_2 + 2NaOH -> NaCl + NaClO + H_2O,ク,冷希NaOH水溶液との反応,2
```

## 化学式・反応式の入力ルール

化学式は、普通のテキストとして入力します。

| 入力 | 表示の意味 |
|---|---|
| `H_2O` | 水。2が下付きになる。 |
| `SO_4^2-` | 硫酸イオン。電荷が上付きになる。 |
| `->` | 反応矢印。 |
| `↓` | 沈殿。 |
| `↑` | 気体発生。 |
| `;` | 複数記号の区切り。 |

例：

```text
AgNO_3 + NaCl -> AgCl↓ + NaNO_3
CaCO_3 -> CaO + CO_2↑
Zn(OH)_2 + 4NH_3 -> [Zn(NH_3)_4]^2+ + 2OH^-
```

## GitHub Pagesへの反映

このリポジトリでは、GitHub Actionsを使ってCSVをJSONに変換し、そのままGitHub Pagesにデプロイする想定です。

`.github/workflows/deploy-pages.yml` では、以下の変換が行われます。

```text
chem-quiz/reactions.csv
↓
chem-quiz/reactions.json

inorganic-kakuron-quiz/reactions.csv
↓
inorganic-kakuron-quiz/reactions.json
```

それぞれ別々のCSVから別々のJSONを生成するため、化学反応式小テストと各論編のデータは混ざりません。

## ローカルで確認する方法

GitHubにアップロードする前に、自分のPC上で確認したい場合は、各フォルダでCSVをJSONに変換してからローカルサーバーを起動します。

### 化学反応式小テスト

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

## 印刷・PDF化の方法

1. 小テストページを開く。
2. 出題分類・出題数・乱数シードなどを設定する。
3. `小テストを生成` を押す。
4. `印刷` を押す。
5. 印刷画面でプリンタを選ぶ。
6. PDF化したい場合は、印刷先で `PDFに保存` を選ぶ。

解答用紙を不要にしたい場合は、画面上の `解答用紙も生成する` のチェックを外してから生成します。

## よくある編集ミス

### CSV内にカンマを入れたい場合

CSVではカンマが列の区切りとして扱われます。
問題文や備考にカンマを含めたい場合は、そのセル全体をダブルクォートで囲みます。

```csv
001,第I部,例,"ナトリウム, カリウムについて答える。",2Na + 2H_2O -> 2NaOH + H_2↑,ア,,1
```

### 分類記号・所属記号を間違えた場合

未定義の記号を入れると、読み込み時にエラーになります。

例えば、化学反応式小テストでは `ク` は未定義です。
各論編では `ク` は17族元素として定義されています。

### `reactions.json` が更新されない場合

GitHub Actionsが失敗している可能性があります。

リポジトリ上部の `Actions` タブを開き、最新の実行結果を確認してください。
CSVの書式ミスがある場合、変換処理で止まることがあります。

## 運用方針

- 問題の正本は `reactions.csv` とする。
- `reactions.json` は自動生成ファイルとして扱う。
- GitHub上で問題を編集する場合は、基本的にCSVだけを編集する。
- 反応式編と各論編は別フォルダ・別CSVで管理する。
- 小テストのURLはREADME冒頭に置き、すぐアクセスできるようにする。
