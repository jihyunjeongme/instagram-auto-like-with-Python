import time
import datetime
import random
from selenium import webdriver
from slacker import Slacker
from urllib.parse import quote

token = 'your slack token'
slacker = Slacker(token)

browser = webdriver.PhantomJS(service_args=["--ignore-ssl-errors=true", "--ssl-protocol=any"])
browser.set_window_size(1280, 1024)

browser.get('https://instagram.com/')
time.sleep(3)


id = 'id'
password = 'password'
hash_tags = ['your','hashtag']
most_like_tags = hash_tags[:1]

class InstaJob:
    @classmethod
    def run(cls, start_index=1, end_index=2):
        start_text = "{id} Insta Auto Like Start : {time}".format(id=id, time=datetime.datetime.now())
        print('start')
        slacker.chat.post_message('#general', text=start_text)
        for i in range(start_index, end_index):
            cls.login()
            cls.timeline_like()
            cls.hashtag_like()
        end_text = "{id} Insta Auto Like End : {time}".format(id=id, time=datetime.datetime.now())
        slacker.chat.post_message('#general', text=end_text)

    @classmethod
    def login(cls):
        login_link = browser.find_element_by_css_selector('a._b93kq')
        login_link.click()

        username_input = browser.find_elements_by_css_selector('input._o716c')[0]
        username_input.send_keys(id)
        time.sleep(2 + random.random() * 0.3)
        password_input = browser.find_elements_by_css_selector('input._o716c')[1]
        password_input.send_keys(password)
        password_input.submit()
        time.sleep(2)
        print("login success")

    @classmethod
    def timeline_like(cls):
        print('timeline like start')
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        try:
            for i in range(130):
                time.sleep(3)
                browser.find_elements_by_css_selector('span._8scx2.coreSpriteHeartOpen')[0].click()
        except:
            slacker.chat.post_message('#general', text="raise timeline like error")
            pass


    @classmethod
    def hashtag_like(cls):
        print('hashtag like start')
        for hash_tag in hash_tags:
            print(hash_tag + " 좋아요 작업을 시작합니다")
            browser.get("https://www.instagram.com/explore/tags/" + quote(hash_tag))
            time.sleep(4 + random.random() * 1.2)
            element = browser.find_elements_by_css_selector("div._mck9w._gvoze._f2mse")[9]
            element.find_element_by_css_selector("div._e3il2").click()
            time.sleep(5)

            if any(e in hash_tag for e in most_like_tags):
                count_number = 50
            else:
                count_number = 30

            for i in range(1, count_number):
                try:
                    browser.find_element_by_css_selector("span._8scx2.coreSpriteHeartOpen").click()
                    time.sleep(1 + random.random() * 1.2)
                    browser.find_element_by_css_selector("a._3a693.coreSpriteRightPaginationArrow").click()
                    time.sleep(0.8 + random.random() * 1.3)
                except:
                    browser.find_element_by_css_selector("a._3a693.coreSpriteRightPaginationArrow").click()
                    time.sleep(1 + random.random() * 1.2)

if __name__ == '__main__':
    InstaJob.run()
