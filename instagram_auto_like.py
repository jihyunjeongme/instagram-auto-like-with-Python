import time
import datetime
import random
from selenium import webdriver
from slacker import Slacker
from urllib.parse import quote
from selenium.common.exceptions import NoSuchElementException


# ======== 1. Setting Options =======
# slack_token : 작업이 진행될 때 중간 중간 슬랙에 메세지 발송
slack_token = 'token'
slacker = Slacker(slack_token)
options = webdriver.ChromeOptions()

# Chrome을 안 띄우고 수행하고 싶으면 아래 주석을 해제(리눅스 서버에서 작업시 headless 추천, 디버깅시는 headless 주석처리)
# options.add_argument("headless")

# Chrome 설정 : 진짜 유저가 작업하는 것처럼 보이도록 설정
options.add_argument("window-size=1920x1080")
options.add_argument("disable-gpu")
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 \
                      (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
options.add_argument("lang=ko_KR")

# ======= 2. Setting id, password, hashtag ======
id = 'id'
password = 'password'

timeline_like_count = 120

# hash_tags : 좋아요할 전체 해시태그 리스트
# important_hash_tags : 중요해서 더 많이 like할 해시태그 리스트
important_hash_tags = ['코딩']
important_hash_tags_count = 120
hash_tags = ['코딩', '공대생', '공스타그램', '책스타그램','파이썬','프로그래밍','개발자','통계학과','스타트업','딥러닝']
hash_tags_count = 60

# ======== 3. InstaJob Class ======


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
            "const getParameter = WebGLRenderingContext.getParameter;WebGLRenderingContext.prototype.getParameter = \
            function(parameter) {if (parameter === 37445) {return 'NVIDIA Corporation'} if (parameter === 37446) \
            {return 'NVIDIA GeForce GTX 980 Ti OpenGL Engine';}return getParameter(parameter);};")

        browser.get('https://instagram.com/')

        start_text = "{id} Insta Auto Like Start : {time}".format(id=id, time=datetime.datetime.now())
        print(start_text)
        slacker.chat.post_message('#general', text=start_text)
        for i in range(start_index, end_index):
            cls.login()
            cls.timeline_like()
            cls.hash_tags_like()
        end_text = "{id} Insta Auto Like End : {time}".format(id=id, time=datetime.datetime.now())
        slacker.chat.post_message('#general', text=end_text)
        browser.quit()

    @classmethod
    def login(cls):
        """
        인스타그램 메인에서 로그인하는 함수
        """
        login_link = browser.find_element_by_css_selector('p.izU2O').find_element_by_css_selector('a')
        login_link.click()
        time.sleep(3.5)

        username_input = browser.find_elements_by_css_selector('input._2hvTZ')[0]
        username_input.send_keys(id)
        time.sleep(2 + random.random() * 0.3)
        password_input = browser.find_elements_by_css_selector('input._2hvTZ')[1]
        password_input.send_keys(password)
        time.sleep(1)
        password_input.submit()
        time.sleep(2)
        print("login success")

    @classmethod
    def timeline_like(cls):
        """
        timeline_likg_count만큼 타임라인의 좋아요를 누름
        이 부분에 not clickable at point라고 error가 발생되고 있습니다. 추후 수정 필요
        """
        print('timeline like start')
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        try:
            for i in range(timeline_like_count):
                time.sleep(1.5)
                browser.find_elements_by_css_selector('span.glyphsSpriteHeart__outline__24__grey_9.Szr5J')[0].click()
                time.sleep(1.5)

        except Exception as e:
            print("Error! ", e)
            slacker.chat.post_message('#general', text="raise timeline like error")
            pass

    @classmethod
    def hash_tags_like(cls):
        """
        hash_tags_like
        위에서 설정한 important_hash_tags와 hash_tags들을 각 횟수만큼 좋아요
        만약 컨텐츠가 중간에 삭제되거나 페이지가 없으면
        다음 해시태그로 이동되도록 예외처리
        """
        print('hash_tags like start')
        for hash_tag in hash_tags:
            try:
                print(hash_tag + " 좋아요 작업을 시작합니다")
                browser.get("https://www.instagram.com/explore/tags/" + quote(hash_tag))
                time.sleep(5 + random.random() * 1.2)
                element = browser.find_elements_by_css_selector("div._9AhH0")[9]
                element.click()
                time.sleep(5)

                if any(e in hash_tag for e in important_hash_tags):
                    count_number = important_hash_tags_count
                else:
                    count_number = hash_tags_count

                for i in range(1, count_number):
                    try:
                        browser.find_element_by_css_selector("span.glyphsSpriteHeart__outline__24__grey_9.Szr5J").click()
                        time.sleep(1 + random.random() * 1.2)
                        time.sleep(1.2 + random.random() * 1.3)
                    except:
                        browser.find_element_by_css_selector("a.HBoOv.coreSpriteRightPaginationArrow").click()
                        time.sleep(1 + random.random() * 1.2)

            except NoSuchElementException as e:
                print("NoSuch Error", e)
                pass

            except Exception as e:
                print("Error! ", e)


if __name__ == '__main__':
    import instagram_auto_like
    instagram_auto_like.InstaJob.run()
