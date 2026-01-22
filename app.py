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
# CUSTOM CSS (FINAL UI – HIGH CONTRAST & PREMIUM)
# =====================================================
st.markdown("""
<style>
.main {
    background-color: #f4f9f4;
}

/* Header */
.title-box {
    background: linear-gradient(90deg, #1b5e20, #4caf50);
    padding: 25px;
    border-radius: 16px;
    color: white;
    text-align: center;
    margin-bottom: 25px;
}

/* White sections */
.section {
    background-color: #ffffff;
    padding: 22px;
    border-radius: 14px;
    margin-bottom: 22px;
    box-shadow: 0px 4px 14px rgba(0,0,0,0.08);
    color: #1b1b1b;
}

/* Highlight cards */
.highlight {
    background-color: #e8f5e9;
    padding: 20px;
    border-radius: 14px;
    color: #1b1b1b;
    box-shadow: 0px 3px 10px rgba(0,0,0,0.08);
}

.highlight h2, .highlight h3 {
    color: #1b5e20;
    margin-bottom: 8px;
}

.highlight p {
    color: #263238;
    font-size: 16px;
    font-weight: 500;
}
</style>
""", unsafe_allow_html=True)

# =====================================================
# HEADER
# =====================================================
st.markdown("""
<div class="title-box">
    <h1>🌾 AI Farmer Assistant</h1>
    <h4>AI-Powered Multi-Rule Decision Support System for Smart Agriculture</h4>
</div>
""", unsafe_allow_html=True)

# =====================================================
# INPUT SECTION
# =====================================================
st.markdown("<div class='section'><h2>🧾 Farmer Input Details</h2></div>", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)

with c1:
    soil = st.selectbox("🌱 Soil Type", ["Black", "Red", "Alluvial", "Sandy"])
with c2:
    season = st.selectbox("☀️ Season", ["Kharif", "Rabi", "Zaid"])
with c3:
    duration = st.selectbox(
        "⏳ Crop Duration",
        ["Short (2–3 months)", "Medium (3–5 months)", "Long (5+ months)"]
    )
with c4:
    water = st.selectbox("💧 Water Availability", ["Low", "Medium", "High"])

# =====================================================
# PRIMARY AI – CROP RECOMMENDATION (RULE-BASED)
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
# KNOWLEDGE BASE (EXPANDED)
# =====================================================
knowledge_base = {
    "Rice": {
        "price": "₹2200–2400 / quintal",
        "trend": "Increasing",
        "base_budget": 28000,
        "fertilizers": ["Urea", "DAP", "Potash"],
        "advice": "Maintain standing water and control stem borer."
    },
    "Wheat": {
        "price": "₹2100–2300 / quintal",
        "trend": "Stable",
        "base_budget": 24000,
        "fertilizers": ["Urea", "DAP"],
        "advice": "Ensure timely irrigation and monitor rust disease."
    },
    "Cotton": {
        "price": "₹6300–6700 / quintal",
        "trend": "Stable",
        "base_budget": 40000,
        "fertilizers": ["NPK", "Zinc", "Urea"],
        "advice": "Monitor bollworms and avoid excess irrigation."
    },
    "Maize": {
        "price": "₹2000–2200 / quintal",
        "trend": "Stable",
        "base_budget": 24000,
        "fertilizers": ["Urea", "DAP"],
        "advice": "Split fertilizer application and control fall armyworm."
    },
    "Groundnut": {
        "price": "₹5000–5400 / quintal",
        "trend": "Decreasing",
        "base_budget": 30000,
        "fertilizers": ["Gypsum", "SSP", "Potash"],
        "advice": "Ensure good drainage and apply gypsum at flowering."
    },
    "Millets": {
        "price": "₹2800–3200 / quintal",
        "trend": "Increasing",
        "base_budget": 17000,
        "fertilizers": ["Compost", "Low-dose NPK"],
        "advice": "Low water crop, suitable for dry regions."
    },
    "Sugarcane": {
        "price": "₹340–380 / quintal",
        "trend": "Stable",
        "base_budget": 50000,
        "fertilizers": ["Urea", "DAP", "Potash"],
        "advice": "Ensure irrigation and control early shoot borer."
    },
    "Pulses": {
        "price": "₹6000–6500 / quintal",
        "trend": "Increasing",
        "base_budget": 20000,
        "fertilizers": ["DAP", "Rhizobium culture"],
        "advice": "Avoid excess nitrogen and improve soil fertility."
    },
    "Soybean": {
        "price": "₹4200–4600 / quintal",
        "trend": "Stable",
        "base_budget": 28000,
        "fertilizers": ["DAP", "Potash"],
        "advice": "Ensure proper drainage and pest monitoring."
    },
    "Sunflower": {
        "price": "₹5500–6000 / quintal",
        "trend": "Increasing",
        "base_budget": 22000,
        "fertilizers": ["Urea", "DAP"],
        "advice": "Control leaf spot disease and maintain soil moisture."
    }
}

# =====================================================
# SECONDARY AI – RISK ANALYSIS (MULTI-RULE)
# =====================================================
def risk_analysis(crop, water, duration):
    risks = []

    if crop in ["Rice", "Sugarcane"] and water == "Low":
        risks.append("⚠️ High water requirement crop with low water availability.")

    if crop in ["Cotton", "Sugarcane"] and duration == "Short (2–3 months)":
        risks.append("⚠️ Crop duration is insufficient for this crop.")

    if crop in ["Millets", "Pulses"] and water == "High":
        risks.append("ℹ️ Excess irrigation is not required for this crop.")

    if not risks:
        risks.append("✅ No major risk detected for selected conditions.")

    return risks

# =====================================================
# DYNAMIC BUDGET AI
# =====================================================
def dynamic_budget(crop, water):
    budget = knowledge_base[crop]["base_budget"]

    if water == "Low":
        budget += 3000
    elif water == "High":
        budget -= 2000

    return f"₹{budget} per acre (adjusted based on water availability)"

# =====================================================
# CONDITIONAL FINAL ADVISORY AI
# =====================================================
def conditional_advice(crop, water, duration):
    advice = knowledge_base[crop]["advice"]

    if water == "Low":
        advice += " Use drip irrigation to conserve water."
    if duration == "Short (2–3 months)":
        advice += " Prefer early-maturing crop varieties."

    return advice

# =====================================================
# RUN AI BUTTON
# =====================================================
st.write("")
center = st.columns([1, 2, 1])[1]
with center:
    run_ai = st.button("🚀 Run AI Recommendation", use_container_width=True)

# =====================================================
# OUTPUT SECTION
# =====================================================
if run_ai:
    crop = recommend_crop(soil, season, duration, water)
    data = knowledge_base[crop]

    st.markdown("<div class='section'><h2>🤖 AI Decision Output</h2></div>", unsafe_allow_html=True)

    o1, o2, o3 = st.columns(3)

    with o1:
        st.markdown(
            f"<div class='highlight'><h3>🌾 Recommended Crop</h3>"
            f"<h2 style='font-size:32px;'>{crop}</h2></div>",
            unsafe_allow_html=True
        )

    with o2:
        st.markdown(
            f"<div class='highlight'><h3>📊 Market Analysis</h3>"
            f"<p><b>Price:</b> {data['price']}</p>"
            f"<p><b>Trend:</b> {data['trend']}</p></div>",
            unsafe_allow_html=True
        )

    with o3:
        st.markdown(
            f"<div class='highlight'><h3>🧪 Fertilizers</h3>"
            f"<p>{', '.join(data['fertilizers'])}</p></div>",
            unsafe_allow_html=True
        )

    st.markdown("<div class='section'><h3>💸 Estimated Budget</h3>"
                f"<p>{dynamic_budget(crop, water)}</p></div>",
                unsafe_allow_html=True)

    st.markdown("<div class='section'><h3>⚠️ Risk & Condition Analysis</h3>",
                unsafe_allow_html=True)
    for r in risk_analysis(crop, water, duration):
        if "⚠️" in r:
            st.warning(r)
        else:
            st.info(r)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='section'><h3>🌟 Final AI Advisory</h3>"
                f"<p>{conditional_advice(crop, water, duration)}</p></div>",
                unsafe_allow_html=True)

# =====================================================
# FOOTER
# =====================================================
st.markdown("""
<hr>
<center>
<b>AI for Agriculture & Rural Support</b><br>
Hackathon Project 🌾🤖
</center>
""", unsafe_allow_html=True)
