FROM python:3.11.2-slim AS runner

WORKDIR "/cms/"

ARG branch
ARG commitId
ARG buildAt

LABEL poweredBy="https://github.com/jeyrce/cms" \
	author="Jeyrce.Lu<jeyrce@gmail.com>" \
	branch="${branch}" \
	commitId="${commitId}" \
	buildAt="${buildAt}"

ENV CMS_DB_NAME="cmdb" \
	CMS_DB_USERNAME="cms" \
	CMS_DB_PASSWORD="cms" \
	CMS_DB_HOST="mysql" \
	CMS_DB_PORT="3306" \
	CMS_CACHE_CONN="redis://:redis@redis:6379/7" \
	CMS_CELERY_BROKER_URL="redis://:redis@redis:6379/8" \
	C_FORCE_ROOT=1 \
	CMS_LISTEN_ADDR="0.0.0.0:8000"

COPY . .

RUN /usr/local/bin/python -m pip install --upgrade pip && \
    pip install -r requirements.txt \
    -i http://mirrors.cloud.tencent.com/pypi/simple  \
    --trusted-host mirrors.cloud.tencent.com \
    --no-cache-dir && \
    python manage.py collectstatic


# web
CMD ["sh", "-c", "python manage.py runserver --insecure --no-color $CMS_LISTEN_ADDR"]

# celery
# CMD ["sh", "-c", "celery -A jobs worker --loglevel=info --concurrency=4"]
