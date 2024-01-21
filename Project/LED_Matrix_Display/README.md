# LED_Matrix_Display
支援控制 LED 燈條，以及在 16 x 16 的 LED 矩陣上顯示文字或圖片。

## 目錄
- [系統環境](#系統環境)
- [系統設定](#系統設定)
- [範例](#範例)
- [備註](#備註)

## 系統環境
- Raspberry Pi 3 Model B+
    - Ubuntu 22.04.3 LTS
    - Python 3.10.12

- WS2812B
    - 16 x 16 矩陣 LED

## 系統設定
- ### 修改網路參數
    查看網路資訊
    ```bash
    ip address
    ```
    編輯網路參數
    ```bash
    sudo nano /etc/netplan/50-cloud-init.yaml
    ```
    [參數範例](#50-cloud-inityaml參數)

- ### 安裝 SSH Server
    安裝 SSH
    ```bash
    sudo apt install openssh-server
    ```
    啟動 SSH
    ```bash
    sudo /etc/init.d/ssh start
    ```

- ### 更新系統套件
    檢查套件
    ```bash
    sudo apt update
    ```
    更新套件
    ```bash
    sudo apt upgrade
    ```
    清除套件安裝包
    ```bash
    sudo apt clean
    ```

- ### 移除 Cloud-init
    移除 Cloud-init
    ```bash
    sudo apt purge cloud-init -y
    ```
    刪除殘留檔案
    ```bash
    sudo rm -rf /etc/cloud && sudo rm -rf /var/lib/cloud/
    ```
    重啟系統
    ```bash
    sudo reboot
    ```

- ### 設定虛擬記憶體
    查看記憶體資訊
    ```bash
    free -h
    ```
    新建 4096Mb 虛擬記憶體
    ```bash
    sudo fallocate -l 4096M /swapfile
    ```
    設定虛擬記憶體權限
    ```bash
    sudo chmod 600 /swapfile
    ```
    設定虛擬記憶體
    ```bash
    sudo mkswap /swapfile
    ```
    啟動虛擬記憶體
    ```bash
    sudo swapon /swapfile
    ```
    開機自動啟動虛擬記憶體
    ```bash
    echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
    ```
    重啟系統
    ```bash
    sudo reboot
    ```

- ### 安裝系統套件
    安裝必要套件
    ```bash
    sudo apt install python3-pip python3.10-venv raspi-config cmake libjpeg-dev zlib1g-dev
    ```
    清除套件安裝包
    ```bash
    sudo apt clean
    ```
    
- ### 建立虛擬環境
    新建虛擬環境
    ```bash
    python3 -m venv .venv    
    ```
    [虛擬環境使用方式](#虛擬環境)

- ### 安裝 Python 模組
    套件清單：[requirement.txt](requirement.txt)
    
    更新 PIP
    ```bash
    pip install --upgrade pip setuptools wheel
    ```
    安裝必要模組
    ```bash
    python3 -m pip install --force-reinstall adafruit-blinka
    ```
    ```bash
    pip install -r requirement.txt
    ```
    清除模組安裝包
    ```bash
    pip cache purge
    ```

## 範例
### 自製模組
- [WS2812B 控制](ws2812b.py)
- [點陣化](pixelation.py)

### 主程式
- [Demo](demo.py)

### 字型
- [思源黑體](NotoSansTC.ttf)

### 圖片
- [圖一](img_0.png)
- [圖二](img_1.png)
- [圖三](img_2.png)


## 備註
- ### 虛擬環境
    進入虛擬環境
    ```bash
    source .venv/bin/activate
    ```
    退出虛擬環境
    ```bash
    deactivate
    ```

- ### 50-cloud-init.yaml參數
    預設：
    ```yaml
    # This file is generated from information provided by the datasource.  Changes
    # to it will not persist across an instance reboot.  To disable cloud-init's
    # network configuration capabilities, write a file
    # /etc/cloud/cloud.cfg.d/99-disable-network-config.cfg with the following:
    # network: {config: disabled}
    network:
        ethernets:
            eth0:
                dhcp4: true
                optional: true
        version: 2
    ```
    修改後：
    ```yaml
    # This file is generated from information provided by the datasource.  Changes
    # to it will not persist across an instance reboot.  To disable cloud-init's
    # network configuration capabilities, write a file
    # /etc/cloud/cloud.cfg.d/99-disable-network-config.cfg with the following:
    # network: {config: disabled}
    network:
        ethernets:
            eth0:
                addresses: [192.168.12.34/24]
                gateway4: 192.168.12.1
                nameservers:
                    addresses: [8.8.8.8,8.8.4.4]
                dhcp4: false
        version: 2
    ```
    
