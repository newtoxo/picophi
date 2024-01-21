# Docker
Docker for Linux

## 目錄
- [系統環境](#系統環境)
- [Docker 安裝](#docker-安裝)
- [環境設定](#環境設定)
- [備註](#備註)

## 系統環境
- VM Server
    - Ubuntu 22.04.3 LTS

## Docker 安裝
[詳細教學](/picophi/Linux/Docker/README.md)

## 環境設定
- ### VM 環境
    安裝 SteamCMD
    ```bash
    sudo docker run -itd --network=host --name=PalworldServer cm2network/steamcmd bash
    ```
    進入 SteamCMD 的 Container
    ```bash
    sudo docker exec -it <"container_id"> bash
    ```
- ### Container 環境
    執行 SteamCMD
    ```bash
    ./steamcmd.sh
    ```
- ### SteamCMD 環境
    匿名登入 SteamCMD：
    ```bash
    login anonymous
    ```
    下載 Palworld Server：
    ```bash
    app_update 2394010 validate
    ```
    下載完成後退出 SteamCMD：
    ```bash
    quit
    ```
- ### Container 環境
    啟動 Server
    ```bash
    ~/Steam/steamapps/common/PalServer/PalServer.sh
    ```

## 備註
- ### 停止 Server
    停止 Container
    ```bash
    sudo docker stop <"container_id">
    ```
- ### 重新啟動 Server
    啟動 Container
    ```bash
    sudo docker start <"container_id">
    ```
    進入 SteamCMD 的 Container
    ```bash
    sudo docker exec -it <"container_id"> bash
    ```
    啟動 Server
    ```bash
    ~/Steam/steamapps/common/PalServer/PalServer.sh
    ```
- ### 重新命名 Container
    ```bash
    sudo docker rename <"old_name"> <"new_name">
    ```
