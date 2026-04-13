# 🚀 SwiftBite — Food Delivery Time Predictor
**React + Flask + ML + Google Maps**

---

## ⚙️ Setup & Run

### 1. Install Python dependencies
```bash
pip install -r requirements.txt
```

### 2. Add your Google Maps API Key
Open `templates/index.html` and find:
```
key=YOUR_GOOGLE_MAPS_API_KEY
```
Replace it with your actual key from https://console.cloud.google.com

Enable these APIs in Google Cloud Console:
- ✅ Maps JavaScript API
- ✅ Places API
- ✅ Directions API

### 3. Run Flask
```bash
python app.py
```
Visit → http://127.0.0.1:5000

---

## 📁 Structure
```
swiftbite/
├── app.py              ← Flask server + ML model (trains on startup)
├── requirements.txt
└── templates/
    └── index.html      ← Full React app (single page, home + predict)
```

---

## 🤖 ML Model
| | |
|---|---|
| Algorithm | Linear Regression (scikit-learn) |
| Features | Distance (km), Prep Time (min), Traffic (0/1/2) |
| Output | Delivery time in minutes |
| Training | 2000 synthetic records, auto-trained at startup |

## 🎨 Frontend
- **React 18** (via CDN Babel + UMD — no build step needed)
- **Poppins** font — same family used by Swiggy/Zomato
- Bright orange theme (#ff5a1f) matching food delivery apps
- Two views: Home Page + Predict Page (client-side routing)
- Google Maps with dark-food-themed style, click-to-pin, autocomplete
