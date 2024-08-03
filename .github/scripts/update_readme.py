headers = {
    'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
    'Accept': 'application/rss+xml'
}
feed = feedparser.parse("https://bellringstar.tistory.com/rss", request_headers=headers)