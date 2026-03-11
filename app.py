import streamlit as st
import pandas as pd
import altair as alt

# 1. Page Configuration
st.set_page_config(page_title="Executive Investment Proposal | SOMA", layout="wide", initial_sidebar_state="expanded")

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
    st.markdown("<h2 style='text-align: center; color: #1E3A8A; font-family: sans-serif;'>🔒 Confidential Executive Dashboard <br> منصة الإدارة التنفيذية المغلقة</h2>", unsafe_allow_html=True)
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
    .data-card-soma {{ background-color: #F8FAFC; border-left: 6px solid #059669; border-right: 6px solid #059669; padding: 20px; margin-bottom: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); border-radius: 5px; }}
    .data-card-wh {{ background-color: #FAFAF9; border-left: 6px solid #DC2626; border-right: 6px solid #DC2626; padding: 20px; margin-bottom: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); border-radius: 5px; }}
    .corp-table {{ width: 100%; border-collapse: collapse; margin-bottom: 25px; font-size: 1.1rem; text-align: {text_align}; direction: {direction}; }}
    .corp-table th {{ background-color: #1E3A8A; color: #FFFFFF; padding: 15px; text-align: {text_align}; border: 1px solid #CBD5E1; font-weight: 700; }}
    .corp-table td {{ padding: 15px; border: 1px solid #CBD5E1; color: #1E293B; }}
    .corp-table tr:nth-child(even) {{ background-color: #F1F5F9; }}
    .highlight-adv {{ color: #059669; font-weight: 900; background-color: #D1FAE5; }}
    .highlight-dis {{ color: #DC2626; font-weight: 700; background-color: #FEE2E2; }}
    .total-investment {{ font-size: 1.8rem; font-weight: 900; color: #FFFFFF; text-align: center; background-color: #1E3A8A; padding: 20px; border-radius: 8px; margin-top: 20px; }}
    .metric-value {{ font-size: 2rem; font-weight: bold; color: #1E3A8A; }}
    </style>
""", unsafe_allow_html=True)

# 3. Sidebar Navigation
nav_options = {
    "English": [
        "1. Executive Summary", 
        "2. Structural & Engineering Superiority", 
        "3. Operational Efficiency & ROI ♻️", 
        "4. Long-Term Opex & Service 🔧", 
        "5. Hidden Costs (TCO) 📊", 
        "6. Turn-Key Investment", 
        "7. Strategic Partnership 🚀"
    ],
    "العربية": [
        "1. الملخص التنفيذي", 
        "2. التفوق الهيكلي والهندسي", 
        "3. كفاءة التشغيل والعائد (ROI) ♻️", 
        "4. تكاليف الصيانة والاستدامة 🔧", 
        "5. التكاليف الخفية (TCO) 📊", 
        "6. استثمار المشروع المتكامل", 
        "7. شراكة التحدي والإثبات 🚀"
    ]
}

page_selection = st.sidebar.radio("Navigation / الفهرس:" if lang == "English" else "فهرس التقرير:", nav_options[lang])

st.sidebar.markdown("---")
if lang == "English":
    st.sidebar.markdown("**Prepared For:**\nYmtaco for Trading and Investment Ltd.\n\n**Prepared By:**\nWaheed Waleed Malik\nNexFlexo | SOMA Agent")
else:
    st.sidebar.markdown("**تم الإعداد لصالح:**\nإدارة شركة Ymtaco للتجارة والاستثمار\n\n**إعداد التقرير:**\nوحيد وليد مالك\nNexFlexo | الوكيل المعتمد لشركة SOMA")

# ==========================================
# Page 1: Executive Summary
# ==========================================
if page_selection in ["1. Executive Summary", "1. الملخص التنفيذي"]:
    if lang == "English":
        st.markdown('<div class="executive-title">1. Executive Summary: Strategic Press Investment</div>', unsafe_allow_html=True)
        st.write("This proposal outlines a comprehensive technical and financial evaluation for the upcoming flexible packaging capital investment. The core analysis compares the **SOMA OPTIMA2 850-1270-8 EG** (Flagship Class) against the **W&H Alphaflex** (Economy/Entry-Level Class).")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class="data-card-soma">
                <h3 style="color: #059669; margin-top: 0;">🏆 SOMA OPTIMA 2</h3>
                <p><strong>Classification:</strong> Flagship / Premium Class - Fully Equipped.</p>
                <p><strong>Structural Integrity:</strong> 130mm doubled frames guaranteeing absolute stability and long-term durability.</p>
                <p><strong>Operational Focus:</strong> The absolute "Champion of Short Runs", featuring rapid changeovers, open-source spare parts, and floor-level operator ergonomics.</p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class="data-card-wh">
                <h3 style="color: #DC2626; margin-top: 0;">⚠️ W&H Alphaflex</h3>
                <p><strong>Classification:</strong> Economy / Entry-Level Class - Stripped down to fit low budgets.</p>
                <p><strong>Structural Integrity:</strong> Lightweight ~55-60mm frames, prone to resonance at high speeds.</p>
                <p><strong>Operational Focus:</strong> Restrictive vendor lock-in for spare parts, high service costs, and poor ergonomic design (hard to reach upper decks from the floor).</p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown('<div class="executive-title">1. الملخص التنفيذي: التقييم الاستراتيجي للاستثمار</div>', unsafe_allow_html=True)
        st.write("يوضح هذا التقرير التحليل الفني والمالي الشامل لقرار الاستثمار القادم في خطوط التغليف المرن. تعتمد المقارنة الجوهرية على وضع ماكينة **SOMA OPTIMA2 850-1270-8 EG** (الفئة الرائدة) في مواجهة ماكينة **W&H Alphaflex** (الفئة الاقتصادية).")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class="data-card-soma">
                <h3 style="color: #059669; margin-top: 0;">🏆 SOMA OPTIMA 2</h3>
                <p><strong>التصنيف السوقي:</strong> قمة الهرم التكنولوجي (Flagship Class) - كاملة المواصفات.</p>
                <p><strong>الصلابة الهيكلية:</strong> جدران معدنية مزدوجة بسماكة 130 ملم تضمن استقراراً مطلقاً وعمراً افتراضياً طويلاً.</p>
                <p><strong>التوجه التشغيلي:</strong> "بطلة الطلبيات القصيرة"، تغيير سريع للطلبيات، قطع غيار غير محتكرة، وتصميم مريح يتيح للطباع الوصول لأعلى وحدة طباعة من مستوى الأرض.</p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class="data-card-wh">
                <h3 style="color: #DC2626; margin-top: 0;">⚠️ W&H Alphaflex</h3>
                <p><strong>التصنيف السوقي:</strong> الفئة الاقتصادية (Entry-Level) - مجردة لخفض التكلفة.</p>
                <p><strong>الصلابة الهيكلية:</strong> جدران خفيفة بسماكة 55-60 ملم تقريباً، مما يجعلها عرضة للاهتزاز (Bouncing) على السرعات العالية.</p>
                <p><strong>التوجه التشغيلي:</strong> احتكار عالي لقطع الغيار، تكاليف صيانة باهظة، وتصميم غير مريح (مرتفعة جداً وتصعب إدارتها من مستوى الأرض).</p>
            </div>
            """, unsafe_allow_html=True)

# ==========================================
# Page 2: Structural & Engineering Benchmarking
# ==========================================
elif page_selection in ["2. Structural & Engineering Superiority", "2. التفوق الهيكلي والهندسي"]:
    if lang == "English":
        st.markdown('<div class="executive-title">2. Structural Integrity & Engineering Superiority</div>', unsafe_allow_html=True)
        st.write("A machine's lifespan and print quality (HD) are directly determined by its core structural rigidity.")
        
        # Frame Thickness Chart
        st.subheader("Machine Frame Wall Thickness (Resonance Elimination)")
        frame_data = pd.DataFrame({
            'Machine': ['SOMA Optima 2 (Double Wall)', 'W&H Alphaflex'],
            'Thickness (mm)': [130, 60]
        })
        chart1 = alt.Chart(frame_data).mark_bar(size=60).encode(
            x=alt.X('Machine:N', title=''),
            y=alt.Y('Thickness (mm):Q', title='Frame Thickness in Millimeters'),
            color=alt.condition(alt.datum.Machine == 'SOMA Optima 2 (Double Wall)', alt.value('#059669'), alt.value('#DC2626'))
        ).properties(height=300)
        st.altair_chart(chart1, use_container_width=True)

        st.markdown("""
        <table class="corp-table">
            <tr><th>Engineering Specification</th><th>SOMA Optima 2</th><th>W&H Alphaflex</th><th>Operational Impact</th></tr>
            <tr><td><strong>Machine Frame Thickness</strong></td><td class="highlight-adv">130 mm (Doubled)</td><td class="highlight-dis">~ 55 - 60 mm</td><td>Massive difference in long-term stability and elimination of bouncing at high speeds.</td></tr>
            <tr><td><strong>Operator Ergonomics (Height)</strong></td><td class="highlight-adv">Accessible from floor</td><td class="highlight-dis">Too High</td><td>Optima 2 allows operators to touch the highest printing deck and change sleeves easily without ladders.</td></tr>
            <tr><td><strong>Printing Cylinder Mandrels</strong></td><td class="highlight-adv">Carbon Composite</td><td class="highlight-dis">Standard Steel</td><td>Carbon absorbs vibrations, ensuring perfect HD dot reproduction.</td></tr>
            <tr><td><strong>Pre-Shipment Testing</strong></td><td class="highlight-adv">Full F.A.T. Performed</td><td class="highlight-dis">Not Standard</td><td>SOMA performs full Factory Acceptance Tests before shipment to guarantee zero installation surprises.</td></tr>
        </table>
        """, unsafe_allow_html=True)
    else:
        st.markdown('<div class="executive-title">2. التفوق الهيكلي والصلابة الهندسية</div>', unsafe_allow_html=True)
        st.write("العمر الافتراضي للماكينة وجودة الطباعة الدقيقة (HD) يعتمدان بشكل مباشر على الصلابة الهيكلية والميكانيكية للماكينة.")
        
        st.subheader("مقارنة سماكة الهيكل المعدني (القدرة على امتصاص الاهتزازات)")
        frame_data = pd.DataFrame({
            'الماكينة': ['SOMA Optima 2 (جدار مزدوج)', 'W&H Alphaflex'],
            'السماكة (ملم)': [130, 60]
        })
        chart1 = alt.Chart(frame_data).mark_bar(size=60).encode(
            x=alt.X('الماكينة:N', title='', sort=None),
            y=alt.Y('السماكة (ملم):Q', title='سماكة الهيكل بالمليمتر'),
            color=alt.condition(alt.datum.الماكينة == 'SOMA Optima 2 (جدار مزدوج)', alt.value('#059669'), alt.value('#DC2626'))
        ).properties(height=300)
        st.altair_chart(chart1, use_container_width=True)

        st.markdown("""
        <table class="corp-table">
            <tr><th>المواصفات الهندسية</th><th>SOMA Optima 2</th><th>W&H Alphaflex</th><th>التأثير التشغيلي</th></tr>
            <tr><td><strong>سماكة جدار الماكينة (Frame)</strong></td><td class="highlight-adv">130 ملم (مزدوج)</td><td class="highlight-dis">~ 55 - 60 ملم</td><td>فارق هائل في الاستقرار طويل الأمد والقضاء التام على الاهتزاز (Bouncing).</td></tr>
            <tr><td><strong>بيئة العمل (ارتفاع الماكينة)</strong></td><td class="highlight-adv">في متناول اليد من الأرض</td><td class="highlight-dis">مرتفعة جداً</td><td>تصميم SOMA يتيح للطباع الوصول لأعلى وحدة طباعة وتغيير السليفات بسهولة تامة من مستوى الأرض.</td></tr>
            <tr><td><strong>أعمدة أسطوانات الطباعة</strong></td><td class="highlight-adv">كاربون فايبر</td><td class="highlight-dis">حديد عادي</td><td>الكاربون يمتص الاهتزازات تماماً لضمان جودة HD.</td></tr>
            <tr><td><strong>اختبارات ما قبل الشحن</strong></td><td class="highlight-adv">شاملة (F.A.T)</td><td class="highlight-dis">غير قياسية</td><td>SOMA هي الوحيدة التي تقوم بتشغيل واختبار الماكينة بالكامل (FAT) قبل الشحن لضمان عدم وجود أي مفاجآت عند التركيب.</td></tr>
        </table>
        """, unsafe_allow_html=True)

# ==========================================
# Page 3: Operational Efficiency (Wash-up & Ink)
# ==========================================
elif page_selection in ["3. Operational Efficiency & ROI ♻️", "3. كفاءة التشغيل والعائد (ROI) ♻️"]:
    if lang == "English":
        st.markdown('<div class="executive-title">3. Operational Efficiency & Ink Management</div>', unsafe_allow_html=True)
        st.write("SOMA provides intelligent, flexible systems that drastically reduce daily consumable waste (Solvents & High-pigment Inks).")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 💧 Wash-up Statistics (Inkstorm vs. Turboclean)")
            st.write("SOMA's system is open-sourced and highly customizable to real customer needs, unlike rigid competitor systems.")
            wash_data = pd.DataFrame({
                'Program': ['Fast Wash', 'Normal Wash', 'Deep Wash'],
                'SOMA Solvent (L)': [5, 10, 15],
                'W&H Solvent (L)': [0, 12, 0] # 0 used to indicate missing rigid data
            })
            st.markdown("""
            * **Short Program:** 5 Liters / 5 Minutes
            * **Medium Program:** 10 Liters / 7 Minutes
            * **Long Program:** 15 Liters / 10 Minutes
            """)
        with col2:
            st.markdown("### 🎨 SOMA Ink Cartridge System")
            st.write("A revolutionary system designed specifically for short runs and expensive special effect/metallic colours.")
            st.markdown("""
            * **Max Volume:** Only 4.5 Liters required to run.
            * **Benefit:** Massively reduces residual ink waste.
            * **Features:** Optionally available with inline viscosity control, stirrer, and level sensor.
            * **ROI:** Saves thousands of Euros annually on wasted spot colours compared to standard large ink buckets.
            """)
    else:
        st.markdown('<div class="executive-title">3. كفاءة التشغيل اليومية وعائد الاستثمار (ROI)</div>', unsafe_allow_html=True)
        st.write("تقدم SOMA أنظمة ذكية ومرنة لتقليل هدر المواد الاستهلاكية اليومية (المذيبات والأحبار الخاصة) بشكل جذري.")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 💧 إحصائيات دورة الغسيل (Inkstorm)")
            st.write("نظام SOMA مفتوح وقابل للتخصيص حسب احتياج العميل الفعلي، مما يوفر استهلاك المذيبات (Solvent) بذكاء.")
            st.markdown("""
            <div style="background-color: #F8FAFC; padding: 15px; border-radius: 5px; border-right: 5px solid #2563EB;">
            <b>برنامج الغسيل السريع (الخفيف):</b> يستهلك 5 لتر فقط / 5 دقائق.<br>
            <b>برنامج الغسيل المتوسط:</b> يستهلك 10 لتر / 7 دقائق.<br>
            <b>برنامج الغسيل العميق:</b> يستهلك 15 لتر / 10 دقائق.
            </div>
            """, unsafe_allow_html=True)
            st.info("بينما النظام المنافس (W&H) يستهلك متوسط 12 لتر لكل دورة غسيل ببرمجة مغلقة ومقيدة.")
            
        with col2:
            st.markdown("### 🎨 نظام خراطيش الحبر (Ink Cartridge)")
            st.write("نظام ثوري مصمم خصيصاً للطلبيات القصيرة (Short Runs) والألوان الخاصة والمعدنية باهظة الثمن.")
            st.markdown("""
            <div style="background-color: #F8FAFC; padding: 15px; border-radius: 5px; border-right: 5px solid #059669;">
            * **السعة القصوى:** 4.5 لتر فقط تكفي لتشغيل الوحدة.<br>
            * **الفائدة المالية:** يقلل تكلفة الحبر المهدر المتبقي في الخراطيم والمضخات بشكل هائل.<br>
            * **المميزات:** يأتي مع جهاز تحكم آلي باللزوجة، خلاط، وحساس لمستوى الحبر.
            </div>
            """, unsafe_allow_html=True)

# ==========================================
# Page 4: Long-Term Opex & Service
# ==========================================
elif page_selection in ["4. Long-Term Opex & Service 🔧", "4. تكاليف الصيانة والاستدامة 🔧"]:
    if lang == "English":
        st.markdown('<div class="executive-title">4. Long-Term Opex & Service Agility</div>', unsafe_allow_html=True)
        st.write("The true cost of a machine is revealed in year 3 and beyond. SOMA adopts an 'Open Source' policy to protect customer OPEX.")
        
        st.markdown("""
        <table class="corp-table">
            <tr><th>Operational Aspect</th><th>SOMA Policy</th><th>W&H Policy (Hidden Weakness)</th></tr>
            <tr><td><strong>Spare Parts Pricing</strong></td><td class="highlight-adv">Standardized & Highly Competitive</td><td class="highlight-dis">Very High Prices (Vendor Monopoly)</td></tr>
            <tr><td><strong>Freedom of Procurement</strong></td><td class="highlight-adv">Open Source (Free to buy locally)</td><td class="highlight-dis">Restricted (Must buy from manufacturer)</td></tr>
            <tr><td><strong>Service Fees</strong></td><td class="highlight-adv">Low service & intervention costs</td><td class="highlight-dis">Premium/High service costs</td></tr>
            <tr><td><strong>Machine Retrofitting</strong></td><td class="highlight-adv">Highly retrofittable & upgradeable</td><td class="highlight-dis">Less flexible / Extremely high price to upgrade</td></tr>
            <tr><td><strong>Technological Innovation</strong></td><td class="highlight-adv">Agile implementation of new tech</td><td class="highlight-dis">Slower to adapt to customized needs</td></tr>
        </table>
        """, unsafe_allow_html=True)
    else:
        st.markdown('<div class="executive-title">4. تكاليف التشغيل والصيانة (الاستدامة طويلة الأمد)</div>', unsafe_allow_html=True)
        st.write("التكلفة الحقيقية للماكينة تظهر بعد السنة الثالثة. تعتمد SOMA سياسة 'المصادر المفتوحة' لحماية ميزانية العميل التشغيلية (OPEX) من الاحتكار.")
        
        st.markdown("""
        <table class="corp-table">
            <tr><th>جانب التشغيل والصيانة</th><th>سياسة شركة SOMA</th><th>سياسة شركة W&H (نقطة الضعف الخفية)</th></tr>
            <tr><td><strong>أسعار قطع الغيار</strong></td><td class="highlight-adv">قياسية وتنافسية جداً</td><td class="highlight-dis">أسعار مبالغ فيها (احتكار الشركة المصنعة)</td></tr>
            <tr><td><strong>حرية التوريد والشراء</strong></td><td class="highlight-adv">سياسة مفتوحة (يمكن شراء القطع من السوق المحلي)</td><td class="highlight-dis">مقيدة (إجبار العميل على الشراء من ألمانيا فقط)</td></tr>
            <tr><td><strong>أجور الخدمة والصيانة</strong></td><td class="highlight-adv">تكاليف زيارات وخدمة منخفضة ومنطقية</td><td class="highlight-dis">تكاليف خدمة (Service Cost) عالية جداً</td></tr>
            <tr><td><strong>ترقية الماكينة مستقبلاً (Retrofit)</strong></td><td class="highlight-adv">مرونة عالية جداً وقابلة للترقية بتكلفة معقولة</td><td class="highlight-dis">مرونة أقل وتكلفة باهظة جداً لأي إضافة مستقبلية</td></tr>
            <tr><td><strong>الابتكار التكنولوجي</strong></td><td class="highlight-adv">معدل أعلى في ابتكار وتطبيق التكنولوجيا الحديثة</td><td class="highlight-dis">بطء في تلبية التعديلات الخاصة للعميل</td></tr>
        </table>
        """, unsafe_allow_html=True)

# ==========================================
# Page 5: TCO Hidden Costs
# ==========================================
elif page_selection in ["5. Hidden Costs (TCO) 📊", "5. التكاليف الخفية (TCO) 📊"]:
    if lang == "English":
        st.markdown('<div class="executive-title">5. Total Cost of Ownership (Hidden Costs Analysis)</div>', unsafe_allow_html=True)
        st.write("Evaluating the initial capital expenditure against the requisite add-ons necessary to achieve identical production readiness.")
        
        data = pd.DataFrame({'Missing Component': ['ITS Cooling', '100% Camera', 'Sleeves & Aniloxes', 'Carbon Mandrels', 'Roll Lift'], 'Estimated Cost (€)': [50000, 71000, 50000, 30000, 15000]})
        chart = alt.Chart(data).mark_bar(color='#DC2626', cornerRadiusEnd=4).encode(
            x=alt.X('Estimated Cost (€):Q', title='Hidden Cost (€)'), y=alt.Y('Missing Component:N', sort='-x', title=''), tooltip=['Missing Component', 'Estimated Cost (€)']
        ).properties(height=300, title="Required Add-ons for W&H Alphaflex")
        st.altair_chart(chart, use_container_width=True)

        st.markdown("""
        <table class="corp-table">
            <tr><th>Critical Equipment / Add-on</th><th>SOMA Optima 2</th><th>W&H Alphaflex</th><th>Estimated Upgrade Cost (€)</th></tr>
            <tr><td><strong>Ink Thermal Stabilization (ITS)</strong></td><td class="highlight-adv">✅ Integrated & Included</td><td class="highlight-dis">❌ Customer Responsibility</td><td><strong>~ € 50,000</strong></td></tr>
            <tr><td><strong>100% Print Inspection Camera</strong></td><td class="highlight-adv">✅ Included (BST iPQ Check)</td><td class="highlight-dis">❌ Optional Add-on</td><td><strong>~ € 71,000</strong></td></tr>
            <tr><td><strong>Printing Sleeves & Aniloxes (8+8)</strong></td><td class="highlight-adv">✅ Included</td><td class="highlight-dis">❌ Customer Responsibility</td><td><strong>~ € 50,000</strong></td></tr>
            <tr><td><strong>Carbon Fiber Mandrels</strong></td><td class="highlight-adv">✅ Standard Inclusion</td><td class="highlight-dis">⚠️ Optional Upgrade</td><td><strong>~ € 30,000</strong></td></tr>
            <tr><td><strong>Payment Terms</strong></td><td class="highlight-adv">✅ Net Wire Transfers</td><td class="highlight-dis">❌ 75% Letter of Credit (L/C)</td><td><strong>Significant Bank Fees</strong></td></tr>
        </table>
        """, unsafe_allow_html=True)
        st.error("📉 **Financial Conclusion:** The Alphaflex base price is deceptive. To elevate it to the operational standard of the Optima 2, Ymtaco would incur over **€ 200,000** in hidden capital expenditures.")
    
    else:
        st.markdown('<div class="executive-title">5. التكلفة الإجمالية للملكية (التكاليف الخفية)</div>', unsafe_allow_html=True)
        st.write("يعرض هذا القسم التكلفة الحقيقية (Hidden Costs) لترقية العرض الاقتصادي المنافس ليصل إلى مستوى الكفاءة القياسية في ماكينة SOMA.")
        
        data = pd.DataFrame({'الإضافة المطلوبة': ['نظام تبريد الحبر (ITS)', 'كاميرا فحص 100%', 'سليفات وأنيلوكس', 'ترقية أعمدة الكاربون', 'رافعة الرولات'], 'التكلفة التقديرية (يورو)': [50000, 71000, 50000, 30000, 15000]})
        chart = alt.Chart(data).mark_bar(color='#DC2626', cornerRadiusEnd=4).encode(
            x=alt.X('التكلفة التقديرية (يورو):Q', title='التكلفة المفقودة (يورو)'), y=alt.Y('الإضافة المطلوبة:N', sort='-x', title=''), tooltip=['الإضافة المطلوبة', 'التكلفة التقديرية (يورو)']
        ).properties(height=300, title="قيمة الإضافات المطلوبة لتجهيز ماكينة W&H")
        st.altair_chart(chart, use_container_width=True)

        st.markdown("""
        <table class="corp-table">
            <tr><th>البند الفني / الإضافة</th><th>SOMA Optima 2 (شامل وجاهز)</th><th>W&H Alphaflex (عرض أساسي)</th><th>التكلفة المخفية التقديرية</th></tr>
            <tr><td><strong>نظام تبريد الحبر (ITS)</strong></td><td class="highlight-adv">✅ مدمج وشامل بالعرض</td><td class="highlight-dis">❌ غير مشمول (مسؤولية العميل)</td><td><strong>~ € 50,000</strong></td></tr>
            <tr><td><strong>كاميرا فحص الجودة 100%</strong></td><td class="highlight-adv">✅ شاملة (BST iPQ Check)</td><td class="highlight-dis">❌ غير مشمولة</td><td><strong>~ € 71,000</strong></td></tr>
            <tr><td><strong>أطقم السليفات والأنيلوكس (8+8)</strong></td><td class="highlight-adv">✅ شاملة للبدء فوراً</td><td class="highlight-dis">❌ غير مشمولة</td><td><strong>~ € 50,000</strong></td></tr>
            <tr><td><strong>أعمدة كاربون فايبر للطباعة</strong></td><td class="highlight-adv">✅ مواصفة قياسية أساسية</td><td class="highlight-dis">⚠️ تتطلب ترقية (حديد قياسياً)</td><td><strong>~ € 30,000</strong></td></tr>
            <tr><td><strong>الشروط المالية والبنكية</strong></td><td class="highlight-adv">✅ حوالات بنكية ميسرة (Wire)</td><td class="highlight-dis">❌ اعتماد مستندي 75% (L/C)</td><td><strong>تجميد سيولة + رسوم بنكية عالية</strong></td></tr>
        </table>
        """, unsafe_allow_html=True)
        st.error("📉 **الخلاصة المالية:** السعر الأساسي لماكينة Alphaflex خادع مالياً. للوصول بها إلى المستوى التشغيلي القياسي لماكينة Optima 2، سيتكبد المصنع أكثر من **200,000 يورو** كإضافات حتمية.")

# ==========================================
# Page 6: Turn-Key Investment
# ==========================================
elif page_selection in ["6. Turn-Key Investment", "6. استثمار المشروع المتكامل"]:
    if lang == "English":
        st.markdown('<div class="executive-title">6. Complete Flexible Packaging Suite (Turn-Key)</div>', unsafe_allow_html=True)
        st.write("SOMA offers a comprehensive, synchronized production line. Procuring all machinery from a single advanced ecosystem ensures seamless integration and qualifies Ymtaco for our highest tier of commercial discounts.")
        st.markdown("""
        <table class="corp-table">
            <tr><th>Equipment Category</th><th>Exact Model Specification</th><th>Valuation (EUR)</th></tr>
            <tr><td><strong>Central Impression Flexo Press</strong></td><td>SOMA OPTIMA2 850-1270-8 EG (500 m/min)</td><td>€ 2,480,000</td></tr>
            <tr><td><strong>Automatic Plate Mounter</strong></td><td>SOMA S-MOUNT A 1300 (with IRIS System)</td><td>€ 220,000</td></tr>
            <tr><td><strong>Solventless Laminator</strong></td><td>SOMA LAMIFLEX E 1320 (400 m/min)</td><td>€ 410,000</td></tr>
            <tr><td><strong>Slitter Rewinder</strong></td><td>SOMA PLUTO III.2 1350 (650 m/min)</td><td>€ 242,740</td></tr>
        </table>
        """, unsafe_allow_html=True)
        st.markdown('<div class="total-investment">Total Turn-Key Project Value: € 3,352,740</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="executive-title">6. قيمة استثمار المشروع المتكامل (Turn-Key)</div>', unsafe_allow_html=True)
        st.write("نحن في SOMA لا نبيع مجرد ماكينة مفردة، بل نبني لك مصنعاً متكاملاً بأعلى درجات التوافق التكنولوجي. شراء الحزمة الكاملة يمنح المصنع خصماً استثنائياً لا يمكن منافسته.")
        st.markdown("""
        <table class="corp-table">
            <tr><th>نوع المعدة / الماكينة</th><th>الموديل والمواصفات الدقيقة</th><th>القيمة (يورو)</th></tr>
            <tr><td><strong>مطبعة فليكسو 8 ألوان (Cl-Press)</strong></td><td>SOMA OPTIMA2 850-1270-8 EG (500 m/min)</td><td>€ 2,480,000</td></tr>
            <tr><td><strong>ماكينة تركيب السليفات الأوتوماتيكية</strong></td><td>SOMA S-MOUNT A 1300 (مزودة بنظام IRIS)</td><td>€ 220,000</td></tr>
            <tr><td><strong>ماكينة اللامنيشن (بدون مذيبات)</strong></td><td>SOMA LAMIFLEX E 1320 (400 m/min)</td><td>€ 410,000</td></tr>
            <tr><td><strong>ماكينة التقطيع وإعادة اللف (سلتر)</strong></td><td>SOMA PLUTO III.2 1350 (650 m/min)</td><td>€ 242,740</td></tr>
        </table>
        """, unsafe_allow_html=True)
        st.markdown('<div class="total-investment">إجمالي الاستثمار للمشروع المتكامل: € 3,352,740</div>', unsafe_allow_html=True)

# ==========================================
# Page 7: Partnership & FAT
# ==========================================
elif page_selection in ["7. Strategic Partnership 🚀", "7. شراكة التحدي والإثبات 🚀"]:
    if lang == "English":
        st.markdown('<div class="executive-title">7. Strategic Partnership & F.A.T. Guarantee</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="data-card-soma">
            <h3 style="color: #0F172A; margin-top:0;">🎓 Comprehensive Training Masterclass</h3>
            <p style="font-size: 1.1rem; color: #0F172A;"><b>In the event of purchasing the complete suite of all 4 machines, you will receive a special, unprecedented training program:</b></p>
            <ul style="line-height: 1.8; font-size: 1.1rem; color: #334155;">
                <li><b>Phase 1:</b> 10 Days of intensive on-site commissioning and operator training at Ymtaco.</li>
                <li><b>Phase 2:</b> 2 additional weeks of advanced on-site training 3 months post-installation.</li>
                <li><b>Phase 3:</b> 1 Full Month of intensive, hands-on training for your lead operators at the SOMA European manufacturing facility.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div style="border: 3px solid #1E3A8A; padding: 30px; border-radius: 8px; background-color: #EFF6FF; margin-top: 30px; text-align: center;">
            <h2 style="color: #1E3A8A; margin-top:0;">The Engineering Proof Challenge (F.A.T.)</h2>
            <p style="font-size: 1.3rem; color: #475569; line-height: 1.6;">
                We do not rely on brochures. SOMA is the only manufacturer that insists on a full <b>Factory Acceptance Test (F.A.T.)</b> prior to machine shipment.<br><br>
                We cordially invite the Ymtaco executive teams to our manufacturing facility in Europe. <b>Bring your most demanding, highly complex HD printing designs.</b> Watch the Optima 2 calibrate, register, and execute the run with near-zero waste in a matter of minutes.<br>
                <span style="color: #1E3A8A; font-weight: bold; font-size: 1.5rem;">Trust what you see, not just a brand name!</span>
            </p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown('<div class="executive-title">7. الشراكة الاستراتيجية وضمان اختبار المصنع (F.A.T)</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="data-card-soma">
            <h3 style="color: #0F172A; margin-top:0;">🎓 باقة التدريب الماستركلاس (غير مسبوقة)</h3>
            <p style="font-size: 1.2rem; color: #0F172A;"><b>في حال شراء الـ 4 ماكينات بالكامل، سوف تحصلون على تدريب خاص وحصري يشمل:</b></p>
            <ul style="line-height: 1.8; font-size: 1.1rem; color: #334155; padding-right: 20px;">
                <li><b>المرحلة الأولى:</b> 10 أيام من التدريب المكثف بموقعكم أثناء التركيب والتشغيل.</li>
                <li><b>المرحلة الثانية:</b> أسبوعين إضافيين من التدريب المتقدم بموقعكم بعد 3 أشهر من التشغيل لضمان الاستقرار.</li>
                <li><b>المرحلة الثالثة:</b> استضافة فريقكم لمدة <b>شهر كامل</b> للتدريب العملي الاحترافي في مصنع SOMA بأوروبا.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div style="border: 3px solid #1E3A8A; padding: 30px; border-radius: 8px; background-color: #EFF6FF; margin-top: 30px; text-align: center;">
            <h2 style="color: #1E3A8A; margin-top:0;">دعوة للتحدي القاطع واختبار الـ (F.A.T)</h2>
            <p style="font-size: 1.3rem; color: #475569; line-height: 1.6;">
                نحن لا نعتمد على الكتيبات. SOMA هي الشركة الوحيدة التي تصر على إجراء <b>اختبار قبول المصنع (F.A.T)</b> بالكامل قبل شحن الماكينة.<br><br>
                نوجه دعوة رسمية لإدارة شركة Ymtaco لزيارة مصانعنا في أوروبا. <b>نتحداكم بإحضار أعقد وأصعب تصاميمكم الطباعية (HD).</b> شاهدوا بأعينكم كيف تقوم ماكينة <b>Optima 2</b> بضبط الريجستر آلياً وطباعة التصميم بصفر هدر وفي دقائق معدودة.<br>
                <span style="color: #1E3A8A; font-weight: bold; font-size: 1.5rem;">استثماركم يستحق أن تختبروه بأنفسكم قبل التوقيع!</span>
            </p>
        </div>
        """, unsafe_allow_html=True)
