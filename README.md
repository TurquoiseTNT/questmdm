# QuestMDM

Self-hosted Flask-based ADB MDM controller for Meta Quest devices. Automatically detects USB-connected headsets, enables wireless ADB, and notifies users upon success.

## Features
- Automatic ADB over TCP setup
- Web UI with device listing
- Custom notification broadcast
- Fallback Wi-Fi assist

## Setup
```bash
git clone https://github.com/turquoisetnt/questmdm.git
cd questmdm
pip install -r requirements.txt
bash scripts/auto_pair.sh &
python3 main.py
```

Visit `http://localhost:8080/` to see devices.

---

Let me know if you want this pushed to GitHub directly or need packaging as a `.deb` or Docker container.
