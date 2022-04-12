#Twitterライブラリを使用(NodeBoxに追加済み)
import twitter
#Twitter APIにアクセスする。
api = twitter.Twitter("yourTwitterID","yourPassword")
#Twitterにメッセージを送る。
message = u"Twitter APIのテスト"
api.statuses.update(status=message.encode("utf-8"))
