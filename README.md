# Docker 사용법 여행기

---

## 목차

- [Docker 사용법 여행기](#docker-사용법-여행기)
  - [목차](#목차)
  - [Command](#command)
  - [Entrypoint와 Command](#entrypoint와-command)

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
