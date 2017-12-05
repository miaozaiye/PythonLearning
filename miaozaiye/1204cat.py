from stdpackage import instream,outstream
import sys

from stdpackage.outstream import OutStream
from stdpackage.instream import InStream



def _readHTML(NUMBER):
    WEBSITE = 'https://www.proginn.com/wo/'+NUMBER
    page = InStream(WEBSITE)
    html = page.readAll()

    # print(html)
    return html

def price(NUMBER):
    html = _readHTML(NUMBER)
    ind1 = html.find('work-price')
    ind2 = html.find('price',ind1)
    start = html.find('>',ind2)
    end = html.find('</span',start)
    print(ind1,ind2,start,end)
    price = html[start+21:end]
    print('this is price:',price)

def main():
    NUMBER = sys.argv[1]

    price(NUMBER)


main()