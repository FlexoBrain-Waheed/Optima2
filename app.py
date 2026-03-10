import streamlit as st
import pandas as pd
import altair as alt

# 1. Page Configuration
st.set_page_config(page_title="Strategic Investment Evaluation", page_icon="🚀", layout="wide")

# 2. Custom CSS for beautiful tables and styling
st.markdown("""
    <style>
    .main-header { font-size: 2.5rem; font-weight: 900; color: #1E3A8A; margin-bottom: 0px; }
    .sub-header { font-size: 1.5rem; color: #4B5563; margin-bottom: 20px; }
    .soma-col { background-color: #ECFDF5; padding: 15px; border-radius: 10px; border-left: 5px solid #10B981; }
    .wh-col { background-color: #FEF2F2; padding: 15px; border-radius: 10px; border-left: 5px solid #EF4444; }
    .custom-table { width: 100%; border-collapse: collapse; margin-top: 20px; font-size: 1.1rem; }
    .custom-table th { background-color: #1E3A8A; color: white; padding: 12px; text-align: left; }
    .custom-table td { border-bottom: 1px solid #E5E7EB; padding: 12px; }
    .highlight-green { background-color: #D1FAE5; color: #065F46; font-weight: bold; }
    .highlight-red { background-color: #FEE2E2; color: #991B1B; }
    </style>
""", unsafe_allow_html=True)

# 3. Sidebar Navigation
st.sidebar.image("https://img.icons8.com/color/96/000000/combo-chart--v1.png", width=80)
st.sidebar.title("Presentation Menu")
st.sidebar.markdown("---")
page = st.sidebar.radio("Navigate to:", [
    "1. The Paradigm Shift",
    "2. Hidden Costs (TCO) 📊",
    "3. Technical Superiority ⚙️",
    "4. Operator Ergonomics 👷‍♂️",
    "5. The SOMA Challenge 🚀"
])

st.sidebar.markdown("---")
st.sidebar.markdown("**Presented by:**\n\n**Waheed Waleed Malik**\n\nFlexo Consultation Services\n\nNexFlexo")

# 4. Main Content Logic based on Sidebar Selection

if page == "1. The Paradigm Shift":
    st.markdown('<p class="main-header">Strategic Investment Evaluation</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">SOMA Optima 2 vs. W&H Alphaflex</p>', unsafe_allow_html=True)
    st.markdown("---")
    
    st.info("💡 **The Strategic Question:** Does it make sense to pay over €2 Million for a stripped-down economy model when you can own top-tier technology for the exact same budget?")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="soma-col">
            <h2 style='color:#065F46;'>🏆 SOMA Optima 2 (Flagship Class)</h2>
            <p><strong>Status:</strong> The absolute pinnacle of SOMA’s technology.</p>
            <p><strong>Maturity:</strong> A 100% reliable platform. Built on deep operational experience since 2013 with zero structural flaws.</p>
            <p><strong>Reputation:</strong> Known as the "Master of Flexibility" and the "Bounce Killer" in the European market.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class="wh-col">
            <h2 style='color:#991B1B;'>⚠️ W&H Alphaflex (Economy Class)</h2>
            <p><strong>Status:</strong> Positioned by the manufacturer as an 'Entry-Level' press. Stripped down to fit lower budgets.</p>
            <p><strong>Maturity:</strong> Newly launched in mid-2024. Its economical structure is largely untested in harsh, long-term operational environments.</p>
            <p><strong>Conclusion:</strong> Never let your factory be the testing ground for a new economy model.</p>
        </div>
        """, unsafe_allow_html=True)

elif page == "2. Hidden Costs (TCO) 📊":
    st.markdown('<p class="main-header">Total Cost of Ownership (TCO) & Hidden Costs</p>', unsafe_allow_html=True)
    st.write("The SOMA Optima2 is quoted as a comprehensive production system. To match its level of automation, quality control, and operator ergonomics, the alternative offer requires substantial and costly add-ons.")
    
    # Visual Chart for Hidden Costs
    st.subheader("Visualizing the Missing Value (Estimated € Add-ons)")
    data = pd.DataFrame({
        'Component': ['ITS Cooling', '100% Camera', 'Sleeves & Aniloxes', 'Carbon Mandrels', 'Roll Lift'],
        'Estimated Cost (€)': [50000, 71000, 50000, 30000, 15000]
    })
    chart = alt.Chart(data).mark_bar(color='#EF4444').encode(
        x=alt.X('Estimated Cost (€):Q', title='Hidden Cost in Euros'),
        y=alt.Y('Component:N', sort='-x', title='Missing Equipment in Alphaflex'),
        tooltip=['Component', 'Estimated Cost (€)']
    ).properties(height=250)
    st.altair_chart(chart, use_container_width=True)

    # HTML Styled Table
    st.markdown("""
    <table class="custom-table">
        <tr>
            <th>Feature / Equipment</th>
            <th>SOMA Optima 2 (Turn-Key)</th>
            <th>W&H Alphaflex (Base Offer)</th>
            <th>Estimated Hidden Cost</th>
        </tr>
        <tr>
            <td><strong>Ink Cooling (ITS)</strong></td>
            <td class="highlight-green">✅ Included & Integrated</td>
            <td class="highlight-red">❌ Customer Responsibility</td>
            <td><strong>~ € 50,000</strong></td>
        </tr>
        <tr>
            <td><strong>100% Inspection Camera</strong></td>
            <td class="highlight-green">✅ Included (BST iPQ Check)</td>
            <td class="highlight-red">❌ Optional Add-on</td>
            <td><strong>~ € 71,000</strong></td>
        </tr>
        <tr>
            <td><strong>Printing Sleeves & Aniloxes</strong></td>
            <td class="highlight-green">✅ Included (1 Full Set: 8+8)</td>
            <td class="highlight-red">❌ Customer Responsibility</td>
            <td><strong>~ € 50,000</strong></td>
        </tr>
        <tr>
            <td><strong>Printing Cylinder Mandrels</strong></td>
            <td class="highlight-green">✅ Carbon Composite (Anti-Bounce)</td>
            <td class="highlight-red">⚠️ Steel</td>
            <td><strong>~ € 30,000</strong></td>
        </tr>
        <tr>
            <td><strong>Rewind Roll Lift</strong></td>
            <td class="highlight-green">✅ Included</td>
            <td class="highlight-red">❌ Optional Add-on</td>
            <td><strong>~ € 15,000</strong></td>
        </tr>
    </table>
    """, unsafe_allow_html=True)

elif page == "3. Technical Superiority ⚙️":
    st.markdown('<p class="main-header">Smart Engineering for Maximum Profit</p>', unsafe_allow_html=True)
    st.write("Beyond the financial savings, the SOMA Optima2 is engineered with advanced, purpose-built technologies designed to eliminate waste and flawlessly handle demanding substrates.")

    st.markdown("""
    <table class="custom-table">
        <tr>
            <th>Technical Feature</th>
            <th>SOMA Optima 2 (Advanced Standard)</th>
            <th>W&H Alphaflex (Basic Standard)</th>
            <th>The Direct Advantage</th>
        </tr>
        <tr>
            <td><strong>Print Repeat Range</strong></td>
            <td class="highlight-green">360 mm – 850 mm</td>
            <td class="highlight-red">370 mm – 800 mm</td>
            <td><strong>Maximum Job Flexibility:</strong> Accept a wider variety of customer orders.</td>
        </tr>
        <tr>
            <td><strong>Thin Film & ALU Handling</strong></td>
            <td class="highlight-green">MINK brushed spreader & hard anodized rollers</td>
            <td class="highlight-red">Standard aluminum grooved rollers</td>
            <td><strong>Flawless Production:</strong> Eliminates wrinkling on PE films & protects from ALU wear.</td>
        </tr>
        <tr>
            <td><strong>Tension Control Isolation</strong></td>
            <td class="highlight-green">Dedicated Out-Feed Unit (Pre-rewind separation)</td>
            <td class="highlight-red">Standard continuous web path</td>
            <td><strong>Absolute Print Accuracy:</strong> Isolates printing tension from winding tension.</td>
        </tr>
        <tr>
            <td><strong>Impression & Register Setup</strong></td>
            <td class="highlight-green">IRIS & Falcon II (Fully automatic)</td>
            <td class="highlight-red">EASY SET S (Semi-automatic)</td>
            <td><strong>Near-Zero Waste:</strong> Intelligent systems cut expensive material waste and setup time.</td>
        </tr>
    </table>
    """, unsafe_allow_html=True)

elif page == "4. Operator Ergonomics 👷‍♂️":
    st.markdown('<p class="main-header">Empowering Your Workforce</p>', unsafe_allow_html=True)
    st.markdown("### The Impact of Equipment Weight on Daily Productivity")
    
    col1, col2 = st.columns(2)
    with col1:
        st.success("### ✅ SOMA Optima 2")
        st.metric(label="Air Shaft Weight", value="19 kg", delta="Lightweight Aluminum", delta_color="normal")
        st.write("**Operator Impact:** Fast, safe, and efficient manual roll changes by a single operator.")
        st.write("**Lifespan:** Built as a Monoblock structure spanning 15-20 years of absolute efficiency.")

    with col2:
        st.error("### ⚠️ W&H Alphaflex")
        st.metric(label="Air Shaft Weight", value="Heavy", delta="Standard Mechanical", delta_color="inverse")
        st.write("**Operator Impact:** Severe physical strain, slower changeovers, higher risk of injury.")
        st.write("**Lifespan:** Entry-level economical frames may show structural issues after 7-10 years.")

elif page == "5. The SOMA Challenge 🚀":
    st.markdown('<p class="main-header">A Complete Partnership & The SOMA Challenge</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background-color: #F8FAFC; padding: 25px; border-radius: 10px; border-left: 8px solid #2563EB; margin-bottom: 20px;">
        <h3 style="color: #1E3A8A;">🤝 Exclusive Turn-Key Package</h3>
        <p style="font-size: 1.2rem;">If Ymtaco invests in the complete suite <b>(Optima 2 Press, S-Mount, Lamiflex, Pluto)</b>, we will provide a special massive discount on the total project.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="background-color: #F8FAFC; padding: 25px; border-radius: 10px; border-left: 8px solid #059669; margin-bottom: 20px;">
        <h3 style="color: #065F46;">🎓 Unbeatable Training Program</h3>
        <ul style="font-size: 1.1rem;">
            <li><b>10 Days</b> of intensive on-site training during installation.</li>
            <li><b>2 Extra Weeks</b> of advanced on-site training 3 months later (Free of charge).</li>
            <li><b>1 Full Month in Europe</b> at the SOMA factory to elevate your team to world-class professionals.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="background-color: #FEF2F2; padding: 30px; border-radius: 10px; border: 2px solid #DC2626; text-align: center;">
        <h2 style="color: #991B1B;">⚔️ The Ultimate Proof: The SOMA Challenge</h2>
        <p style="font-size: 1.2rem;">Because true trust is built on experience, not ink on paper, we extend an open invitation to our factory. <b>Bring your most complex and difficult printing designs.</b> Watch us set it up and print HD quality with near-zero waste in minutes.</p>
        <h3 style="color: #DC2626;">Trust what you see, not just a brand name.</h3>
    </div>
    """, unsafe_allow_html=True)
