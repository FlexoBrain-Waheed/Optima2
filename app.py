import streamlit as st
import pandas as pd
import altair as alt

# 1. Page Configuration
st.set_page_config(page_title="Executive Investment Evaluation", layout="wide", initial_sidebar_state="expanded")

# ==========================================
# 🔒 نظام الحماية بكلمة المرور (Login System)
# ==========================================
SECRET_PASSWORD = "Ymtaco2026"

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.markdown("""
        <style>
        .stTextInput input { text-align: center; font-size: 1.2rem; }
        </style>
    """, unsafe_allow_html=True)
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: #1E3A8A; font-family: sans-serif;'>🔒 Confidential Executive Dashboard <br> منصة التقييم الاستثماري المغلقة</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #64748B; font-size: 1.1rem;'>Please enter the password / يرجى إدخال كلمة المرور</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        pwd = st.text_input("Password", type="password", label_visibility="collapsed", placeholder="Enter Password / أدخل كلمة المرور...")
        if st.button("Access Dashboard / دخول ➔", use_container_width=True):
            if pwd == SECRET_PASSWORD:
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("Incorrect Password! / كلمة المرور غير صحيحة ❌")
    st.stop()
# ==========================================

# 2. Language Selection
lang = st.sidebar.radio("🌐 Select Language / اختر اللغة:", ["English", "العربية"])
st.sidebar.markdown("---")

# Dynamic CSS based on language
if lang == "العربية":
    direction = "rtl"
    text_align = "right"
    font_family = "'Tajawal', sans-serif"
    css_import = "@import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700;900&display=swap');"
    sidebar_align = "rtl"
else:
    direction = "ltr"
    text_align = "left"
    font_family = "'Roboto', sans-serif"
    css_import = "@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700;900&display=swap');"
    sidebar_align = "ltr"

st.markdown(f"""
    <style>
    {css_import}
    html, body, [class*="css"] {{
        font-family: {font_family};
        direction: {direction};
        text-align: {text_align};
    }}
    [data-testid="stSidebar"] {{
        direction: {sidebar_align};
    }}
    .executive-title {{ font-size: 2.2rem; font-weight: 900; color: #0F172A; border-bottom: 3px solid #1E3A8A; padding-bottom: 10px; margin-bottom: 20px; }}
    .data-card {{ background-color: #F8FAFC; border-top: 5px solid #1E3A8A; padding: 20px; margin-bottom: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); border-radius: 8px; height: 100%; }}
    .corp-table {{ width: 100%; border-collapse: collapse; margin-bottom: 30px; font-size: 1.05rem; text-align: {text_align}; direction: {direction}; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }}
    .corp-table th {{ background-color: #1E3A8A; color: #FFFFFF; padding: 12px; text-align: {text_align}; border: 1px solid #CBD5E1; font-weight: 700; }}
    .corp-table td {{ padding: 12px; border: 1px solid #CBD5E1; color: #1E293B; }}
    .corp-table tr:nth-child(even) {{ background-color: #F8FAFC; }}
    .highlight-adv {{ color: #0F172A; font-weight: 700; background-color: #E2E8F0; border-left: 4px solid #1E3A8A !important; }}
    .highlight-mid {{ color: #334155; font-weight: 500; background-color: #F1F5F9; }}
    .highlight-dis {{ color: #475569; font-weight: 400; background-color: #FFFFFF; }}
    .total-investment {{ font-size: 1.8rem; font-weight: 900; color: #FFFFFF; text-align: center; background-color: #1E3A8A; padding: 20px; border-radius: 8px; margin-top: 20px; }}
    .winner-cell {{ font-weight: 900; color: #059669; background-color: #D1FAE5; text-align: center; border: 2px solid #059669 !important; }}
    .winner-cell-shared {{ font-weight: 700; color: #1E3A8A; background-color: #DBEAFE; text-align: center; border: 1px solid #93C5FD !important; }}
    .winner-cell-tie {{ font-weight: 600; color: #475569; background-color: #F1F5F9; text-align: center; border: 1px solid #CBD5E1 !important; }}
    .section-header {{ background-color: #334155 !important; color: white !important; font-size: 1.15rem; font-weight: bold; text-align: center !important; }}
    </style>
""", unsafe_allow_html=True)

# 3. Sidebar Navigation
nav_options = {
    "English": [
        "1. Executive Summary", 
        "2. Engineering & Performance", 
        "3. Operational Efficiency", 
        "4. OPEX & Service Policy", 
        "5. Total Cost of Ownership (TCO)", 
        "6. Turn-Key Investment", 
        "7. Factory Acceptance & Training",
        "8. S-Mount Automation ROI",
        "9. IRIS vs smartGPS Tech",
        "10. Standard Value Battlecard 🏆"
    ],
    "العربية": [
        "1. الملخص التنفيذي", 
        "2. التقييم الهندسي والأداء", 
        "3. الكفاءة التشغيلية", 
        "4. سياسة الصيانة والتشغيل (OPEX)", 
        "5. التكلفة الإجمالية للملكية (TCO)", 
        "6. استثمار المشروع المتكامل", 
        "7. اختبار المصنع والتدريب",
        "8. العائد الاستثماري للماونتر",
        "9. تقنية IRIS مقابل smartGPS",
        "10. المواجهة الشاملة والمواصفات 🏆"
    ]
}

page_selection = st.sidebar.radio("Navigation / الفهرس:" if lang == "English" else "فهرس التقرير:", nav_options[lang])

st.sidebar.markdown("---")
if lang == "English":
    st.sidebar.markdown("**Prepared For:**\nYmtaco for Trading and Investment Ltd.\n\n**Prepared By:**\nWaheed Alkarraein\nNexFlexo | SOMA")
else:
    st.sidebar.markdown("**تم الإعداد لصالح:**\nإدارة شركة Ymtaco للتجارة والاستثمار\n\n**إعداد التقرير:**\nوحيد الكراعين\nNexFlexo | SOMA")

# ==========================================
# Page 1: Executive Summary
# ==========================================
if page_selection in ["1. Executive Summary", "1. الملخص التنفيذي"]:
    if lang == "English":
        st.markdown('<div class="executive-title">1. Executive Summary: Objective Investment Benchmark</div>', unsafe_allow_html=True)
        st.markdown("""This report provides an objective technical and financial evaluation for the upcoming flexible packaging capital investment. The analysis benchmarks the **SOMA OPTIMA2** against two primary market alternatives: the **BOBST Expert CI** and the **W&H Alphaflex**.""")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("""
            <div class="data-card" style="border-top-color: #1E3A8A;">
                <h3 style="color: #1E3A8A; margin-top: 0;">SOMA OPTIMA 2</h3>
                <p><strong>Classification:</strong> High-Performance Flagship.</p>
                <p><strong>Performance:</strong> Upgraded to 600 m/min with a robust 130mm Cast-Iron frame.</p>
                <p><strong>Strategy:</strong> Engineered for rapid, ergonomic changeovers with comprehensive base inclusions, eliminating hidden CAPEX surprises.</p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class="data-card" style="border-top-color: #64748B;">
                <h3 style="color: #475569; margin-top: 0;">BOBST Expert CI</h3>
                <p><strong>Classification:</strong> Mainstream Standard.</p>
                <p><strong>Performance:</strong> Limited to 500 m/min operating speed.</p>
                <p><strong>Strategy:</strong> Offers a base machine requiring significant financial add-ons (TCO) for basic operational readiness (Cameras, Sleeves, Corona, etc.).</p>
            </div>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown("""
            <div class="data-card" style="border-top-color: #94A3B8;">
                <h3 style="color: #64748B; margin-top: 0;">W&H Alphaflex</h3>
                <p><strong>Classification:</strong> Economy / Entry-Level.</p>
                <p><strong>Performance:</strong> 500 m/min limit on lightweight frames.</p>
                <p><strong>Strategy:</strong> Designed to lower initial quotation values by stripping standard features, shifting the financial burden to post-purchase upgrades.</p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown('<div class="executive-title">1. الملخص التنفيذي: التقييم الاستثماري المحايد</div>', unsafe_allow_html=True)
        st.markdown("""يقدم هذا التقرير تقييماً فنياً ومالياً موضوعياً لقرار الاستثمار القادم. تقارن الدراسة بين ماكينة **SOMA OPTIMA2** كمعيار للأداء العالي، في مواجهة بديلين في السوق: **BOBST Expert CI** و **W&H Alphaflex**.""")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("""
            <div class="data-card" style="border-top-color: #1E3A8A;">
                <h3 style="color: #1E3A8A; margin-top: 0;">SOMA OPTIMA 2</h3>
                <p><strong>التصنيف السوقي:</strong> الفئة الرائدة (الأداء العالي).</p>
                <p><strong>الأداء الفعلي:</strong> تمت الترقية لسرعة 600 م/دقيقة بهيكل معدني جبار من الحديد الزهر (Cast-Iron) بسماكة 130 ملم.</p>
                <p><strong>الاستراتيجية:</strong> مصممة للتشغيل السريع والمريح، مع تضمين كافة التجهيزات الأساسية في العرض المبدئي لمنع أي صدمات مالية لاحقة.</p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class="data-card" style="border-top-color: #64748B;">
                <h3 style="color: #475569; margin-top: 0;">BOBST Expert CI</h3>
                <p><strong>التصنيف السوقي:</strong> الفئة القياسية المعتمدة.</p>
                <p><strong>الأداء الفعلي:</strong> مقيدة بسرعة تشغيل قصوى تبلغ 500 م/دقيقة.</p>
                <p><strong>الاستراتيجية:</strong> تقدم الماكينة الأساسية مجردة، مما يتطلب إضافات مالية هائلة (TCO) لتعمل بكفاءة (الكاميرات، السليفات، الكورونا، رافعات الرولات، الخ).</p>
            </div>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown("""
            <div class="data-card" style="border-top-color: #94A3B8;">
                <h3 style="color: #64748B; margin-top: 0;">W&H Alphaflex</h3>
                <p><strong>التصنيف السوقي:</strong> الفئة الاقتصادية (للمبتدئين).</p>
                <p><strong>الأداء الفعلي:</strong> سرعة 500 م/دقيقة على هيكل خفيف.</p>
                <p><strong>الاستراتيجية:</strong> مصممة لخفض السعر المبدئي (CAPEX) عبر تجريد الماكينة من أنظمة الأتمتة الأساسية، مما يخفي التكلفة التشغيلية الحقيقية.</p>
            </div>
            """, unsafe_allow_html=True)

# ==========================================
# Page 2: Structural & Engineering Superiority
# ==========================================
elif page_selection in ["2. Engineering & Performance", "2. التقييم الهندسي والأداء"]:
    if lang == "English":
        st.markdown('<div class="executive-title">2. Engineering Specifications & Performance Benchmarking</div>', unsafe_allow_html=True)
        st.markdown("""A tri-lateral comparative analysis of core mechanical properties and operator ergonomics across the three platforms.""")
        
        st.markdown("""
        <table class="corp-table">
            <tr><th>Engineering Specification</th><th>SOMA Optima 2 (Upgraded)</th><th>BOBST Expert CI</th><th>W&H Alphaflex</th></tr>
            <tr><td><strong>Max Production Speed</strong></td><td class="highlight-adv">600 m/min</td><td class="highlight-mid">500 m/min</td><td class="highlight-dis">500 m/min</td></tr>
            <tr><td><strong>Print Repeat Range</strong></td><td class="highlight-adv">360 - 850 mm (up to 900)</td><td class="highlight-mid">370 - 800 mm</td><td class="highlight-dis">370 - 800 mm</td></tr>
            <tr><td><strong>Machine Frame Material</strong></td><td class="highlight-adv">130 mm Cast-Iron (Vibration absorbing)</td><td class="highlight-mid">100 mm Steel</td><td class="highlight-dis">55-60 mm Steel</td></tr>
            <tr><td><strong>Drying Tunnel Length</strong></td><td class="highlight-adv">6.0 Meters (23 Nozzles)</td><td class="highlight-mid">4.5 Meters</td><td class="highlight-dis">5.7 Meters</td></tr>
            <tr><td><strong>Operator Ergonomics (Height)</strong></td><td class="highlight-adv">Accessible from floor (Easy changeovers)</td><td class="highlight-mid">Excessively high (Hard to reach decks)</td><td class="highlight-dis">High structure</td></tr>
            <tr><td><strong>Process Visibility (Decks)</strong></td><td class="highlight-adv">Transparent Full Glass Windows</td><td class="highlight-mid">Partially Closed Covers</td><td class="highlight-dis">Closed (No Glass)</td></tr>
            <tr><td><strong>Water Cooling (Drive Side)</strong></td><td class="highlight-adv">✅ Included</td><td class="highlight-dis">❌ Missing</td><td class="highlight-dis">❌ Missing</td></tr>
        </table>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<h4 style="color: #1E3A8A; text-align: center;">🚀 Max Production Speed (m/min)</h4>', unsafe_allow_html=True)
            speed_data = pd.DataFrame({'Machine': ['SOMA Optima 2', 'BOBST Expert CI', 'W&H Alphaflex'], 'Speed (m/min)': [600, 500, 500]})
            chart_speed = alt.Chart(speed_data).mark_bar(size=50).encode(
                x=alt.X('Machine:N', title='', sort=None),
                y=alt.Y('Speed (m/min):Q', title='Max Speed (m/min)', scale=alt.Scale(domain=[0, 700])),
                color=alt.Color('Machine:N', scale=alt.Scale(domain=['SOMA Optima 2', 'BOBST Expert CI', 'W&H Alphaflex'], range=['#1E3A8A', '#64748B', '#94A3B8']), legend=None)
            ).properties(height=300)
            st.altair_chart(chart_speed, use_container_width=True)

        with col2:
            st.markdown('<h4 style="color: #1E3A8A; text-align: center;">👁️ Operator Visibility & Ergonomics Index (%)</h4>', unsafe_allow_html=True)
            df_ergo = pd.DataFrame({
                'Machine': ['SOMA Optima 2', 'BOBST Expert CI', 'W&H Alphaflex'],
                'Ergonomic Score': [100, 60, 40]
            })
            chart_ergo = alt.Chart(df_ergo).mark_bar(size=50).encode(
                x=alt.X('Machine:N', title='', sort=None),
                y=alt.Y('Ergonomic Score:Q', title='Efficiency & Vision Score (%)'),
                color=alt.Color('Machine:N', scale=alt.Scale(domain=['SOMA Optima 2', 'BOBST Expert CI', 'W&H Alphaflex'], range=['#1E3A8A', '#64748B', '#94A3B8']), legend=None)
            ).properties(height=300)
            st.altair_chart(chart_ergo, use_container_width=True)

    else:
        st.markdown('<div class="executive-title">2. التقييم الهندسي والأداء التشغيلي</div>', unsafe_allow_html=True)
        st.markdown("""تحليل مقارن دقيق للخصائص الميكانيكية الأساسية وبيئة عمل المشغل (Ergonomics) بين المنصات الثلاث.""")
        
        st.markdown("""
        <table class="corp-table">
            <tr><th>المواصفات الهندسية</th><th>SOMA Optima 2 (الإصدار المُرقى)</th><th>BOBST Expert CI</th><th>W&H Alphaflex</th></tr>
            <tr><td><strong>السرعة الإنتاجية القصوى</strong></td><td class="highlight-adv">600 متر / دقيقة</td><td class="highlight-mid">500 متر / دقيقة</td><td class="highlight-dis">500 متر / دقيقة</td></tr>
            <tr><td><strong>نطاق تكرار الطباعة (Repeat)</strong></td><td class="highlight-adv">360 - 850 ملم (يصل لـ 900)</td><td class="highlight-mid">370 - 800 ملم</td><td class="highlight-dis">370 - 800 ملم</td></tr>
            <tr><td><strong>مادة جدار الهيكل وسماكته</strong></td><td class="highlight-adv">حديد زهر (Cast-Iron) بسماكة 130 ملم</td><td class="highlight-mid">حديد صلب 100 ملم</td><td class="highlight-dis">حديد صلب 55-60 ملم</td></tr>
            <tr><td><strong>طول نفق التجفيف الرئيسي</strong></td><td class="highlight-adv">6.0 أمتار (23 فوهة)</td><td class="highlight-mid">4.5 متر</td><td class="highlight-dis">5.7 متر (17 فوهة)</td></tr>
            <tr><td><strong>بيئة العمل (تغيير الطلبيات)</strong></td><td class="highlight-adv">في متناول اليد من الأرض مباشرة</td><td class="highlight-mid">مرتفعة جداً ومجهدة للعمال</td><td class="highlight-dis">هيكل مرتفع</td></tr>
            <tr><td><strong>الرؤية البصرية لوحدات الطباعة</strong></td><td class="highlight-adv">نوافذ زجاجية شفافة بالكامل</td><td class="highlight-mid">أغطية معدنية شبه مغلقة</td><td class="highlight-dis">أغطية مغلقة (بدون زجاج نهائياً)</td></tr>
            <tr><td><strong>نظام التبريد المائي بجهة الإدارة</strong></td><td class="highlight-adv">✅ مشمول</td><td class="highlight-dis">❌ غير مشمول</td><td class="highlight-dis">❌ غير مشمول</td></tr>
        </table>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<h4 style="color: #1E3A8A; text-align: center;">🚀 السرعة الإنتاجية القصوى المعتمدة (متر/دقيقة)</h4>', unsafe_allow_html=True)
            speed_data = pd.DataFrame({'الماكينة': ['SOMA Optima 2', 'BOBST Expert CI', 'W&H Alphaflex'], 'السرعة': [600, 500, 500]})
            chart_speed = alt.Chart(speed_data).mark_bar(size=50).encode(
                x=alt.X('الماكينة:N', title='', sort=None),
                y=alt.Y('السرعة:Q', title='السرعة القصوى (م/دقيقة)', scale=alt.Scale(domain=[0, 700])),
                color=alt.Color('الماكينة:N', scale=alt.Scale(domain=['SOMA Optima 2', 'BOBST Expert CI', 'W&H Alphaflex'], range=['#1E3A8A', '#64748B', '#94A3B8']), legend=None)
            ).properties(height=300)
            st.altair_chart(chart_speed, use_container_width=True)

        with col2:
            st.markdown('<h4 style="color: #1E3A8A; text-align: center;">👁️ مؤشر راحة المشغل وشفافية المراقبة (%)</h4>', unsafe_allow_html=True)
            df_ergo = pd.DataFrame({
                'الماكينة': ['SOMA Optima 2', 'BOBST Expert CI', 'W&H Alphaflex'],
                'المؤشر': [100, 60, 40]
            })
            chart_ergo = alt.Chart(df_ergo).mark_bar(size=50).encode(
                x=alt.X('الماكينة:N', title='', sort=None),
                y=alt.Y('المؤشر:Q', title='مؤشر الكفاءة والرؤية (%)'),
                color=alt.Color('الماكينة:N', scale=alt.Scale(domain=['SOMA Optima 2', 'BOBST Expert CI', 'W&H Alphaflex'], range=['#1E3A8A', '#64748B', '#94A3B8']), legend=None)
            ).properties(height=300)
            st.altair_chart(chart_ergo, use_container_width=True)

# ==========================================
# Page 3: Operational Efficiency (Wash-up & Ink) 
# ==========================================
elif page_selection in ["3. Operational Efficiency", "3. الكفاءة التشغيلية"]:
    if lang == "English":
        st.markdown('<div class="executive-title">3. Operational Efficiency & Fluid Management</div>', unsafe_allow_html=True)
        st.markdown("""Evaluation of fluid management systems and their impact on daily consumable optimization.""")
        
        st.markdown('<h3 style="color: #1E3A8A; margin-top: 20px;">💧 Wash-up Cycle Data</h3>', unsafe_allow_html=True)
        st.markdown("""
        <table class="corp-table">
            <tr>
                <th>Wash Cycle Parameter</th>
                <th>SOMA Optima 2 (Inkstorm)</th>
                <th>BOBST Expert CI (smartWASH/Standard)</th>
                <th>W&H Alphaflex (Turboclean S)</th>
            </tr>
            <tr>
                <td><strong>Fast Wash Time / Solvent Used</strong></td>
                <td class="highlight-adv">5 Minutes / 5 Liters</td>
                <td class="highlight-mid">Standard Cycle dependent</td>
                <td class="highlight-dis">4 Minutes / 12 Liters</td>
            </tr>
            <tr>
                <td><strong>Normal Wash Time / Solvent Used</strong></td>
                <td class="highlight-adv">7 Minutes / 10 Liters</td>
                <td class="highlight-mid">~ 6-8 Minutes / ~ 10-12 Liters</td>
                <td class="highlight-dis">4 Minutes / 14 Liters</td>
            </tr>
            <tr>
                <td><strong>System Architecture</strong></td>
                <td class="highlight-adv">Open & Customizable</td>
                <td class="highlight-mid">Standard Programmed</td>
                <td class="highlight-dis">Restricted Parameters</td>
            </tr>
        </table>
        """, unsafe_allow_html=True)
        
        st.markdown('<h3 style="color: #1E3A8A; margin-top: 30px;">🎨 SOMA Ink Cartridge System: Spot Color Optimization</h3>', unsafe_allow_html=True)
        
        col_text, col_chart = st.columns([1.2, 1])
        with col_text:
            st.markdown("""
            <div class="data-card">
                <p style="font-size: 1.1rem;">A precise volume management system engineered to optimize premium and spot colors.</p>
                <ul style="line-height: 1.8;">
                    <li><b>Micro-Volume Operation:</b> Requires a maximum operating volume of <b>4.5 Liters</b>.</li>
                    <li><b>Direct DBC Connection (15cm):</b> Ultra-short 15cm connections to the DBC result in minimal residual ink volume.</li>
                    <li><b>Premium Ink Efficiency:</b> Drastically reduces material costs when processing expensive metallic or spot colors.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
        with col_chart:
            df_ink = pd.DataFrame({
                'System': ['Traditional Architecture (W&H/BOBST)', 'SOMA Ink Cartridge (15cm)'],
                'Residual Ink Waste (Liters/Job)': [3.5, 0.2]
            })
            chart_ink = alt.Chart(df_ink).mark_bar(size=40).encode(
                x=alt.X('Residual Ink Waste (Liters/Job):Q', title='Residual Ink per Job (Liters)'),
                y=alt.Y('System:N', sort='-x', title=''),
                color=alt.condition(alt.datum.System == 'SOMA Ink Cartridge (15cm)', alt.value('#1E3A8A'), alt.value('#94A3B8')),
                tooltip=['System', 'Residual Ink Waste (Liters/Job)']
            ).properties(height=250, title="Residual Ink Assessment (Per Spot Color)")
            st.altair_chart(chart_ink, use_container_width=True)

    else:
        st.markdown('<div class="executive-title">3. الكفاءة التشغيلية وإدارة السوائل</div>', unsafe_allow_html=True)
        st.markdown("""تقييم أنظمة الغسيل وإدارة الأحبار وأثرها على تحسين استهلاك المواد اليومية (المذيبات والأحبار باهظة الثمن).""")
        
        st.markdown('<h3 style="color: #1E3A8A; margin-top: 20px;">💧 بيانات دورة الغسيل واستهلاك المذيبات (Solvents)</h3>', unsafe_allow_html=True)
        st.markdown("""
        <table class="corp-table">
            <tr>
                <th>معايير دورة الغسيل</th>
                <th>SOMA Optima 2 (نظام Inkstorm)</th>
                <th>BOBST Expert CI (نظام قياسي)</th>
                <th>W&H Alphaflex (نظام Turboclean)</th>
            </tr>
            <tr>
                <td><strong>الغسيل السريع (الوقت / الاستهلاك)</strong></td>
                <td class="highlight-adv">5 دقائق / 5 لتر فقط</td>
                <td class="highlight-mid">يعتمد على الدورة القياسية</td>
                <td class="highlight-dis">4 دقائق / 12 لتر (هدر عالي)</td>
            </tr>
            <tr>
                <td><strong>الغسيل العادي (الوقت / الاستهلاك)</strong></td>
                <td class="highlight-adv">7 دقائق / 10 لتر</td>
                <td class="highlight-mid">~ 6-8 دقائق / ~ 10-12 لتر</td>
                <td class="highlight-dis">4 دقائق / 14 لتر</td>
            </tr>
            <tr>
                <td><strong>هيكلية النظام البرمجية</strong></td>
                <td class="highlight-adv">مفتوح وقابل للضبط حسب كيمياء الحبر</td>
                <td class="highlight-mid">مُبرمج قياسياً</td>
                <td class="highlight-dis">معايير مسبقة الضبط / مقيدة</td>
            </tr>
        </table>
        """, unsafe_allow_html=True)
        
        st.markdown('<h3 style="color: #1E3A8A; margin-top: 30px;">🎨 نظام خراطيش الحبر (Ink Cartridge): تحسين استهلاك الألوان الخاصة</h3>', unsafe_allow_html=True)
        
        col_text, col_chart = st.columns([1.2, 1])
        with col_text:
            st.markdown("""
            <div class="data-card">
                <p style="font-size: 1.1rem;">نظام دقيق لإدارة الحجم مصمم لتقليل التكلفة عند طباعة الألوان الخاصة (Spot Colors).</p>
                <ul style="line-height: 1.8;">
                    <li><b>التشغيل بالحجم الدقيق:</b> يتطلب حجم تشغيل أقصى يبلغ <b>4.5 لتر فقط</b>.</li>
                    <li><b>اتصال مباشر بـ 15 سم:</b> يستخدم خراطيم قصيرة جداً (15 سم) متصلة مباشرة بغرفة الشفرات (DBC)، مما يقضي على هدر الحبر المتبقي داخل الخراطيم الطويلة.</li>
                    <li><b>كفاءة الأحبار الممتازة:</b> فعال جداً في خفض تكاليف المواد عند استخدام الألوان المعدنية (الذهبي، الفضي) باهظة الثمن.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
        with col_chart:
            df_ink_ar = pd.DataFrame({
                'النظام': ['الأنظمة التقليدية (W&H / BOBST)', 'نظام SOMA خراطيش (خراطيم 15 سم)'],
                'الحبر المتبقي (لتر)': [3.5, 0.2]
            })
            chart_ink_ar = alt.Chart(df_ink_ar).mark_bar(size=40).encode(
                x=alt.X('الحبر المتبقي (لتر):Q', title='متوسط الحبر المتبقي لكل طلبية (لتر)'),
                y=alt.Y('النظام:N', sort='-x', title=''),
                color=alt.condition(alt.datum.النظام == 'نظام SOMA خراطيش (خراطيم 15 سم)', alt.value('#1E3A8A'), alt.value('#94A3B8')),
                tooltip=['النظام', 'الحبر المتبقي (لتر)']
            ).properties(height=250, title="تقييم هدر الحبر المتبقي (للون الواحد)")
            st.altair_chart(chart_ink_ar, use_container_width=True)

# ==========================================
# Page 4: Long-Term Opex & Service
# ==========================================
elif page_selection in ["4. OPEX & Service Policy", "4. سياسة الصيانة والتشغيل (OPEX)"]:
    if lang == "English":
        st.markdown('<div class="executive-title">4. Operational Expenditure (OPEX) & Service Policy</div>', unsafe_allow_html=True)
        st.markdown("""Assessment of post-warranty operational costs based on manufacturer service frameworks.""")
        
        st.markdown("""
        <table class="corp-table">
            <tr><th>Operational Aspect</th><th>SOMA Framework</th><th>BOBST Framework</th><th>W&H Framework</th></tr>
            <tr><td><strong>Spare Parts Sourcing</strong></td><td class="highlight-adv">Open Source (Much lower prices)</td><td class="highlight-mid">Premium Pricing</td><td class="highlight-dis">Restricted Pricing</td></tr>
            <tr><td><strong>Service Cost Structure</strong></td><td class="highlight-adv">Standardized intervention rates</td><td class="highlight-mid">High Premium tier rates</td><td class="highlight-dis">High Premium service tier rates</td></tr>
            <tr><td><strong>Asset Retrofitting</strong></td><td class="highlight-adv">Designed for high upgradeability</td><td class="highlight-mid">Rigid </td><td class="highlight-dis">Rigid specification</td></tr>
            <tr><td><strong>Innovation Rate</strong></td><td class="highlight-adv">High frequency of updates</td><td class="highlight-mid">Standard cycle</td><td class="highlight-dis">Standard cycle</td></tr>
        </table>
        """, unsafe_allow_html=True)
    else:
        st.markdown('<div class="executive-title">4. النفقات التشغيلية (OPEX) وسياسة الصيانة</div>', unsafe_allow_html=True)
        st.markdown("""تقييم تكاليف التشغيل لما بعد فترة الضمان بناءً على الأطر الخدمية وتقنيات الاستدامة للشركات الثلاث.""")
        
        st.markdown("""
        <table class="corp-table">
            <tr><th>جانب التشغيل والصيانة</th><th>إطار عمل SOMA</th><th>إطار عمل BOBST</th><th>إطار عمل W&H</th></tr>
            <tr><td><strong>تسعير ومصادر قطع الغيار</strong></td><td class="highlight-adv">منصة مفتوحة (أسعار أقل بكثير)</td><td class="highlight-mid">تسعير احتكاري (Premium)</td><td class="highlight-dis">تسعير احتكاري (Premium)</td></tr>
            <tr><td><strong>هيكل تكاليف الخدمة</strong></td><td class="highlight-adv">معدلات تدخل وصيانة قياسية عادلة</td><td class="highlight-mid">رسوم خدمة وتدخل مرتفعة جداً</td><td class="highlight-dis">رسوم خدمة وتدخل مرتفعة جداً</td></tr>
            <tr><td><strong>ترقية الأصول (Retrofit)</strong></td><td class="highlight-adv">قابلية هائلة للتحديث والترقية المباشرة</td><td class="highlight-mid">نظام صلب يصعب ترقيته</td><td class="highlight-dis">نظام صلب يصعب ترقيته</td></tr>
            <tr><td><strong>معدل الابتكار التكنولوجي</strong></td><td class="highlight-adv">معدل ابتكار واستجابة عالي جداً</td><td class="highlight-mid">دورة ابتكار بطيئة</td><td class="highlight-dis">دورة ابتكار بطيئة</td></tr>
        </table>
        """, unsafe_allow_html=True)

# ==========================================
# Page 5: TCO Hidden Costs
# ==========================================
elif page_selection in ["5. Total Cost of Ownership (TCO)", "5. التكلفة الإجمالية للملكية (TCO)"]:
    if lang == "English":
        st.markdown('<div class="executive-title">5. Total Cost of Ownership (TCO) Analysis</div>', unsafe_allow_html=True)
        st.markdown("""A financial alignment analyzing the initial base configuration against the necessary additions required to achieve equivalent operational capability.""")
        
        data = pd.DataFrame({
            'Equipment Add-on': ['100% Camera', 'Corona + In-feed Unit', 'Sleeves & Aniloxes', 'ALU/PE Kit (Spreader/Anodized)', 'Lifts (Unwind/Rewind)', 'Push-off Device', 'Insetter (Reprint)'], 
            'Estimated Value (€)': [70000, 55000, 55000, 50000, 30000, 20000, 10000]
        })
        chart = alt.Chart(data).mark_bar(color='#64748B', cornerRadiusEnd=4).encode(
            x=alt.X('Estimated Value (€):Q', title='Estimated Missing Value (€)'), y=alt.Y('Equipment Add-on:N', sort='-x', title=''), tooltip=['Equipment Add-on', 'Estimated Value (€)']
        ).properties(height=350, title="Valuation of Necessary Add-ons Missing from BOBST Expert CI")
        st.altair_chart(chart, use_container_width=True)

        st.markdown("""
        <table class="corp-table">
            <tr><th>Operational Requirement</th><th>SOMA Optima 2</th><th>BOBST Expert CI</th><th>W&H Alphaflex</th></tr>
            <tr><td><strong>Initial Sleeves & Aniloxes (8+8)</strong></td><td class="highlight-adv">✔️ Included</td><td class="highlight-mid">❌ Missing (~ €55k)</td><td class="highlight-dis">❌ Missing (~ €50k)</td></tr>
            <tr><td><strong>100% Inspection Camera</strong></td><td class="highlight-adv">✔️ Included (BST)</td><td class="highlight-mid">❌ Missing (~ €70k)</td><td class="highlight-dis">❌ Missing (~ €71k)</td></tr>
            <tr><td><strong>Corona + In-feed Unit (PE Control)</strong></td><td class="highlight-adv">✔️ Included</td><td class="highlight-mid">❌ Missing (~ €55k)</td><td class="highlight-dis">❌ Missing (~ €55k)</td></tr>
            <tr><td><strong>ALU/PE Handling Kit (Spreader)</strong></td><td class="highlight-adv">✔️ Included</td><td class="highlight-mid">❌ Missing (~ €50k)</td><td class="highlight-dis">❌ Missing (~ €50k)</td></tr>
            <tr><td><strong>Roll Lifts on Unwind/Rewind</strong></td><td class="highlight-adv">✔️ Included</td><td class="highlight-mid">❌ Missing (~ €30k)</td><td class="highlight-dis">❌ Missing (~ €15k)</td></tr>
            <tr><td><strong>Sleeve Push-off Device</strong></td><td class="highlight-adv">✔️ Included</td><td class="highlight-mid">❌ Missing (~ €20k)</td><td class="highlight-dis">❌ Missing (~ €20k)</td></tr>
            <tr><td><strong>Reprint / Insetter Capability</strong></td><td class="highlight-adv">✔️ Included</td><td class="highlight-mid">❌ Missing (~ €10k)</td><td class="highlight-dis">❌ Missing (~ €10k)</td></tr>
        </table>
        """, unsafe_allow_html=True)
        st.info("📊 **Financial Note:** The initial CAPEX of the competitor base models requires critical adjustment. Aligning the BOBST Expert CI to SOMA's standard involves approximately **€ 290,000** in mandatory hardware additions.")
    
    else:
        st.markdown('<div class="executive-title">5. تحليل التكلفة الإجمالية للملكية (TCO) والتكاليف الخفية</div>', unsafe_allow_html=True)
        st.markdown("""مواءمة مالية تفصيلية تحلل العروض المبدئية المجردة مقابل الإضافات الضرورية المطلوبة لتحقيق قدرة تشغيلية متكافئة لخط الإنتاج.""")
        
        data = pd.DataFrame({
            'المعدة المطلوبة': ['كاميرا فحص 100%', 'وحدة كورونا + سحب (In-feed)', 'سليفات وأنيلوكس', 'تجهيزات طباعة ALU/PE', 'رافعات رولات (فك ولف)', 'دفاعة سليفات (Push-off)', 'وحدة طباعة متكررة (Insetter)'], 
            'القيمة التقديرية (يورو)': [70000, 55000, 55000, 50000, 30000, 20000, 10000]
        })
        chart = alt.Chart(data).mark_bar(color='#64748B', cornerRadiusEnd=4).encode(
            x=alt.X('القيمة التقديرية (يورو):Q', title='القيمة المفقودة (يورو)'), y=alt.Y('المعدة المطلوبة:N', sort='-x', title=''), tooltip=['المعدة المطلوبة', 'القيمة التقديرية (يورو)']
        ).properties(height=350, title="حجم التكاليف الخفية والنواقص في عرض BOBST Expert CI لتطابق مواصفات SOMA")
        st.altair_chart(chart, use_container_width=True)

        st.markdown("""
        <table class="corp-table">
            <tr><th>المتطلب التشغيلي</th><th>SOMA Optima 2</th><th>BOBST Expert CI</th><th>W&H Alphaflex</th></tr>
            <tr><td><strong>أطقم السليفات والأنيلوكس (8+8)</strong></td><td class="highlight-adv">✔️ مشمولة بالكامل</td><td class="highlight-mid">❌ غير مشمولة (~ €55,000)</td><td class="highlight-dis">❌ غير مشمولة (~ €50,000)</td></tr>
            <tr><td><strong>كاميرا فحص الجودة 100%</strong></td><td class="highlight-adv">✔️ مشمولة (BST iPQ)</td><td class="highlight-mid">❌ غير مشمولة (~ €70,000)</td><td class="highlight-dis">❌ غير مشمولة (~ €71,000)</td></tr>
            <tr><td><strong>وحدة كورونا + In-feed (لضبط طباعة PE)</strong></td><td class="highlight-adv">✔️ مشمولة بالكامل</td><td class="highlight-mid">❌ غير مشمولة (~ €55,000)</td><td class="highlight-dis">❌ غير مشمولة (~ €55,000)</td></tr>
            <tr><td><strong>تجهيزات طباعة ALU و PE</strong></td><td class="highlight-adv">✔️ مشمولة بالكامل</td><td class="highlight-mid">❌ غير مشمولة (~ €50,000)</td><td class="highlight-dis">❌ غير مشمولة (~ €50,000)</td></tr>
            <tr><td><strong>رافعات رولات هيدروليكية (للفك واللف)</strong></td><td class="highlight-adv">✔️ مشمولة بالكامل</td><td class="highlight-mid">❌ غير مشمولة (~ €30,000)</td><td class="highlight-dis">❌ غير مشمولة (~ €15,000)</td></tr>
            <tr><td><strong>نظام الدفع الآلي للسليفات (Push-off)</strong></td><td class="highlight-adv">✔️ مشمولة بالكامل</td><td class="highlight-mid">❌ غير مشمول (~ €20,000)</td><td class="highlight-dis">❌ غير مشمول (~ €20,000)</td></tr>
            <tr><td><strong>تجهيز الطباعة المتكررة (Reprint/Insetter)</strong></td><td class="highlight-adv">✔️ مشمولة بالكامل</td><td class="highlight-mid">❌ غير مشمول (~ €10,000)</td><td class="highlight-dis">❌ غير مشمول (~ €10,000)</td></tr>
        </table>
        """, unsafe_allow_html=True)
        st.info("📊 **الخلاصة المالية (الصدمة):** العروض المنافسة قدمت ماكينة بهيكل مجرد لتبدو أرخص. لتصل ماكينة BOBST لمستوى التجهيز القياسي في SOMA، سيتكبد المصنع حوالي **290,000 يورو** إضافية كحد أدنى لسد النواقص التشغيلية.")

# ==========================================
# Page 6: Turn-Key Investment
# ==========================================
elif page_selection in ["6. Turn-Key Investment", "6. استثمار المشروع المتكامل"]:
    if lang == "English":
        st.markdown('<div class="executive-title">6. Comprehensive Production Suite Valuation</div>', unsafe_allow_html=True)
        st.markdown("""SOMA provides an integrated production line. Procuring the entire suite from a single technology ecosystem ensures compatibility and activates premium commercial discounting.""")
        st.markdown("""
        <table class="corp-table">
            <tr><th>Asset Category</th><th>Model Specification</th><th>Valuation (EUR)</th></tr>
            <tr><td><strong>Central Impression Flexo Press</strong></td><td>SOMA OPTIMA2 850-1270-8 EG (600 m/min, 6m Tunnel)</td><td>€ 2,480,000</td></tr>
            <tr><td><strong>Automatic Plate Mounter</strong></td><td>SOMA S-MOUNT A 1300 (with IRIS System)</td><td>€ 220,000</td></tr>
            <tr><td><strong>Solventless Laminator</strong></td><td>SOMA LAMIFLEX E 1320 (400 m/min)</td><td>€ 410,000</td></tr>
            <tr><td><strong>Slitter Rewinder</strong></td><td>SOMA PLUTO III.2 1350 (650 m/min)</td><td>€ 242,740</td></tr>
        </table>
        """, unsafe_allow_html=True)
        st.markdown('<div class="total-investment">Total Suite Valuation: € 3,352,740</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="executive-title">6. تقييم خط الإنتاج المتكامل (Turn-Key)</div>', unsafe_allow_html=True)
        st.markdown("""تقدم SOMA خط إنتاج متكامل. شراء الحزمة الكاملة من بيئة تكنولوجية واحدة يضمن التوافق التام ويُفعّل أعلى فئات الخصومات التجارية.""")
        st.markdown("""
        <table class="corp-table">
            <tr><th>فئة الأصل</th><th>المواصفات الدقيقة للموديل</th><th>القيمة (يورو)</th></tr>
            <tr><td><strong>مطبعة فليكسو المركزية</strong></td><td>SOMA OPTIMA2 850-1270-8 EG (سرعة 600، نفق 6 متر)</td><td>€ 2,480,000</td></tr>
            <tr><td><strong>الماونتر الأوتوماتيكي</strong></td><td>SOMA S-MOUNT A 1300 (مزود بنظام IRIS)</td><td>€ 220,000</td></tr>
            <tr><td><strong>ماكينة اللامنيشن</strong></td><td>SOMA LAMIFLEX E 1320 (400 متر/دقيقة)</td><td>€ 410,000</td></tr>
            <tr><td><strong>السلتر (التقطيع)</strong></td><td>SOMA PLUTO III.2 1350 (650 متر/دقيقة)</td><td>€ 242,740</td></tr>
        </table>
        """, unsafe_allow_html=True)
        st.markdown('<div class="total-investment">التقييم الإجمالي للمشروع: € 3,352,740</div>', unsafe_allow_html=True)

# ==========================================
# Page 7: Partnership & FAT
# ==========================================
elif page_selection in ["7. Factory Acceptance & Training", "7. اختبار المصنع والتدريب"]:
    if lang == "English":
        st.markdown('<div class="executive-title">7. Implementation & Verification Protocols</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="data-card">
            <h3 style="color: #1E3A8A; margin-top:0;">Technical Training & Investment Protocol</h3>
            <p style="font-size: 1.1rem; color: #0F172A;"><b>SOMA invests heavily in operator competence, far exceeding standard 5-day competitor offerings:</b></p>
            <ul style="line-height: 1.8; font-size: 1.1rem; color: #334155;">
                <li><b>Competitor Benchmark (BOBST):</b> Offers only 5 days of basic training.</li>
                <li><b>SOMA Phase 1:</b> 10 Days of intensive on-site commissioning and training (Value: €22,000).</li>
                <li><b>SOMA Phase 2:</b> 2 weeks of advanced on-site optimization 3 months post-installation (Free of charge).</li>
                <li><b>SOMA Phase 3:</b> 1 Month of technical immersion for key operators at the SOMA European facility (Free of charge, customer covers travel/stay).</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div style="border: 1px solid #CBD5E1; padding: 30px; border-radius: 8px; background-color: #F8FAFC; margin-top: 30px; text-align: center;">
            <h2 style="color: #1E3A8A; margin-top:0;">Automatic Factory Acceptance Test (F.A.T.)</h2>
            <p style="font-size: 1.1rem; color: #475569; line-height: 1.6;">
                SOMA is the only manufacturer that enforces an automatic, full <b>Factory Acceptance Test (F.A.T.)</b> prior to asset shipment.<br><br>
                The Ymtaco executive and technical teams are invited to our European manufacturing facility to conduct live testing. Complex production designs may be executed to verify registration, setup times, and HD print capability under measured conditions prior to final deployment.
            </p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown('<div class="executive-title">7. بروتوكولات التنفيذ واختبار المصنع</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="data-card">
            <h3 style="color: #1E3A8A; margin-top:0;">الاستثمار في تدريب المشغلين (مقارنة حاسمة)</h3>
            <p style="font-size: 1.1rem; color: #0F172A;"><b>تستثمر SOMA بشكل هائل في كفاءة المشغلين، متجاوزة عروض الـ 5 أيام القياسية للمنافسين:</b></p>
            <ul style="line-height: 1.8; font-size: 1.1rem; color: #334155;">
                <li><b>المنافس (BOBST):</b> يقدم 5 أيام فقط من التدريب الأساسي.</li>
                <li><b>SOMA المرحلة 1:</b> 10 أيام من التدريب والتشغيل المكثف في موقع المصنع (القيمة الفعلية: 22,000 يورو).</li>
                <li><b>SOMA المرحلة 2:</b> أسبوعين من التدريب المتقدم للتحسين بعد 3 أشهر من التركيب (مجاناً بالكامل).</li>
                <li><b>SOMA المرحلة 3:</b> شهر كامل من التدريب الفني المتعمق للمشغلين الأساسيين في منشأة SOMA الأوروبية (التدريب مجاني، العميل يتكفل بالسفر والإقامة فقط).</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div style="border: 1px solid #CBD5E1; padding: 30px; border-radius: 8px; background-color: #F8FAFC; margin-top: 30px; text-align: center;">
            <h2 style="color: #1E3A8A; margin-top:0;">الاختبار الآلي للماكينة قبل الشحن (F.A.T.)</h2>
            <p style="font-size: 1.1rem; color: #475569; line-height: 1.6;">
                SOMA هي الشركة الوحيدة التي تصر على إجراء <b>اختبار قبول المصنع (F.A.T) أوتوماتيكياً</b> بالكامل قبل شحن الأصول.<br><br>
                ندعو الفرق الفنية والتنفيذية في Ymtaco إلى منشأتنا التصنيعية في أوروبا لإجراء اختبارات حية. يمكن تنفيذ تصاميم إنتاجية معقدة للتحقق من دقة التطابق (Registration)، أوقات التجهيز، وجودة الطباعة (HD) تحت ظروف قياسية قبل التوقيع النهائي.
            </p>
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# Page 8: S-Mount ROI (Auto vs. Manual)
# ==========================================
elif page_selection in ["8. S-Mount Automation ROI", "8. العائد الاستثماري للماونتر"]:
    if lang == "English":
        st.markdown('<div class="executive-title">8. S-Mount ROI: Automated vs. Manual Mounting</div>', unsafe_allow_html=True)
        st.markdown("""Analysis based on a simulated output of **150 jobs per month**, averaging **8 colors per job** (1,200 sleeves).""")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### ⏱️ Labor Allocation")
            st.markdown("""
            * **Manual System / Samm 2.0:** Est. 10 mins/color. (1,200 sleeves = **200 Hours/Month**). Requires multiple skilled operators.
            * **S-Mount (Auto):** Est. 1.5 mins/color. (1,200 sleeves = **30 Hours/Month**). Single operator requirement. Equivalent to competitive systems costing over €220k.
            """)
            df_time = pd.DataFrame({'System': ['Manual Mounter', 'SOMA S-Mount (Auto)'], 'Hours/Month': [200, 30]})
            chart_time = alt.Chart(df_time).mark_bar(size=50).encode(
                x=alt.X('System:N', title='', sort=None),
                y=alt.Y('Hours/Month:Q', title='Labor (Hours/Month)'),
                color=alt.condition(alt.datum.System == 'SOMA S-Mount (Auto)', alt.value('#1E3A8A'), alt.value('#94A3B8'))
            ).properties(height=250)
            st.altair_chart(chart_time, use_container_width=True)

        with col2:
            st.markdown("### 🎯 Registration Accuracy Impact")
            st.markdown("""
            * **Error Metric:** Manual mounting historically tracks a **~30% remount rate** due to registration faults.
            * **Downtime Metric:** 45 remounts/month at 30 mins each = **22.5 hours of lost press availability**.
            * **Financial Metric:** At an est. machine rate of €250/hour, downtime costs approach **€5,625 monthly**.
            """)
            df_cost = pd.DataFrame({'System': ['Manual Errors (30%)', 'SOMA S-Mount (0%)'], 'Cost (€/Month)': [5625, 0]})
            chart_cost = alt.Chart(df_cost).mark_bar(size=50).encode(
                x=alt.X('System:N', title='', sort=None),
                y=alt.Y('Cost (€/Month):Q', title='Downtime Cost (€/Month)'),
                color=alt.condition(alt.datum.System == 'SOMA S-Mount (0%)', alt.value('#1E3A8A'), alt.value('#94A3B8'))
            ).properties(height=250)
            st.altair_chart(chart_cost, use_container_width=True)

    else:
        st.markdown('<div class="executive-title">8. دراسة تحليلية: الماونتر الأوتوماتيكي مقابل اليدوي</div>', unsafe_allow_html=True)
        st.markdown("""تحليل مبني على محاكاة إنتاجية تبلغ **150 طلبية شهرياً**، بمتوسط **8 ألوان للطلبية** (1,200 سليف).""")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### ⏱️ تخصيص العمالة والوقت")
            st.markdown("""
            * **النظام اليدوي / SAMM 2.0:** تقدير 10 دقائق/لون. (1,200 سليف = **200 ساعة عمل شهرياً**). يتطلب مشغلين ذوي مهارة عالية.
            * **نظام S-Mount (الآلي):** تقدير 1.5 دقيقة/لون. (1,200 سليف = **30 ساعة عمل شهرياً**). يتطلب مشغلاً واحداً. يكافئ كفاءة أنظمة منافسة يتجاوز سعرها 220 ألف يورو.
            """)
            df_time = pd.DataFrame({'النظام': ['الماونتر اليدوي', 'SOMA S-Mount (آلي)'], 'ساعات/شهر': [200, 30]})
            chart_time = alt.Chart(df_time).mark_bar(size=50).encode(
                x=alt.X('النظام:N', title='', sort=None),
                y=alt.Y('ساعات/شهر:Q', title='العمالة (ساعات/شهر)'),
                color=alt.condition(alt.datum.النظام == 'SOMA S-Mount (آلي)', alt.value('#1E3A8A'), alt.value('#94A3B8'))
            ).properties(height=250)
            st.altair_chart(chart_time, use_container_width=True)

        with col2:
            st.markdown("### 🎯 أثر دقة التطابق (Registration)")
            st.markdown("""
            * **مؤشر الأخطاء:** تاريخياً، يسجل التركيب اليدوي **معدل إعادة تركيب ~30%** بسبب أخطاء التطابق.
            * **مؤشر التوقف:** 45 إعادة تركيب/شهر (30 دقيقة لكل منها) = **فقدان 22.5 ساعة من توافر المطبعة**.
            * **المؤشر المالي:** باحتساب تكلفة المطبعة بـ 250 يورو/ساعة، تكاليف التوقف تقارب **5,625 يورو شهرياً**.
            """)
            df_cost = pd.DataFrame({'النظام': ['أخطاء يدوية (30%)', 'SOMA S-Mount (0%)'], 'التكلفة (يورو/شهر)': [5625, 0]})
            chart_cost = alt.Chart(df_cost).mark_bar(size=50).encode(
                x=alt.X('النظام:N', title='', sort=None),
                y=alt.Y('التكلفة (يورو/شهر):Q', title='تكلفة التوقف (يورو/شهر)'),
                color=alt.condition(alt.datum.النظام == 'SOMA S-Mount (0%)', alt.value('#1E3A8A'), alt.value('#94A3B8'))
            ).properties(height=250)
            st.altair_chart(chart_cost, use_container_width=True)

# ==========================================
# Page 9: IRIS vs smartGPS Tech
# ==========================================
elif page_selection in ["9. IRIS vs smartGPS Tech", "9. تقنية IRIS مقابل smartGPS"]:
    if lang == "English":
        st.markdown('<div class="executive-title">9. Setup Automation: SOMA IRIS vs. BOBST smartGPS</div>', unsafe_allow_html=True)
        st.markdown("""Both SOMA IRIS and BOBST smartGPS utilize embedded RFID chips and magnets in the sleeves to transfer offline mounting data to the press. However, the critical differentiation lies in **how the data is physically measured** at the mounter.""")
        
        st.markdown('<h3 style="color: #1E3A8A; margin-top: 20px;">🔍 Technological Mechanism</h3>', unsafe_allow_html=True)
        st.markdown("""
        <table class="corp-table">
            <tr>
                <th>Parameter</th>
                <th>SOMA IRIS (Tactile Measurement)</th>
                <th>BOBST smartGPS (Optical/Laser)</th>
            </tr>
            <tr>
                <td><strong>Data Carrier Method</strong></td>
                <td class="highlight-adv">Standardized Sleeves equipped with RFID and Magnets</td>
                <td class="highlight-mid">Proprietary Sleeves equipped with RFID and Magnets</td>
            </tr>
            <tr>
                <td><strong>Measurement Mechanism</strong></td>
                <td class="highlight-adv">Utilizes highly sensitive mechanical contact sensors (pedals) to trace the exact physical topography of the plate.</td>
                <td class="highlight-mid">Relies on optical/laser scanning which may misinterpret transparent dirt or clear plate anomalies.</td>
            </tr>
            <tr>
                <td><strong>Defect Detection & TIR</strong></td>
                <td class="highlight-adv">Physically detects dirt, plate damage, and uneven sleeves, generating a precise TIR report before printing.</td>
                <td class="highlight-mid">Optical scanning is significantly less effective at detecting physical, transparent debris on the plate surface.</td>
            </tr>
            <tr>
                <td><strong>Automation Core</strong></td>
                <td class="highlight-adv">Fully Automatic Impression & Register via SOMA Falcon / BST Smart Register (Standard).</td>
                <td class="highlight-mid">Only Smart-SET (Semi-Automatic register and impression).</td>
            </tr>
        </table>
        """, unsafe_allow_html=True)
        
        st.markdown('<h3 style="color: #1E3A8A; margin-top: 30px;">📊 Estimated Material Optimization (150 Jobs/Month)</h3>', unsafe_allow_html=True)
        
        df_waste = pd.DataFrame({
            'Setup Method': ['Traditional Optical Setup (W&H)', 'SOMA IRIS / smartGPS'],
            'Est. Waste (Meters/Month)': [30000, 1500]
        })
        chart_waste = alt.Chart(df_waste).mark_bar(size=50).encode(
            x=alt.X('Setup Method:N', title='', sort=None),
            y=alt.Y('Est. Waste (Meters/Month):Q', title='Substrate Used in Setup (Meters)'),
            color=alt.condition(alt.datum['Setup Method'] == 'SOMA IRIS / smartGPS', alt.value('#1E3A8A'), alt.value('#94A3B8'))
        ).properties(height=300)
        st.altair_chart(chart_waste, use_container_width=True)

    else:
        st.markdown('<div class="executive-title">9. تكنولوجيا إعداد الطباعة: IRIS مقابل smartGPS</div>', unsafe_allow_html=True)
        st.markdown("""يعتمد كل من نظام SOMA IRIS ونظام BOBST smartGPS على **شرائح RFID ومغانط** مدمجة في السليفات لنقل بيانات المونتاج إلى المطبعة. لكن الفارق الجوهري والخطير يكمن في **طريقة أخذ القياسات الفعلية (Measurement)** أثناء مرحلة التجهيز.""")
        
        st.markdown('<h3 style="color: #1E3A8A; margin-top: 20px;">🔍 المقارنة التكنولوجية والتشغيلية</h3>', unsafe_allow_html=True)
        st.markdown("""
        <table class="corp-table">
            <tr>
                <th>المعيار</th>
                <th>SOMA IRIS (قراءة ميكانيكية لمسية)</th>
                <th>BOBST smartGPS (قراءة بصرية/ليزر)</th>
            </tr>
            <tr>
                <td><strong>طريقة تخزين ونقل البيانات</strong></td>
                <td class="highlight-adv">سليفات مجهزة بشرائح RFID ومغانط (متوافقة للاستخدام القياسي)</td>
                <td class="highlight-mid">سليفات مجهزة بشرائح RFID ومغانط (محتكرة ومكلفة)</td>
            </tr>
            <tr>
                <td><strong>آلية أخذ القياس (Offline)</strong></td>
                <td class="highlight-adv">تستخدم مستشعرات لمسية ميكانيكية دقيقة (Pedals) تلامس الكليشيه فعلياً وتأخذ قراءات الطوبوغرافيا المادية.</td>
                <td class="highlight-mid">تعتمد على المسح البصري/الليزر (والذي قد يخطئ في قراءة الأوساخ الشفافة أو العيوب غير المرئية).</td>
            </tr>
            <tr>
                <td><strong>تقييم الجودة واكتشاف العيوب</strong></td>
                <td class="highlight-adv">الاحتكاك المادي يكتشف الأوساخ والتشوهات بدقة، ويصدر تقرير (TIR) قبل الطباعة لحماية الخامات.</td>
                <td class="highlight-mid">المسح البصري أقل كفاءة بكثير في اكتشاف العيوب والأوساخ المادية الموجودة على سطح السليف.</td>
            </tr>
            <tr>
                <td><strong>جوهر الأتمتة (Register & Impression)</strong></td>
                <td class="highlight-adv">ضبط أوتوماتيكي بالكامل عبر أنظمة SOMA Falcon و BST Smart Register (مواصفة قياسية).</td>
                <td class="highlight-mid">نظام Smart-SET فقط (ضبط شبه آلي للضغوط والتطابق).</td>
            </tr>
        </table>
        """, unsafe_allow_html=True)
        
        st.markdown('<h3 style="color: #1E3A8A; margin-top: 30px;">📊 تحسين استهلاك الخامات التقديري (150 طلبية/شهر)</h3>', unsafe_allow_html=True)
            
        df_waste = pd.DataFrame({
            'طريقة الإعداد': ['الضبط التقليدي البصري (مثل W&H)', 'نظام SOMA IRIS / smartGPS'],
            'الاستهلاك المقدر (متر/شهر)': [30000, 1500]
        })
        chart_waste = alt.Chart(df_waste).mark_bar(size=50).encode(
            x=alt.X('طريقة الإعداد:N', title='', sort=None),
            y=alt.Y('الاستهلاك المقدر (متر/شهر):Q', title='الخامات المهدرة في الإعداد (متر)'),
            color=alt.condition(alt.datum['طريقة الإعداد'] == 'نظام SOMA IRIS / smartGPS', alt.value('#1E3A8A'), alt.value('#94A3B8'))
        ).properties(height=300)
        st.altair_chart(chart_waste, use_container_width=True)

# ==========================================
# Page 10: The Ultimate Battlecard
# ==========================================
elif page_selection in ["10. Standard Value Battlecard 🏆", "10. المواجهة الشاملة والمواصفات 🏆"]:
    if lang == "English":
        st.markdown('<div class="executive-title">10. The Ultimate Battlecard: What You Pay For vs. What You Get 🏆</div>', unsafe_allow_html=True)
        st.markdown("""This matrix illustrates the true value of the base quotation by comparing the standard, out-of-the-box specifications. SOMA provides a fully-loaded flagship press, whereas competitors offer standard or stripped-down machines requiring expensive upgrades.""")
        
        st.markdown('<h4 class="section-header">1. Core Mechanics & Dimensions</h4>', unsafe_allow_html=True)
        st.markdown("""
        <table class="corp-table">
            <tr><th style="width: 25%;">Critical Specification</th><th style="width: 25%; text-align: center;">SOMA Optima 2</th><th style="width: 25%; text-align: center;">BOBST Expert CI</th><th style="width: 25%; text-align: center;">W&H Alphaflex</th></tr>
            <tr><td><strong>Max Production Speed</strong></td><td class="highlight-adv" style="text-align: center;">600 m/min</td><td style="text-align: center;">500 m/min</td><td style="text-align: center;">500 m/min</td></tr>
            <tr><td><strong>Print Repeat Range</strong></td><td class="highlight-adv" style="text-align: center;">360 - 850 mm (up to 900)</td><td style="text-align: center;">370 - 800 mm</td><td style="text-align: center;">370 - 800 mm</td></tr>
            <tr><td><strong>Web Tension Range</strong></td><td class="highlight-adv" style="text-align: center;">10 - 400 N (Extended)</td><td style="text-align: center;">20 - 350 N</td><td style="text-align: center;">20 - 350 N</td></tr>
            <tr><td><strong>Machine Frame Material</strong></td><td class="highlight-adv" style="text-align: center;">130 mm Cast-Iron (Doubled)</td><td style="text-align: center;">100 mm Steel</td><td style="text-align: center;">55 - 60 mm Steel</td></tr>
            <tr><td><strong>Lightweight Winding Shafts</strong></td><td class="highlight-adv" style="text-align: center;">✅ YES (Lighted 3" & 6")</td><td style="text-align: center;">❌ Optional</td><td style="text-align: center;">❌ NO</td></tr>
            <tr><td><strong>Carbon Fiber Mandrels</strong></td><td class="highlight-adv" style="text-align: center;">✅ Included</td><td style="text-align: center;">✅ Included</td><td style="text-align: center;">⚠️ Optional Upgrade</td></tr>
            <tr><td><strong>Anilox Base Mandrel Dia.</strong></td><td class="highlight-adv" style="text-align: center;">175.1 mm (Max Stability)</td><td style="text-align: center;">172.0 mm</td><td style="text-align: center;">Standard / Smaller</td></tr>
            <tr><td><strong>Anilox Circumference</strong></td><td class="highlight-adv" style="text-align: center;">625 mm</td><td style="text-align: center;">630 mm</td><td style="text-align: center;">Standard</td></tr>
        </table>
        """, unsafe_allow_html=True)

        st.markdown('<h4 class="section-header">2. Fluid & Thermal Management</h4>', unsafe_allow_html=True)
        st.markdown("""
        <table class="corp-table">
            <tr><th style="width: 25%;">Critical Specification</th><th style="width: 25%; text-align: center;">SOMA Optima 2</th><th style="width: 25%; text-align: center;">BOBST Expert CI</th><th style="width: 25%; text-align: center;">W&H Alphaflex</th></tr>
            <tr><td><strong>Viscosity Control (2 Liquids)</strong></td><td class="highlight-adv" style="text-align: center;">✅ YES (Dual Liquid)</td><td style="text-align: center;">❌ NO (1 Liquid Only)</td><td style="text-align: center;">❌ NO (1 Liquid Only)</td></tr>
            <tr><td><strong>Ink/Solvent Level Sensors</strong></td><td class="highlight-adv" style="text-align: center;">✅ YES</td><td style="text-align: center;">❌ Optional</td><td style="text-align: center;">❌ Optional</td></tr>
            <tr><td><strong>Water Cooling on Drive Side</strong></td><td class="highlight-adv" style="text-align: center;">✅ YES</td><td style="text-align: center;">❌ NO</td><td style="text-align: center;">❌ NO</td></tr>
            <tr><td><strong>Heat Exchanger (Ink Cooling)</strong></td><td class="highlight-adv" style="text-align: center;">✅ YES</td><td style="text-align: center;">✅ YES</td><td style="text-align: center;">❌ NO</td></tr>
            <tr><td><strong>Compressed Air Purifying Unit</strong></td><td class="highlight-adv" style="text-align: center;">✅ YES</td><td style="text-align: center;">✅ YES</td><td style="text-align: center;">❌ Optional</td></tr>
            <tr><td><strong>Drying Tunnel Length</strong></td><td class="highlight-adv" style="text-align: center;">6.0 Meters (23 Nozzles)</td><td style="text-align: center;">5.6 Meters</td><td style="text-align: center;">5.7 Meters (17 Nozzles)</td></tr>
            <tr><td><strong>Fast Wash Solvent Usage</strong></td><td class="highlight-adv" style="text-align: center;">5 Liters</td><td style="text-align: center;">Standard</td><td style="text-align: center;">12 Liters</td></tr>
        </table>
        """, unsafe_allow_html=True)

        st.markdown('<h4 class="section-header">3. Automation & Safety</h4>', unsafe_allow_html=True)
        st.markdown("""
        <table class="corp-table">
            <tr><th style="width: 25%;">Critical Specification</th><th style="width: 25%; text-align: center;">SOMA Optima 2</th><th style="width: 25%; text-align: center;">BOBST Expert CI</th><th style="width: 25%; text-align: center;">W&H Alphaflex</th></tr>
            <tr><td><strong>Prepared for Smart System</strong></td><td class="highlight-adv" style="text-align: center;">✅ YES (Included)</td><td style="text-align: center;">❌ Optional</td><td style="text-align: center;">❌ NO</td></tr>
            <tr><td><strong>Auto Impression & Register</strong></td><td class="highlight-adv" style="text-align: center;">✅ Fully Auto (Falcon/BST)</td><td style="text-align: center;">⚠️ Semi-Auto (Smart-SET)</td><td style="text-align: center;">❌ Manual</td></tr>
            <tr><td><strong>Sleeve Ejection System</strong></td><td class="highlight-adv" style="text-align: center;">✅ Fully Auto Push-off</td><td style="text-align: center;">❌ NO / Semi-Auto</td><td style="text-align: center;">⚠️ Basic Ejectors</td></tr>
            <tr><td><strong>Reprint / Insetter Capability</strong></td><td class="highlight-adv" style="text-align: center;">✅ YES</td><td style="text-align: center;">❌ Missing (~10k)</td><td style="text-align: center;">❌ Missing (~10k)</td></tr>
            <tr><td><strong>Fire Extinguishing System</strong></td><td class="highlight-adv" style="text-align: center;">✅ YES</td><td style="text-align: center;">✅ YES</td><td style="text-align: center;">❌ Optional</td></tr>
            <tr><td><strong>Lifting Carts (Unwind/Rewind)</strong></td><td class="highlight-adv" style="text-align: center;">✅ YES</td><td style="text-align: center;">❌ NO (Motorized only)</td><td style="text-align: center;">❌ NO</td></tr>
            <tr><td><strong>Antistatic Units (Total)</strong></td><td class="highlight-adv" style="text-align: center;">2 Units (4 Bars)</td><td style="text-align: center;">2 Units (4 Bars)</td><td style="text-align: center;">2 Units (4 Bars)</td></tr>
            <tr><td><strong>100% Inspection Camera</strong></td><td class="highlight-adv" style="text-align: center;">✅ Included (BST)</td><td style="text-align: center;">❌ Missing (~70k)</td><td style="text-align: center;">❌ Missing (~71k)</td></tr>
        </table>
        """, unsafe_allow_html=True)

        st.markdown('<h4 class="section-header">4. OPEX, Training & Peripherals</h4>', unsafe_allow_html=True)
        st.markdown("""
        <table class="corp-table">
            <tr><th style="width: 25%;">Critical Specification</th><th style="width: 25%; text-align: center;">SOMA Optima 2</th><th style="width: 25%; text-align: center;">BOBST Expert CI</th><th style="width: 25%; text-align: center;">W&H Alphaflex</th></tr>
            <tr><td><strong>Training Program</strong></td><td class="highlight-adv" style="text-align: center;">10 Days + 2 Weeks + 1 Month</td><td style="text-align: center;">5 Days Only</td><td style="text-align: center;">Standard</td></tr>
            <tr><td><strong>3" & 6" Cores Included</strong></td><td class="highlight-adv" style="text-align: center;">✅ YES (Both Included)</td><td style="text-align: center;">⚠️ 3" Only</td><td style="text-align: center;">⚠️ 3" Only</td></tr>
            <tr><td><strong>Initial Sleeves (8+8)</strong></td><td class="highlight-adv" style="text-align: center;">✅ Included</td><td style="text-align: center;">❌ Missing (~55k)</td><td style="text-align: center;">❌ Missing (~50k)</td></tr>
            <tr><td><strong>Corona + In-feed Unit</strong></td><td class="highlight-adv" style="text-align: center;">✅ Included</td><td style="text-align: center;">❌ Missing (~55k)</td><td style="text-align: center;">❌ Missing (~55k)</td></tr>
            <tr><td><strong>ALU/PE Handling Kit</strong></td><td class="highlight-adv" style="text-align: center;">✅ Included</td><td style="text-align: center;">❌ Missing (~50k)</td><td style="text-align: center;">❌ Missing (~50k)</td></tr>
            <tr><td><strong>Process Visibility (Glass)</strong></td><td class="highlight-adv" style="text-align: center;">✅ Full Glass</td><td style="text-align: center;">⚠️ Partial</td><td style="text-align: center;">❌ Closed</td></tr>
        </table>
        """, unsafe_allow_html=True)

    else:
        st.markdown('<div class="executive-title">10. المواجهة الشاملة: ما تدفعه مقابل ما تحصل عليه فعلياً 🏆</div>', unsafe_allow_html=True)
        st.markdown("""توضح هذه المصفوفة القيمة الحقيقية لكل عرض مالي من خلال مقارنة المواصفات الأساسية المشمولة في السعر (Standard Equipment). تقدم SOMA ماكينة جاهزة تماماً للأداء العالي (Fully-loaded)، بينما يقدم المنافسون هياكل تتطلب ترقيات باهظة لتصل لنفس الكفاءة التشغيلية.""")
        
        st.markdown('<h4 class="section-header">1. الهيكل الميكانيكي والأبعاد</h4>', unsafe_allow_html=True)
        st.markdown("""
        <table class="corp-table">
            <tr><th style="width: 25%;">المواصفة الحيوية (المشمولة بالسعر)</th><th style="width: 25%; text-align: center;">SOMA Optima 2</th><th style="width: 25%; text-align: center;">BOBST Expert CI</th><th style="width: 25%; text-align: center;">W&H Alphaflex</th></tr>
            <tr><td><strong>السرعة الإنتاجية القصوى</strong></td><td class="highlight-adv" style="text-align: center;">600 متر/دقيقة</td><td style="text-align: center;">500 متر/دقيقة</td><td style="text-align: center;">500 متر/دقيقة</td></tr>
            <tr><td><strong>نطاق تكرار الطباعة (Repeat)</strong></td><td class="highlight-adv" style="text-align: center;">360 - 850 ملم (إلى 900)</td><td style="text-align: center;">370 - 800 ملم</td><td style="text-align: center;">370 - 800 ملم</td></tr>
            <tr><td><strong>نطاق شد الرول (Web Tension)</strong></td><td class="highlight-adv" style="text-align: center;">10 - 400 N (نطاق أوسع)</td><td style="text-align: center;">20 - 350 N</td><td style="text-align: center;">20 - 350 N</td></tr>
            <tr><td><strong>مادة وسماكة الهيكل (Frame)</strong></td><td class="highlight-adv" style="text-align: center;">حديد زهر 130 ملم (مزدوج)</td><td style="text-align: center;">صلب 100 ملم</td><td style="text-align: center;">صلب 55 - 60 ملم</td></tr>
            <tr><td><strong>أعمدة شد خفيفة الوزن (Shafts)</strong></td><td class="highlight-adv" style="text-align: center;">✅ نعم (مضيئة 3 و 6 إنش)</td><td style="text-align: center;">❌ اختياري</td><td style="text-align: center;">❌ لا</td></tr>
            <tr><td><strong>أعمدة كاربون فايبر للطباعة</strong></td><td class="highlight-adv" style="text-align: center;">✅ مشمولة</td><td style="text-align: center;">✅ مشمولة</td><td style="text-align: center;">⚠️ ترقية اختيارية</td></tr>
            <tr><td><strong>القطر الخارجي لعمود الأنيلوكس</strong></td><td class="highlight-adv" style="text-align: center;">175.1 ملم (استقرار مطلق)</td><td style="text-align: center;">172.0 ملم</td><td style="text-align: center;">قياسي / أصغر</td></tr>
            <tr><td><strong>محيط أسطوانة الأنيلوكس</strong></td><td class="highlight-adv" style="text-align: center;">625 ملم</td><td style="text-align: center;">630 ملم</td><td style="text-align: center;">قياسي</td></tr>
        </table>
        """, unsafe_allow_html=True)

        st.markdown('<h4 class="section-header">2. إدارة الحرارة والسوائل</h4>', unsafe_allow_html=True)
        st.markdown("""
        <table class="corp-table">
            <tr><th style="width: 25%;">المواصفة الحيوية (المشمولة بالسعر)</th><th style="width: 25%; text-align: center;">SOMA Optima 2</th><th style="width: 25%; text-align: center;">BOBST Expert CI</th><th style="width: 25%; text-align: center;">W&H Alphaflex</th></tr>
            <tr><td><strong>التحكم باللزوجة (لنوعين من السوائل)</strong></td><td class="highlight-adv" style="text-align: center;">✅ نعم (مزدوج)</td><td style="text-align: center;">❌ لا (سائل واحد فقط)</td><td style="text-align: center;">❌ لا (سائل واحد فقط)</td></tr>
            <tr><td><strong>حساسات مستوى الحبر والمذيبات</strong></td><td class="highlight-adv" style="text-align: center;">✅ نعم</td><td style="text-align: center;">❌ اختياري</td><td style="text-align: center;">❌ اختياري</td></tr>
            <tr><td><strong>التبريد المائي من جهة الإدارة</strong></td><td class="highlight-adv" style="text-align: center;">✅ نعم</td><td style="text-align: center;">❌ لا</td><td style="text-align: center;">❌ لا</td></tr>
            <tr><td><strong>مبادل حراري لتبريد الحبر</strong></td><td class="highlight-adv" style="text-align: center;">✅ نعم</td><td style="text-align: center;">✅ نعم</td><td style="text-align: center;">❌ لا</td></tr>
            <tr><td><strong>وحدة تنقية الهواء المضغوط</strong></td><td class="highlight-adv" style="text-align: center;">✅ نعم</td><td style="text-align: center;">✅ نعم</td><td style="text-align: center;">❌ اختياري</td></tr>
            <tr><td><strong>طول نفق التجفيف</strong></td><td class="highlight-adv" style="text-align: center;">6.0 أمتار (23 فوهة)</td><td style="text-align: center;">5.6 متر</td><td style="text-align: center;">5.7 متر (17 فوهة)</td></tr>
            <tr><td><strong>هدر المذيبات في الغسيل السريع</strong></td><td class="highlight-adv" style="text-align: center;">5 لتر فقط</td><td style="text-align: center;">استهلاك قياسي</td><td style="text-align: center;">12 لتر (هدر عالي)</td></tr>
        </table>
        """, unsafe_allow_html=True)

        st.markdown('<h4 class="section-header">3. الأتمتة وأنظمة الأمان</h4>', unsafe_allow_html=True)
        st.markdown("""
        <table class="corp-table">
            <tr><th style="width: 25%;">المواصفة الحيوية (المشمولة بالسعر)</th><th style="width: 25%; text-align: center;">SOMA Optima 2</th><th style="width: 25%; text-align: center;">BOBST Expert CI</th><th style="width: 25%; text-align: center;">W&H Alphaflex</th></tr>
            <tr><td><strong>مجهزة للأنظمة الذكية (مشمول بالسعر)</strong></td><td class="highlight-adv" style="text-align: center;">✅ نعم (مشمول)</td><td style="text-align: center;">❌ اختياري</td><td style="text-align: center;">❌ لا</td></tr>
            <tr><td><strong>أتمتة الضغوط والتطابق</strong></td><td class="highlight-adv" style="text-align: center;">✅ آلي بالكامل (Falcon/BST)</td><td style="text-align: center;">⚠️ شبه آلي (Smart-SET)</td><td style="text-align: center;">❌ يدوي</td></tr>
            <tr><td><strong>نظام إخراج السليفات</strong></td><td class="highlight-adv" style="text-align: center;">✅ دفع آلي (Push-off)</td><td style="text-align: center;">❌ لا / شبه آلي</td><td style="text-align: center;">⚠️ طاردات أساسية</td></tr>
            <tr><td><strong>تجهيز الطباعة المتكررة (Insetter)</strong></td><td class="highlight-adv" style="text-align: center;">✅ نعم</td><td style="text-align: center;">❌ غير مشمول (~10k)</td><td style="text-align: center;">❌ غير مشمول (~10k)</td></tr>
            <tr><td><strong>نظام إطفاء الحرائق</strong></td><td class="highlight-adv" style="text-align: center;">✅ نعم</td><td style="text-align: center;">✅ نعم</td><td style="text-align: center;">❌ اختياري</td></tr>
            <tr><td><strong>رافعات رولات للفك واللف</strong></td><td class="highlight-adv" style="text-align: center;">✅ نعم</td><td style="text-align: center;">❌ لا (عربة آلية فقط)</td><td style="text-align: center;">❌ لا</td></tr>
            <tr><td><strong>وحدات منع الكهرباء الساكنة</strong></td><td class="highlight-adv" style="text-align: center;">وحدتين (4 بارات)</td><td style="text-align: center;">وحدتين (4 بارات)</td><td style="text-align: center;">وحدتين (4 بارات)</td></tr>
            <tr><td><strong>كاميرا فحص الجودة 100%</strong></td><td class="highlight-adv" style="text-align: center;">✅ مشمولة (BST)</td><td style="text-align: center;">❌ غير مشمولة (~70k)</td><td style="text-align: center;">❌ غير مشمولة (~71k)</td></tr>
        </table>
        """, unsafe_allow_html=True)

        st.markdown('<h4 class="section-header">4. التشغيل والتدريب (OPEX)</h4>', unsafe_allow_html=True)
        st.markdown("""
        <table class="corp-table">
            <tr><th style="width: 25%;">المواصفة الحيوية (المشمولة بالسعر)</th><th style="width: 25%; text-align: center;">SOMA Optima 2</th><th style="width: 25%; text-align: center;">BOBST Expert CI</th><th style="width: 25%; text-align: center;">W&H Alphaflex</th></tr>
            <tr><td><strong>برنامج تدريب المشغلين</strong></td><td class="highlight-adv" style="text-align: center;">10 أيام + أسبوعين + شهر</td><td style="text-align: center;">5 أيام فقط</td><td style="text-align: center;">قياسي</td></tr>
            <tr><td><strong>محاور مقاس 3 و 6 إنش (Cores)</strong></td><td class="highlight-adv" style="text-align: center;">✅ نعم (كلاهما مشمول)</td><td style="text-align: center;">⚠️ 3 إنش فقط</td><td style="text-align: center;">⚠️ 3 إنش فقط</td></tr>
            <tr><td><strong>أطقم السليفات المبدئية (8+8)</strong></td><td class="highlight-adv" style="text-align: center;">✅ مشمولة</td><td style="text-align: center;">❌ غير مشمولة (~55k)</td><td style="text-align: center;">❌ غير مشمولة (~50k)</td></tr>
            <tr><td><strong>وحدة كورونا + وحدة سحب (In-feed)</strong></td><td class="highlight-adv" style="text-align: center;">✅ مشمولة</td><td style="text-align: center;">❌ غير مشمولة (~55k)</td><td style="text-align: center;">❌ غير مشمولة (~55k)</td></tr>
            <tr><td><strong>تجهيزات طباعة ALU و PE</strong></td><td class="highlight-adv" style="text-align: center;">✅ مشمولة بالكامل</td><td style="text-align: center;">❌ غير مشمولة (~50k)</td><td style="text-align: center;">❌ غير مشمولة (~50k)</td></tr>
            <tr><td><strong>رؤية وشفافية وحدات الطباعة</strong></td><td class="highlight-adv" style="text-align: center;">✅ زجاج شفاف بالكامل</td><td style="text-align: center;">⚠️ أغطية جزئية</td><td style="text-align: center;">❌ مغلقة (انعدام الرؤية)</td></tr>
        </table>
        """, unsafe_allow_html=True)
