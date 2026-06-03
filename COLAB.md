# Google Colabで動かす

このアプリはStreamlit製なので、Colab上では公開トンネルを使ってブラウザから開きます。

## いちばん簡単な手順

1. Google Colabで `colab_launcher.ipynb` を開く
2. GitHubに置いている場合は、最初のコードセルの `REPO_URL` にリポジトリURLを入れる
3. GitHubに置いていない場合は、セルの案内に従って `app.py`、`curriculum.py`、`requirements.txt` をアップロードする
4. 上から順番にセルを実行する
5. 最後に表示される `https://...trycloudflare.com` のURLを開く

## 注意

- 発行されるURLは、Colabのセッションが動いている間だけ有効です。
- Colabを閉じたりランタイムが切断されたりすると、URLも使えなくなります。
- ずっと残る公開URLが必要なら、Streamlit Community CloudやHugging Face Spacesにデプロイしてください。

