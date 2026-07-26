import joblib
import numpy as np
import pandas as pd
import streamlit as st
import plotly.graph_objects as go
from datetime import datetime

# ----------------------------------------------------------------------------
# Page Configuration
# ----------------------------------------------------------------------------
st.set_page_config(
    page_title="Gold Price Predictor",
    page_icon="🪙",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ----------------------------------------------------------------------------
# Custom Styling
# ----------------------------------------------------------------------------
st.markdown(
    """
    <style>
    /* Overall app background */
    .stApp {
        background: linear-gradient(180deg, #0f1117 0%, #1a1c25 100%);
    }

    /* Headline */
    .gold-title {
        font-size: 2.6rem;
        font-weight: 800;
        background: linear-gradient(90deg, #FFD700, #FFA500);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0;
    }
    .gold-subtitle {
        color: #b5b5c0;
        font-size: 1.05rem;
        margin-top: 0.2rem;
    }

    /* Cards */
    .metric-card {
        background: rgba(255, 215, 0, 0.06);
        border: 1px solid rgba(255, 215, 0, 0.25);
        border-radius: 14px;
        padding: 1.2rem 1.4rem;
        text-align: center;
    }

    /* Buttons */
    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #FFD700, #FFA500);
        color: #111;
        font-weight: 700;
        font-size: 1.05rem;
        border: none;
        border-radius: 10px;
        padding: 0.7rem 0;
        transition: transform 0.15s ease, box-shadow 0.15s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 18px rgba(255, 215, 0, 0.35);
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: #14151c;
        border-right: 1px solid rgba(255,215,0,0.15);
    }

    hr {
        border-color: rgba(255,215,0,0.15);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------------
# Header
# ----------------------------------------------------------------------------
st.markdown('<div class="gold-title">🪙 Gold Price (GLD) Predictor</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="gold-subtitle">Estimate GLD ETF price from live market-style '
    "indicators using a trained Random Forest model.</div>",
    unsafe_allow_html=True,
)
st.markdown("---")

# ----------------------------------------------------------------------------
# Load Model
# ----------------------------------------------------------------------------
@st.cache_resource
def load_model():
    return joblib.load("gold_model.pkl")


model_loaded = True
try:
    model = load_model()
except Exception:
    model_loaded = False
    st.error(
        "⚠️ Model file `gold_model.pkl` not found in this directory. "
        "Train and save the model there to enable predictions — the "
        "interface below still works for exploring inputs."
    )

# ----------------------------------------------------------------------------
# Session state for prediction history
# ----------------------------------------------------------------------------
if "history" not in st.session_state:
    st.session_state.history = pd.DataFrame(
        columns=["Time", "SPX", "USO", "SLV", "EUR/USD", "Predicted GLD"]
    )

# ----------------------------------------------------------------------------
# Sidebar — presets & info
# ----------------------------------------------------------------------------
with st.sidebar:
    st.header("⚙️ Scenario Presets")
    st.caption("Jump-start the inputs with a market scenario, then fine-tune.")

    preset = st.radio(
        "Choose a preset",
        ["Custom", "2013 Baseline", "Bull Market (Risk-On)", "Crisis (Flight to Safety)"],
        index=0,
    )

    presets = {
        "2013 Baseline": dict(spx=1654.30, uso=31.84, slv=20.08, eur_usd=1.28),
        "Bull Market (Risk-On)": dict(spx=4200.00, uso=68.00, slv=24.50, eur_usd=1.10),
        "Crisis (Flight to Safety)": dict(spx=2300.00, uso=18.00, slv=14.00, eur_usd=1.05),
    }

    st.markdown("---")
    st.header("📈 Session Stats")
    if len(st.session_state.history) > 0:
        st.metric("Predictions made", len(st.session_state.history))
        st.metric(
            "Avg. predicted GLD",
            f"${st.session_state.history['Predicted GLD'].mean():.2f}",
        )
    else:
        st.caption("No predictions yet this session.")

    st.markdown("---")
    st.caption(
        "ℹ️ **About the model**: Random Forest Regressor trained on historical "
        "SPX, USO, SLV, and EUR/USD data to estimate GLD ETF price."
    )

# ----------------------------------------------------------------------------
# Tabs
# ----------------------------------------------------------------------------
tab_predict, tab_insights, tab_history = st.tabs(
    ["🚀 Predict", "🔍 Input Insights", "🗒️ History"]
)

# ----------------------------------------------------------------------------
# TAB 1 — Predict
# ----------------------------------------------------------------------------
with tab_predict:
    st.subheader("📊 Input Financial Indicators")

    defaults = presets.get(preset, dict(spx=1654.30, uso=31.84, slv=20.08, eur_usd=1.28))

    col1, col2 = st.columns(2)

    with col1:
        spx = st.slider(
            "SPX — S&P 500 Index",
            min_value=500.0,
            max_value=5000.0,
            value=float(defaults["spx"]),
            step=10.0,
            help="Standard & Poor's 500 stock market index",
        )
        uso = st.slider(
            "USO — United States Oil Fund",
            min_value=1.0,
            max_value=200.0,
            value=float(defaults["uso"]),
            step=1.0,
            help="United States Oil Fund ETF value",
        )

    with col2:
        slv = st.slider(
            "SLV — Silver Price ETF",
            min_value=1.0,
            max_value=100.0,
            value=float(defaults["slv"]),
            step=0.5,
            help="iShares Silver Trust ETF value",
        )
        eur_usd = st.slider(
            "EUR/USD — Exchange Rate",
            min_value=0.50,
            max_value=3.00,
            value=float(defaults["eur_usd"]),
            step=0.01,
            help="Euro to US Dollar exchange rate",
        )

    # Live snapshot of inputs as a small radar-ish bar chart
    st.markdown("###### Current input snapshot")
    snap_fig = go.Figure(
        go.Bar(
            x=["SPX", "USO", "SLV", "EUR/USD"],
            y=[spx, uso, slv, eur_usd],
            marker_color=["#4C9AFF", "#FF7A45", "#B0B0B0", "#36CFC9"],
            text=[f"{spx:.2f}", f"{uso:.2f}", f"{slv:.2f}", f"{eur_usd:.2f}"],
            textposition="outside",
        )
    )
    snap_fig.update_layout(
        height=260,
        margin=dict(t=10, b=10, l=10, r=10),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="#e0e0e0",
        yaxis_type="log",
        showlegend=False,
    )
    st.plotly_chart(snap_fig, use_container_width=True)

    st.markdown("---")

    predict_col, _ = st.columns([1, 2])
    with predict_col:
        run = st.button("🚀 Predict Gold Price", disabled=not model_loaded)

    if run:
        input_data = np.array([[spx, uso, slv, eur_usd]])
        prediction = model.predict(input_data)[0]

        # Rough uncertainty band using the forest's individual trees, if available
        lower, upper = prediction, prediction
        try:
            tree_preds = np.array(
                [t.predict(input_data)[0] for t in model.estimators_]
            )
            lower, upper = np.percentile(tree_preds, [10, 90])
        except Exception:
            pass

        st.balloons()

        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown(
                f'<div class="metric-card"><h3>💰</h3>'
                f"<div style='font-size:1.6rem;font-weight:700;color:#FFD700;'>"
                f"${prediction:.2f}</div><div style='color:#b5b5c0;'>Predicted GLD</div></div>",
                unsafe_allow_html=True,
            )
        with c2:
            st.markdown(
                f'<div class="metric-card"><h3>📉</h3>'
                f"<div style='font-size:1.6rem;font-weight:700;'>${lower:.2f}</div>"
                f"<div style='color:#b5b5c0;'>Low estimate (10th pct.)</div></div>",
                unsafe_allow_html=True,
            )
        with c3:
            st.markdown(
                f'<div class="metric-card"><h3>📈</h3>'
                f"<div style='font-size:1.6rem;font-weight:700;'>${upper:.2f}</div>"
                f"<div style='color:#b5b5c0;'>High estimate (90th pct.)</div></div>",
                unsafe_allow_html=True,
            )

        st.markdown("")
        gauge_fig = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=prediction,
                number={"prefix": "$", "valueformat": ".2f"},
                gauge={
                    "axis": {"range": [max(0, lower - 10), upper + 10]},
                    "bar": {"color": "#FFD700"},
                    "steps": [
                        {"range": [lower, upper], "color": "rgba(255,215,0,0.15)"}
                    ],
                },
                title={"text": "Predicted GLD Price"},
            )
        )
        gauge_fig.update_layout(
            height=280,
            margin=dict(t=40, b=10, l=30, r=30),
            paper_bgcolor="rgba(0,0,0,0)",
            font_color="#e0e0e0",
        )
        st.plotly_chart(gauge_fig, use_container_width=True)

        st.info(
            "Note: The model is a Random Forest Regressor. The low/high band comes "
            "from the spread across individual trees in the forest, not a formal "
            "confidence interval."
        )

        # Log to history
        new_row = pd.DataFrame(
            [
                {
                    "Time": datetime.now().strftime("%H:%M:%S"),
                    "SPX": spx,
                    "USO": uso,
                    "SLV": slv,
                    "EUR/USD": eur_usd,
                    "Predicted GLD": round(float(prediction), 2),
                }
            ]
        )
        st.session_state.history = pd.concat(
            [st.session_state.history, new_row], ignore_index=True
        )

# ----------------------------------------------------------------------------
# TAB 2 — Input Insights
# ----------------------------------------------------------------------------
with tab_insights:
    st.subheader("🔍 How each input compares to its typical range")

    ranges = {
        "SPX": (500.0, 5000.0, spx),
        "USO": (1.0, 200.0, uso),
        "SLV": (1.0, 100.0, slv),
        "EUR/USD": (0.50, 3.00, eur_usd),
    }

    for name, (lo, hi, val) in ranges.items():
        pct = (val - lo) / (hi - lo) * 100
        st.write(f"**{name}**  ·  current: `{val:.2f}`  ·  range: `{lo}–{hi}`")
        st.progress(min(max(pct / 100, 0.0), 1.0))

    st.markdown("---")
    st.subheader("🌳 Feature importance")
    if model_loaded:
        try:
            importances = model.feature_importances_
            feat_names = ["SPX", "USO", "SLV", "EUR/USD"]
            imp_fig = go.Figure(
                go.Bar(
                    x=importances,
                    y=feat_names,
                    orientation="h",
                    marker_color="#FFD700",
                )
            )
            imp_fig.update_layout(
                height=300,
                margin=dict(t=10, b=10, l=10, r=10),
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                font_color="#e0e0e0",
                xaxis_title="Relative importance",
            )
            st.plotly_chart(imp_fig, use_container_width=True)
        except Exception:
            st.caption("Feature importance isn't available for this model type.")
    else:
        st.caption("Load a model to see feature importance.")

# ----------------------------------------------------------------------------
# TAB 3 — History
# ----------------------------------------------------------------------------
with tab_history:
    st.subheader("🗒️ Prediction history (this session)")

    if len(st.session_state.history) == 0:
        st.caption("Run a prediction to start building your session history.")
    else:
        st.dataframe(st.session_state.history, use_container_width=True)

        trend_fig = go.Figure(
            go.Scatter(
                x=st.session_state.history["Time"],
                y=st.session_state.history["Predicted GLD"],
                mode="lines+markers",
                line=dict(color="#FFD700", width=3),
                marker=dict(size=8),
            )
        )
        trend_fig.update_layout(
            height=320,
            margin=dict(t=20, b=10, l=10, r=10),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font_color="#e0e0e0",
            yaxis_title="Predicted GLD ($)",
            xaxis_title="Time",
        )
        st.plotly_chart(trend_fig, use_container_width=True)

        csv = st.session_state.history.to_csv(index=False).encode("utf-8")
        st.download_button(
            "⬇️ Download history as CSV",
            data=csv,
            file_name="gld_prediction_history.csv",
            mime="text/csv",
        )

        if st.button("🗑️ Clear history"):
            st.session_state.history = st.session_state.history.iloc[0:0]
            st.rerun()
