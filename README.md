这是一个基于 [django](https://github.com/django/django) 的典型cms系统模板项目，目标是可以快速创建一个基于 web 的内容管理系统。

## 主要特点

- 集成了现代化界面 [django-simpleui](https://github.com/newpanjing/simpleui) 来替换原本django原本的ui
- 将url进行了刻意复杂化处理，防止搜索引擎或者黑客工具进行路由扫描
- 集成了简单的 celery 定时&异步任务

## 使用方法

**注意: 所有用法都基于django生态，详细用法请阅读官方文档: [[django 管理站点]](https://docs.djangoproject.com/zh-hans/4.1/ref/contrib/admin/)**

### 1、基于模板增加新的内容管理模块

```shell
git clone https://github.com/jeyrce/cms.git

cd cms

pip install -r requirements.txt

django-admin startapp <your app>
```

### 2、增加 ORM 模型

```shell
cd <your app>

vim model.py

django-admin makemigrations
```

### 3、增加定时&异步任务

```shell
cd jobs

vim <your job>.py

# --- 
from celery import shared_task

@shared_task
def your_logic(*args, **kwargs):
    ...
```

### 4、构建&启动

```shell
make build image=<镜像名字>

# 提前准备好需要使用的 cache 和 db 组件（默认用redis + mariadb）

docker run -it --rm django-admin migrate

docker run -it --rm --name cms <镜像名字> 
```

### 5、访问后台

```shell
docker exec -it <容器id> python manage.py createsuperuser

open http://127.0.0.1:8000/
```
