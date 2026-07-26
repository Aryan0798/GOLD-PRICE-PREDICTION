<div align="center">

# 🪙 Gold Price (GLD) Predictor

### Predict the price of gold from the pulse of the market

*A dark, gold-themed Streamlit app that turns four market signals into a live GLD price estimate.*

![Python](https://img.shields.io/badge/Python-3.9%2B-FFD700?style=flat-square&logo=python&logoColor=black)
![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-FF4B4B?style=flat-square&logo=streamlit)
![Model](https://img.shields.io/badge/Model-Random%20Forest-orange?style=flat-square)
![Status](https://img.shields.io/badge/Status-Ready%20to%20Run-brightgreen?style=flat-square)

</div>

---

## ✨ Why this app is fun to use

Gold doesn't move on its own — it reacts to stocks, oil, silver, and the
dollar. This app lets you **play market strategist**: drag a few sliders to
simulate a scenario, hit predict, and watch the model translate those
signals into a gold price, live, with an uncertainty band and a gauge that
reacts in real time.

| 🎛️ | 📊 | 🔮 | 🗒️ |
|---|---|---|---|
| **Slider-driven inputs** — feel the market move as you drag | **Live snapshot chart** — see your inputs before you even predict | **Gauge + confidence band** — not just a number, a range | **Session history** — every guess logged, charted, and exportable |

---

## 🚀 Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Make sure gold_model.pkl sits next to APP.py

# 3. Launch
streamlit run APP.py
```

Then open **http://localhost:8501** — it should launch automatically.

---

## 🧭 Tour of the app

### 1. ⚙️ Scenario Presets *(sidebar)*
Don't want to guess numbers from scratch? Pick a mood for the market:

| Preset | Vibe |
|---|---|
| 📅 **2013 Baseline** | The historical reference point the model was trained around |
| 🐂 **Bull Market (Risk-On)** | Stocks soaring, oil strong, dollar confident |
| 🛡️ **Crisis (Flight to Safety)** | Stocks falling, investors running to safe havens |

### 2. 🚀 Predict tab
Drag the four sliders — **SPX**, **USO**, **SLV**, **EUR/USD** — and watch a
live bar chart of your inputs update instantly. Hit **Predict Gold Price**
and get:

- 💰 a headline prediction
- 📉📈 a low/high range (10th–90th percentile across the forest's trees)
- 🌡️ a gauge chart showing where your prediction lands

### 3. 🔍 Input Insights tab
See exactly how "extreme" your inputs are relative to their typical range,
and which indicator the model actually leans on most (feature importance).

### 4. 🗒️ History tab
Every prediction you make is logged with a timestamp. Watch your own trend
line form as you experiment, then **download the whole session as CSV**.

---

## 🧩 Under the hood

```
Inputs (SPX, USO, SLV, EUR/USD)
        │
        ▼
  Random Forest Regressor  ──▶  Predicted GLD price
        │
        ▼
  Spread across all trees  ──▶  Low / High uncertainty band
```

The model is a **scikit-learn `RandomForestRegressor`**, saved as
`gold_model.pkl` and loaded with `joblib`. Because a random forest is really
a committee of decision trees, the app peeks at what each individual tree
predicts to build a rough confidence range — a nice free bonus of the
algorithm.

---

## 📦 Requirements

```
streamlit
numpy
pandas
joblib
plotly
scikit-learn
```

```bash
pip install -r requirements.txt
```

Requires **Python 3.9+**.

---

## 🧠 Training your own model

Don't have `gold_model.pkl` yet? Here's the shape it expects:

```python
import joblib
from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)   # columns: SPX, USO, SLV, EUR/USD

joblib.dump(model, "gold_model.pkl")
```

Drop the resulting `.pkl` next to `APP.py` and you're live. No model yet?
The app still opens — you can explore the inputs — it just keeps the
**Predict** button politely disabled until it has something to predict with.

---

## 📊 Input cheat sheet

| Indicator | What it is | Typical range |
|---|---|---|
| 📈 **SPX** | S&P 500 Index | 500 – 5,000 |
| 🛢️ **USO** | United States Oil Fund ETF | 1 – 200 |
| 🥈 **SLV** | iShares Silver Trust ETF | 1 – 100 |
| 💱 **EUR/USD** | Euro → US Dollar rate | 0.50 – 3.00 |

---

## ⚠️ A few honest caveats

- The low/high band is the **spread across the forest's trees**, not a
  formal statistical confidence interval — treat it as a rough sense of
  agreement, not a guarantee.
- **History is session-only** — it resets when the app restarts or the
  browser tab closes. Download it as CSV if you want to keep it.
- This is a modeling demo, not financial advice — real gold prices depend
  on far more than four numbers.

---

<div align="center">

Made for exploring how market signals connect to gold — drag some sliders and see what happens. 🪙

</div>
