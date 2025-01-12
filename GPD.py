from requests_html import HTMLSession
import wget
from time import  sleep
import os

session = HTMLSession()
cycleN = 0
countEr = 0

try:
    os.makedirs("pdf")
except FileExistsError:
    # directory already exists
    pass

with open('input.txt', 'r') as file:
    line_count = sum(1 for line in file)
file.close()
with open('input.txt', 'r') as file:
    for ptN in file:
        cycleN += 1
        print('Index: #' + str(cycleN) + '/' + str(line_count) + '\nErrors: ' + str(countEr))
        url = 'https://patents.google.com/patent/' + ptN
        
        r = session.get(url.strip())
        print('URL: ' + url + 'Status: ' + str(r))
        if str(r) == '<Response [200]>':
            r.html.render(sleep = 3, timeout = 50)
            pdf_url = r.html.find('a.style-scope.patent-result', first=True).attrs['href']
            print ('PDF URL: ' + pdf_url)
            wget.download(pdf_url, out = 'pdf')
            
            print('\nDownload succes')
            print('______________________________________________________\n\n')
            sleep(1)
        else:
            countEr +=1;
            with open('errors.txt', 'a') as fileEr:
                fileEr.write(str(cycleN) + ' - ' + ptN)
            fileEr.close()
            print ('Error open webpage!')
            print('______________________________________________________\n\n')
            continue
file.close()
