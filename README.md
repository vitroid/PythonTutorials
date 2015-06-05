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