## 2주차

### Crwaling 기초

[수업자료](https://github.com/web-together/Crawling-Session)

### Django Template 씌우기

[수업자료](https://github.com/web-together/Template-On-Django)

### Django Session 관리

[참고자료](https://developer.mozilla.org/ko/docs/Learn/Server-side/Django/Sessions)
[공식문서](https://docs.djangoproject.com/en/2.0/topics/http/sessions/)

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

#### 세션

세션은 사전 형식으로 이루어져 있으며 views.py가 받는 request 인자 (HTTPRequest)를 통해 접근할 수 있습니다.

```
# key값(e.g. 'my_car')으로 세션값 받아오기. 없다면 KeyError
my_car = request.session['my_car']

# 세션 값 받아오기. 만일 없다면 두 번째 인자로 디폴트 값 생성
my_car = request.session.get('my_car', 'mini')

# 세션 값 설정하기. 
request.session['my_car'] = 'mini'

# 세션 값 지우기 
del request.session['my_car']
```

**예제 : Session을 통한 댓글 저장코드**
```
def post_comment(request, new_comment):

    # 'has_commented' 라는 key 가 있다면 value 를 return 하고, 아니면 False 를 return 합니다.)
    if request.session.get('has_commented', False):
        return HttpResponse("You've already commented.")
    
    c = comments.Comment(comment=new_comment)
    c.save()
    
    # has_commented 를 True로 설정
    request.session['has_commented'] = True
    return HttpResponse('Thanks for your comment!')
```

#### 세션 저장



#### 예제 코드 (프로젝트 코드)

세션의 CRUD를 클래스로 만든 파이썬 파일을 하나 따로 정의하고,

views.py에서 import해서 사용하는 방식

```
class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_ID)
        if not cart:
            cart = self.session[settings.CART_ID] = {}
        self.cart = cart

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def __iter__(self):
        product_ids = self.cart.keys()

        products = Product.objects.filter(id__in=product_ids)

        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']

            yield item


    def add(self, product, quantity=1, is_update=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity':0, 'price':str(product.price)}

        if is_update:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity

        self.save()

    def save(self):
        self.session[settings.CART_ID] = self.cart
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del(self.cart[product_id])
            self.save()

    def clear(self):
        self.session[settings.CART_ID] = {}
        self.session.modified = True

    def get_product_total(self):
        return sum(Decimal(item['price'])*item['quantity'] for item in self.cart.values())
```
