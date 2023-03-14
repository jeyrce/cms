buildAt:=$(shell date "+%Y-%m-%d/%H:%M:%S")
commitId:=$(shell git rev-parse --short HEAD)
branch:=$(shell git symbolic-ref --short -q HEAD)
image := jeyrce/cms:latest

.PHONY: all
all: build

.PHONY: server
server:
	@echo "运行web服务"
	python manage.py runserver --insecure --no-color 127.0.0.1:8000

.PHONY: celery
celery:
	@echo "运行celery任务引擎"
	celery -A jobs worker --loglevel=info --concurrency=4

.PHONY: build
build:
	@echo "构建docker镜像"
	-docker buildx rm cms
	-docker buildx create --name cms --bootstrap --use
	docker buildx build -t ${image} \
		--build-arg branch=${branch} \
		--build-arg commitId=${commitId} \
		--build-arg buildAt=${buildAt} \
		--platform linux/386,linux/amd64,linux/arm64 \
		--pull \
		--push \
		.
	-docker buildx rm cms

