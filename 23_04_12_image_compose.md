# 2일차

## 목차

- [2일차](#2일차)
  - [목차](#목차)
  - [images](#images)
  - [실습](#실습)
    - [tensorflow](#tensorflow)
    - [miniconda3](#miniconda3)
    - [jupyter notebook](#jupyter-notebook)
  - [Dockerfile 상세](#dockerfile-상세)
  - [연습](#연습)
    - [python](#python)
  - [docker-compose](#docker-compose)

```bash
docker logs my-nginx
docker logs --tail 5 my-nginx
docker logs -f my-nginx
docker logs -f -t my-nginx
```

- docker logs 확인

---

## images

```bash
docker image inspect nginx
```

docker의 이미지의 상세 내역을 확인할 수 있음

```bash
docker run -it --name my-ubuntu ubuntu

echo hello ubuntu > my_file

exit

docker start my-ubuntu 

docker commit -a byeongryul -m "add my_file" my-ubuntu my-ubuntu:v1.0.0
```

- images 만들기

```Dockerfile
FROM ubuntu:20.04
RUN apt-get update
CMD ["echo", "Hello Ubuntu"]
```

```bash
docker build -t my-app:v1 .
```

- 위 Docker 파일을 토대로 image를 생성함

```bash
touch .dockerignore

*/tmep*
*/*/temp*
temp?
*.md
!README.md
```

- 올리지 않을 요소를 지정할 수 있음

```bash
docker save -o my-ubuntu.tar  my-ubuntu
docker load -i my-ubuntu.tar
```

도커 공유와 삭제

---

## 실습

### tensorflow

1. pull 이미지 가져오기
2. run 컨테이너 실행
3. 컨테이너 접속 후 python 실행
4. 디바이스 목록 확인

```bash
docker pull tensorflow/tensorflow
docker run --name my-tensorflow2 tensorflow/tensorflow
docker run --name my-tensorflow -it tensorflow/tensorflow bash   

python3
from tensorflow.python.client import device_lib
device_lib.list_local_devices()
```

### miniconda3

1. pull
2. run
3. 활성 유무
4. pandas와 numpy 버전 확인

```bash
docker pull continuumio/miniconda3
docker run --name my-conda -it continuumio/miniconda3 bash

conda install pandas -y
conda list | grep -E "pandas|numpy"
```

### jupyter notebook

1. 앞선 컨테이너에 jupyter 설치

```bash
docker run --name my-conda-port -p 8888:8888 -it continuumio/miniconda3 bash

conda install pandas jupyter -y
jupyter notebook --allow-root --no-browser --ip 0.0.0.0
```

## Dockerfile 상세

```dockerfile
FROM
LABEL maintainer="128592asp@gmail.com"
LABEL version="1.0.0"
LABEL description="연습"
RUN mkdir container
COPY ./local ./container
CMD ["echo", "ubuntu"]
# 명시적 약속
EXPOSE 8080 
# 환경 설정
ENV PATH=.
```

---

## 연습

### python

1. dockerfile 만들기
2. python 베이스로 빌드하기

---

## docker-compose

- 프로그램을 전체가 관리할 수 있도록 함

```bash
docker-compose up -d --scale web=3
```
