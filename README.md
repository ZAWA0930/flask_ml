# flask_ml
flaskを使用し、tensorflowで学習させたモデルを使った犬猫を判別するwebアプリです。
主に、flaskの練習用として作成しました。
デプロイはしていません。

# DEMO
今回は、レイアウトは気にせずh5モデルが使用できるか確認するために作成しました。
![image](https://github.com/ZAWA0930/flask_ml/assets/93305831/874ec85b-e332-4afa-b77d-9c8c167644c6)

ファイルから画像を選び、判定開始ボタンを押すと以下の画像のように犬か猫を判定できます
![image](https://github.com/ZAWA0930/flask_ml/assets/93305831/5a5ac3be-e8a7-43c0-a67c-91f22dfcbbb2)


# Requirement

flask
werkzeug
tensorflow

# Note

モデルはGoogleColabを使用して作成しました。精度はあまり求めす、約8割程度です。
h5だと重すぎると感じたためTfliteモデルに変換して行うべきでした。

# Author

* 作成者:ZAWA0930
* e-mail:zawazawagold4649@gmail.com


