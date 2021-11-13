import requests
from bs4 import BeautifulSoup as BS
import os







#sdadasd

def sqs():
    pass
#sdadasd1
def ses():
    pass
#sdadasd
#sdadasd2
def sts():
    pass


#sdadasd1
def srs():
    pass

#sdadasd#sdadasd#sdadasd3
def ssw():
    pass


#sdadasd4
def sas():
    pass













url ="https://habr.com/ru/all/"
print("введите ключевое слово")
word=str(input())
flag = "1"
i = 0
t=""
count=0
a=[]
while flag == "1":
    request = requests.get(url)
    soup = BS(request.text, "html.parser")
    teme = soup.find_all("h2", class_='tm-article-snippet__title tm-article-snippet__title_h2')
    for temes in teme:
        temes=temes.find('a', {'class':'tm-article-snippet__title-link'})
        if word.upper( ) in str(temes).upper( ):
            sublink = temes.get('href')
            t =t + '\n'+ str(temes.text) + "     " + "https://habr.com"+ str(sublink)
            count+=1

    if t not in a:
        print(url)
        print(t)
    a.append(t)
    print("_________________________")
    print("Еще? 1=да 0=нет 5=перезапуск")
    if count!=0:
        flag=str(input())

    if flag=='1' or count==0:
        url = 'https://habr.com/ru/all/page'+str(i+1)+"/"
        #print(url)
    elif flag =="0":
        break
    elif flag == "5":
        os.system('habr.py')
    i+=1
    count=0

#window = Tk()
#window.title("Добро пожаловать в приложение PythonRu")
#lbl = Label(window, text=str(t))
#lbl.grid(column=0, row=0)
#window.mainloop()