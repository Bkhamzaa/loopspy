from ast import Return
from os import link
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import html_to_json
import json
import re
import urllib.request


fp = urllib.request.urlopen("https://www.facebook.com/ads/archive/render_ad/?id=550017620166870&access_token=EAAOmIkyczYcBAEPFEIMq0ZBeEw4uHTfYpr5EQ0hqCO6P0ZCZCjI6vtLL1p9KuP51aZBAqPUDYOJGl22tfYN6YryT2Ql648s3ZBjcbGhUKiBPwpTkwqOONCDsVzNX2yzlVojTjNR8EOfyVbS4sfGzMY37qTzJEY66BoEP1MTd88DFr6ZCiqY7crjd8G5akyqKhuvQTjCsRWPyKEPnG0qtHmJs3bCquNEkYfLjJ3O44Y7p68I4oOhS17ZABm4ezavxnu5R17qcrc3vgZDZD")

mybytes = fp.read()

mystr = mybytes.decode("utf8")
fp.close()

#print(mystr)

########### hedhi ki tabda el ads feha barcha itsawer in5arij kol taswira wa7adha ######
found_img = re.search('"cards":(.+)creation_time', mystr)
link_img=mystr[found_img.start():found_img.end()]
#print(link_img)

list_str=link_img.replace('],"creation_time','')
list_str=list_str.replace('/','')
text = list_str.split(',')
print(text[0])



def card(text):
    list_of_img=[]
    list_of_vid=[]  
    for i in range(len(text)):
        if (text[i]).find('original_image_url') != -1:
            rmv=text[i].replace('"original_image_url":"','')
            rmv=rmv.replace('"','')
            list_of_img.append(rmv)

        else:
            if (text[i]).find('video_hd_url') != -1:
                rm_v=text[i].replace('{"video_hd_url":"','')
                rm_v=rm_v.replace('"','')
                list_of_vid.append(rm_v)

    print (list_of_img)
    print (list_of_vid)


def img(text):
    found_img = re.search('"images":(.+),"videos"', mystr)or re.search('"images":(.+),"image_crops"', mystr)
    link_img=mystr[found_img.start():found_img.end()]
    list_str=link_img.replace('"images":[','')
    list_str=list_str.replace('],"videos"','') or list_str.replace(',"image_crops"','')
    list_str=list_str.replace('/','')

    nb =list_str.count("original_image_url")
    list_test=list_str.replace('{','')
    list_test=list_test.replace('}','')

#print(nb)

    po=list_test.replace('"original_image_url":','')

    text = po.split(',')
    list_of_img=[]
    for x in range(0, nb*2, 2):
        
        list_of_img.append(text[x])
    print(list_of_img)

def extra_images():
    found_img = re.search('"extra_images":(.+)"extra_links"', mystr)
    link_img=mystr[found_img.start():found_img.end()]
    #print(link_img)

    list_str=link_img.replace('"extra_images":[','')
    list_str=list_str.replace('],"extra_links"','')
    list_str=list_str.replace('/','')
    nb =list_str.count("original_image_handle")
    text = list_str.split(',')
    #print(text)


    list_of_img=[]
    for x in range(0, nb*2, 2):
        rm_v=text[x].replace('{"original_image_handle":"','')
        rm_v=rm_v.replace('"','')
        list_of_img.append(rm_v)
        #print(list_of_img[0])
