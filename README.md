# 📊 Developer Survey Exploratory Data Analysis (EDA)

## 🔍 Overview

This project explores a developer survey dataset to understand **career trends in the tech industry**. Using **Exploratory Data Analysis (EDA)**, it uncovers relationships between **professional experience, job satisfaction, remote work preferences, education levels, employment types, and programming languages**.

The focus is on generating **clear insights and visualizations**, rather than building predictive models.

---

## 🎯 Project Goals

* 📈 Analyze how **years of professional experience** relate to **job satisfaction**
* 🏠 Understand **remote work distribution** across employment types
* 💻 Identify **popular programming languages in the United States**
* 🎓 Explore the relationship between **education level and employment**
* 🧹 Produce a **clean, analysis-ready dataset**

---

## ⚙️ What This Project Does

### 🧼 Data Preparation

* Loads survey data from a CSV file
* Handles missing values in key columns using statistical methods
* Cleans inconsistent country names for accurate filtering

### 📊 Exploratory Analysis

* Groups developers by **experience ranges**
* Calculates and visualizes **median job satisfaction**
* Examines **job satisfaction distribution**
* Analyzes **remote work trends**
* Identifies **top programming languages used by U.S. developers**
* Explores **experience vs satisfaction scores**
* Visualizes **education vs employment** relationships using heatmaps

### 💾 Output

* Generates multiple charts for insight discovery
* Saves a cleaned dataset as:

  ```
  survey_data_eda.csv
  ```

---

## 🧩 Sample Code Snippet

*(Minimal example used in the project)*

```python
df['Employment'] = df['Employment'].fillna(df['Employment'].mode()[0])
df['YearsCodePro'] = pd.to_numeric(df['YearsCodePro'], errors='coerce')
```

This snippet shows how missing values are handled and how experience data is prepared for analysis.

---

## 🛠️ Tools & Libraries

* 🐍 **Python**
* 🧮 **Pandas** – data manipulation
* 📉 **Matplotlib** – data visualization
* 🎨 **Seaborn** – statistical plots

---

## 💡 Insights You Can Gain

* 📊 Whether **more experience leads to higher job satisfaction**
* 🏡 How **remote work adoption** varies by job type
* 💻 Which **programming languages dominate the U.S. market**
* 🎓 How **education level aligns with employment categories**

---

## 👨‍💻 Ideal For

* 📁 Data analysis & EDA practice
* ⭐ Portfolio projects
* 🌍 Understanding developer workforce trends
* 📊 Preparing datasets for dashboards or further analysis

---

## 🚀 Future Improvements

* 📐 Add statistical correlation metrics
* 📊 Build interactive dashboards
* 🌎 Compare trends across multiple countries
* 🤖 Extend analysis with machine learning models

---

## 📄 License

This project is intended for **educational and analytical purposes**.



## Author: Varrun Vashisht 
* 🗂️ Add a **project structure section**
* 🧠 Write a **portfolio or LinkedIn project summary**
