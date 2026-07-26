# 🪙 Gold Price (GLD) Predictor

An interactive Streamlit app that estimates the price of the GLD ETF (gold)
from four market indicators — SPX, USO, SLV, and EUR/USD — using a trained
Random Forest Regressor.

## Features

- **Dark, gold-themed UI** with styled metric cards and a custom sidebar
- **Slider-based inputs** for SPX, USO, SLV, and EUR/USD
- **Scenario presets** — 2013 Baseline, Bull Market, Crisis — to quickly load
  realistic input combinations
- **Live input snapshot chart** that updates as you move the sliders
- **Prediction with uncertainty band** (10th–90th percentile across the
  forest's individual trees) plus a gauge chart
- **Input Insights tab** — see where each input sits in its typical range,
  and view model feature importance
- **History tab** — every prediction made in the session is logged, plotted
  as a trend line, and downloadable as a CSV

## Requirements

- Python 3.9+
- A trained model file named `gold_model.pkl` (a scikit-learn
  `RandomForestRegressor`) in the same directory as `APP.py`

Install dependencies:

```bash
pip install streamlit numpy pandas joblib plotly scikit-learn
```

Or, with a `requirements.txt`:

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

## Running the app

```bash
streamlit run APP.py
```

Streamlit will open the app in your browser (default:
`http://localhost:8501`).

## Model file

The app expects `gold_model.pkl` — a pickled scikit-learn model saved with
`joblib.dump()` — to sit in the same folder as `APP.py`. Example of how such
a model might be trained and saved:

```python
import joblib
from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)  # X_train columns: SPX, USO, SLV, EUR/USD

joblib.dump(model, "gold_model.pkl")
```

If `gold_model.pkl` is missing, the app still loads so you can explore the
inputs, but the **Predict** button stays disabled and a warning is shown.

## Inputs

| Indicator | Description                          | Typical range |
|-----------|---------------------------------------|----------------|
| SPX       | S&P 500 Index                         | 500 – 5000     |
| USO       | United States Oil Fund ETF value      | 1 – 200        |
| SLV       | iShares Silver Trust ETF value        | 1 – 100        |
| EUR/USD   | Euro to US Dollar exchange rate       | 0.50 – 3.00    |

## Notes

- The low/high band shown after a prediction comes from the spread of
  predictions across the individual trees in the Random Forest — it is a
  rough uncertainty estimate, not a formal statistical confidence interval.
- Prediction history is stored only for the current browser session (it
  resets when the app restarts or the session ends).
