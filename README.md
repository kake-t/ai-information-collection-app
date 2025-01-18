# AI 情報収集アプリ

## 概要

AI で今日の AI に関するニュースを生成して、ニュースをメールで配信する。

## システム構成図

![システム構成図](./assets/system_configuration.png)

### システムに必要なもの

-   AWS アカウント
-   perplexity の API キー

## 開発環境

-   OS: Linux
-   エディター: vscode (cursor)
-   docker

## トラブルシュート

### devcontainer の中で、test が実行できない。

解決方法：vscode の python 拡張機能が読み込めていないのが原因。vscode で開いたコンテナ画面を閉じて、再度開く。extensions を開いて、python の拡張機能が`reload window`になっていたらそのボタンを押して画面を開き直す。以上で test が実行できるはず。
