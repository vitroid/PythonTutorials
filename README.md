#使い方
このテキストは、WinPythonを使った2日間の集中講義で、まったくプログラミングをしたことのない理系の学生にPythonを教えることを目標とした教材です。
これ以外に、印刷物で配布しているレジュメがあります。いずれはそれもアップロードしたいと思います。

いろいろ足りないところもあると思います。お気付きの点はcitroid@gmail.comまでお知らせいただけると、改良の役に立てさせていただきます。

#WinPythonのインストール
今回の講義では(昨年までと違い)、WinPythonを利用します。WinPythonはその名の通り、WindowsでPythonを使うためのパッケージで、科学にPythonを使う人のために、いろんなライブラリ(拡張機能)をよりすぐってあり、将来研究での本格的な利用にも耐える設計になっています。なお、USBメモリにインストールする場合には、以下の作業は自宅のWindows PCで行っても構いません。

パッケージは以下のURLからダウンロードします。
    http://sourceforge.net/projects/winpython/

画面中央の緑のDownloadボタンをクリックすると、ダウンロードされます。ただし、けっこう時間がかかるので、近くの友人がすでにダウンロードしたものを持っていれば、そのファイル(WinPython……exe)をコピーするのが早道です。

ダウンロードしたファイルを開いて下さい。しばらくして、 “Destination Folder” (インストール先フォルダ)を聞いてきます。ここで内蔵ディスクを選ぶと内蔵ディスクに、USBメモリを選ぶとUSBメモリにインストールされます。1ギガバイトの空き容量が必要ですが、岡大のシステムはディスク容量がとても小さいので、USBメモリを選ぶことをおすすめします。

インストールにはかなり時間がかかります。家で作業する場合は、夕食を作るなり風呂に入るなりして気長に待って下さい。大学で作業する場合は情報端末室の開室時間に注意して作業して下さい。

インストールがおわったら、インストール先フォルダの中に「WinPython-32bit-3.4.3.2」のような名前のフォルダができているはずです。フォルダの中の「IPython Notebook.exe」を今回の演習で使います。

#IPython notebookのMacOSへのインストール
##HomeBrewの人
1. Python3をインストールします。

    % brew install python3

2. pipを使って、IPythonをインストールします。

    % pip3 install ipython pyzmq jsonschema Jinja2 tornado matplotlib simply spicy numpy scikit-image

3. IPython notebookのファイル(拡張子.ipynb)のあるフォルダで、IPython notebookを起動します。ブラウザ内で編集画面が使えるようになります。

    % ipython3 notebook

##MacPortsの人
1. Python3とPIP (Python用のパッケージマネージャ)をインストールします。(管理者権限)

    % sudo port install python34 py34-pip

2. pipを使って、IPythonをインストールします。(管理者権限)

    % sudo pip3 install ipython pyzmq jsonschema Jinja2 tornado matplotlib simply spicy numpy scikit-image

3. IPython notebookのファイル(拡張子.ipynb)のあるフォルダで、IPython notebookを起動します。ブラウザ内で編集画面が使えるようになります。

    % ipython3 notebook

#参考資料
##Pythonプログラムを書くのに役立つサイト
Pythonには、古いバージョン(バージョン2系)と新しいバージョン(バージョン3系)があり、微妙に文法が変わっています。今回の実習は3系の文法を説明しています。

* [Python言語のオンラインマニュアル(日本語)](http://docs.python.jp/3/) Pythonの書き方のほか、各種ライブラリを紹介している。
* [WinPython](http://sourceforge.net/projects/winpython/) この講義で使用しているWinPython(WP)の提供元(英語)。最新版を入手可能
* [Scipy](http://www.scipy.org) WPに含まれる高度な数値計算ライブラリの情報(英語)。
* [pandas](http://pandas.pydata.org/) WPに含まれるデータ解析ライブラリpandasの情報(英語)。
* [Dive into Python3](http://diveintopython3-ja.rdy.jp/) Python2との違い(日本語)。Python3に移行するメリットが簡潔に明快に書かれている。すでにPython2をどこかでさわったことがある人は読むとよい。
* [CodeAcademy](http://www.codecademy.com/tracks/python) フリーオンライン教材CodeAcademyで学ぶPython。講義を聞くのがかったるい人はこっちで学ぶことも可能。
* [Google App Engine](https://developers.google.com/appengine/?hl=ja) Googleが提供するウェブアプリケーション開発環境Google App Engine。ウェブサーバ上で動くアプリケーションを無料でPythonで開発できる(日本語)。

iPhoneのApp Storeで検索すると、iPhone上でPythonプログラムを書いて走らせることもできるようです。

(Editing test)
