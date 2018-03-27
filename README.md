# instagram-auto-like-with-Python

파이썬을 활용한 인스타그램 자동 좋아요 소스

목적 : 인스타그램을 활용하는데 조금 더 편하게 자동화하고 싶었고 현재 업체에서 팔로워 1000명 모집! 프로그램들을 만들어보고 싶었습니다

사용한 라이브러리 : Selenium

셀레니움의 장점 : 웹 브라우저를 직접 작동할 경우 용이(단, 속도가 느린편이나 인스타그램측에서 많은 좋아요수를 할 경우 제재를 가하기 때문에 셀레니움으로 활용해도 좋다고 판단)

### 사용 방법
```
# instagram_auto_like 파일에
# id = 'id'
# password = 'password'
# hash_tags = ['your hash tag1', 'your hash tag2'] 채우기
python3 instgram_auto_like.py
```

### 구현한 기능

- 인스타그램 메인 화면에서 Follower들의 글을 자동 좋아요

- 특정 해시태그를 검색한 후, n회 자동 좋아요

- 작업이 완료되면 슬랙으로 메세지 전송


### 더 익혀야 할 것들

- 데이터베이스 지식
- 웹프로그래밍 지식 ( Flask나 Django )


