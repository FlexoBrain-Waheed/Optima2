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
    </style>
""", unsafe_allow_html=True)

# 3. Sidebar Navigation Dictionary
nav_options = {
    "English": ["1. Executive Summary", "2. Technical Benchmarking", "3. Hidden Costs (TCO) 📊", "4. Turn-Key Investment", "5. Strategic Partnership 🚀"],
    "العربية": ["1. الملخص التنفيذي", "2. المقارنة الفنية والهندسية", "3. التكاليف الخفية (TCO) 📊", "4. استثمار المشروع المتكامل", "5. شراكة التحدي والإثبات 🚀"]
}

page_selection = st.sidebar.radio("Navigation / الفهرس:" if lang == "English" else "فهرس التقرير:", nav_options[lang])

st.sidebar.markdown("---")
if lang == "English":
    st.sidebar.markdown("**Prepared For:**\nYmtaco for Trading and Investment Ltd.\n\n**Prepared By:**\nWaheed Alkarraein\nFlexo Consultation Services\nNexFlexo")
else:
    st.sidebar.markdown("**تم الإعداد لصالح:**\nإدارة شركة Ymtaco للتجارة والاستثمار\n\n**إعداد التقرير:**\nوحيد وليد مالك\nFlexo Consultation Services\nNexFlexo")

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
                <p><strong>Maturity:</strong> 2nd Generation, highly stable platform engineered to eliminate structural vibrations.</p>
                <p><strong>Operational Focus:</strong> The absolute "Champion of Short Runs", featuring rapid changeovers and absolute reliance on AI to eliminate material waste.</p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class="data-card-wh">
                <h3 style="color: #DC2626; margin-top: 0;">⚠️ W&H Alphaflex</h3>
                <p><strong>Classification:</strong> Economy / Entry-Level Class - Stripped down to fit low budgets.</p>
                <p><strong>Maturity:</strong> Launched mid-2024. Represents an unproven structural framework in long-term, high-stress environments.</p>
                <p><strong>Operational Focus:</strong> Lacks essential smart automation, resulting in longer setup times and reliance on expensive, rare operator expertise.</p>
            </div>
            """, unsafe_allow_html=True)
        st.info("💡 **The Strategic Question:** Does it make sense to pay over €2 Million for a stripped-down economy model when you can own the fully equipped flagship technology for the same budget?")
    else:
        st.markdown('<div class="executive-title">1. الملخص التنفيذي: التقييم الاستراتيجي للاستثمار</div>', unsafe_allow_html=True)
        st.write("يوضح هذا التقرير التحليل الفني والمالي الشامل لقرار الاستثمار القادم في خطوط التغليف المرن. تعتمد المقارنة الجوهرية على وضع ماكينة **SOMA OPTIMA2 850-1270-8 EG** (الفئة الرائدة) في مواجهة ماكينة **W&H Alphaflex** (الفئة الاقتصادية).")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class="data-card-soma">
                <h3 style="color: #059669; margin-top: 0;">🏆 SOMA OPTIMA 2</h3>
                <p><strong>التصنيف السوقي:</strong> قمة الهرم التكنولوجي (Flagship Class) - كاملة المواصفات.</p>
                <p><strong>النضج والموثوقية:</strong> منصة ناضجة ومجربة بقوة (الجيل الثاني)، مبنية لتلاشي أي اهتزازات ميكانيكية.</p>
                <p><strong>التوجه التشغيلي:</strong> مصممة خصيصاً لتكون "بطلة الطلبيات القصيرة والمتوسطة"، بفضل سرعة التجهيز الفائقة، والاعتماد المطلق على الذكاء الصناعي لتقليل هدر الخامات.</p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class="data-card-wh">
                <h3 style="color: #DC2626; margin-top: 0;">⚠️ W&H Alphaflex</h3>
                <p><strong>التصنيف السوقي:</strong> الفئة الاقتصادية (Entry-Level) - مجردة لخفض التكلفة.</p>
                <p><strong>النضج والموثوقية:</strong> حديثة الولادة (منتصف 2024)، هيكلها الاقتصادي غير مجرب لسنوات طويلة تحت ضغط التشغيل القاسي.</p>
                <p><strong>التوجه التشغيلي:</strong> ماكينة أساسية تم تجريدها من تكنولوجيا الأتمتة العالية، مما يتطلب وقتاً أطول للتجهيز وعمالة فنية نادرة ومكلفة لضبط الجودة.</p>
            </div>
            """, unsafe_allow_html=True)
        st.info("💡 **السؤال الاستراتيجي:** هل من المنطقي دفع ميزانية ضخمة تتجاوز 2 مليون يورو لشراء (الفئة السياحية/الاقتصادية) المجردة من الإضافات، بينما بنفس الميزانية يمكنك امتلاك (الفئة الملكية) وقمة التكنولوجيا؟")

# ==========================================
# Page 2: Technical Benchmarking
# ==========================================
elif page_selection in ["2. Technical Benchmarking", "2. المقارنة الفنية والهندسية"]:
    if lang == "English":
        st.markdown('<div class="executive-title">2. Engineering & Technical Benchmarking</div>', unsafe_allow_html=True)
        st.write("A direct comparison of the structural and technological components critical for long-term print stability and waste reduction.")
        st.markdown("""
        <table class="corp-table">
            <tr><th>Engineering Specification</th><th>SOMA Optima 2 (Standard Config)</th><th>W&H Alphaflex (Base Config)</th><th>Operational Impact</th></tr>
            <tr><td><strong>Printing Cylinder Mandrels</strong></td><td class="highlight-adv">Carbon Composite (Anti-Bounce)</td><td class="highlight-dis">Standard Steel</td><td>Carbon mandrels effectively absorb vibrations, ensuring precise registration (HD Print) at max speeds.</td></tr>
            <tr><td><strong>Print Repeat Length</strong></td><td class="highlight-adv">360 mm – 850 mm</td><td class="highlight-dis">370 mm – 800 mm</td><td>Broader repeat range allows for maximum job flexibility.</td></tr>
            <tr><td><strong>Impression & Register Setting</strong></td><td class="highlight-adv">IRIS & Falcon II (Fully Automated)</td><td class="highlight-dis">EASY SET (Semi-Automated)</td><td>IRIS utilizes plate topography for zero-waste setup, significantly reducing substrate and ink loss.</td></tr>
            <tr><td><strong>Tension Control Isolation</strong></td><td class="highlight-adv">Dedicated Out-Feed Unit</td><td class="highlight-dis">Standard Web Path</td><td>Isolates printing tension from winding tension, critical for PE/thin films.</td></tr>
            <tr><td><strong>Operator Ergonomics (Shafts)</strong></td><td class="highlight-adv">Lightweight Aluminum (19 kg)</td><td class="highlight-dis">Heavy Mechanical Shafts</td><td>Drastically reduces physical fatigue, expediting manual roll changeovers safely.</td></tr>
        </table>
        """, unsafe_allow_html=True)
    else:
        st.markdown('<div class="executive-title">2. المقارنة الفنية والهندسية المباشرة</div>', unsafe_allow_html=True)
        st.write("مقارنة صارمة للت التفوق الميكانيكي والبرمجي الذي يضمن استقرار الطباعة (HD) ويقضي على الهدر اليومي.")
        st.markdown("""
        <table class="corp-table">
            <tr><th>الميزة الهندسية</th><th>SOMA Optima 2 (المواصفات القياسية)</th><th>W&H Alphaflex (العرض الأساسي)</th><th>التأثير التشغيلي المباشر</th></tr>
            <tr><td><strong>أعمدة أسطوانات الطباعة</strong></td><td class="highlight-adv">كاربون فايبر (Carbon Fiber)</td><td class="highlight-dis">حديد (Steel Mandrels)</td><td>الكاربون فايبر يمتص الاهتزازات تماماً ويضمن جودة طباعة (HD) على السرعات العالية بدون اهتزاز.</td></tr>
            <tr><td><strong>نطاق تكرار الطباعة</strong></td><td class="highlight-adv">360 ملم – 850 ملم</td><td class="highlight-dis">370 ملم – 800 ملم</td><td>مرونة قصوى لقبول شريحة أوسع بكثير من طلبات العملاء وأحجام التغليف.</td></tr>
            <tr><td><strong>أنظمة ضبط الجودة والريجستر</strong></td><td class="highlight-adv">IRIS & Falcon II (أوتوماتيكي بالكامل)</td><td class="highlight-dis">EASY SET S (شبه أوتوماتيكي)</td><td>نظام IRIS الذكي يضبط الطباعة مسبقاً بصفر هدر تقريباً (يوفر مئات الآلاف من الريالات سنوياً).</td></tr>
            <tr><td><strong>التعامل مع الأفلام المطاطية</strong></td><td class="highlight-adv">وحدة سحب مخصصة (Out-feed Unit)</td><td class="highlight-dis">مسار ورق تقليدي</td><td>فصل الشد أثناء الطباعة عن شد اللف يضمن دقة تطابق الألوان المطلقة على خامات PE.</td></tr>
            <tr><td><strong>راحة المشغل (أعمدة اللف)</strong></td><td class="highlight-adv">أعمدة ألمنيوم خفيفة (19 كجم فقط)</td><td class="highlight-dis">أعمدة ميكانيكية ثقيلة جداً</td><td>تسريع جذري لعملية تبديل الرولات يدوياً، مع حماية العمال من الإصابات والإرهاق.</td></tr>
        </table>
        """, unsafe_allow_html=True)

# ==========================================
# Page 3: TCO Hidden Costs
# ==========================================
elif page_selection in ["3. Hidden Costs (TCO) 📊", "3. التكاليف الخفية (TCO) 📊"]:
    if lang == "English":
        st.markdown('<div class="executive-title">3. Total Cost of Ownership (Hidden Costs Analysis)</div>', unsafe_allow_html=True)
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
        st.markdown('<div class="executive-title">3. التكلفة الإجمالية للملكية (التكاليف الخفية)</div>', unsafe_allow_html=True)
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
# Page 4: Turn-Key Investment
# ==========================================
elif page_selection in ["4. Turn-Key Investment", "4. استثمار المشروع المتكامل"]:
    if lang == "English":
        st.markdown('<div class="executive-title">4. Complete Flexible Packaging Suite (Turn-Key)</div>', unsafe_allow_html=True)
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
        st.markdown('<div class="executive-title">4. قيمة استثمار المشروع المتكامل (Turn-Key)</div>', unsafe_allow_html=True)
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
# Page 5: Partnership
# ==========================================
elif page_selection in ["5. Strategic Partnership 🚀", "5. شراكة التحدي والإثبات 🚀"]:
    if lang == "English":
        st.markdown('<div class="executive-title">5. Strategic Partnership & Service Guarantee</div>', unsafe_allow_html=True)
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
            <h2 style="color: #1E3A8A; margin-top:0;">The Engineering Proof Challenge</h2>
            <p style="font-size: 1.3rem; color: #475569; line-height: 1.6;">
                We cordially invite the Ymtaco executive teams to our manufacturing facility in Europe. <b>Bring your most demanding, highly complex HD printing designs.</b><br><br>
                Witness the Optima 2 calibrate, register, and execute the run with near-zero waste in a matter of minutes. Verify the engineering integrity before committing your capital.<br>
                <span style="color: #1E3A8A; font-weight: bold; font-size: 1.5rem;">Trust what you see, not just a brand name!</span>
            </p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown('<div class="executive-title">5. الشراكة الاستراتيجية وتحدي الإثبات الميداني</div>', unsafe_allow_html=True)
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
            <h2 style="color: #1E3A8A; margin-top:0;">دعوة للتحدي الميداني القاطع</h2>
            <p style="font-size: 1.3rem; color: #475569; line-height: 1.6;">
                نوجه دعوة رسمية لإدارة شركة Ymtaco لزيارة مصانعنا في أوروبا. <b>نتحداكم بإحضار أعقد وأصعب تصاميمكم الطباعية (HD).</b><br><br>
                شاهدوا بأعينكم كيف تقوم ماكينة <b>Optima 2</b> بضبط الريجستر آلياً وطباعة التصميم بصفر هدر وفي دقائق معدودة.<br>
                <span style="color: #1E3A8A; font-weight: bold; font-size: 1.5rem;">استثماركم يستحق أن تختبروه بأنفسكم قبل التوقيع!</span>
            </p>
        </div>
        """, unsafe_allow_html=True)
