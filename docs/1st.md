
## 1주차

 - `6.5` shop 앱 만들기 부터
 - `6.6` 소셜 로그인 추가 까지

### > URL Reverse

[참고자료](https://wayhome25.github.io/django/2017/05/05/django-url-reverse/)

`get_absolute_url`

- 객체의 반환 url(주로 상세 페이지 주소)을 반환하는 메서드
- 객체를 수정하거나 추가했을 때 이동할 주소를 위해 호출한다
- 템플릿에서 상세 화면에서 이동하는 링크를 만들 때 호출한다
- `get_absolute_url`에 사용되는 `reverse` 함수
    - URL 패턴 이름을 가지고 해당 패턴을 찾아 주소를 만들어주는 함수
    - 되돌아갈 페이지의 패턴 이름이 `product app`의 `product_in_category` 인 셈
    - args는 여러 값들을 리스트로 전달하는 데에 사용 (url을 만드는 데에 필요한 pk)
    - detail view를 제공하는 객체에 대해서 무조건 

template tag 상의 `{% url 'detail' object.id %}` 와 본질적으로 같다

```
<a href="{{product.get_absolute_url}}" class="btn btn-primary">View Detail</a>
```

```
{% for c in categories %}
    <a href="{{c.get_absolute_url}}" class="list-group-item {% if current_category.slug == c.slug %}active{%endif %}">{{c.name}}</a>
{% endfor %}

```

#### code 

```
/models.py
    from django.urls import reverse
    ...
    
    class Category(models.Model):
        ...
        def get_absolute_url(self):
            return reverse('shop:product_in_category', args=[self.slug])


    class Product(models.Model):
        ...
        def get_absolute_url(self):
            return reverse('shop:product_detail', args=[self.id, self.slug])
```

*객체 추가/수정에 대한 기본 반환 주소는 `get_absolute_url`으로 본인 페이지로 설정해두고,*   
*특정 링크만 다른 페이지로 넘어가게끔 설계하는 게 일반적*

### > Slug

#### 개념 

URL의 이름을 모델 내의 객체를 기반으로 짓는 방법

> https://web-together.github.io/ 의 12번 째 post의 제목이 `Hello World` 였다면?

 - https://web-together.github.io/post/12 (id)
 - https://web-together.github.io/post/Hello%20World (str)
 - https://web-together.github.io/post/Hello-World   (slug)

#### code 

```
models.py/
    slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True)
    
    # max_length    = slug의 최대 길이
    # db_index      = 해당 필드를 인덱스 값으로 지정
    # allow_unicode = (한글 지원) 영문을 제외한 다른 언어도 사용할 수 있게 한다

```

```
urls.py/
    path('<slug:category_slug>/', product_in_category, name='product_in_category'),
```

> 인자의 기본값은 None (없으면 None, 있으면 category_slug)

```
views.py/
    def product_in_category(request, category_slug=None):       
        current_category = None
        categories = Category.objects.all()
        products = Product.objects.filter(available_display=True)

        if category_slug:
            current_category = get_object_or_404(Category, slug=category_slug)  
            products = products.filter(category=current_category)

        return render(request, 'shop/list.html',
                    {'current_category': current_category, 
                    'categories': categories, 
                    'products': products})

    def product_detail(request, id, product_slug=None):
        product = get_object_or_404(Product, id=id, slug=product_slug)

        return render(request, 'shop/detail.html', {'product': product, 'add_to_cart':add_to_cart})
```