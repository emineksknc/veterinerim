# Veterinerim Uygulaması
Proje Django 1.11.29 ve Python 3.7 ile yazılmış olup, bir veteriner projesi olarak sunulmuştur. Kullanıcılar uygulamaya üye olabilir, Birden fazla Evcil Hayvanını tanıtabilir, güncelleyebilir ve silebilir. 

## Kurulum
İndirdikten sonra proje dizini içerisinde :

virtualenv venv

**_Linux & Mac:_** ``` source venv/bin/activate```

**_Windows:_** ``` venv\Scripts\activate```

```pip install -r requirements.txt```

```python manage.py makemigrations```

```python manage.py migrate```

```python manage.py createsuper```

```python manage.py runserver```

## Kullanılan Araçlar

> Responsive tasarımlar için **bootstrap4** kullanılmıştır.
>> Formların gösterimi için **django_crispy_forms** kullanılmıştır.
>>> Database olarak sqlite kullanılmıştır.

