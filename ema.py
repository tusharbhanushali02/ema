import requests
import time
import random
from bs4 import BeautifulSoup

BOT_TOKEN = "6251749622:AAElTewJeNadErqeG5IegaSE_RACiYa6rYs"
CHANNEL_NAME = "@entifymovies"
MSG = ""
moviename = ""
link1 = ""
link2 = ""

mode = input("Are you Testing : ")
mode = str(mode)
sleeptimemax = input("Enter Sleep Time Max : ")
sleeptimemin = input("Enter Sleep Time Min : ")
max = input("Enter Range Max : ")
min = input("Enter Range Min : ")
end = int(max)
start = int(min)

# page
for x in range(start,end):

    url = "https://khatrimazaful.world/category/dual-audio-hindi-english-movies/page/" + str(x)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    movies = soup.find_all("h2", class_="entry-title")

    # movie
    for movie in movies:
        src = movie.find("a")
        srcs = src.string
        moviename = srcs

        ur = src.get('href')
        response = requests.get(ur)
        soup = BeautifulSoup(response.content, "html.parser")

        movies = soup.find_all("h3")

        # link
        i = 1
        for movie in movies:
            q = movie.string
            src = movie.find("a")
            if(src):
                href = str(src.get('href'))
                href = f'weefly-url.000webhostapp.com/entify/?og={href}'

                if(i == 1):
                    link1 = ""
                if(href.find('blogspot')==-1):
                    link1 = f"<a href='{href}'><b>{q}</b></a>\n\n"
                else:
                    link1 = ""
                if(i == 2):
                    link2 = f"<a href='{href}'><b>{q}</b></a>"
                i = i + 1

        # msg movie

        MSG = f"{moviename} 🎥 \n\n-----------------------------------------\n ❤️ LOVE IT SHARE IT ! ❤️ \n ----------------------------------------- \n\n Download Links 🔥 \n\n {link1} {link2} \n\n -----------------------------------------"

        print(MSG)

        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHANNEL_NAME}&text={MSG}&parse_mode=HTML&disable_notification=True"

        if(mode=="n"):
            requests.get(url)

        sleeptimemax = int(sleeptimemax)
        sleeptimemin = int(sleeptimemin)
        sleeptime = random.randint(sleeptimemin,sleeptimemax)
        print(sleeptime)
        time.sleep(sleeptime)
