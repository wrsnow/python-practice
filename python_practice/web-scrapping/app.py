import sys
import os
import requests
from bs4 import BeautifulSoup

module_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(module_dir)
from colors import Bcolors



colored = Bcolors()
print(colored)
html = requests.get("http://quotes.toscrape.com/").text
soup = BeautifulSoup(html, "lxml")
quotes = soup.find_all("div", class_="quote")

for quote in quotes:
  text_content = quote.find("span", class_="text").text
  author = quote.find("small", class_="author").text
  print("-"*60)
  print(f"""
{colored.GREEN}quote: {text_content}{colored.ENDC}
{colored.YELLOW}author: {author}{colored.ENDC}
        """)

