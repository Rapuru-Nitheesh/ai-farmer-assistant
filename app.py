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
# CUSTOM CSS
# =====================================================
st.markdown("""
<style>
.main { background-color: #f4f9f4; }
.title-box {
    background: linear-gradient(90deg, #1b5e20, #4caf50);
    padding: 25px;
    border-radius: 16px;
    color: white;
    text-align: center;
    margin-bottom: 25px;
}
.section {
    background-color: #ffffff;
    padding: 22px;
    border-radius: 14px;
    margin-bottom: 22px;
    box-shadow: 0px 4px 14px rgba(0,0,0,0.08);
}
.highlight {
    background-color: #e8f5e9;
    padding: 20px;
    border-radius: 14px;
    box-shadow: 0px 3px 10px rgba(0,0,0,0.08);
}
</style>
""", unsafe_allow_html=True)

# =====================================================
# HEADER
# =====================================================
st.markdown("""
<div class="title-box">
    <h1>🌾 AI Farmer Assistant</h1>
    <h4>Responsible AI Decision Support System for Smart Agriculture</h4>
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
# PRIMARY AI – RULE BASED
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
    "Rice": {"price":"₹2200–2400","trend":"Increasing","budget":28000,"fert":["Urea","DAP"],"advice":"Maintain standing water."},
    "Wheat":{"price":"₹2100–2300","trend":"Stable","budget":24000,"fert":["Urea","DAP"],"advice":"Ensure timely irrigation."},
    "Cotton":{"price":"₹6300–6700","trend":"Stable","budget":40000,"fert":["NPK","Zinc"],"advice":"Monitor bollworms."},
    "Maize":{"price":"₹2000–2200","trend":"Stable","budget":24000,"fert":["Urea","DAP"],"advice":"Control fall armyworm."},
    "Groundnut":{"price":"₹5000–5400","trend":"Decreasing","budget":30000,"fert":["Gypsum","SSP"],"advice":"Ensure drainage."},
    "Millets":{"price":"₹2800–3200","trend":"Increasing","budget":17000,"fert":["Compost"],"advice":"Low water crop."},
    "Sugarcane":{"price":"₹340–380","trend":"Stable","budget":50000,"fert":["Urea","DAP"],"advice":"Ensure irrigation."},
    "Pulses":{"price":"₹6000–6500","trend":"Increasing","budget":20000,"fert":["DAP"],"advice":"Avoid excess nitrogen."},
    "Soybean":{"price":"₹4200–4600","trend":"Stable","budget":28000,"fert":["DAP"],"advice":"Ensure drainage."},
    "Sunflower":{"price":"₹5500–6000","trend":"Increasing","budget":22000,"fert":["Urea"],"advice":"Control leaf spot."}
}

# =====================================================
# SCENARIO 1 – EXPLAINABILITY
# =====================================================
def explain_decision(soil, season, duration, water, crop):
    return [
        f"Soil type ({soil}) supports {crop}.",
        f"Season ({season}) matches growth cycle.",
        f"Crop duration ({duration}) is compatible.",
        f"Water availability ({water}) considered."
    ]

# =====================================================
# SCENARIO 2 – EARLY RISK + INTERVENTION
# =====================================================
def risk_analysis(crop, water, duration):
    risks = []
    level = "Low"
    if crop in ["Rice","Sugarcane"] and water == "Low":
        risks.append("High water demand with low water availability.")
        level = "High"
    if crop in ["Cotton","Sugarcane"] and duration == "Short (2–3 months)":
        risks.append("Insufficient duration for crop.")
        level = "Medium"
    if not risks:
        risks.append("No major risk detected.")
    return risks, level

# =====================================================
# SCENARIO 4 – AUTONOMY MODE
# =====================================================
def autonomy_mode(level):
    if level == "High":
        return "Human-in-the-loop (Manual confirmation required)"
    elif level == "Medium":
        return "Human-on-the-loop (Monitoring required)"
    else:
        return "Fully Autonomous Recommendation"

# =====================================================
# RESPONSIBILITY (SCENARIO 3)
# =====================================================
def responsibility_note():
    return {
        "Model Type":"Rule-Based Responsible AI",
        "Decision Owner":"AI Farmer Assistant (Advisory)",
        "Final Authority":"Farmer / Agri Expert",
        "Model Version":"v1.0"
    }

# =====================================================
# RUN BUTTON
# =====================================================
run = st.button("🚀 Run AI Recommendation", use_container_width=True)

# =====================================================
# OUTPUT
# =====================================================
if run:
    crop = recommend_crop(soil, season, duration, water)
    data = knowledge_base[crop]
    risks, level = risk_analysis(crop, water, duration)

    st.markdown("<div class='section'><h2>🤖 AI Decision Output</h2></div>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(f"<div class='highlight'><h3>🌾 Crop</h3><h2>{crop}</h2></div>", unsafe_allow_html=True)
    with c2:
        st.markdown(f"<div class='highlight'><h3>📊 Market</h3>Price: {data['price']}<br>Trend: {data['trend']}</div>", unsafe_allow_html=True)
    with c3:
        st.markdown(f"<div class='highlight'><h3>🧪 Fertilizers</h3>{', '.join(data['fert'])}</div>", unsafe_allow_html=True)

    st.markdown("<div class='section'><h3>🔍 Why this decision?</h3></div>", unsafe_allow_html=True)
    for e in explain_decision(soil, season, duration, water, crop):
        st.write("•", e)

    st.markdown(f"<div class='section'><h3>⚠️ Risk Level: {level}</h3></div>", unsafe_allow_html=True)
    for r in risks:
        st.info(r)

    st.markdown(f"<div class='section'><h3>⚙️ Autonomy Mode</h3>{autonomy_mode(level)}</div>", unsafe_allow_html=True)

    st.markdown("<div class='section'><h3>📜 Responsibility</h3></div>", unsafe_allow_html=True)
    for k,v in responsibility_note().items():
        st.write(f"**{k}:** {v}")

# =====================================================
# FOOTER
# =====================================================
st.markdown("""
<hr>
<center>
<b>Hackathon Project – Responsible AI for Agriculture 🌾</b>
</center>
""", unsafe_allow_html=True)
