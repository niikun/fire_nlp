# fire_nlp
building NLP app with fire

## Python Script

#!/usr/bin/env python3
```bash
touch hello.py
chmod +x hello.py
./hello.py
```

## TextBlob
TextBlobはテキストデータを処理するためのPythonライブラリです。
品詞タグ付け、名詞句抽出、感情分析、分類など、一般的な自然言語処理（NLP）タスクに飛び込むためのシンプルなAPIを提供します。https://textblob.readthedocs.io/en/dev/

## 名詞抽出

nameの後ろに名詞を入れてもらえれば、wikipediaから名詞を検索して、その中に含まれる名詞を抽出できます。
"""bash
./search_nlp.py --name OpenAI
"""