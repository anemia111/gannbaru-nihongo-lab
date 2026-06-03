# がんばる日本語ラボ

「がんばって」だけに頼らず、相手の状況に合った励まし、共感、提案を練習する日本語教材アプリです。

## 機能

- 学習マップとレッスン進捗
- 例文、重要表現、教師用メモ
- 場面別の作文、発話練習、セルフチェック
- 選択式の確認テストと解説
- 配布用ワークシート、教師用ガイド、進捗CSVの出力

## 起動

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Google Colabで起動

Colabで動かす場合は、`colab_launcher.ipynb` を開いて上から順番に実行してください。
Streamlitを起動したあと、Cloudflare Tunnel経由の一時公開URLが表示されます。

詳しい手順は [COLAB.md](COLAB.md) を参照してください。

## Streamlit Community Cloud

このリポジトリをデプロイする場合は、メインファイルに `app.py` を指定してください。

詳しい公開手順は [STREAMLIT_CLOUD.md](STREAMLIT_CLOUD.md) を参照してください。
