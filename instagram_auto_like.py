import time
import datetime
import random
from selenium import webdriver
from slacker import Slacker
from urllib.parse import quote

token = 'your token key'
slacker = Slacker(token)
options = webdriver.ChromeOptions()
# options.add_argument("headless")
options.add_argument("window-size=1920x1080")
# options.add_argument("disable-gpu")
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
options.add_argument("lang=ko_KR")


time.sleep(3)


id = 'id'
password = 'password'
most_like_tags = []
hash_tags = ['your hash tag1', 'your hash tag2']

class InstaJob:
    @classmethod
    def run(cls, start_index=1, end_index=2):
        print('browser loading..')
        global browser
        browser = webdriver.Chrome('chromedriver', chrome_options=options)

        browser.execute_script("Object.defineProperty(navigator, 'plugins', {get: function() {return[1, 2, 3, 4, 5]}})")
        browser.execute_script(
            "Object.defineProperty(navigator, 'languages', {get: function() {return ['ko-KR', 'ko']}})")
        browser.execute_script(
            "const getParameter = WebGLRenderingContext.getParameter;WebGLRenderingContext.prototype.getParameter = function(parameter) {if (parameter === 37445) {return 'NVIDIA Corporation'} if (parameter === 37446) {return 'NVIDIA GeForce GTX 980 Ti OpenGL Engine';}return getParameter(parameter);};")

        browser.get('https://instagram.com/')

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
        login_link = browser.find_element_by_css_selector('p._g9ean').find_element_by_css_selector('a')
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
        #browser.find_elements_by_css_selector('a._giku3._8scx2._e8tsh.coreSpriteGlyphBlack')[0].click()
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
            element = browser.find_elements_by_css_selector("div._mck9w._gvoze._tn0ps")[9]
            element.find_element_by_css_selector("div._e3il2").click()
            time.sleep(5)

            if any(e in hash_tag for e in most_like_tags):
                count_number = 50
            else:
                count_number = 120

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
    import instagram_auto_like
    instagram_auto_like.InstaJob.run()
