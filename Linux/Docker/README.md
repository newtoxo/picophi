# Docker
Docker for Linux

## 目錄
- [系統環境](#系統環境)
- [安裝](#安裝)
- [更新](#更新)
- [卸載](#卸載)
- [Dockerfile](Dockerfile)
- [指令](#指令)
- [備註](#備註)

## 系統環境
- VM Server
    - Ubuntu 22.04.3 LTS

## 安裝
移除衝突套件
```bash
for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt-get remove $pkg; done
```
設定 Docker 套件
```bash
sudo apt update
```
```bash
sudo apt install ca-certificates curl gnupg
```
```bash
sudo install -m 0755 -d /etc/apt/keyrings
```
```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
```
```bash
sudo chmod a+r /etc/apt/keyrings/docker.gpg
```
```bash
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```
```bash
sudo apt update
```
```bash
sudo apt clean
```
安裝 Docker 最新版本
```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

## 更新
更新至 Docker 最新版本
```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```
更新至 Docker 特定版本
- 列出可用版本
    ```bash
    apt-cache madison docker-ce | awk '{ print $3 }'
    ```
- 安裝指定版本（ex: 5:24.0.7-1~ubuntu.22.04~jammy）
    ```bash
    VERSION_STRING=5:24.0.7-1~ubuntu.22.04~jammy
    sudo apt-get install docker-ce=$VERSION_STRING docker-ce-cli=$VERSION_STRING containerd.io docker-buildx-plugin docker-compose-plugin
    ```

## 卸載
卸載 Docker 套件
```bash
sudo apt purge docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin docker-ce-rootless-extras
```
刪除所有 image
```bash
sudo rm -rf /var/lib/docker
```
刪除所有 container
```bash
sudo rm -rf /var/lib/containerd
```

## 指令
- build Dockerfile
    ```bash
    sudo docker build -t <image-name> .
    ```
- 運行 image
    ```bash
    sudo docker run <image-name>
    ```
- 查看所有 image
    ```bash
    sudo docker images -a
    ```
- 刪除 image
    ```bash
    sudo docker rmi <image-id>
    ```
- 查看所有 container
    ```bash
    sudo docker ps -a
    ```
- 刪除 container
    ```bash
    sudo docker rm <container-id>
    ```

## 備註