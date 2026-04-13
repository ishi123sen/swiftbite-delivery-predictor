# 🚀 SwiftBite — Food Delivery Time Predictor
React + Flask + ML + Google Maps

---

## ⚙️ Setup & Run

### 1. Install Python dependencies
pip install -r requirements.txt

### 2. Add your Google Maps API Key
Open templates/index.html and find:
key=YOUR_GOOGLE_MAPS_API_KEY

Replace it with your actual key from Google Cloud Console

Enable these APIs:
- Maps JavaScript API
- Places API
- Directions API

### 3. Run Flask
python app.py

Visit:
http://127.0.0.1:5000

---

## 📁 Structure

swiftbite/
├── app.py
├── requirements.txt
└── templates/
    └── index.html

---

## 🤖 ML Model

- Algorithm: Linear Regression (scikit-learn)
- Features: Distance, Prep Time, Traffic
- Output: Delivery time in minutes
- Training: 2000 synthetic records

---

## 🎨 Frontend

- React (CDN)
- Google Maps API
- Clean UI like Swiggy
- Real-time distance calculation