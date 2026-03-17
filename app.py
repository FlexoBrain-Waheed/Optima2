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
    .data-card {{ background-color: #F8FAFC; border-left: 6px solid #1E3A8A; border-right: 6px solid #1E3A8A; padding: 20px; margin-bottom: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); border-radius: 5px; }}
    .corp-table {{ width: 100%; border-collapse: collapse; margin-bottom: 25px; font-size: 1.1rem; text-align: {text_align}; direction: {direction}; }}
    .corp-table th {{ background-color: #1E3A8A; color: #FFFFFF; padding: 15px; text-align: {text_align}; border: 1px solid #CBD5E1; font-weight: 700; }}
    .corp-table td {{ padding: 15px; border: 1px solid #CBD5E1; color: #1E293B; }}
    .corp-table tr:nth-child(even) {{ background-color: #F1F5F9; }}
    .highlight-adv {{ color: #0F172A; font-weight: 700; background-color: #E2E8F0; }}
    .highlight-dis {{ color: #475569; font-weight: 400; background-color: #F8FAFC; }}
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
        "9. IRIS Topography System"
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
        "9. تقنية IRIS الطوبوغرافية"
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
        st.markdown('<div class="executive-title">1. Executive Summary: Objective Investment Evaluation</div>', unsafe_allow_html=True)
        st.markdown("""This report provides an objective technical and financial evaluation for the upcoming flexible packaging capital investment. The analysis contrasts the **SOMA OPTIMA2 850-1270-8 EG** (High-Performance/Flagship Class) with the **W&H Alphaflex** (Standard/Economy Class).""")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class="data-card">
                <h3 style="color: #1E3A8A; margin-top: 0;">SOMA OPTIMA 2</h3>
                <p><strong>Market Classification:</strong> Flagship / High-Performance Tier.</p>
                <p><strong>Structural Design:</strong> 130mm doubled frames designed for extended stability and high-speed operation (Upgraded to 600 m/min).</p>
                <p><strong>Operational Focus:</strong> Engineered for rapid job changeovers, utilizing advanced automation (IRIS) and an open-source OPEX policy.</p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class="data-card">
                <h3 style="color: #1E3A8A; margin-top: 0;">W&H Alphaflex</h3>
                <p><strong>Market Classification:</strong> Economy / Entry-Level Tier.</p>
                <p><strong>Structural Design:</strong> 55-60mm frames, optimized for standard operational speeds (500 m/min).</p>
                <p><strong>Operational Focus:</strong> Configured to reduce initial CAPEX by utilizing standard manual/semi-automatic systems and proprietary service models.</p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown('<div class="executive-title">1. الملخص التنفيذي: التقييم الاستثماري الموضوعي</div>', unsafe_allow_html=True)
        st.markdown("""يقدم هذا التقرير تقييماً فنياً ومالياً محايداً لقرار الاستثمار القادم في خطوط التغليف المرن. تقارن الدراسة بين ماكينة **SOMA OPTIMA2 850-1270-8 EG** (فئة الأداء العالي/الرائدة) وماكينة **W&H Alphaflex** (الفئة القياسية/الاقتصادية).""")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class="data-card">
                <h3 style="color: #1E3A8A; margin-top: 0;">SOMA OPTIMA 2</h3>
                <p><strong>التصنيف السوقي:</strong> الفئة الرائدة (Flagship) / الأداء العالي.</p>
                <p><strong>التصميم الهيكلي:</strong> جدران مزدوجة بسماكة 130 ملم مصممة للاستقرار طويل الأمد والتشغيل بسرعات فائقة (تمت الترقية إلى 600 متر/دقيقة).</p>
                <p><strong>التوجه التشغيلي:</strong> مصممة لتسريع تغيير الطلبيات بالاعتماد على الأتمتة المتقدمة (IRIS) وسياسة صيانة مفتوحة المصدر.</p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class="data-card">
                <h3 style="color: #1E3A8A; margin-top: 0;">W&H Alphaflex</h3>
                <p><strong>التصنيف السوقي:</strong> الفئة الاقتصادية (Entry-Level) / القياسية.</p>
                <p><strong>التصميم الهيكلي:</strong> جدران بسماكة 55-60 ملم، محسنة للعمل بالسرعات القياسية (500 متر/دقيقة).</p>
                <p><strong>التوجه التشغيلي:</strong> مصممة لتقليل التكلفة الرأسمالية المبدئية (CAPEX) باستخدام أنظمة يدوية/شبه آلية قياسية، ونماذج صيانة مقيدة.</p>
            </div>
            """, unsafe_allow_html=True)

# ==========================================
# Page 2: Structural & Engineering Superiority
# ==========================================
elif page_selection in ["2. Engineering & Performance", "2. التقييم الهندسي والأداء"]:
    if lang == "English":
        st.markdown('<div class="executive-title">2. Engineering Specifications & Performance Benchmarking</div>', unsafe_allow_html=True)
        st.markdown("""A comparative analysis of the core mechanical properties and thermal management capacities of both platforms.""")
        
        st.markdown("""
        <table class="corp-table">
            <tr><th>Engineering Specification</th><th>SOMA Optima 2 (Upgraded)</th><th>W&H Alphaflex</th><th>Operational Impact</th></tr>
            <tr><td><strong>Max Production Speed</strong></td><td class="highlight-adv">600 m/min</td><td class="highlight-dis">500 m/min</td><td>Higher throughput capacity and overall equipment effectiveness (OEE).</td></tr>
            <tr><td><strong>Drying Tunnel & Capacity</strong></td><td class="highlight-adv">6 Meters / 23 Drying Heads (with iDry system)</td><td class="highlight-dis">5.7 Meters / 17 Drying Heads</td><td>SOMA provides superior drying capacity. The iDry system automatically regulates drying based on solvent concentration, significantly reducing energy costs.</td></tr>
            <tr><td><strong>Cooling Cylinder</strong></td><td class="highlight-adv">448 mm Diameter</td><td class="highlight-dis">Standard</td><td>Increased diameter handles higher thermal loads efficiently at 600 m/min.</td></tr>
            <tr><td><strong>Machine Frame Thickness</strong></td><td class="highlight-adv">130 mm (Doubled)</td><td class="highlight-dis">~ 55 - 60 mm</td><td>Thicker frames effectively dampen resonance and vibration at peak speeds.</td></tr>
            <tr><td><strong>Anilox Mandrel Dimensions</strong></td><td class="highlight-adv">Diam. 175.1 mm / Perim. 625 mm</td><td class="highlight-dis">Standard Dimensions</td><td>Larger perimeter acts as a stabilizing core, minimizing flex.</td></tr>
            <tr><td><strong>Power Failure Protection (UPS)</strong></td><td class="highlight-adv">Included + Auto Printing Deck Throw-off</td><td class="highlight-dis">Included (20 KVA)</td><td>SOMA's UPS actively protects printing plates by automatically disengaging decks during outages.</td></tr>
            <tr><td><strong>Process Visibility</strong></td><td class="highlight-adv">Transparent Glass Windows</td><td class="highlight-dis">Closed (No Glass)</td><td>Enables constant visual monitoring of the print process.</td></tr>
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
            st.markdown('<h4 style="color: #1E3A8A; text-align: center;">🔥 Drying Capacity (Nozzles)</h4>', unsafe_allow_html=True)
            df_dry = pd.DataFrame({'Machine': ['SOMA Optima 2 (6m Tunnel)', 'W&H Alphaflex (5.7m Tunnel)'], 'Drying Nozzles': [23, 17]})
            chart_dry = alt.Chart(df_dry).mark_bar(size=50).encode(
                x=alt.X('Machine:N', title='', sort=None),
                y=alt.Y('Drying Nozzles:Q', title='Number of Drying Nozzles'),
                color=alt.condition(alt.datum.Machine == 'SOMA Optima 2 (6m Tunnel)', alt.value('#1E3A8A'), alt.value('#94A3B8'))
            ).properties(height=300)
            st.altair_chart(chart_dry, use_container_width=True)

    else:
        st.markdown('<div class="executive-title">2. التقييم الهندسي والأداء التشغيلي</div>', unsafe_allow_html=True)
        st.markdown("""تحليل مقارن للخصائص الميكانيكية الأساسية وقدرات الإدارة الحرارية للمنصتين.""")
        
        st.markdown("""
        <table class="corp-table">
            <tr><th>المواصفات الهندسية</th><th>SOMA Optima 2 (الإصدار المُرقى)</th><th>W&H Alphaflex</th><th>التأثير التشغيلي</th></tr>
            <tr><td><strong>السرعة الإنتاجية القصوى</strong></td><td class="highlight-adv">600 متر / دقيقة</td><td class="highlight-dis">500 متر / دقيقة</td><td>زيادة مباشرة في الطاقة الإنتاجية وكفاءة المعدات (OEE).</td></tr>
            <tr><td><strong>نفق التجفيف (Drying Tunnel)</strong></td><td class="highlight-adv">6 أمتار / 23 فوهة تجفيف (مزود بنظام iDry)</td><td class="highlight-dis">5.7 متر / 17 فوهة تجفيف</td><td>قدرة تجفيف أعلى. نظام iDry يقوم بضبط الطاقة آلياً بناءً على تركيز المذيبات، مما يقلل تكلفة استهلاك الطاقة بشكل كبير.</td></tr>
            <tr><td><strong>درفيل التبريد (Cooling Cylinder)</strong></td><td class="highlight-adv">قطر 448 ملم</td><td class="highlight-dis">قياسي</td><td>قطر أكبر للتعامل مع الأحمال الحرارية العالية بكفاءة على سرعة 600 متر/دقيقة.</td></tr>
            <tr><td><strong>سماكة جدار الماكينة (Frame)</strong></td><td class="highlight-adv">130 ملم (مزدوج)</td><td class="highlight-dis">~ 55 - 60 ملم</td><td>هيكل أكثر سماكة لامتصاص الاهتزازات (Resonance) على السرعات القصوى.</td></tr>
            <tr><td><strong>أبعاد أعمدة الأنيلوكس</strong></td><td class="highlight-adv">القطر: 175.1 ملم / المحيط: 625 ملم</td><td class="highlight-dis">أبعاد قياسية</td><td>المحيط الأكبر يوفر مركز ثقل يحد من الانحناء الميكانيكي.</td></tr>
            <tr><td><strong>الحماية من انقطاع التيار (UPS)</strong></td><td class="highlight-adv">مشمول + خاصية الإبعاد الآمن لوحدات الطباعة</td><td class="highlight-dis">مشمول (20 KVA)</td><td>نظام SOMA يقوم بإبعاد أسطوانات الطباعة آلياً عند انقطاع الكهرباء لحماية الكليشيهات من التلف.</td></tr>
            <tr><td><strong>الرؤية البصرية للعملية</strong></td><td class="highlight-adv">نوافذ زجاجية شفافة</td><td class="highlight-dis">وحدات مغلقة (بدون زجاج)</td><td>تتيح المراقبة البصرية المستمرة لسير الطباعة لاكتشاف الأخطاء مبكراً.</td></tr>
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
            st.markdown('<h4 style="color: #1E3A8A; text-align: center;">🔥 قدرة نفق التجفيف (عدد الفوهات)</h4>', unsafe_allow_html=True)
            df_dry = pd.DataFrame({'الماكينة': ['SOMA Optima 2 (نفق 6 متر)', 'W&H Alphaflex (نفق 5.7 متر)'], 'فوهات التجفيف': [23, 17]})
            chart_dry = alt.Chart(df_dry).mark_bar(size=50).encode(
                x=alt.X('الماكينة:N', title='', sort=None),
                y=alt.Y('فوهات التجفيف:Q', title='عدد فوهات التجفيف (Nozzles)'),
                color=alt.condition(alt.datum.الماكينة == 'SOMA Optima 2 (نفق 6 متر)', alt.value('#1E3A8A'), alt.value('#94A3B8'))
            ).properties(height=300)
            st.altair_chart(chart_dry, use_container_width=True)

# ==========================================
# Page 3: Operational Efficiency (Wash-up & Ink) 
# ==========================================
elif page_selection in ["3. Operational Efficiency", "3. الكفاءة التشغيلية"]:
    if lang == "English":
        st.markdown('<div class="executive-title">3. Operational Efficiency & Fluid Management</div>', unsafe_allow_html=True)
        st.markdown("""Evaluation of the fluid management systems and their impact on daily consumable optimization (Solvents & Inks).""")
        
        st.markdown('<h3 style="color: #1E3A8A; margin-top: 20px;">💧 Wash-up Cycle Data: Inkstorm vs. Turboclean</h3>', unsafe_allow_html=True)
        st.markdown("""
        <table class="corp-table">
            <tr>
                <th>Wash Cycle Parameter</th>
                <th>SOMA Optima 2 (Inkstorm)</th>
                <th>W&H Alphaflex (Turboclean S)</th>
            </tr>
            <tr>
                <td><strong>Fast Wash Time / Solvent Used</strong></td>
                <td class="highlight-adv">5 Minutes / 5 Liters</td>
                <td class="highlight-dis">4 Minutes / 12 Liters</td>
            </tr>
            <tr>
                <td><strong>Normal Wash Time / Solvent Used</strong></td>
                <td class="highlight-adv">7 Minutes / 10 Liters</td>
                <td class="highlight-dis">4 Minutes / 14 Liters</td>
            </tr>
            <tr>
                <td><strong>Deep Wash Time / Solvent Used</strong></td>
                <td class="highlight-adv">10 Minutes / 15 Liters</td>
                <td class="highlight-dis">4-10 Minutes / 16 Liters</td>
            </tr>
            <tr>
                <td><strong>System Architecture</strong></td>
                <td class="highlight-adv">Open & Customizable to specific ink chemistry</td>
                <td class="highlight-dis">Pre-set / Restricted parameters</td>
            </tr>
        </table>
        """, unsafe_allow_html=True)
        
        st.markdown('<h3 style="color: #1E3A8A; margin-top: 30px;">🎨 SOMA Ink Cartridge System: Spot Color Optimization</h3>', unsafe_allow_html=True)
        
        col_text, col_chart = st.columns([1.2, 1])
        with col_text:
            st.markdown("""
            <div class="data-card">
                <p style="font-size: 1.1rem;">A precise volume management system engineered to optimize the consumption of premium and spot colors.</p>
                <ul style="line-height: 1.8;">
                    <li><b>Micro-Volume Operation:</b> Requires a maximum operating volume of <b>4.5 Liters</b>.</li>
                    <li><b>Direct DBC Connection (15cm):</b> Utilizes ultra-short 15cm connections directly to the Doctor Blade Chamber (DBC), resulting in minimal residual ink volume within hoses.</li>
                    <li><b>Premium Ink Efficiency:</b> Highly effective for reducing material costs when processing expensive metallic or spot colors.</li>
                    <li><b>Process Control:</b> Features inline automatic viscosity control, stirring, and level sensing.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
        with col_chart:
            df_ink = pd.DataFrame({
                'System': ['Standard System (Long Hoses)', 'SOMA Ink Cartridge (15cm)'],
                'Residual Ink Waste (Liters/Job)': [3.5, 0.2]
            })
            chart_ink = alt.Chart(df_ink).mark_bar(size=40).encode(
                x=alt.X('Residual Ink Waste (Liters/Job):Q', title='Residual Ink per Job (Liters)'),
                y=alt.Y('System:N', sort='-x', title=''),
                color=alt.condition(alt.datum.System == 'SOMA Ink Cartridge (15cm)', alt.value('#1E3A8A'), alt.value('#94A3B8')),
                tooltip=['System', 'Residual Ink Waste (Liters/Job)']
            ).properties(height=250, title="Residual Ink Assessment (Spot Color Change)")
            st.altair_chart(chart_ink, use_container_width=True)

    else:
        st.markdown('<div class="executive-title">3. الكفاءة التشغيلية وإدارة السوائل</div>', unsafe_allow_html=True)
        st.markdown("""تقييم أنظمة إدارة السوائل وأثرها على تحسين استهلاك المواد اليومية (المذيبات والأحبار).""")
        
        st.markdown('<h3 style="color: #1E3A8A; margin-top: 20px;">💧 بيانات دورة الغسيل: نظام Inkstorm مقابل Turboclean</h3>', unsafe_allow_html=True)
        st.markdown("""
        <table class="corp-table">
            <tr>
                <th>معايير دورة الغسيل</th>
                <th>SOMA Optima 2 (نظام Inkstorm)</th>
                <th>W&H Alphaflex (نظام Turboclean)</th>
            </tr>
            <tr>
                <td><strong>الغسيل السريع (الوقت / الاستهلاك)</strong></td>
                <td class="highlight-adv">5 دقائق / 5 لتر</td>
                <td class="highlight-dis">4 دقائق / 12 لتر</td>
            </tr>
            <tr>
                <td><strong>الغسيل العادي (الوقت / الاستهلاك)</strong></td>
                <td class="highlight-adv">7 دقائق / 10 لتر</td>
                <td class="highlight-dis">4 دقائق / 14 لتر</td>
            </tr>
            <tr>
                <td><strong>الغسيل العميق (الوقت / الاستهلاك)</strong></td>
                <td class="highlight-adv">10 دقائق / 15 لتر</td>
                <td class="highlight-dis">4-10 دقائق / 16 لتر</td>
            </tr>
            <tr>
                <td><strong>هيكلية النظام</strong></td>
                <td class="highlight-adv">مفتوح وقابل للضبط حسب كيمياء الحبر</td>
                <td class="highlight-dis">معايير مسبقة الضبط / مقيدة</td>
            </tr>
        </table>
        """, unsafe_allow_html=True)
        
        st.markdown('<h3 style="color: #1E3A8A; margin-top: 30px;">🎨 نظام خراطيش الحبر (Ink Cartridge): تحسين استهلاك الألوان الخاصة</h3>', unsafe_allow_html=True)
        
        col_text, col_chart = st.columns([1.2, 1])
        with col_text:
            st.markdown("""
            <div class="data-card">
                <p style="font-size: 1.1rem;">نظام دقيق لإدارة الحجم مصمم لتحسين استهلاك الألوان الخاصة والممتازة.</p>
                <ul style="line-height: 1.8;">
                    <li><b>التشغيل بالحجم الدقيق:</b> يتطلب حجم تشغيل أقصى يبلغ <b>4.5 لتر فقط</b>.</li>
                    <li><b>اتصال مباشر بـ 15 سم:</b> يستخدم خراطيم قصيرة جداً (15 سم) متصلة مباشرة بغرفة الشفرات (DBC)، مما يؤدي إلى تقليل الحبر المتبقي داخل الخراطيم للحد الأدنى.</li>
                    <li><b>كفاءة الأحبار الممتازة:</b> فعال جداً في خفض تكاليف المواد عند استخدام الألوان الخاصة أو المعدنية باهظة الثمن.</li>
                    <li><b>التحكم بالعملية:</b> مزود بنظام آلي مدمج للتحكم باللزوجة، والخلط، واستشعار المستوى.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
        with col_chart:
            df_ink_ar = pd.DataFrame({
                'النظام': ['الأنظمة القياسية (خراطيم طويلة)', 'نظام SOMA خراطيش (خراطيم 15 سم)'],
                'الحبر المتبقي (لتر)': [3.5, 0.2]
            })
            chart_ink_ar = alt.Chart(df_ink_ar).mark_bar(size=40).encode(
                x=alt.X('الحبر المتبقي (لتر):Q', title='متوسط الحبر المتبقي لكل طلبية (لتر)'),
                y=alt.Y('النظام:N', sort='-x', title=''),
                color=alt.condition(alt.datum.النظام == 'نظام SOMA خراطيش (خراطيم 15 سم)', alt.value('#1E3A8A'), alt.value('#94A3B8')),
                tooltip=['النظام', 'الحبر المتبقي (لتر)']
            ).properties(height=250, title="تقييم الحبر المتبقي (عند تغيير لون خاص)")
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
            <tr><th>Operational Aspect</th><th>SOMA Framework</th><th>W&H Framework</th></tr>
            <tr><td><strong>Spare Parts Sourcing</strong></td><td class="highlight-adv">Open Source (Authorized local procurement permitted)</td><td class="highlight-dis">Restricted (Vendor procurement mandated)</td></tr>
            <tr><td><strong>Service Cost Structure</strong></td><td class="highlight-adv">Standardized intervention rates</td><td class="highlight-dis">Premium service tier rates</td></tr>
            <tr><td><strong>Asset Retrofitting</strong></td><td class="highlight-adv">Designed for high upgradeability</td><td class="highlight-dis">Rigid specification / High upgrade costs</td></tr>
        </table>
        """, unsafe_allow_html=True)
    else:
        st.markdown('<div class="executive-title">4. النفقات التشغيلية (OPEX) وسياسة الصيانة</div>', unsafe_allow_html=True)
        st.markdown("""تقييم تكاليف التشغيل لما بعد فترة الضمان بناءً على الأطر الخدمية للشركات المصنعة.""")
        
        st.markdown("""
        <table class="corp-table">
            <tr><th>جانب التشغيل والصيانة</th><th>إطار عمل SOMA</th><th>إطار عمل W&H</th></tr>
            <tr><td><strong>مصادر قطع الغيار</strong></td><td class="highlight-adv">مفتوح المصدر (يُسمح بالشراء المحلي المعتمد)</td><td class="highlight-dis">مقيد (يلزم الشراء من الشركة المصنعة)</td></tr>
            <tr><td><strong>هيكل تكاليف الخدمة</strong></td><td class="highlight-adv">معدلات تدخل وصيانة قياسية</td><td class="highlight-dis">معدلات خدمة ذات تسعير ممتاز (Premium)</td></tr>
            <tr><td><strong>ترقية الأصول (Retrofit)</strong></td><td class="highlight-adv">مصممة بقابلية عالية للترقية المستقبلية</td><td class="highlight-dis">مواصفات صلبة / تكاليف ترقية مرتفعة</td></tr>
        </table>
        """, unsafe_allow_html=True)

# ==========================================
# Page 5: TCO Hidden Costs
# ==========================================
elif page_selection in ["5. Total Cost of Ownership (TCO)", "5. التكلفة الإجمالية للملكية (TCO)"]:
    if lang == "English":
        st.markdown('<div class="executive-title">5. Total Cost of Ownership (TCO) Analysis</div>', unsafe_allow_html=True)
        st.markdown("""A detailed financial alignment analyzing the initial base configuration against the necessary additions required to achieve equivalent operational capability.""")
        
        data = pd.DataFrame({'Equipment Add-on': ['ITS Cooling', '100% Camera', 'Sleeves & Aniloxes', 'Carbon Mandrels', 'ALU/PE Handling Kit', 'Roll Lift'], 'Estimated Value (€)': [50000, 71000, 50000, 30000, 50000, 15000]})
        chart = alt.Chart(data).mark_bar(color='#94A3B8', cornerRadiusEnd=4).encode(
            x=alt.X('Estimated Value (€):Q', title='Estimated Value (€)'), y=alt.Y('Equipment Add-on:N', sort='-x', title=''), tooltip=['Equipment Add-on', 'Estimated Value (€)']
        ).properties(height=300, title="Valuation of Necessary Add-ons for Standard Economy Configuration")
        st.altair_chart(chart, use_container_width=True)

        st.markdown("""
        <table class="corp-table">
            <tr><th>Operational Requirement</th><th>SOMA Optima 2</th><th>W&H Alphaflex</th><th>Estimated Alignment Cost (€)</th></tr>
            <tr><td><strong>Ink Thermal Stabilization (ITS)</strong></td><td class="highlight-adv">✔️ Integrated</td><td class="highlight-dis">➖ Not Included</td><td><strong>~ € 50,000</strong></td></tr>
            <tr><td><strong>100% Print Inspection Camera</strong></td><td class="highlight-adv">✔️ Included (BST iPQ Check)</td><td class="highlight-dis">➖ Optional Add-on</td><td><strong>~ € 71,000</strong></td></tr>
            <tr><td><strong>Initial Sleeves & Aniloxes (8+8)</strong></td><td class="highlight-adv">✔️ Included</td><td class="highlight-dis">➖ Not Included</td><td><strong>~ € 50,000</strong></td></tr>
            <tr><td><strong>ALU & PE Handling Kit (In/Out-feed)</strong></td><td class="highlight-adv">✔️ Included</td><td class="highlight-dis">➖ Not Included</td><td><strong>~ € 50,000</strong></td></tr>
            <tr><td><strong>Carbon Fiber Mandrels</strong></td><td class="highlight-adv">✔️ Standard</td><td class="highlight-dis">➖ Optional Upgrade</td><td><strong>~ € 30,000</strong></td></tr>
            <tr><td><strong>Payment Terms</strong></td><td class="highlight-adv">✔️ Net Wire Transfers</td><td class="highlight-dis">➖ 75% L/C Requirement</td><td><strong>Variable Bank Fees</strong></td></tr>
        </table>
        """, unsafe_allow_html=True)
        st.info("📊 **Financial Note:** The initial CAPEX of the base economy model requires careful assessment. Aligning it to the high-performance standard of the Optima 2 involves approximately **€ 250,000** in required additions.")
    
    else:
        st.markdown('<div class="executive-title">5. تحليل التكلفة الإجمالية للملكية (TCO)</div>', unsafe_allow_html=True)
        st.markdown("""مواءمة مالية تفصيلية تحلل التكوين الأساسي المبدئي مقابل الإضافات الضرورية المطلوبة لتحقيق قدرة تشغيلية مكافئة.""")
        
        data = pd.DataFrame({'المعدة المطلوبة': ['نظام تبريد الحبر (ITS)', 'كاميرا فحص 100%', 'سليفات وأنيلوكس', 'ترقية أعمدة الكاربون', 'تجهيزات طباعة ALU/PE', 'رافعة الرولات'], 'القيمة التقديرية (يورو)': [50000, 71000, 50000, 30000, 50000, 15000]})
        chart = alt.Chart(data).mark_bar(color='#94A3B8', cornerRadiusEnd=4).encode(
            x=alt.X('القيمة التقديرية (يورو):Q', title='القيمة التقديرية (يورو)'), y=alt.Y('المعدة المطلوبة:N', sort='-x', title=''), tooltip=['المعدة المطلوبة', 'القيمة التقديرية (يورو)']
        ).properties(height=300, title="تقييم الإضافات الضرورية لتكوين الفئة الاقتصادية القياسية")
        st.altair_chart(chart, use_container_width=True)

        st.markdown("""
        <table class="corp-table">
            <tr><th>المتطلب التشغيلي</th><th>SOMA Optima 2</th><th>W&H Alphaflex</th><th>تكلفة المواءمة التقديرية</th></tr>
            <tr><td><strong>نظام تبريد الحبر (ITS)</strong></td><td class="highlight-adv">✔️ مدمج بالنظام</td><td class="highlight-dis">➖ غير مشمول</td><td><strong>~ € 50,000</strong></td></tr>
            <tr><td><strong>كاميرا فحص الجودة 100%</strong></td><td class="highlight-adv">✔️ مشمولة (BST iPQ Check)</td><td class="highlight-dis">➖ إضافة اختيارية</td><td><strong>~ € 71,000</strong></td></tr>
            <tr><td><strong>أطقم السليفات والأنيلوكس (8+8)</strong></td><td class="highlight-adv">✔️ مشمولة</td><td class="highlight-dis">➖ غير مشمولة</td><td><strong>~ € 50,000</strong></td></tr>
            <tr><td><strong>تجهيزات طباعة ALU و PE</strong></td><td class="highlight-adv">✔️ مشمولة</td><td class="highlight-dis">➖ غير مشمولة</td><td><strong>~ € 50,000</strong></td></tr>
            <tr><td><strong>أعمدة كاربون فايبر للطباعة</strong></td><td class="highlight-adv">✔️ مواصفة قياسية</td><td class="highlight-dis">➖ تتطلب ترقية</td><td><strong>~ € 30,000</strong></td></tr>
            <tr><td><strong>الشروط المالية</strong></td><td class="highlight-adv">✔️ حوالات بنكية (Wire)</td><td class="highlight-dis">➖ اشتراط 75% اعتماد (L/C)</td><td><strong>رسوم بنكية متغيرة</strong></td></tr>
        </table>
        """, unsafe_allow_html=True)
        st.info("📊 **ملاحظة مالية:** يتطلب التقييم المالي (CAPEX) للنموذج الاقتصادي الأساسي تحليلاً دقيقاً. مواءمة النموذج ليصل للمعيار عالي الأداء لماكينة Optima 2 يتطلب حوالي **250,000 يورو** من الإضافات الضرورية.")

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
# Page 9: SOMA IRIS (Zero Waste Tech)
# ==========================================
elif page_selection in ["9. IRIS Topography System", "9. تقنية IRIS الطوبوغرافية"]:
    if lang == "English":
        st.markdown('<div class="executive-title">9. IRIS Technology: Optimized Print Setup</div>', unsafe_allow_html=True)
        st.markdown("""The **IRIS (Intelligent Register and Impression Setting)** utilizes mechanical contact sensors (pedals) to map the physical topography of the plate offline. This data automates impression and register settings on the press, optimizing setup material usage.""")
        
        st.markdown('<h3 style="color: #1E3A8A; margin-top: 20px;">🔍 Technological Mechanism</h3>', unsafe_allow_html=True)
        st.markdown("""
        <table class="corp-table">
            <tr>
                <th>Parameter</th>
                <th>SOMA IRIS (Tactile Topography)</th>
                <th>Optical/Standard Systems</th>
            </tr>
            <tr>
                <td><strong>Measurement</strong></td>
                <td class="highlight-adv">Tactile sensors map physical plate topography</td>
                <td class="highlight-dis">Optical reading of dots or RFID dependencies</td>
            </tr>
            <tr>
                <td><strong>Pre-Press QA</strong></td>
                <td class="highlight-adv">Generates TIR (Total Indicator Reading) report prior to print</td>
                <td class="highlight-dis">Standard visual inspection</td>
            </tr>
            <tr>
                <td><strong>Future Scalability</strong></td>
                <td class="highlight-adv">Platform designed for 2027 Digital Proofing integration</td>
                <td class="highlight-dis">Hardware limitations may require replacement</td>
            </tr>
        </table>
        """, unsafe_allow_html=True)
        
        st.markdown('<h3 style="color: #1E3A8A; margin-top: 30px;">📊 Estimated Material Optimization (150 Jobs/Month)</h3>', unsafe_allow_html=True)
        
        df_waste = pd.DataFrame({
            'Setup Method': ['Standard Camera Setup', 'SOMA IRIS'],
            'Est. Waste (Meters/Month)': [30000, 1500]
        })
        chart_waste = alt.Chart(df_waste).mark_bar(size=50).encode(
            x=alt.X('Setup Method:N', title='', sort=None),
            y=alt.Y('Est. Waste (Meters/Month):Q', title='Substrate Used in Setup (Meters)'),
            color=alt.condition(alt.datum['Setup Method'] == 'SOMA IRIS', alt.value('#1E3A8A'), alt.value('#94A3B8'))
        ).properties(height=300)
        st.altair_chart(chart_waste, use_container_width=True)

    else:
        st.markdown('<div class="executive-title">9. تكنولوجيا IRIS: التحسين الطوبوغرافي لإعداد الطباعة</div>', unsafe_allow_html=True)
        st.markdown("""يستخدم نظام **IRIS** مستشعرات اتصال ميكانيكية لمسح الطوبوغرافيا المادية للكليشيه (Offline). تقوم هذه البيانات بأتمتة إعدادات الضغط والتطابق على المطبعة، مما يحسن استهلاك مواد التجهيز.""")
        
        st.markdown('<h3 style="color: #1E3A8A; margin-top: 20px;">🔍 الآلية التكنولوجية</h3>', unsafe_allow_html=True)
        st.markdown("""
        <table class="corp-table">
            <tr>
                <th>المعيار</th>
                <th>SOMA IRIS (قراءة طوبوغرافية)</th>
                <th>الأنظمة البصرية/القياسية</th>
            </tr>
            <tr>
                <td><strong>آلية القياس</strong></td>
                <td class="highlight-adv">مستشعرات لمسية ترسم الطوبوغرافيا الفيزيائية للكليشيه</td>
                <td class="highlight-dis">قراءة بصرية للنقاط أو الاعتماد على تقنية RFID</td>
            </tr>
            <tr>
                <td><strong>فحص الجودة المسبق</strong></td>
                <td class="highlight-adv">إصدار تقرير (TIR) قبل بدء الطباعة الفعلية</td>
                <td class="highlight-dis">فحص بصري قياسي</td>
            </tr>
            <tr>
                <td><strong>القابلية للتوسع</strong></td>
                <td class="highlight-adv">منصة مهيأة لدمج تقنية (Digital Proofing) لعام 2027</td>
                <td class="highlight-dis">قيود في الأجهزة قد تتطلب الاستبدال</td>
            </tr>
        </table>
        """, unsafe_allow_html=True)
        
        st.markdown('<h3 style="color: #1E3A8A; margin-top: 30px;">📊 تحسين استهلاك المواد التقديري (150 طلبية/شهر)</h3>', unsafe_allow_html=True)
            
        df_waste = pd.DataFrame({
            'طريقة الإعداد': ['الضبط القياسي / الكاميرات', 'نظام SOMA IRIS'],
            'الاستهلاك المقدر (متر/شهر)': [30000, 1500]
        })
        chart_waste = alt.Chart(df_waste).mark_bar(size=50).encode(
            x=alt.X('طريقة الإعداد:N', title='', sort=None),
            y=alt.Y('الاستهلاك المقدر (متر/شهر):Q', title='الخامات المستخدمة في الإعداد (متر)'),
            color=alt.condition(alt.datum['طريقة الإعداد'] == 'نظام SOMA IRIS', alt.value('#1E3A8A'), alt.value('#94A3B8'))
        ).properties(height=300)
        st.altair_chart(chart_waste, use_container_width=True)
