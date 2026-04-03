import streamlit as st

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(
    page_title="AI Farmer Assistant",
    page_icon="🌾",
    layout="wide"
)

# =====================================================
# CUSTOM CSS (MODERN UI)
# =====================================================
st.markdown("""
<style>

/* Background */
.main {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    color: #ffffff;
}

/* Title */
.title-box {
    background: linear-gradient(90deg, #00c853, #64dd17);
    padding: 28px;
    border-radius: 18px;
    color: #002b11;
    text-align: center;
    margin-bottom: 25px;
    box-shadow: 0px 6px 20px rgba(0,0,0,0.3);
}

/* Section */
.section {
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(10px);
    padding: 22px;
    border-radius: 16px;
    margin-bottom: 22px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.25);
    border: 1px solid rgba(255,255,255,0.1);
}

/* Highlight cards */
.highlight {
    background: linear-gradient(135deg, #00e676, #00c853);
    padding: 20px;
    border-radius: 16px;
    color: #003d1f;
    font-weight: bold;
    text-align: center;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.3);
    transition: transform 0.2s ease;
}

.highlight:hover {
    transform: scale(1.05);
}

/* Button */
.stButton>button {
    background: linear-gradient(90deg, #ff9800, #ff5722);
    color: white;
    font-size: 18px;
    border-radius: 12px;
    padding: 10px;
    border: none;
    transition: 0.3s;
}

.stButton>button:hover {
    transform: scale(1.05);
    background: linear-gradient(90deg, #ff5722, #e64a19);
}

/* Risk */
.risk-high {
    background: #ff5252;
    padding: 15px;
    border-radius: 12px;
    color: white;
}

.risk-medium {
    background: #ffb300;
    padding: 15px;
    border-radius: 12px;
    color: black;
}

.risk-low {
    background: #00e676;
    padding: 15px;
    border-radius: 12px;
    color: black;
}

/* Info */
.stInfo {
    background-color: #1e88e5 !important;
    color: white !important;
    border-radius: 10px;
}

footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# HEADER
# =====================================================
st.markdown("""
<div class="title-box">
    <h1>🌾 AI Farmer Assistant</h1>
    <h4>Smart Agriculture Decision Support System</h4>
</div>
""", unsafe_allow_html=True)

# =====================================================
# INPUTS
# =====================================================
st.markdown("<div class='section'><h2>🧾 Farmer Input Details</h2></div>", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)

with c1:
    soil = st.selectbox("🌱 Soil Type", ["Black", "Red", "Alluvial", "Sandy"])
with c2:
    season = st.selectbox("☀️ Season", ["Kharif", "Rabi", "Zaid"])
with c3:
    duration = st.selectbox("⏳ Crop Duration",
                            ["Short (2–3 months)", "Medium (3–5 months)", "Long (5+ months)"])
with c4:
    water = st.selectbox("💧 Water Availability", ["Low", "Medium", "High"])

# =====================================================
# AI LOGIC
# =====================================================
def recommend_crop(soil, season, duration, water):
    if soil == "Alluvial" and water == "High":
        return "Rice"
    elif soil == "Black" and season == "Kharif" and duration == "Long (5+ months)":
        return "Cotton"
    elif soil == "Red" and season == "Rabi":
        return "Groundnut"
    elif soil == "Black" and season == "Rabi":
        return "Wheat"
    elif soil == "Sandy" and water == "Low":
        return "Millets"
    elif soil == "Alluvial" and season == "Kharif":
        return "Sugarcane"
    elif soil == "Red" and duration == "Short (2–3 months)":
        return "Pulses"
    elif soil == "Black" and duration == "Medium (3–5 months)":
        return "Soybean"
    elif soil == "Sandy" and season == "Zaid":
        return "Sunflower"
    else:
        return "Maize"

# =====================================================
# KNOWLEDGE BASE
# =====================================================
knowledge_base = {
    "Rice": {"price":"₹2200–2400","trend":"Increasing","budget":28000,"fert":["Urea","DAP"],"advice":"Maintain water level."},
    "Wheat":{"price":"₹2100–2300","trend":"Stable","budget":24000,"fert":["Urea","DAP"],"advice":"Timely irrigation."},
    "Cotton":{"price":"₹6300–6700","trend":"Stable","budget":40000,"fert":["NPK","Zinc"],"advice":"Check pests."},
    "Maize":{"price":"₹2000–2200","trend":"Stable","budget":24000,"fert":["Urea","DAP"],"advice":"Control worms."},
    "Groundnut":{"price":"₹5000–5400","trend":"Decreasing","budget":30000,"fert":["Gypsum","SSP"],"advice":"Good drainage."},
    "Millets":{"price":"₹2800–3200","trend":"Increasing","budget":17000,"fert":["Compost"],"advice":"Low water crop."},
    "Sugarcane":{"price":"₹340–380","trend":"Stable","budget":50000,"fert":["Urea","DAP"],"advice":"Needs irrigation."},
    "Pulses":{"price":"₹6000–6500","trend":"Increasing","budget":20000,"fert":["DAP"],"advice":"Avoid nitrogen."},
    "Soybean":{"price":"₹4200–4600","trend":"Stable","budget":28000,"fert":["DAP"],"advice":"Proper drainage."},
    "Sunflower":{"price":"₹5500–6000","trend":"Increasing","budget":22000,"fert":["Urea"],"advice":"Leaf care."}
}

# =====================================================
# RISK ANALYSIS
# =====================================================
def risk_analysis(crop, water, duration):
    risks = []
    level = "Low"

    if crop in ["Rice","Sugarcane"] and water == "Low":
        risks.append("High water demand but low availability.")
        level = "High"

    if crop in ["Cotton","Sugarcane"] and duration == "Short (2–3 months)":
        risks.append("Insufficient crop duration.")
        level = "Medium"

    if not risks:
        risks.append("No major risks detected.")

    return risks, level

# =====================================================
# BUTTON
# =====================================================
run = st.button("🚀 Run AI Recommendation", use_container_width=True)

# =====================================================
# OUTPUT
# =====================================================
if run:
    crop = recommend_crop(soil, season, duration, water)
    data = knowledge_base[crop]
    risks, level = risk_analysis(crop, water, duration)

    st.markdown("<div class='section'><h2>🤖 AI Recommendation</h2></div>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(f"<div class='highlight'><h3>🌾 Crop</h3><h2>{crop}</h2></div>", unsafe_allow_html=True)
    with c2:
        st.markdown(f"<div class='highlight'><h3>📊 Market</h3>Price: {data['price']}<br>Trend: {data['trend']}</div>", unsafe_allow_html=True)
    with c3:
        st.markdown(f"<div class='highlight'><h3>🧪 Fertilizers</h3>{', '.join(data['fert'])}</div>", unsafe_allow_html=True)

    # Risk color
    risk_class = "risk-low"
    if level == "High":
        risk_class = "risk-high"
    elif level == "Medium":
        risk_class = "risk-medium"

    st.markdown(f"<div class='{risk_class}'><h3>⚠️ Risk Level: {level}</h3></div>", unsafe_allow_html=True)

    for r in risks:
        st.info(r)

# =====================================================
# FOOTER
# =====================================================
st.markdown("""
<hr>
<center>
<b>🌾 Smart Farming with AI</b>
</center>
""", unsafe_allow_html=True)
