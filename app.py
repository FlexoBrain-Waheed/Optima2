import streamlit as st
import pandas as pd

# --- إعدادات الصفحة ---
st.set_page_config(page_title="NexFlexo | Strategic Investment", page_icon="🚀", layout="wide")

# --- تنسيق CSS مخصص للجمالية ---
st.markdown("""
    <style>
    .main-title {font-size: 40px; color: #0B2545; font-weight: bold; text-align: center;}
    .sub-title {font-size: 20px; color: #13315C; text-align: center; margin-bottom: 30px;}
    .highlight {color: #E63946; font-weight: bold;}
    .card {background-color: #F0F4F8; padding: 20px; border-radius: 10px; margin-bottom: 10px; border-left: 5px solid #0B2545;}
    </style>
""", unsafe_allow_html=True)

# --- القائمة الجانبية (Sidebar) ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3256/3256094.png", width=100) # يمكنك استبداله برابط شعار NexFlexo
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", [
    "1. Executive Summary", 
    "2. TCO & Hidden Costs", 
    "3. Technical Superiority", 
    "4. The Partnership Challenge"
])

st.sidebar.markdown("---")
st.sidebar.write("**Presented by:**")
st.sidebar.write("Waheed Waleed Malik")
st.sidebar.write("NexFlexo | SOMA Agent")

# ==========================================
# الصفحة الأولى: الملخص التنفيذي
# ==========================================
if page == "1. Executive Summary":
    st.markdown('<div class="main-title">Strategic Investment Evaluation</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">SOMA Optima 2 vs. W&H Alphaflex</div>', unsafe_allow_html=True)
    
    st.write("### The Paradigm Shift: Flagship vs. Economy")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="card">
        <h4>🇩🇪 W&H Alphaflex (Economy Class)</h4>
        <ul>
            <li>Positioned officially as an <b>Entry-Level</b> press.</li>
            <li>Stripped down to fit lower budgets.</li>
            <li>A new 2024 release (Untested long-term).</li>
            <li><span class="highlight">Risk:</span> Becoming a testing ground for a budget model.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
        <h4>🇨🇿 SOMA Optima 2 (Flagship Class)</h4>
        <ul>
            <li>The absolute <b>pinnacle of SOMA’s technology</b>.</li>
            <li>A fully-equipped, premium Full-Option machine.</li>
            <li>A 100% mature and reliable platform (since 2013).</li>
            <li><span class="highlight">Advantage:</span> Proven stability and world-class quality.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    st.info("💡 **The Strategic Question:** Does it make sense to pay over €2 Million for a stripped-down economy model when you can own top-tier flagship technology for the same budget?")

# ==========================================
# الصفحة الثانية: التكاليف الخفية
# ==========================================
elif page == "2. TCO & Hidden Costs":
    st.markdown('<div class="main-title">Total Cost of Ownership (TCO)</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">Uncovering the Hidden Costs of the "Base" Offer</div>', unsafe_allow_html=True)

    st.write("The SOMA Optima2 is a **Turn-Key** solution. To match its level, the competitor requires costly add-ons.")
    
    # استخدام أعمدة لعرض التكاليف المخفية كأرقام تفاعلية
    c1, c2, c3, c4 = st.columns(4)
    c1.metric(label="Missing Cooling (ITS)", value="~ € 50k", delta="- Hidden Cost", delta_color="inverse")
    c2.metric(label="Missing 100% Camera", value="~ € 71k", delta="- Hidden Cost", delta_color="inverse")
    c3.metric(label="Missing Sleeves (8+8)", value="~ € 50k", delta="- Hidden Cost", delta_color="inverse")
    c4.metric(label="Missing Carbon Mandrels", value="~ € 30k", delta="- Hidden Cost", delta_color="inverse")

    st.write("---")
    st.write("### TCO Detailed Comparison")
    
    tco_data = {
        "Feature / Equipment": ["Ink Cooling & Thermal Stabilization (ITS)", "100% Print Inspection Camera", "Printing Sleeves & Aniloxes (8+8)", "Printing Cylinder Mandrels", "Rewind Roll Lift", "Operator Ergonomics (Shafts)"],
        "SOMA Optima 2 (Turn-Key)": ["✅ Included & Integrated", "✅ Included (BST iPQ Check)", "✅ Included", "✅ Carbon Composite (Stable)", "✅ Included", "✅ Lightweight Aluminum (19kg)"],
        "W&H Alphaflex (Base Offer)": ["❌ Customer Responsibility", "❌ Optional Add-on", "❌ Customer Responsibility", "⚠️ Steel (Heavy)", "❌ Optional Add-on", "❌ Standard Heavy Shafts"]
    }
    df_tco = pd.DataFrame(tco_data)
    st.dataframe(df_tco, use_container_width=True, hide_index=True)

# ==========================================
# الصفحة الثالثة: التفوق الفني
# ==========================================
elif page == "3. Technical Superiority":
    st.markdown('<div class="main-title">Engineering Supremacy</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">Advanced Technology for Maximum Profit</div>', unsafe_allow_html=True)

    tech_data = {
        "Technical Feature": ["Print Repeat Range", "Thin Film & ALU Handling", "Tension Control Isolation", "Impression & Register Setup"],
        "SOMA Optima 2 (Advanced)": ["360 mm – 850 mm", "MINK brushed spreader & hard anodized rollers", "Dedicated Out-Feed Unit (Pre-rewind)", "IRIS & Falcon II (Fully automatic)"],
        "W&H Alphaflex (Basic)": ["370 mm – 800 mm", "Standard aluminum grooved rollers", "Standard continuous web path", "EASY SET (Semi-automatic)"],
        "The SOMA Advantage": ["Maximum Job Flexibility", "Flawless Production on PE/ALU", "Absolute Print Accuracy", "Near-Zero Waste Setup"]
    }
    df_tech = pd.DataFrame(tech_data)
    st.table(df_tech)

    st.write("---")
    with st.expander("🔻 Click to reveal: Operational Impact (Waste & Dependency)"):
        st.write("""
        * **Zero Waste Guarantee:** SOMA's topography-based setup cuts expensive material waste during changeovers.
        * **Operator Independence:** Alphaflex's semi-auto systems require highly-paid expert operators. SOMA uses AI to set itself flawlessly, reducing human error.
        * **Lifespan:** Optima 2 is a robust Monoblock designed to dominate for 15-20 years.
        """)

# ==========================================
# الصفحة الرابعة: الشراكة والتحدي
# ==========================================
elif page == "4. The Partnership Challenge":
    st.markdown('<div class="main-title">A Complete Partnership</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">We build your project, not just sell a machine.</div>', unsafe_allow_html=True)

    st.success("**Exclusive Turn-Key Package:** Special massive discount if investing in the complete suite (Press, S-Mount, Lamiflex, Pluto).")

    st.write("### Unbeatable Training Program")
    col_t1, col_t2, col_t3 = st.columns(3)
    col_t1.info("🛠️ **10 Days**\n\nIntensive on-site training during installation.")
    col_t2.info("📅 **2 Extra Weeks**\n\nAdvanced free training after 3 months of operation.")
    col_t3.info("✈️ **1 Full Month**\n\nAt the SOMA factory in Europe to reach world-class mastery.")

    st.write("---")
    st.write("### 🎯 The SOMA Challenge")
    st.markdown("""
    > "Because true trust is built on experience, not ink on paper, we extend an open invitation to visit our factory. 
    > **Bring your most complex and difficult printing designs.** Watch us set them up and print HD quality with near-zero waste in minutes. 
    > Your investment deserves to be seen overcoming the toughest challenges before you make a final decision."
    """)
