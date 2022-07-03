# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from webdriver_manager.chrome import ChromeDriverManager


# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get("https://www.facebook.com/ads/archive/render_ad/?id=402810998437834&access_token=EAAOmIkyczYcBAIg2Gom7jQ170Nw7zswX9mV9SWnsvEdbjuwkhzpcZAZAAJrns5QOpljZAwFqAO2dLQjFQWhBH8EoAKZBa4KOjmAqHSErc5sZCxHzWRdghInjI1ZBSFVL5PGBZAmMUBRInmHxZBoi6K2gZBNU4j5vHmKWHgeZA29ncteIMnShHHfkDVyp0jyO58dhhiTcUuNAFSN2E1FQLzU5AHDHwz3gsEuA0estKuzkFo38lpysTanIZAykZAsRvmFhkk6rNtL1oINdwQZDZD")
# elem = driver.find_elements_by_tag_name("video")
# print(elem.__getattribute__("loop_poster"))

# driver.close()

from fileinput import filename
from tkinter import font
from facebook_scraper import get_posts
import facebook_scraper 

from requests import post
#posts = get_posts('881851445263149', pages=3)

#for p in get_posts('211054052816263',pages=10,filename='testing.csv'):
#    print(p['post_id'],p["post_text"],p['post_url'])

for p in get_posts(post_urls="https://facebook.com/211054052816263/posts/1066162523972074"):
    print(p['post_id'],p["post_text"],p['post_url'])    