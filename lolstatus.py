import requests
from bs4 import BeautifulSoup

def status(nickname) :
    try :
        url = "https://www.op.gg/summoners/kr/" + nickname
        res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        res.raise_for_status()

        soup = BeautifulSoup(res.text, "lxml")

        tier_rank = soup.find("div", {"class" : "tier-rank"}).text
        tier_rank = tier_rank[:1].upper() + tier_rank[1:]
        lp = soup.find("div", {"class" : "tier-info"}).find("span", {"class" : "lp"}).text

        tier = tier_rank + " | " + lp

        win_lose = soup.find("span", {"class" : "win-lose"}).text.replace("Win Rate "," (") + ")"

        return tier + "\n" + win_lose
    except :
        return "유저를 찾을 수 없습니다."