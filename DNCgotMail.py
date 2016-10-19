import requests, sys, os
from bs4 import BeautifulSoup

LOG_PATH = '/path/to/log/file'
DUMP_PATH = '/path/to/dump/file'

BASE_URL = 'https://wikileaks.org/dnc-emails/emailid/'

def get_contents(path, mode='r', content=None):
    with open(path, mode, encoding='utf-8') as f:
        if mode == 'r':
            contents = f.read()
            return contents
        elif mode == 'w':
            f.write(content)
            return True

logNum = int(get_contents(LOG_PATH)) if os.path.exists(LOG_PATH) else None

def get_mail(email_number):
    response = requests.get(BASE_URL + str(email_number))
    soup = BeautifulSoup(response.text, 'lxml')
    email_content = soup.find('div', {'class':'email-content'})
    #print(email_content.text)
    return email_content.text.strip()

def write_mail(content, num):
    text = get_contents(DUMP_PATH)
    text = text + '\n\n'+str(num)+'--------------------\n\n' + content
    
    writer = get_contents(DUMP_PATH, mode='w', content=text)
    if writer:
        return True
    else:
        return False

#def write_dict(content, num):
    

#email_dict = {}    
if not logNum:
    for i in range(1,11):
        mail = get_mail(i)
        script = write_mail(mail, i)
        if script:
            with open(LOG_PATH, 'w', encoding='utf-8') as f:
                f.write(str(i))
                if i % 100 == 0:
                    print('logged %s' % i)

else:
    for i in range(logNum+1, 22457):
        mail = get_mail(i)
        

        script = write_mail(mail, i)
        if script:
            with open(LOG_PATH, 'w', encoding='utf-8') as f:
                f.write(str(i))
                if i % 100 == 0:
                    print('logged %s' % i)

        
        
