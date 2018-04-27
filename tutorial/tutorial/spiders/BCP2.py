from bs4 import BeautifulSoup

import urllib.request as ur


url = 'http://www.data.jma.go.jp/obd/stats/etrn/view/monthly_s3_en.php?block_no=47401&view=1'
html = ur.urlopen(url).read()
soup = BeautifulSoup(html,"html.parser" )
table = soup.find_all('table', class_='data2_s')
rows = table[0].find_all('tr')
fo = open('fo.txt','w')
for r in rows:
    fo.write(str(r.txt) + '\n')
fo.close()