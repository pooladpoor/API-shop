

# api shop

api برای فروشگاه اینترنتی

## پیش‌نیازها

برای اجرای این پروژه، ابتدا باید موارد زیر را بر روی سیستم خود نصب داشته باشید:

- [Docker](https://www.docker.com/get-started)

## مراحل اجرای پروژه

### 1. کلون کردن مخزن (Repository)
ابتدا مخزن پروژه را کلون کنید:

```bash
git clone https://github.com/pooladpoor/API-shop.git
```
به دایرکتوری پروژه بروید:
```bash
cd API-shop
```

### 2. اجرای پروژه 
ابتدا کانتینر را بسازید :
```bash
docker build -t shop-api:latest .   
```
بعد آن را اجرا کنید :
```bash
docker run -p 8000:8000 shop-api 
```
## 3.استفاده کنید

- [داکیومنت](http://localhost:8000/api/schema/swagger-ui/)
- 
- [پنل ادمین](http://localhost:8000/admin)
###### username : pooladpoor
###### password : 1234


