# Streamlit Community Cloudで公開する

このアプリはStreamlit Community Cloudにそのままデプロイできます。

## 必要なファイル

GitHubリポジトリのルートに、少なくとも次のファイルを置いてください。

- `app.py`
- `curriculum.py`
- `requirements.txt`
- `.streamlit/config.toml`

任意ですが、説明用に次のファイルも置くと管理しやすくなります。

- `README.md`
- `COLAB.md`
- `STREAMLIT_CLOUD.md`

## 公開手順

1. GitHubで新しいリポジトリを作る
2. このフォルダのファイルをGitHubリポジトリへアップロードする
3. https://share.streamlit.io/ を開く
4. GitHubアカウントでログインする
5. `Create app` をクリックする
6. `Yup, I have an app` を選ぶ
7. 次の内容を指定する

| 項目 | 指定内容 |
| --- | --- |
| Repository | アップロードしたGitHubリポジトリ |
| Branch | `main` |
| Main file path | `app.py` |
| App URL | 好きな英数字の名前 |

8. `Deploy` をクリックする
9. 数分待って、表示された `https://...streamlit.app/` を開く

## 更新方法

アプリ公開後は、GitHub上のファイルを編集して保存すれば、Streamlit Cloud側にも反映されます。
依存関係を変えた場合は、再インストールに少し時間がかかることがあります。

## 公開範囲

GitHubリポジトリが公開リポジトリの場合、アプリも基本的に公開で共有しやすい状態になります。
授業や教材として配布するなら、公開リポジトリにしておくのが一番わかりやすいです。

## トラブル時に見る場所

Streamlit Cloudのアプリ画面右側にログが表示されます。
エラーが出た場合は、まず次を確認してください。

- `Main file path` が `app.py` になっているか
- `requirements.txt` がリポジトリにあるか
- `curriculum.py` が `app.py` と同じ階層にあるか
- Python versionは通常デフォルトで問題ないか

