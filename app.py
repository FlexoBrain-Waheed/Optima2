import streamlit as st

# إعدادات الصفحة لتكون واسعة ومناسبة للعرض
st.set_page_config(page_title="Strategic Investment Evaluation", page_icon="📈", layout="wide")

# شريحة الغلاف (العنوان الرئيسي)
st.title("Strategic Investment Evaluation")
st.subheader("SOMA Optima 2 vs. W&H Alphaflex")
st.markdown("**Presented by:** Flexo Consultation Services | Waheed Alkarraein")
st.markdown("---")

# إنشاء نظام التبويبات لتعمل كأنها "شرائح" العرض التقديمي
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "1. Market Positioning", 
    "2. Reliability", 
    "3. Smart Engineering", 
    "4. Ergonomics", 
    "5. Total Cost (TCO)", 
    "6. The Challenge"
])

# الشريحة الأولى
with tab1:
    st.header("The Paradigm Shift: Flagship vs. Economy")
    st.info("**The Strategic Question:** Does it make sense to pay over €2 Million for a stripped-down economy model when you can own top-tier technology for the same budget?")
    col1, col2 = st.columns(2)
    with col1:
        st.success("#### ✅ SOMA Optima 2 (Flagship Class)\n"
                   "The absolute pinnacle of SOMA’s technology. A fully-equipped, premium machine.")
    with col2:
        st.warning("#### ⚠️ W&H Alphaflex (Economy Class)\n"
                   "Positioned as an 'Entry-Level' press. Stripped down to fit lower budgets.")

# الشريحة الثانية
with tab2:
    st.header("Proven Reliability vs. The Testing Ground")
    st.error("**Conclusion:** Never let your factory be the testing ground for a new economy model.")
    st.markdown("""
    * **SOMA Optima 2:** A mature, 100% reliable platform. Built on deep operational experience with zero structural flaws.
    * **W&H Alphaflex:** Newly launched in mid-2024. Its economical structure is largely untested in harsh, long-term operational environments.
    """)

# الشريحة الثالثة
with tab3:
    st.header("Smart Engineering for Maximum Profit")
    st.markdown("""
    * **SOMA Optima 2 (Bounce Killer):** Uses aerospace-grade Carbon Composite mandrels and integrated Ink Thermal Stabilization (ITS).
    * **W&H Alphaflex:** Relies on heavy steel mandrels and lacks an integrated cooling system, leading to potential bouncing and color instability.
    * **Zero Waste Guarantee:** SOMA's IRIS topography-based setup drastically reduces setup time and material waste compared to semi-automatic systems.
    """)

# الشريحة الرابعة
with tab4:
    st.header("Empowering Your Workforce (Operator Ergonomics)")
    st.success("**The Result:** SOMA dramatically reduces physical strain on operators, ensuring faster, safer, and much more efficient manual roll changes every single shift.")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### ✅ SOMA Optima 2")
        st.markdown("Features **19 kg Lightweight Air Shafts**.")
    with col2:
        st.markdown("### ⚠️ W&H Alphaflex")
        st.markdown("Uses standard, **heavy mechanical shafts**.")

# الشريحة الخامسة (الجدول المالي)
with tab5:
    st.header("The Hidden Costs of 'Base' Offers")
    st.markdown("""
    The SOMA Optima 2 is a complete **'Turn-Key'** solution ready for immediate high-quality production. 
    The competitor's offer requires significant hidden additions to reach the same operational level.
    """)
    
    # جدول المقارنة باستخدام Streamlit Markdown
    st.markdown("""
    | Feature / Equipment | SOMA Optima 2 (Turn-Key) | W&H Alphaflex (Base Offer) | Estimated Hidden Cost (If W&H is chosen) |
    | :--- | :--- | :--- | :--- |
    | **Ink Cooling (ITS)** | ✅ Included & Integrated | ❌ Customer Responsibility | **~ € 50,000** |
    | **100% Camera** | ✅ Included (iPQ Check) | ❌ Optional Add-on | **~ € 71,000** |
    | **Sleeves & Aniloxes** | ✅ Included (1 Full Set: 8+8) | ❌ Customer Responsibility | **~ € 50,000** |
    | **Payment Terms** | ✅ Flexible Wire Transfers | ❌ 75% Letter of Credit (L/C) | **Bank Fees + Tied-up Cash** |
    """)

# الشريحة السادسة
with tab6:
    st.header("A Complete Partnership & The SOMA Challenge")
    st.markdown("""
    ### 🤝 Exclusive
