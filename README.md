# instagram-auto-like-with-Python
- 파이썬을 활용한 인스타그램 자동 좋아요
- 목적
    - 파이썬에 적응하기 위해
    - 인스타그램 좋아요를 대신 해주는 프로그램 구현
    - 지인들에게 프로그래밍의 흥미를 돋구기 위해
- 사용한 라이브러리
    - Selenium
        - 웹 브라우저를 직접 작동하기 쉬움
        - 속도가 느리다는 단점이 있지만 크롤링시 치명적이고 인스타그램 좋아요 프로그램에선 단점이 아님(너무 빠르게, 많이 좋아요하면 Block당함)
    - Slacker
    - 그 외엔 기본 라이브러리 활용

### Notice
- 인스타그램에서 element의 주소값을 종종 바꿉니다. 그럴 경우 Error가 당연히 발생합니다

### 사용 방법
- Clone : ```git clone git@github.com:zzsza/instagram-auto-like-with-Python.git```
- Selenium 설치(pip3 대신 pip도 가능)
    - ```pip3 install seleinum```
- Chrome Driver 설치. 설치 방법은 [이준범님 블로그](https://beomi.github.io/2017/02/27/HowToMakeWebCrawler-With-Selenium/) 참고
- ```vi instagram_auto_like.py``` 후, Setting Options, Setting id, password, hashtag에 자신의 값 입력
- 그 후, 터미널에서 실행
```
python3 instgram_auto_like.py
```

### 구현한 기능
- 인스타그램 메인 화면에서 Follower들의 글 자동 좋아요
- 특정 해시태그를 검색한 후, n회 자동 좋아요
- 특정 작업시 슬랙으로 메세지 전송
- 해시태그 좋아요시 컨텐츠의 오류로 페이지가 사라지면, 해당 작업을 건너뛰고 다시 수행



