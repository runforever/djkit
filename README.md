# Django Starter Kit

## description
初始化 Django，Django REST framework 项目

## include
1. [Django](https://www.djangoproject.com) 1.10.4
2. [Django REST framework](http://www.django-rest-framework.org) 3.5.3 提供 restful 风格接口
3. [JWT](https://github.com/GetBlimp/django-rest-framework-jwt) 接口认证
4. [django cors header](https://github.com/ottoyiu/django-cors-headers) 浏览器跨域支持
5. [Raven](https://github.com/getsentry/raven-python) Sentry Client 异常提示
6. [psycopg2](https://github.com/getsentry/raven-python) PostgreSQL 客户端

## 目录结构说明
```
story
|── .gitignore      # Python gitignore
|── .venv           # virtualenv
├── manage.py
├── requirements
│   ├── base.txt
│   ├── dev.txt
│   └── prod.txt
└── story
├── __init__.py
├── admin.py       # 自动加载所有 models 到 django admin
├── migrations
│   └── __init__.py
├── models         # 所有 models 统一放到这个文件夹管理
│   └── __init__.py
├── settings       # 生产环境和开发环境 settings 做隔离
│   ├── __init__.py
│   ├── local_settings.py.tpl
│   └── settings.py
├── urls.py
    └── wsgi.py
```

## usage
```pip install git+https://github.com/BurnishTechCN/djkit.git```

`djkit init your-project-name`

## License
![wtfpl](http://www.wtfpl.net/wp-content/uploads/2012/12/wtfpl-badge-1.png)
