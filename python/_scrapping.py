import requests, bs4, sys

res = requests.get('https://www.ksl.com/classifieds/search/?keyword=server')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text, "html.parser")
print(type(noStarchSoup))

def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)

# print(dir(res))
# print(dir(noStarchSoup.select('div')))
uprint(noStarchSoup.select('h3'))

# <h3 class="price listing-detail-line">