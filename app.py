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
    .corp-table {{ width: 100%; border-collapse: collapse; margin-bottom: 25px; font-size: 1.05rem; text-align: {text_align}; direction: {direction}; }}
    .corp-table th {{ background-color: #1E3A8A; color: #FFFFFF; padding: 12px; text-align: {text_align}; border: 1px solid #CBD5E1; font-weight: 700; }}
    .corp-table td {{ padding: 12px; border: 1px solid #CBD5E1; color: #1E293B; }}
    .corp-table tr:nth-child(even) {{ background-color: #F8FAFC; }}
    .highlight-adv {{ color: #0F172A; font-weight: 700; background-color: #E2E8F0; border-left: 4px solid #1E3A8A !important; }}
    .highlight-mid {{ color: #334155; font-weight: 500; background-color: #F1F5F9; }}
    .highlight-dis {{ color: #475569; font-weight: 400; background-color: #FFFFFF; }}
    .total-investment {{ font-size: 1.8rem; font-weight: 900; color: #FFFFFF; text-align: center; background-color: #1E3A8A; padding: 20px; border-radius: 8px; margin-top: 20px; }}
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
        "9. IRIS vs smartGPS Tech"
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
        "9. تقنية IRIS مقابل smartGPS"
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
                <p><strong>Performance:</strong> Upgraded to 600 m/min with a robust 130mm doubled frame.</p>
                <p><strong>Strategy:</strong> Engineered for rapid changeovers using topography-based IRIS automation and open-source OPEX policies.</p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class="data-card" style="border-top-color: #64748B;">
                <h3 style="color: #475569; margin-top: 0;">BOBST Expert CI</h3>
                <p><strong>Classification:</strong> Mainstream Standard.</p>
                <p><strong>Performance:</strong> Limited to 500 m/min standard operating speed.</p>
                <p><strong>Strategy:</strong> Relies on the smartGPS system, which mandates the use of highly expensive proprietary RFID-embedded sleeves, creating long-term OPEX lock-in.</p>
            </div>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown("""
            <div class="data-card" style="border-top-color: #94A3B8;">
                <h3 style="color: #64748B; margin-top: 0;">W&H Alphaflex</h3>
                <p><strong>Classification:</strong> Economy / Entry-Level.</p>
                <p><strong>Performance:</strong> 500 m/min limit on lightweight 55-60mm frames.</p>
                <p><strong>Strategy:</strong> Designed to reduce initial CAPEX by stripping standard automation and cooling systems, masking the true operational costs.</p>
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
                <p><strong>الأداء الفعلي:</strong> تمت الترقية لسرعة 600 م/دقيقة بهيكل معدني مزدوج جبار (130 ملم).</p>
                <p><strong>الاستراتيجية:</strong> مصممة لتسريع التجهيز بأتمتة IRIS الطوبوغرافية، مع سياسة تشغيل وصيانة (OPEX) غير احتكارية.</p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class="data-card" style="border-top-color: #64748B;">
                <h3 style="color: #475569; margin-top: 0;">BOBST Expert CI</h3>
                <p><strong>التصنيف السوقي:</strong> الفئة القياسية المعتمدة.</p>
                <p><strong>الأداء الفعلي:</strong> مقيدة بسرعة تشغيل قصوى تبلغ 500 م/دقيقة.</p>
                <p><strong>الاستراتيجية:</strong> تعتمد على نظام smartGPS الذي يُجبر المصنع على شراء سليفات خاصة مدمجة برقاقات (RFID) بأسعار باهظة، مما يرفع تكاليف التشغيل المستمرة بشكل حاد.</p>
            </div>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown("""
            <div class="data-card" style="border-top-color: #94A3B8;">
                <h3 style="color: #64748B; margin-top: 0;">W&H Alphaflex</h3>
                <p><strong>التصنيف السوقي:</strong> الفئة الاقتصادية (للمبتدئين).</p>
                <p><strong>الأداء الفعلي:</strong> سرعة 500 م/دقيقة على هيكل خفيف (55-60 ملم).</p>
                <p><strong>الاستراتيجية:</strong> مصممة لخفض السعر المبدئي (CAPEX) عبر تجريد الماكينة من أنظمة الأتمتة والتبريد الأساسية، مما يخفي التكلفة التشغيلية الحقيقية.</p>
            </div>
            """, unsafe_allow_html=True)

# ==========================================
# Page 2: Structural & Engineering Superiority
# ==========================================
elif page_selection in ["2. Engineering & Performance", "2. التقييم الهندسي والأداء"]:
    if lang == "English":
        st.markdown('<div class="executive-title">2. Engineering Specifications & Performance Benchmarking</div>', unsafe_allow_html=True)
        st.markdown("""A tri-lateral comparative analysis of core mechanical properties across the three platforms.""")
        
        st.markdown("""
        <table class="corp-table">
            <tr><th>Engineering Specification</th><th>SOMA Optima 2 (Upgraded)</th><th>BOBST Expert CI</th><th>W&H Alphaflex</th></tr>
            <tr><td><strong>Max Production Speed</strong></td><td class="highlight-adv">600 m/min</td><td class="highlight-mid">500 m/min</td><td class="highlight-dis">500 m/min</td></tr>
            <tr><td><strong>Print Repeat Range</strong></td><td class="highlight-adv">360 - 850 mm</td><td class="highlight-mid">370 - 800 mm</td><td class="highlight-dis">370 - 800 mm</td></tr>
            <tr><td><strong>Drying Tunnel Length</strong></td><td class="highlight-adv">6.0 Meters (23 Nozzles) w/ iDry</td><td class="highlight-mid">5.6 Meters (4.5m + 1.1m Pre-dryer)</td><td class="highlight-dis">5.7 Meters (17 Nozzles)</td></tr>
            <tr><td><strong>Process Visibility (Decks)</strong></td><td class="highlight-adv">Transparent Full Glass Windows</td><td class="highlight-mid">Partially Closed Covers</td><td class="highlight-dis">Closed (No Glass)</td></tr>
            <tr><td><strong>Anilox Mandrel Dimensions</strong></td><td class="highlight-adv">Massive (Diam. 175.1 mm)</td><td class="highlight-mid">Standard</td><td class="highlight-dis">Standard</td></tr>
            <tr><td><strong>Sleeve Ejection System</strong></td><td class="highlight-adv">Fully Automatic Push-off</td><td class="highlight-dis">❌ NO</td><td class="highlight-dis">Basic Ejectors</td></tr>
        </table>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<h4 style="color: #1E3A8A; text-align: center;">⚙️ Frame Wall Thickness (mm)</h4>', unsafe_allow_html=True)
            frame_data = pd.DataFrame({'Machine': ['SOMA Optima 2', 'W&H Alphaflex'], 'Thickness (mm)': [130, 60]})
            chart1 = alt.Chart(frame_data).mark_bar(size=50).encode(
                x=alt.X('Machine:N', title='', sort=None),
                y=alt.Y('Thickness (mm):Q', title='Frame Thickness (mm)'),
                color=alt.condition(alt.datum.Machine == 'SOMA Optima 2', alt.value('#1E3A8A'), alt.value('#94A3B8'))
            ).properties(height=300)
            st.altair_chart(chart1, use_container_width=True)

        with col2:
            st.markdown('<h4 style="color: #1E3A8A; text-align: center;">🔥 Drying Tunnel Length (Meters)</h4>', unsafe_allow_html=True)
            df_dry = pd.DataFrame({'Machine': ['SOMA Optima 2', 'W&H Alphaflex', 'BOBST Expert CI'], 'Length (m)': [6.0, 5.7, 5.6]})
            chart_dry = alt.Chart(df_dry).mark_bar(size=50).encode(
                x=alt.X('Machine:N', title='', sort=None),
                y=alt.Y('Length (m):Q', title='Tunnel Length (Meters)', scale=alt.Scale(domain=[0, 7])),
                color=alt.Color('Machine:N', scale=alt.Scale(domain=['SOMA Optima 2', 'BOBST Expert CI', 'W&H Alphaflex'], range=['#1E3A8A', '#64748B', '#94A3B8']), legend=None)
            ).properties(height=300)
            st.altair_chart(chart_dry, use_container_width=True)

    else:
        st.markdown('<div class="executive-title">2. التقييم الهندسي والأداء التشغيلي</div>', unsafe_allow_html=True)
        st.markdown("""تحليل مقارن دقيق للخصائص الميكانيكية الأساسية وقدرات الإنتاج بين المنصات الثلاث.""")
        
        st.markdown("""
        <table class="corp-table">
            <tr><th>المواصفات الهندسية</th><th>SOMA Optima 2 (الإصدار المُرقى)</th><th>BOBST Expert CI</th><th>W&H Alphaflex</th></tr>
            <tr><td><strong>السرعة الإنتاجية القصوى</strong></td><td class="highlight-adv">600 متر / دقيقة</td><td class="highlight-mid">500 متر / دقيقة</td><td class="highlight-dis">500 متر / دقيقة</td></tr>
            <tr><td><strong>نطاق تكرار الطباعة (Repeat)</strong></td><td class="highlight-adv">360 - 850 ملم</td><td class="highlight-mid">370 - 800 ملم</td><td class="highlight-dis">370 - 800 ملم</td></tr>
            <tr><td><strong>طول نفق التجفيف الفعلي</strong></td><td class="highlight-adv">6.0 أمتار (23 فوهة) مع تقنية iDry</td><td class="highlight-mid">5.6 متر (نفق رئيسي 4.5م + 1.1م تحضيري)</td><td class="highlight-dis">5.7 متر (17 فوهة)</td></tr>
            <tr><td><strong>الرؤية البصرية لوحدات الطباعة</strong></td><td class="highlight-adv">نوافذ زجاجية شفافة بالكامل</td><td class="highlight-mid">أغطية معدنية شبه مغلقة</td><td class="highlight-dis">أغطية مغلقة (بدون زجاج نهائياً)</td></tr>
            <tr><td><strong>أبعاد أعمدة الأنيلوكس</strong></td><td class="highlight-adv">ضخمة (قطر 175.1 ملم) لمنع الاهتزاز</td><td class="highlight-mid">أبعاد قياسية</td><td class="highlight-dis">أبعاد قياسية</td></tr>
            <tr><td><strong>نظام إخراج السليفات (Ejectors)</strong></td><td class="highlight-adv">دفع أوتوماتيكي بالكامل</td><td class="highlight-dis">❌ NO</td><td class="highlight-dis">طاردات ميكانيكية أساسية</td></tr>
        </table>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<h4 style="color: #1E3A8A; text-align: center;">⚙️ سماكة الهيكل المعدني (ملم)</h4>', unsafe_allow_html=True)
            frame_data = pd.DataFrame({'الماكينة': ['SOMA Optima 2', 'W&H Alphaflex'], 'السماكة (ملم)': [130, 60]})
            chart1 = alt.Chart(frame_data).mark_bar(size=50).encode(
                x=alt.X('الماكينة:N', title='', sort=None),
                y=alt.Y('السماكة (ملم):Q', title='سماكة الهيكل بالمليمتر'),
                color=alt.condition(alt.datum.الماكينة == 'SOMA Optima 2', alt.value('#1E3A8A'), alt.value('#94A3B8'))
            ).properties(height=300)
            st.altair_chart(chart1, use_container_width=True)

        with col2:
            st.markdown('<h4 style="color: #1E3A8A; text-align: center;">🔥 إجمالي طول مسار التجفيف (متر)</h4>', unsafe_allow_html=True)
            df_dry = pd.DataFrame({'الماكينة': ['SOMA Optima 2', 'BOBST Expert CI', 'W&H Alphaflex'], 'الطول (متر)': [6.0, 5.6, 5.7]})
            chart_dry = alt.Chart(df_dry).mark_bar(size=50).encode(
                x=alt.X('الماكينة:N', title='', sort=None),
                y=alt.Y('الطول (متر):Q', title='طول نفق التجفيف (متر)', scale=alt.Scale(domain=[0, 7])),
                color=alt.Color('الماكينة:N', scale=alt.Scale(domain=['SOMA Optima 2', 'BOBST Expert CI', 'W&H Alphaflex'], range=['#1E3A8A', '#64748B', '#94A3B8']), legend=None)
            ).properties(height=300)
            st.altair_chart(chart_dry, use_container_width=True)

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
            <tr><td><strong>Spare Parts Sourcing</strong></td><td class="highlight-adv">Open Source (Authorized local procurement permitted)</td><td class="highlight-mid">Restricted (Smart sleeves mandated)</td><td class="highlight-dis">Restricted (Vendor procurement mandated)</td></tr>
            <tr><td><strong>Setup Tech OPEX Burden</strong></td><td class="highlight-adv">IRIS Topography (Zero recurring cost)</td><td class="highlight-mid">smartGPS (Requires expensive proprietary sleeves)</td><td class="highlight-dis">Optical/Manual (High substrate waste)</td></tr>
            <tr><td><strong>Service Cost Structure</strong></td><td class="highlight-adv">Standardized intervention rates</td><td class="highlight-mid">Premium tier rates</td><td class="highlight-dis">Premium service tier rates</td></tr>
            <tr><td><strong>Asset Retrofitting</strong></td><td class="highlight-adv">Designed for high upgradeability</td><td class="highlight-mid">Rigid (Tied to proprietary tech)</td><td class="highlight-dis">Rigid specification / High upgrade costs</td></tr>
        </table>
        """, unsafe_allow_html=True)
    else:
        st.markdown('<div class="executive-title">4. النفقات التشغيلية (OPEX) وسياسة الصيانة</div>', unsafe_allow_html=True)
        st.markdown("""تقييم تكاليف التشغيل لما بعد فترة الضمان بناءً على الأطر الخدمية وتقنيات الاستدامة للشركات الثلاث.""")
        
        st.markdown("""
        <table class="corp-table">
            <tr><th>جانب التشغيل والصيانة</th><th>إطار عمل SOMA</th><th>إطار عمل BOBST</th><th>إطار عمل W&H</th></tr>
            <tr><td><strong>مصادر قطع الغيار</strong></td><td class="highlight-adv">مفتوح المصدر (يُسمح بالشراء المحلي المعتمد)</td><td class="highlight-mid">مقيد (احتكار سليفات الـ smartGPS)</td><td class="highlight-dis">مقيد (يلزم الشراء من الشركة المصنعة)</td></tr>
            <tr><td><strong>العبء المالي لأنظمة التجهيز</strong></td><td class="highlight-adv">IRIS (قياسات ميكانيكية، لا يوجد تكلفة إضافية مستمرة)</td><td class="highlight-mid">smartGPS (يتطلب شراء سليفات مدمجة بشرائح باهظة الثمن دائماً)</td><td class="highlight-dis">إعداد بصري كاميرات (هدر عالي في الخامات)</td></tr>
            <tr><td><strong>هيكل تكاليف الخدمة</strong></td><td class="highlight-adv">معدلات تدخل وصيانة قياسية عادلة</td><td class="highlight-mid">معدلات خدمة مرتفعة (Premium)</td><td class="highlight-dis">معدلات خدمة ذات تسعير ممتاز (Premium)</td></tr>
            <tr><td><strong>ترقية الأصول (Retrofit)</strong></td><td class="highlight-adv">مصممة بقابلية عالية للترقية المستقبلية</td><td class="highlight-mid">مرتبطة بتقنيات الشركة الخاصة (Rigid)</td><td class="highlight-dis">مواصفات صلبة / تكاليف ترقية مرتفعة</td></tr>
        </table>
        """, unsafe_allow_html=True)

# ==========================================
# Page 5: TCO Hidden Costs
# ==========================================
elif page_selection in ["5. Total Cost of Ownership (TCO)", "5. التكلفة الإجمالية للملكية (TCO)"]:
    if lang == "English":
        st.markdown('<div class="executive-title">5. Total Cost of Ownership (TCO) Analysis</div>', unsafe_allow_html=True)
        st.markdown("""A financial alignment analyzing the initial base configuration against the necessary additions required to achieve equivalent operational capability.""")
        
        data = pd.DataFrame({'Equipment Add-on': ['ITS Cooling', '100% Camera', 'Sleeves & Aniloxes', 'Carbon Mandrels', 'ALU/PE Handling Kit'], 'Estimated Value (€)': [50000, 71000, 50000, 30000, 50000]})
        chart = alt.Chart(data).mark_bar(color='#94A3B8', cornerRadiusEnd=4).encode(
            x=alt.X('Estimated Value (€):Q', title='Estimated Value (€)'), y=alt.Y('Equipment Add-on:N', sort='-x', title=''), tooltip=['Equipment Add-on', 'Estimated Value (€)']
        ).properties(height=300, title="Valuation of Necessary Add-ons for Standard Economy Configuration")
        st.altair_chart(chart, use_container_width=True)

        st.markdown("""
        <table class="corp-table">
            <tr><th>Operational Requirement</th><th>SOMA Optima 2</th><th>BOBST Expert CI</th><th>W&H Alphaflex</th></tr>
            <tr><td><strong>Ink Thermal Stabilization</strong></td><td class="highlight-adv">✔️ Integrated</td><td class="highlight-mid">Depends on spec</td><td class="highlight-dis">➖ Not Included</td></tr>
            <tr><td><strong>100% Inspection Camera</strong></td><td class="highlight-adv">✔️ Included (BST)</td><td class="highlight-mid">Usually Add-on</td><td class="highlight-dis">➖ Optional Add-on</td></tr>
            <tr><td><strong>Initial Sleeves (8+8)</strong></td><td class="highlight-adv">✔️ Included (Standard)</td><td class="highlight-mid">⚠️ Requires highly expensive smartGPS sleeves</td><td class="highlight-dis">➖ Not Included</td></tr>
            <tr><td><strong>ALU & PE Handling Kit</strong></td><td class="highlight-adv">✔️ Included</td><td class="highlight-mid">Usually Add-on</td><td class="highlight-dis">➖ Not Included</td></tr>
            <tr><td><strong>Carbon Fiber Mandrels</strong></td><td class="highlight-adv">✔️ Standard</td><td class="highlight-mid">Standard options vary</td><td class="highlight-dis">➖ Optional Upgrade</td></tr>
        </table>
        """, unsafe_allow_html=True)
        st.info("📊 **Financial Note:** Evaluating BOBST requires accounting for the perpetual OPEX burden of proprietary smartGPS sleeves. Aligning the W&H Alphaflex to the Optima 2 high-performance standard involves approx. **€ 250,000** in required hardware additions.")
    
    else:
        st.markdown('<div class="executive-title">5. تحليل التكلفة الإجمالية للملكية (TCO)</div>', unsafe_allow_html=True)
        st.markdown("""مواءمة مالية تفصيلية تحلل التكوين الأساسي المبدئي مقابل الإضافات الضرورية المطلوبة لتحقيق قدرة تشغيلية متكافئة للماكينات المنافسة.""")
        
        data = pd.DataFrame({'المعدة المطلوبة': ['نظام تبريد الحبر (ITS)', 'كاميرا فحص 100%', 'سليفات وأنيلوكس', 'ترقية أعمدة الكاربون', 'تجهيزات طباعة ALU/PE'], 'القيمة التقديرية (يورو)': [50000, 71000, 50000, 30000, 50000]})
        chart = alt.Chart(data).mark_bar(color='#94A3B8', cornerRadiusEnd=4).encode(
            x=alt.X('القيمة التقديرية (يورو):Q', title='القيمة التقديرية (يورو)'), y=alt.Y('المعدة المطلوبة:N', sort='-x', title=''), tooltip=['المعدة المطلوبة', 'القيمة التقديرية (يورو)']
        ).properties(height=300, title="تقييم الإضافات الضرورية لتكوين الفئة الاقتصادية (Alphaflex)")
        st.altair_chart(chart, use_container_width=True)

        st.markdown("""
        <table class="corp-table">
            <tr><th>المتطلب التشغيلي</th><th>SOMA Optima 2</th><th>BOBST Expert CI</th><th>W&H Alphaflex</th></tr>
            <tr><td><strong>نظام تبريد الحبر (ITS)</strong></td><td class="highlight-adv">✔️ مدمج بالنظام</td><td class="highlight-mid">حسب المواصفة المرفقة</td><td class="highlight-dis">➖ غير مشمول</td></tr>
            <tr><td><strong>كاميرا فحص الجودة 100%</strong></td><td class="highlight-adv">✔️ مشمولة (BST iPQ)</td><td class="highlight-mid">إضافة اختيارية غالباً</td><td class="highlight-dis">➖ إضافة اختيارية</td></tr>
            <tr><td><strong>أطقم السليفات (8+8)</strong></td><td class="highlight-adv">✔️ مشمولة (سليفات قياسية)</td><td class="highlight-mid">⚠️ تتطلب سليفات smartGPS مدمجة بشرائح بأسعار مضاعفة</td><td class="highlight-dis">➖ غير مشمولة</td></tr>
            <tr><td><strong>تجهيزات طباعة ALU و PE</strong></td><td class="highlight-adv">✔️ مشمولة بالكامل</td><td class="highlight-mid">إضافة اختيارية غالباً</td><td class="highlight-dis">➖ غير مشمولة</td></tr>
            <tr><td><strong>أعمدة كاربون فايبر للطباعة</strong></td><td class="highlight-adv">✔️ مواصفة قياسية</td><td class="highlight-mid">حسب المواصفة المطلوبة</td><td class="highlight-dis">➖ تتطلب ترقية</td></tr>
        </table>
        """, unsafe_allow_html=True)
        st.info("📊 **ملاحظة مالية جوهرية:** عند تقييم BOBST، يجب احتساب (العبء المالي المستمر) والمتمثل في إجبار المصنع على شراء سليفات (smartGPS) باهظة الثمن طوال عمر الماكينة. أما بالنسبة لـ W&H Alphaflex، فإن مطابقتها لمستوى أداء Optima 2 يتطلب إضافات بقيمة **250,000 يورو** تقريباً.")

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
            <h3 style="color: #1E3A8A; margin-top:0;">Technical Training Protocol</h3>
            <p style="font-size: 1.1rem; color: #0F172A;"><b>Upon acquisition of the complete 4-machine suite, the following integration program is provided:</b></p>
            <ul style="line-height: 1.8; font-size: 1.1rem; color: #334155;">
                <li><b>Phase 1:</b> 10 Days of on-site commissioning and operational training.</li>
                <li><b>Phase 2:</b> 2 weeks of advanced on-site optimization 3 months post-installation.</li>
                <li><b>Phase 3:</b> 1 Month of technical immersion for key operators at the SOMA European facility.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div style="border: 1px solid #CBD5E1; padding: 30px; border-radius: 8px; background-color: #F8FAFC; margin-top: 30px; text-align: center;">
            <h2 style="color: #1E3A8A; margin-top:0;">Factory Acceptance Test (F.A.T.)</h2>
            <p style="font-size: 1.1rem; color: #475569; line-height: 1.6;">
                SOMA enforces a full <b>Factory Acceptance Test (F.A.T.)</b> prior to asset shipment.<br><br>
                The Ymtaco executive and technical teams are invited to our European manufacturing facility to conduct live testing. Complex production designs may be executed to verify registration, setup times, and HD print capability under measured conditions prior to final deployment.
            </p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown('<div class="executive-title">7. بروتوكولات التنفيذ واختبار المصنع</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="data-card">
            <h3 style="color: #1E3A8A; margin-top:0;">بروتوكول التدريب التقني</h3>
            <p style="font-size: 1.1rem; color: #0F172A;"><b>عند الاستحواذ على الحزمة الكاملة (4 ماكينات)، يتم توفير برنامج الدمج والتدريب التالي:</b></p>
            <ul style="line-height: 1.8; font-size: 1.1rem; color: #334155;">
                <li><b>المرحلة الأولى:</b> 10 أيام من التدريب والتشغيل في موقع المصنع.</li>
                <li><b>المرحلة الثانية:</b> أسبوعين من التدريب المتقدم للتحسين بعد 3 أشهر من التركيب.</li>
                <li><b>المرحلة الثالثة:</b> شهر كامل من التدريب الفني المتعمق للمشغلين الأساسيين في منشأة SOMA الأوروبية.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div style="border: 1px solid #CBD5E1; padding: 30px; border-radius: 8px; background-color: #F8FAFC; margin-top: 30px; text-align: center;">
            <h2 style="color: #1E3A8A; margin-top:0;">اختبار قبول المصنع (F.A.T.)</h2>
            <p style="font-size: 1.1rem; color: #475569; line-height: 1.6;">
                تطبق SOMA معيار <b>اختبار قبول المصنع (F.A.T)</b> بالكامل قبل شحن الأصول.<br><br>
                ندعو الفرق الفنية والتنفيذية في Ymtaco إلى منشأتنا التصنيعية في أوروبا لإجراء اختبارات حية. يمكن تنفيذ تصاميم إنتاجية معقدة للتحقق من دقة التطابق (Registration)، أوقات التجهيز، وجودة الطباعة (HD) تحت ظروف قياسية قبل النقل النهائي.
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
            * **Manual System:** Est. 10 mins/color. (1,200 sleeves = **200 Hours/Month**). Requires multiple skilled operators.
            * **S-Mount (Auto):** Est. 1.5 mins/color. (1,200 sleeves = **30 Hours/Month**). Single operator requirement.
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
            * **النظام اليدوي:** تقدير 10 دقائق/لون. (1,200 سليف = **200 ساعة عمل شهرياً**). يتطلب مشغلين ذوي مهارة عالية.
            * **نظام S-Mount (الآلي):** تقدير 1.5 دقيقة/لون. (1,200 سليف = **30 ساعة عمل شهرياً**). يتطلب مشغلاً واحداً.
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
        st.markdown("""Both SOMA IRIS and BOBST smartGPS utilize RFID chips to transfer offline mounting data to the press. However, the critical differentiation lies in **how the topography is measured** and the **associated OPEX structure.**""")
        
        st.markdown('<h3 style="color: #1E3A8A; margin-top: 20px;">🔍 Technological & Commercial Comparison</h3>', unsafe_allow_html=True)
        st.markdown("""
        <table class="corp-table">
            <tr>
                <th>Parameter</th>
                <th>SOMA IRIS (Tactile Measurement)</th>
                <th>BOBST smartGPS (Optical/Laser)</th>
            </tr>
            <tr>
                <td><strong>Measurement Mechanism</strong></td>
                <td class="highlight-adv">Utilizes highly sensitive mechanical contact sensors (pedals) to trace the exact physical topography of the plate.</td>
                <td class="highlight-mid">Relies on optical/laser scanning which may misinterpret transparent dirt or clear plate anomalies.</td>
            </tr>
            <tr>
                <td><strong>Defect Detection</strong></td>
                <td class="highlight-adv">Physically detects dirt, plate damage, and uneven sleeves, generating a precise TIR report before printing.</td>
                <td class="highlight-mid">Optical scanning is less effective at detecting physical, transparent debris on the plate surface.</td>
            </tr>
            <tr>
                <td><strong>OPEX (Sleeve Dependency)</strong></td>
                <td class="highlight-adv">Open Ecosystem: Can use and retrofit standard sleeves. Zero recurring proprietary costs.</td>
                <td class="highlight-mid">Closed Ecosystem: Mandates continuous purchase of highly expensive proprietary smart sleeves.</td>
            </tr>
            <tr>
                <td><strong>Future-Proofing</strong></td>
                <td class="highlight-adv">Hardware is ready to be upgraded to upcoming Digital Proofing technology (planned for 2027).</td>
                <td class="highlight-mid">System limitations typically require full unit replacements for next-generation upgrades.</td>
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
        st.markdown("""يعتمد كل من نظام SOMA IRIS ونظام BOBST smartGPS على شرائح RFID لنقل بيانات المونتاج إلى المطبعة. لكن الفارق الجوهري والخطير يكمن في **طريقة أخذ القياسات الفعلية (Measurement)** و**هيكلية التكاليف التشغيلية (OPEX)** لكل نظام.""")
        
        st.markdown('<h3 style="color: #1E3A8A; margin-top: 20px;">🔍 المقارنة التكنولوجية والتشغيلية</h3>', unsafe_allow_html=True)
        st.markdown("""
        <table class="corp-table">
            <tr>
                <th>المعيار</th>
                <th>SOMA IRIS (قراءة ميكانيكية لمسية)</th>
                <th>BOBST smartGPS (قراءة بصرية/ليزر)</th>
            </tr>
            <tr>
                <td><strong>آلية أخذ القياس (Offline)</strong></td>
                <td class="highlight-adv">تستخدم مستشعرات لمسية ميكانيكية دقيقة (Pedals) تلامس الكليشيه فعلياً وتأخذ قراءات مادية دقيقة.</td>
                <td class="highlight-mid">تعتمد على المسح البصري/الليزر (والذي قد يخطئ في قراءة الأوساخ الشفافة أو العيوب غير المرئية).</td>
            </tr>
            <tr>
                <td><strong>تقييم الجودة واكتشاف العيوب</strong></td>
                <td class="highlight-adv">الاحتكاك المادي يكتشف الأوساخ والتشوهات بدقة، ويصدر تقرير (TIR) قبل الطباعة لحماية الخامات.</td>
                <td class="highlight-mid">المسح البصري أقل كفاءة بكثير في اكتشاف العيوب والأوساخ المادية الموجودة على سطح السليف.</td>
            </tr>
            <tr>
                <td><strong>الأثر المالي الممتد (OPEX)</strong></td>
                <td class="highlight-adv">بيئة مفتوحة: يمكن استخدام السليفات العادية وتجهيزها بالشرائح بمرونة (بدون تكلفة إضافية مستمرة).</td>
                <td class="highlight-mid">بيئة مغلقة: تُلزم المصنع بشراء سليفات "ذكية" مدمجة خاصة بأسعار باهظة جداً طوال عمر الماكينة.</td>
            </tr>
            <tr>
                <td><strong>الاستدامة للمستقبل (Future-Proof)</strong></td>
                <td class="highlight-adv">الأجهزة مهيأة للترقية لتقنية (Digital Proofing) القادمة في 2027 دون تغيير الماكينة.</td>
                <td class="highlight-mid">الأنظمة المغلقة تتطلب عادة تغييرات جذرية ومكلفة لمواكبة التحديثات المستقبلية.</td>
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
