# 記事データ取得用API

## 仕様

Cloud FunctionのHTTPトリガーを利用したAPIで、スプレッドシートの情報をレスポンスします。

## 必須環境

- Cloud Function

## 利用方法

- スプレッドシートを作成します。
- サービスアカウントを取得し、スプレッドシータへの。Pythonのファイルに記載されているスプレッドシートのURLをかえ、また、トークンもサービスアカウントのトークンを貼り付けてください。
- 各自利用するプラットフォーム上では必要な形にデータを整形してください。

## ライブラリ

- Google API Client['LICENSE'](https://github.com/googleapis/google-api-python-client/blob/main/LICENSE)
- Flask['LICENSE'](https://flask.palletsprojects.com/en/stable/license/)

## ライセンス

このリポジトリはMITライセンスにより保護されています。詳しくは[LICENSE.md](LICENSE.md)をご覧ください。

![Table Image](ref/ex_table.png)
