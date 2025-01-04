# web

AI 情報収集アプリ

## 前提

-   エディター: vscode (cursor)

## トラブルシュート

### ~~問題：openai の API から、「No such project」が返ってくる。~~

~~解決方法：OpenAI の設定画面から新しく Project を作成して、API key もそのプロジェクトで使う設定にする。デフォルトのプロジェクトではエラーなった。~~

### 問題：devcontainer の中で、test が実行できない。

解決方法：vscode の python 拡張機能が読み込めていないのが原因。vscode で開いたコンテナ画面を閉じて、再度開く。extensions を開いて、python の拡張機能が`reload window`になっていたらそのボタンを押して画面を開き直す。以上で test が実行できるはず。
