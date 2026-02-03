# YouTube API (FastAPI) – EC2 Deployment

本プロジェクトは **FastAPI + YouTube Data API** を使用して  
検索 API を提供するバックエンドアプリケーションです。

AWS EC2 上で **systemd による自動起動運用**を行い、  
Uvicorn（ポート **8001**）で公開しています。

---

## 🚀 Features

- FastAPI による軽量で高速な API
- YouTube Data API v3 を利用した動画検索
- systemd による自動起動・永続運用
- EC2（Amazon Linux 2023）での稼働
- /docs で Swagger UI が自動生成

---

## 📁 Directory Structure

```
project-root/
│── main.py
│── requirements.txt
│── services/
│     └── youtube_service.py
│── routes/
│     └── youtube.py
└── ...
```

---

## ⚙ Installation (EC2)

### 1. Python セットアップ

```bash
sudo yum update -y
sudo yum install python3 python3-pip -y
```

### 2. プロジェクトのクローン

```bash
git clone https://github.com/あなたのアカウント/your-youtube-api.git
cd your-youtube-api
```

### 3. 依存ライブラリのインストール

```bash
pip3 install -r requirements.txt
```

---

## ▶ 開発用ローカル起動（任意）

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8001
```

---

## 🛠 systemd による自動起動設定（EC2）

### 1. systemd サービスファイルの作成

```bash
sudo nano /etc/systemd/system/youtube-api.service
```

以下を貼り付ける（ポート8001）：

```ini
[Unit]
Description=YouTube API FastAPI Service
After=network.target

[Service]
User=ec2-user
WorkingDirectory=/home/ec2-user/your-youtube-api
ExecStart=/usr/bin/python3 -m uvicorn main:app --host 0.0.0.0 --port 8001
Restart=always

[Install]
WantedBy=multi-user.target
```

### 2. systemd リロード

```bash
sudo systemctl daemon-reload
```

### 3. サービス起動

```bash
sudo systemctl start youtube-api
```

### 4. 自動起動設定

```bash
sudo systemctl enable youtube-api
```

---

## 🔍 動作確認

### ● ステータス確認

```bash
sudo systemctl status youtube-api
```

`active (running)` ならOK。

### ● ブラウザで確認

```
http://<EC2パブリックIP>:8001/docs
```

### ● API 動作テスト

```bash
curl "http://<EC2パブリックIP>:8001/search?keyword=python"
```

---

## 📦 Deployment Flow

1. GitHubに push  
2. EC2 へ SSH  
3. リポジトリ pull  
4. systemd リスタート：
   ```bash
   sudo systemctl restart youtube-api
   ```
5. 動作確認（/docs）

---

## 📝 YouTube API キー設定（例）

`.env` を用いる場合：

```
YOUTUBE_API_KEY=xxxxxxxxxxxx
```

読み込み例：

```python
import os
from googleapiclient.discovery import build

api_key = os.getenv("YOUTUBE_API_KEY")
youtube = build("youtube", "v3", developerKey=api_key)
```

---

## 📄 License

This project is released under the MIT License.
