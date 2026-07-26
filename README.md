# 🏅 Olympic Games Data Analysis Web Application

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.x-FF4B4B.svg)](https://streamlit.io/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458.svg)](https://pandas.pydata.org/)
[![Plotly](https://img.shields.io/badge/Plotly-Interactive%20Charts-3F4F75.svg)](https://plotly.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An interactive, end-to-end Exploratory Data Analysis (EDA) web application built with **Python**, **Pandas**, and **Streamlit**. This dashboard analyzes 120+ years of Olympic history (from Athens 1896 to Rio 2016), visualizing medal tallies, athlete demographics, country performances, and sport-specific trends.

---

## 📋 Table of Contents
- [Overview](#-overview)
- [Key Features](#-key-features)
- [Project Architecture & File Structure](#-project-architecture--file-structure)
- [Dataset Details](#-dataset-details)
- [Installation & Local Setup](#-installation--local-setup)
- [How to Run](#-how-to-run)
- [Deployment Guide](#-deployment-guide)
- [Technologies Used](#-technologies-used)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 Overview

Understanding historical trends across 120 years of Olympic Games requires interactive exploration rather than static summaries. This application processes modern Olympic data, cleaning and pre-processing raw records to deliver actionable interactive visual analytics across four primary dimensions:

1. **Overall Medal Tally Analysis**
2. **Global & Historical Trends**
3. **Country-Specific Deep Dives**
4. **Athlete Demographics & Physical Profiles**

---

## ✨ Key Features

### 1. 🥇 Medal Tally
- Filter medal counts by **Year** and **Country** simultaneously or individually.
- View accurate medal counts (deduplicated for team sports like Football, Basketball, Relay, etc.).
- Color-coded badges for **Gold**, **Silver**, **Bronze**, and **Total** medals.

### 2. 📊 Overall Analysis
- **High-level Metrics**: Quick summary cards displaying total editions, host cities, sports, events, athletes, and participating nations.
- **Participating Nations Over Time**: Line trends tracking country participation growth across modern Olympics.
- **Events & Sports Trends**: Dynamic charts illustrating the expansion of Olympic event categories over time.
- **Events Heatmap**: A multi-dimensional grid showing events held per sport in each edition.
- **Top Athletes**: Filterable leaderboard of the most successful athletes overall or by individual sports.

### 3. 🌍 Country-Wise Analysis
- **Medal Progress Line Plot**: Historical timeline tracking a selected country's performance across all editions.
- **Sport Heatmap**: Visual breakdown showing which sports yield the most medals for a specific country.
- **Top 10 Athletes**: Dedicated leaderboards for any selected nation's top Olympians.

### 4. 👟 Athlete Demographics
- **Age Distribution**: Comparative probability density curves across overall athletes, Gold, Silver, and Bronze winners.
- **Age vs. Sport Profiles**: Age distribution for Gold medalists categorized by sports (e.g., Gymnastics vs. Equestrian).
- **Height vs. Weight Analysis**: Interactive scatter plots analyzing physical attributes filtered by sport, gender, and medal status.
- **Gender Participation Trends**: Line graphs tracking female vs. male participation ratio growth over 120 years.

---

## 📁 Project Architecture & File Structure

```text
OLYMPIC-ANALYSIS/
│
├── App.py                  # Main Streamlit web app entry point & UI layout
├── helper.py               # Helper functions for calculations and plot data
├── preprocessor.py         # Data cleaning, NOC merging, and transformations
├── OlympicsAnalysis.ipynb  # Initial Exploratory Data Analysis (Jupyter Notebook)
│
├── athlete_events.csv      # Primary dataset (historical athlete records)
├── noc_regions.csv         # NOC region mappings (Country codes to region names)
│
├── requirements.txt        # Python package dependencies
├── setup.sh                # Shell setup script for web deployment
├── Procfile                # Heroku deployment process config
└── .gitignore              # Git ignore rules
```

---

## 💾 Dataset Details

The dataset contains historical records from 120 years of Olympic Games:
1. **`athlete_events.csv`**: Contains over 270,000 individual athlete participation records:
   - `ID`, `Name`, `Sex`, `Age`, `Height`, `Weight`, `Team`, `NOC`, `Games`, `Year`, `Season`, `City`, `Sport`, `Event`, `Medal`.
2. **`noc_regions.csv`**: Maps National Olympic Committee 3-letter codes (`NOC`) to full country names (`region`) and notes.

---

## ⚙️ Installation & Local Setup

### Prerequisites
- Python `3.8` or higher
- `pip` package manager
- `git`

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/olympic-data-analysis.git
cd olympic-data-analysis
```

### 2. Create & Activate a Virtual Environment
- **On Windows:**
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```
- **On macOS / Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🚀 How to Run

Once dependencies are installed, launch the Streamlit application:

```bash
streamlit run App.py
```

The app will open automatically in your default browser at:
`http://localhost:8501`

---

## ☁️ Deployment Guide

This project includes deployment configuration files (`Procfile`, `setup.sh`) suited for various platforms:

### Deploying to Streamlit Community Cloud (Recommended)
1. Push your repository to GitHub.
2. Sign in to [Streamlit Share](https://share.streamlit.io/).
3. Click **"New App"**, select your repository, branch (`main`), and set `App.py` as the main entry point.
4. Click **Deploy**.

---

## 🛠️ Technologies Used

| Category | Technology / Library |
| :--- | :--- |
| **Language** | Python 3.x |
| **Web Framework** | Streamlit |
| **Data Wrangling** | Pandas, NumPy |
| **Data Visualization** | Plotly Express, Plotly Graph Objects, Seaborn, Matplotlib |
| **IDE / Environment** | PyCharm, Jupyter Notebook |

---

## 🤝 Contributing

Contributions are welcome! If you'd like to improve the app or add new visual features:

1. Fork the Repository.
2. Create a Feature Branch (`git checkout -b feature/AwesomeFeature`).
3. Commit your Changes (`git commit -m 'Add some AwesomeFeature'`).
4. Push to the Branch (`git push origin feature/AwesomeFeature`).
5. Open a Pull Request.

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.
