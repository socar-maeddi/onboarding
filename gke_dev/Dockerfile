# 과제1과 동일한 파이썬 버전 이미지 사용
FROM python:3.8.10

# 메타데이터 설정
LABEL owner="Maeddi"

# Working Directory 설정
WORKDIR /app/

# app 관련 파이썬 파일 복사
COPY ./fastapi_apps/main.py /app/
COPY ./fastapi_apps/app.py /app/

# 필요 모듈 설치
COPY ./fastapi_apps/requirements.txt /app/
RUN pip install -r requirements.txt

# 포트 설정
EXPOSE 8000

CMD ["python3", "main.py"]