## 2주차

### Crwaling 기초

[수업자료](https://github.com/web-together/Crawling-Session)

### Django Template 씌우기

[수업자료](https://github.com/web-together/Template-On-Django)

### Django Session 관리

[참고자료](https://developer.mozilla.org/ko/docs/Learn/Server-side/Django/Sessions)

Session이란?

세션은 Django 그리고 대부분의 인터넷에서 사용되는 메카니즘으로, 사이트와 특정 브라우저 사이의 "state"를 유지시키는 것입니다.
특정 브라우저로 로그인한 동안 연결 방식 및 연결 정보가 저장되고, 이 저장된 값들을 state라고 불러도 무방합니다.

세션은 당신이 매 브라우저마다 임의의 데이터를 저장하게 하고, 이 데이터가 브라우저에 접속할 때 마다 사이트에서 활용될 수 있도록 합니다.
물론 이 Session은 연결이 끊기만 종료됩니다.

세션은 주로 접속한 유저와의 빠르고 가벼운 상호작용을 구현할 때 사용됩니다. 

#### 세션의 초기 설정
```
INSTALLED_APPS = [
    ...
    'django.contrib.sessions',
    ....

MIDDLEWARE = [
    ...
    'django.contrib.sessions.middleware.SessionMiddleware',
    ....
```

#### 세션 생성


#### 세션 저장

#### 예제 코드 (프로젝트 코드)
