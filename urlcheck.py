import urllib.request
with open('C:/scripts/URLlib.txt', 'r') as lib:
    urlstr = lib.read()
    urllist = urlstr.splitlines()
for url in urllist:
    try:
        msg = "The status of %s is:" % url
        print(msg)
        print(urllib.request.urlopen("http://"+url).getcode())
    except urllib.error.URLError:
        print("Oops! failed to connect to %s." % url)

