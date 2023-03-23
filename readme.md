# Pythonで学ぶ「Java言語で学ぶデザインパターン入門第3版」

# 環境構築

 - poetryの要求に合う(?)任意VerのPythonをインストールする．MS Store版Pythonはwhere pythonでパスを確認しながらの作業が増えたり，この後インストールするアプリのインストール場所が変わったりして大変になるので，python.orgからを推奨．
 - poetryをインストールする．Pathを通すのを忘れないように．.venvが作成されるように等，設定をする．
 - pyenv-winをインストールする．
 - pyenvを使って任意VerのPythonをインストール．ここのPythonのバージョンは，3.7以上でないと，poetryが正しく動かない．(Poetryのドキュメントに書いてある「3.7+」がそう)
 - poetry initを実行して，Pythonのバージョンだけ指定したpyproject.tomlを作る
 - poetry installを実行して，.venvを作成する
 - poetry add flake8
 - poetry add black
 - poetry shellを実行した状態，つまり.venvの環境に入っている場合，blackやflake8がコマンドとして使える状態になっているため，settings.jsonのblackpathは"black"，flake8pathは"flake8"でOK．フルパス指定しなくてよい

おわり

# 各種ファイルについて

 - .python-version ... pyenvが今いるディレクトリでどのPython環境を起動させるかを判断するためのファイル
 - pyproject.toml ... poetryがインストールしたパッケージのメモ．これを別プロジェクトに移植すれば，poetry installするだけで自動的にまったく同じ仮想環境を作ってくれる
 - poetry.lock ... poetryがインストールしたパッケージと，その依存関係が書かれたファイル(編集厳禁)
 - .venv ... poetry shellを実行することで入れる仮想環境
