# Docker 사용법 여행기

---

## 목차

- [Docker 사용법 여행기](#docker-사용법-여행기)
  - [목차](#목차)
  - [Command](#command)
  - [Entrypoint와 Command](#entrypoint와-command)
  - [volume](#volume)
    - [Host volume](#host-volume)
    - [Volume Container](#volume-container)
    - [Docker volume](#docker-volume)

## Command

```bash
docker pull nginx:1.21
```

- docker의 images를 다운받는다.

```bash
docker images
```

- docker images 확인

```bash
docker run nginx:1.21
```

- images를 통해 실행함

```bash
docker run \
    -i \
    -t \
    --rm \
    -d \
    --name hello \
    -p 80:80 \
    -v /opt/example:/exmaple \
```

- 추가적인 요소를 넣어서 돌릴 수 있음
  - 표준 입력
  - TTY
  - 실행 종료 후 삭제
  - 백그라운드 모드
  - 이름 지정
  - 포트 바인딩
  - 볼륨 바인딩
  - 실행 이미지
  - 실행 명령어

```bash
docker ps
docker ps -a
```

- 실행 중인 container 확인

```bash
dock stop [컨테이너 이름]
```

- 컨테이너 종료

```bash
docker inspect [컨테이너 이름]
```

- 상세한 정보를 확인할 수 있음

```bash
docker pause [컨테이너 이름]
docker unpause [컨테이너 이름]
```

- 리소스 제공을 중지하거나 재개함

```bash
docker kill [컨테이너 이름]
```

- 컨테이너 강제 종료

```bash
docker rm -f [컨테이너 이름]
```

- 컨테이너 삭제

```bash
docker container prune
```

- 실행 중인 컨테이너를 제외한 모든 컨테이너 삭제

## Entrypoint와 Command

- 고정적으로 지정된 명령어 수행

```bash
docker run --entrypoint sh ubuntu
docker run --entrypoint echo ubuntu hello
```

- entrypoint를 통해 command가 실행된 후 중지 됨

```bash
docker run -help
```

```bash
docker run -it -e MY_HOST=1.1.1.1 ubuntu bash
exit
```

- `docker run` 함
- `it` 요소로 들어감
- `e` 환경 변수로 호스트를 넘김
- `ubuntu` 우분투로
- `bash` bash 실행

```bash
nano sample.env
cat sample.env
```

- sample.env 내부에는 `MY_HOST=1.1.1.1` 작성

```bash
docker run -it --env-file sample.env ubuntu env  
```

- 환경요소를 사용할 수 있음

```bash
docker run -d --name my-nginx -p 80:80 nginx
docker exec -it my-nginx bash
docker exec -it my-nginx env
```

- exec를 통해 명령어를 실행함

```bash
docker run --expose 80 nginx
```

- port를 사용하겠다는 선언만 함

---

## volume

- container와 상관없이 저장되어야 하는 파일을 보관하기 위한 기법

### Host volume

```bash
docker run -d -it -p 8080:80 --name my-nginx nginx:1.23

docker run -d -it -p 8080:80 -v ${pwd}/html:/usr/share/nginx/html --name my-nginx nginx:1.23

docker run -d -it -p 8080:80 -v /home/user/docker/html:/usr/share/nginx/html --name my-nginx2 nginx:1.23
```

### Volume Container

```bash
docker run -d --name my-volume -it -v /home/user/docker/html:/usr/share/nginx/html ubuntu

docker run -d -p 8090:80 --name my-nginx2 --volumes-from=my-volume nginx
```

### Docker volume

```bash
docker volume ls

docker volume create --name test-db

docker run -d --name my-sql -v test-db:/var/lib/mysql -p 3307:3306 mysql:5.7

docker run -d --name my-sql -v test-db:/var/lib/mysql -p 3307:3306 --platform linux/amd64 mysql:5.7

docker run -d --name my-sql -v test-db:/var/lib/mysql -p 3307:3306 --platform linux/amd64 -e MYSQL_ROOT_PASSWORD=1234 mysql:5.7

docker volume rm [볼륨 이름]
```
