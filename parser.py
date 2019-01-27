import requests
import subprocess
import time
from bs4 import BeautifulSoup as bs
def main():
    f = open('headers.py', 'w')
    f.write('headers = [\n')
    for x in range(1, 20, 1):
        response = requests.get('https://developers.whatismybrowser.com/useragents/explore/software_name/chrome/'+str(x))
        soup = bs(response.text, 'html.parser')
        attr = []
        for td in soup.find_all('td'):
            attr.append(td)
            if(len(attr)==5 and attr[3].string=='Computer'):
                f.write('\"{}\"'.format(attr[0].string)+',\n')
                attr = []
    f.write(']')
    f.close()

if __name__ == '__main__':
    main()
