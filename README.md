
# 🍽️ Zomato Bangalore Market & Food Intelligence Platform

An end-to-end data analytics and business intelligence dashboard analyzing **51,000+ restaurant listings** across Bangalore to uncover catchment saturation, pricing elasticity, and customer satisfaction drivers.

🔗 **Live Interactive App:** [View Live Dashboard](https://zomato-bangalore-analytics-fxrhlovvhwvgfd83xqb13y.streamlit.app/)

---

## 📌 Executive Summary & Key Findings
* **Catchment Density & Saturation:** Tech corridors and student clusters (**BTM, Koramangala, and HSR**) account for the highest concentration of total outlets, signaling intense competition and high customer turnover.
* **Pricing Elasticity by Format:** **Pubs & Nightlife** and **Buffets** command premium ticket sizes (averaging **₹1,300–₹1,600+ for two** in Indiranagar and Koramangala), maintaining higher median ratings (~4.1/5.0). In contrast, **Delivery and Quick Bites** sustain high-volume demand within the **₹300–₹550** range.
* **Online Delivery Impact:** Over 60% of restaurants support online ordering, demonstrating higher vote engagement compared to traditional dine-in-only establishments.
* **Cuisine Demand:** North Indian, Chinese, and South Indian cuisines dominate market supply, while specialized Cafe and Continental formats show strong margins in premium localities.

---

## 🛠️ Tech Stack & Methodology
* **Language & Analysis:** Python (Pandas, NumPy)
* **Visualization & Analytics:** Plotly Express, Seaborn, Matplotlib
* **Web App & Deployment:** Streamlit Community Cloud
* **Version Control:** Git, GitHub

---

## 🚀 Local Setup
```bash
git clone [https://github.com/rohan-giri2003/zomato-bangalore-analytics.git](https://github.com/rohan-giri2003/zomato-bangalore-analytics.git)
cd zomato-bangalore-analytics
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
