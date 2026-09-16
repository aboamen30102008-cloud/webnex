
from flask import Flask, request, redirect
import urllib.parse

app = Flask(__name__)

PHONE = "201034859496"
DISPLAY_PHONE = "01034859496"


def whatsapp_link(message):
    return (
        "https://wa.me/"
        + PHONE
        + "?text="
        + urllib.parse.quote(message)
    )


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        service = request.form.get("service", "").strip()
        budget = request.form.get("budget", "").strip()
        payment = request.form.get("payment", "").strip()
        details = request.form.get("details", "").strip()

        message = (
            "مرحباً Webnex 👋\n\n"
            "أريد طلب خدمة جديدة.\n\n"
            f"الاسم: {name}\n"
            f"الخدمة: {service}\n"
            f"الميزانية: {budget}\n"
            f"طريقة الدفع: {payment}\n\n"
            "تفاصيل الطلب:\n"
            f"{details}"
        )

        return redirect(whatsapp_link(message))

    return """
<!DOCTYPE html>
<html lang="ar" dir="rtl">

<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Webnex | Digital Solutions</title>

<meta name="description"
content="Webnex - تصميم وتطوير المواقع والحلول الرقمية.">

<style>

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
}

body {
    font-family: Arial, Tahoma, sans-serif;
    background: #050810;
    color: #ffffff;
    overflow-x: hidden;
}

a {
    text-decoration: none;
    color: inherit;
}

button,
input,
select,
textarea {
    font-family: inherit;
}

.container {
    width: 90%;
    max-width: 1200px;
    margin: auto;
}

.blue {
    color: #1597ff;
}

section {
    padding: 100px 0;
}

.dark-section {
    background: #070d16;
}


/* NAVBAR */

nav {
    position: fixed;
    top: 0;
    right: 0;
    width: 100%;
    height: 75px;
    padding: 0 5%;

    display: flex;
    align-items: center;
    justify-content: space-between;

    background: rgba(5, 8, 16, 0.94);
    backdrop-filter: blur(15px);

    border-bottom: 1px solid #17263a;
    z-index: 1000;
}

.logo {
    font-size: 30px;
    font-weight: 900;
}

.logo span {
    color: #1597ff;
}

.links {
    display: flex;
    align-items: center;
    gap: 24px;
}

.links a {
    color: #aeb9c8;
    transition: 0.3s;
}

.links a:hover {
    color: #1597ff;
}

.nav-button {
    background: #1597ff;
    color: white !important;
    padding: 11px 18px;
    border-radius: 10px;
}

.menu {
    display: none;
    background: #0c1725;
    color: white;
    border: 1px solid #26384e;
    border-radius: 10px;
    padding: 9px 13px;
    font-size: 21px;
    cursor: pointer;
}


/* HERO */

.hero {
    min-height: 100vh;

    display: flex;
    align-items: center;
    justify-content: center;

    text-align: center;

    padding: 130px 20px 80px;

    background:
        radial-gradient(
            circle at 50% 0%,
            rgba(21,151,255,0.28),
            transparent 45%
        );
}

.hero-content {
    max-width: 900px;
}

.badge {
    display: inline-block;
    padding: 10px 18px;
    margin-bottom: 25px;

    border: 1px solid #1597ff;
    border-radius: 50px;

    color: #62c3ff;
    background: rgba(21,151,255,0.08);

    font-size: 13px;
}

.hero h1 {
    font-size: clamp(45px, 7vw, 80px);
    line-height: 1.1;
    margin-bottom: 25px;
}

.hero p {
    max-width: 760px;
    margin: auto;
    margin-bottom: 35px;

    color: #9daabd;

    font-size: 18px;
    line-height: 1.9;
}

.buttons {
    display: flex;
    justify-content: center;
    gap: 15px;
    flex-wrap: wrap;
}

.btn {
    display: inline-block;

    padding: 15px 28px;

    border-radius: 12px;

    background: #1597ff;
    border: 1px solid #1597ff;

    color: white;

    font-weight: bold;
    cursor: pointer;

    transition: 0.3s;
}

.btn:hover {
    transform: translateY(-4px);
    box-shadow: 0 15px 35px rgba(21,151,255,0.25);
}

.secondary {
    background: #0d1724;
    border-color: #26384e;
}


/* STATS */

.stats {
    display: flex;
    justify-content: center;
    gap: 55px;
    margin-top: 55px;
    flex-wrap: wrap;
}

.stat {
    text-align: center;
}

.stat strong {
    display: block;
    font-size: 25px;
    margin-bottom: 6px;
}

.stat span {
    color: #718096;
    font-size: 13px;
}


/* TITLES */

.section-title {
    text-align: center;
    margin-bottom: 55px;
}

.section-title small {
    display: block;
    color: #1597ff;
    margin-bottom: 12px;
    letter-spacing: 2px;
}

.section-title h2 {
    font-size: 45px;
    margin-bottom: 15px;
}

.section-title p {
    max-width: 650px;
    margin: auto;
    color: #8997a8;
    line-height: 1.8;
}


/* SERVICES */

.cards {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 22px;
}

.card {
    padding: 30px;

    background: #0b1521;

    border: 1px solid #1b2c40;
    border-radius: 20px;

    transition: 0.3s;
}

.card:hover {
    transform: translateY(-8px);
    border-color: #1597ff;
}

.icon {
    width: 60px;
    height: 60px;

    display: flex;
    align-items: center;
    justify-content: center;

    margin-bottom: 20px;

    border-radius: 15px;

    background: rgba(21,151,255,0.1);

    font-size: 30px;
}

.card h3 {
    font-size: 22px;
    margin-bottom: 12px;
}

.card p {
    color: #8997a8;
    line-height: 1.8;
}


/* PROCESS */

.process {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 18px;
}

.process-card {
    padding: 25px;
    text-align: center;

    background: #0b1521;

    border: 1px solid #1b2c40;
    border-radius: 18px;
}

.number {
    width: 50px;
    height: 50px;

    display: flex;
    align-items: center;
    justify-content: center;

    margin: 0 auto 18px;

    border-radius: 50%;
    background: #1597ff;

    font-weight: bold;
}

.process-card h3 {
    margin-bottom: 10px;
}

.process-card p {
    color: #8997a8;
    line-height: 1.7;
}


/* PORTFOLIO */

.portfolio {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 22px;
}

.project {
    min-height: 280px;
    padding: 30px;

    display: flex;
    flex-direction: column;
    justify-content: flex-end;

    overflow: hidden;

    border-radius: 20px;
    border: 1px solid #1b2c40;

    background:
        radial-gradient(
            circle at top right,
            rgba(21,151,255,0.28),
            transparent 45%
        ),
        #0b1521;

    transition: 0.3s;
}

.project:hover {
    transform: translateY(-7px);
    border-color: #1597ff;
}

.project-icon {
    font-size: 55px;
    margin-bottom: 20px;
}

.project small {
    color: #62c3ff;
    margin-bottom: 8px;
}

.project h3 {
    font-size: 27px;
    margin-bottom: 8px;
}

.project p {
    color: #aab5c3;
    margin-bottom: 18px;
}

.project-link {
    color: #1597ff;
    font-weight: bold;
}


/* PAYMENT */

.payment-box {
    max-width: 900px;
    margin: auto;

    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
}

.payment-card {
    padding: 30px;

    background: #0b1521;

    border: 1px solid #1b2c40;
    border-radius: 20px;

    transition: 0.3s;
}

.payment-card:hover {
    border-color: #1597ff;
    transform: translateY(-5px);
}

.payment-icon {
    font-size: 42px;
    margin-bottom: 15px;
}

.payment-card h3 {
    margin-bottom: 12px;
}

.payment-card p {
    color: #8997a8;
    line-height: 1.8;
}

.payment-number {
    margin-top: 18px;

    padding: 15px;

    background: #07101b;

    border-radius: 12px;

    color: #62c3ff;

    font-size: 19px;
    font-weight: bold;

    direction: ltr;
    text-align: center;
}


/* PRICING */

.pricing {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 22px;
}

.price-card {
    padding: 32px;

    background: #0b1521;

    border: 1px solid #1b2c40;
    border-radius: 20px;

    transition: 0.3s;
}

.price-card:hover {
    transform: translateY(-6px);
}

.price-card.featured {
    border-color: #1597ff;
    box-shadow: 0 20px 50px rgba(21,151,255,0.12);
}

.price-card h3 {
    font-size: 23px;
    margin-bottom: 15px;
}

.price {
    font-size: 30px;
    font-weight: bold;
    margin-bottom: 25px;
}

.price span {
    font-size: 14px;
    color: #78869a;
}

.price-card ul {
    list-style: none;
    margin-bottom: 25px;
}

.price-card li {
    padding: 10px 0;
    color: #9aa7b7;
    border-bottom: 1px solid #172434;
}

.price-card li::before {
    content: "✓";
    color: #20c979;
    margin-left: 8px;
}

.full {
    width: 100%;
    text-align: center;
}


/* WHY */

.why {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 22px;
}

.why-card {
    padding: 28px;

    background: #0b1521;

    border: 1px solid #1b2c40;
    border-radius: 18px;
}

.why-card h3 {
    margin-bottom: 12px;
}

.why-card p {
    color: #8997a8;
    line-height: 1.8;
}


/* CONTACT */

.contact-area {
    display: grid;
    grid-template-columns: 1fr 1.2fr;
    gap: 25px;
}

.contact-box {
    padding: 30px;

    background: #0b1521;

    border: 1px solid #1b2c40;
    border-radius: 20px;
}

.contact-box h3 {
    font-size: 28px;
    margin-bottom: 15px;
}

.contact-box > p {
    color: #8997a8;
    line-height: 1.8;
    margin-bottom: 25px;
}

.contact-item {
    padding: 16px;
    margin-top: 12px;

    background: #0e1a28;

    border-radius: 12px;

    color: #b7c2d0;
}

.contact-item strong {
    color: white;
}


/* FORM */

.form-group {
    margin-bottom: 16px;
}

.form-group label {
    display: block;
    margin-bottom: 8px;
    color: #c8d2df;
    font-size: 14px;
}

.form-control {
    width: 100%;

    padding: 14px 16px;

    background: #07101b;

    color: white;

    border: 1px solid #213247;

    border-radius: 11px;

    outline: none;

    transition: 0.3s;
}

.form-control:focus {
    border-color: #1597ff;

    box-shadow:
        0 0 0 3px rgba(21,151,255,0.08);
}

textarea.form-control {
    min-height: 130px;
    resize: vertical;
}

select.form-control {
    cursor: pointer;
}

.submit {
    width: 100%;
    border: none;
}


/* WHATSAPP */

.whatsapp {
    position: fixed;

    left: 20px;
    bottom: 20px;

    width: 58px;
    height: 58px;

    display: flex;

    align-items: center;
    justify-content: center;

    background: #20c979;

    border-radius: 50%;

    font-size: 28px;

    box-shadow: 0 10px 30px rgba(0,0,0,0.35);

    z-index: 999;

    transition: 0.3s;
}

.whatsapp:hover {
    transform: scale(1.08);
}


/* FOOTER */

footer {
    padding: 35px 0;

    text-align: center;

    background: #03060b;

    border-top: 1px solid #17263a;

    color: #6f7e91;
}

footer strong {
    color: white;
}


/* MOBILE */

@media (max-width: 900px) {

    .cards,
    .pricing,
    .why {
        grid-template-columns: 1fr 1fr;
    }

    .process {
        grid-template-columns: 1fr 1fr;
    }

    .contact-area {
        grid-template-columns: 1fr;
    }

    .payment-box {
        grid-template-columns: 1fr;
    }
}


@media (max-width: 700px) {

    nav {
        height: 68px;
    }

    .logo {
        font-size: 25px;
    }

    .menu {
        display: block;
    }

    .links {
        position: absolute;

        top: 68px;
        right: 5%;
        left: 5%;

        display: none;

        flex-direction: column;

        padding: 20px;

        background: #0b1521;

        border: 1px solid #1b2c40;

        border-radius: 15px;
    }

    .links.active {
        display: flex;
    }

    .links a {
        width: 100%;
        padding: 10px;
        text-align: center;
    }

    .hero {
        padding-top: 120px;
    }

    .hero h1 {
        font-size: 45px;
    }

    .hero p {
        font-size: 16px;
    }

    section {
        padding: 75px 0;
    }

    .section-title h2 {
        font-size: 34px;
    }

    .cards,
    .pricing,
    .why,
    .portfolio,
    .process {
        grid-template-columns: 1fr;
    }

    .stats {
        gap: 30px;
    }

    .project {
        min-height: 240px;
    }
}

</style>
</head>


<body>


<nav>

    <a href="#home" class="logo">
        Web<span>nex</span>
    </a>

    <button class="menu" onclick="toggleMenu()">
        ☰
    </button>

    <div class="links" id="navLinks">

        <a href="#home">الرئيسية</a>
        <a href="#services">الخدمات</a>
        <a href="#portfolio">أعمالنا</a>
        <a href="#pricing">الأسعار</a>
        <a href="#payment">الدفع</a>

        <a href="#contact" class="nav-button">
            اطلب مشروعك
        </a>

    </div>

</nav>


<section class="hero" id="home">

    <div class="hero-content">

        <div class="badge">
            حلول رقمية احترافية 🚀
        </div>

        <h1>
            نبني أفكارك<br>
            <span class="blue">بشكل رقمي</span>
        </h1>

        <p>
            Webnex تساعدك على تحويل فكرتك إلى موقع إلكتروني
            احترافي وسريع ومتجاوب مع جميع الأجهزة.
        </p>

        <div class="buttons">

            <a href="#contact" class="btn">
                ابدأ مشروعك الآن
            </a>

            <a href="#services" class="btn secondary">
                اكتشف خدماتنا
            </a>

        </div>


        <div class="stats">

            <div class="stat">
                <strong>⚡</strong>
                <span>سرعة وأداء</span>
            </div>

            <div class="stat">
                <strong>📱</strong>
                <span>متوافق مع الموبايل</span>
            </div>

            <div class="stat">
                <strong>💻</strong>
                <span>تصميم احترافي</span>
            </div>

        </div>

    </div>

</section>


<section id="services">

    <div class="container">

        <div class="section-title">

            <small>OUR SERVICES</small>

            <h2>خدماتنا</h2>

            <p>
                حلول رقمية مصممة لمساعدة مشروعك على الظهور
                بشكل احترافي على الإنترنت.
            </p>

        </div>


        <div class="cards">

            <div class="card">
                <div class="icon">🌐</div>
                <h3>تصميم المواقع</h3>
                <p>
                    تصميم مواقع حديثة وسريعة ومتجاوبة مع
                    الموبايل والكمبيوتر.
                </p>
            </div>

            <div class="card">
                <div class="icon">🛒</div>
                <h3>المتاجر الإلكترونية</h3>
                <p>
                    إنشاء واجهات احترافية لعرض المنتجات
                    والخدمات بطريقة سهلة.
                </p>
            </div>

            <div class="card">
                <div class="icon">📱</div>
                <h3>صفحات الهبوط</h3>
                <p>
                    صفحات Landing Pages مخصصة للإعلانات
                    وتسويق المنتجات والخدمات.
                </p>
            </div>

            <div class="card">
                <div class="icon">⚙️</div>
                <h3>تطوير المواقع</h3>
                <p>
                    تطوير وتحسين المواقع وإضافة الخصائص
                    التي يحتاجها مشروعك.
                </p>
            </div>

            <div class="card">
                <div class="icon">🎨</div>
                <h3>UI / UX</h3>
                <p>
                    واجهات مستخدم عصرية وسهلة الاستخدام
                    ومناسبة للهوية الخاصة بمشروعك.
                </p>
            </div>

            <div class="card">
                <div class="icon">🔧</div>
                <h3>صيانة وتحديث</h3>
                <p>
                    تحديث محتوى الموقع وإصلاح المشاكل
                    وإضافة التطويرات الجديدة.
                </p>
            </div>

        </div>

    </div>

</section>


<section class="dark-section">

    <div class="container">

        <div class="section-title">

            <small>HOW IT WORKS</small>

            <h2>بنشتغل إزاي؟</h2>

        </div>


        <div class="process">

            <div class="process-card">
                <div class="number">1</div>
                <h3>فكرتك</h3>
                <p>ابعتلنا فكرتك والهدف من المشروع.</p>
            </div>

            <div class="process-card">
                <div class="number">2</div>
                <h3>التخطيط</h3>
                <p>بنحدد الشكل والخصائص المطلوبة.</p>
            </div>

            <div class="process-card">
                <div class="number">3</div>
                <h3>التنفيذ</h3>
                <p>بنبدأ تصميم وتطوير المشروع.</p>
            </div>

            <div class="process-card">
                <div class="number">4</div>
                <h3>التسليم</h3>
                <p>تستلم مشروعك بعد الانتهاء منه.</p>
            </div>

        </div>

    </div>

</section>


<section id="portfolio">

    <div class="container">

        <div class="section-title">

            <small>PORTFOLIO</small>

            <h2>مشاريع يمكننا تنفيذها</h2>

            <p>
                أمثلة على أنواع المواقع التي يمكن تصميمها
                وتطويرها حسب احتياجات العميل.
            </p>

        </div>


        <div class="portfolio">

            <div class="project">
                <div class="project-icon">🛍️</div>
                <small>E-COMMERCE</small>
                <h3>متجر إلكتروني</h3>
                <p>
                    واجهة متجر حديثة لعرض المنتجات والخدمات.
                </p>
                <span class="project-link">
                    اطلب مشروع مشابه →
                </span>
            </div>

            <div class="project">
                <div class="project-icon">🏢</div>
                <small>BUSINESS</small>
                <h3>موقع شركة</h3>
                <p>
                    موقع احترافي لتعريف العملاء بالشركة والخدمات.
                </p>
                <span class="project-link">
                    اطلب مشروع مشابه →
                </span>
            </div>

            <div class="project">
                <div class="project-icon">📣</div>
                <small>LANDING PAGE</small>
                <h3>صفحة إعلانية</h3>
                <p>
                    صفحة مخصصة للإعلانات وجذب العملاء.
                </p>
                <span class="project-link">
                    اطلب مشروع مشابه →
                </span>
            </div>

            <div class="project">
                <div class="project-icon">🚀</div>
                <small>STARTUP</small>
                <h3>مشروع ناشئ</h3>
                <p>
                    موقع عصري لعرض فكرة مشروعك وخدماته.
                </p>
                <span class="project-link">
                    ابدأ فكرتك →
                </span>
            </div>

        </div>

    </div>

</section>


<section class="dark-section" id="pricing">

    <div class="container">

        <div class="section-title">

            <small>PACKAGES</small>

            <h2>باقات مبدئية</h2>

            <p>
                الأسعار مبدئية، والتكلفة النهائية بتتحدد
                حسب تفاصيل المشروع.
            </p>

        </div>


        <div class="pricing">

            <div class="price-card">

                <h3>Starter</h3>

                <div class="price">
                    حسب المشروع
                    <span>EGP</span>
                </div>

                <ul>
                    <li>صفحة أو موقع بسيط</li>
                    <li>تصميم متجاوب</li>
                    <li>زر واتساب</li>
                    <li>تعديل أساسي</li>
                </ul>

                <a href="#contact" class="btn full">
                    اطلب الآن
                </a>

            </div>


            <div class="price-card featured">

                <h3>Professional</h3>

                <div class="price">
                    حسب المشروع
                    <span>EGP</span>
                </div>

                <ul>
                    <li>موقع احترافي</li>
                    <li>عدة أقسام</li>
                    <li>تصميم مخصص</li>
                    <li>خصائص إضافية</li>
                </ul>

                <a href="#contact" class="btn full">
                    اطلب الآن
                </a>

            </div>


            <div class="price-card">

                <h3>Custom</h3>

                <div class="price">
                    مخصص
                    <span>EGP</span>
                </div>

                <ul>
                    <li>مشروع حسب فكرتك</li>
                    <li>خصائص خاصة</li>
                    <li>تطوير متقدم</li>
                    <li>اتفاق حسب المتطلبات</li>
                </ul>

                <a href="#contact" class="btn full">
                    تحدث معنا
                </a>

            </div>

        </div>

    </div>

</section>


<section id="payment">

    <div class="container">

        <div class="section-title">

            <small>PAYMENT METHODS</small>

            <h2>طرق الدفع</h2>

            <p>
                يمكنك اختيار طريقة الدفع المناسبة لك
                والتواصل معنا لتأكيد الطلب.
            </p>

        </div>


        <div class="payment-box">

            <div class="payment-card">

                <div class="payment-icon">📱</div>

                <h3>Vodafone Cash</h3>

                <p>
                    يمكن الدفع عن طريق Vodafone Cash
                    على رقم التواصل الخاص بنا.
                </p>

                <div class="payment-number">
                    01034859496
                </div>

            </div>


            <div class="payment-card">

                <div class="payment-icon">💳</div>

                <h3>InstaPay</h3>

                <p>
                    يمكن استخدام InstaPay للتحويل،
                    ثم التواصل معنا لتأكيد عملية الدفع.
                </p>

                <div class="payment-number">
                    01034859496
                </div>

            </div>

        </div>

    </div>

</section>


<section class="dark-section">

    <div class="container">

        <div class="section-title">

            <small>WHY WEBNEX</small>

            <h2>ليه Webnex؟</h2>

        </div>


        <div class="why">

            <div class="why-card">
                <h3>⚡ سرعة</h3>
                <p>
                    نهتم بأداء الموقع وسرعة تحميل الصفحات
                    على الأجهزة المختلفة.
                </p>
            </div>

            <div class="why-card">
                <h3>📱 Responsive</h3>
                <p>
                    الموقع بيظهر بشكل مناسب على الموبايل
                    والتابلت والكمبيوتر.
                </p>
            </div>

            <div class="why-card">
                <h3>💡 أفكار مخصصة</h3>
                <p>
                    بنقدر نطوّر التصميم والخصائص حسب
                    فكرة ومتطلبات كل مشروع.
                </p>
            </div>

        </div>

    </div>

</section>


<section id="contact">

    <div class="container">

        <div class="section-title">

            <small>CONTACT US</small>

            <h2>ابدأ مشروعك</h2>

            <p>
                املأ البيانات التالية، وبعد الضغط على إرسال
                هتنتقل مباشرة إلى واتساب لإكمال الطلب.
            </p>

        </div>


        <div class="contact-area">


            <div class="contact-box">

                <h3>تواصل معنا</h3>

                <p>
                    لو عندك فكرة موقع أو مشروع رقمي،
                    ابعت التفاصيل وهنبدأ من هناك.
                </p>

                <div class="contact-item">
                    📱 <strong>واتساب:</strong>
                    01034859496
                </div>

                <div class="contact-item">
                    💳 <strong>InstaPay:</strong>
                    01034859496
                </div>

                <div class="contact-item">
                    💰 <strong>Vodafone Cash:</strong>
                    01034859496
                </div>

            </div>


            <div class="contact-box">

                <form method="POST">

                    <div class="form-group">

                        <label>الاسم</label>

                        <input
                            class="form-control"
                            type="text"
                            name="name"
                            placeholder="اكتب اسمك"
                            required
                        >

                    </div>


                    <div class="form-group">

                        <label>الخدمة المطلوبة</label>

                        <select
                            class="form-control"
                            name="service"
                            required
                        >

                            <option value="">
                                اختر الخدمة
                            </option>

                            <option>تصميم موقع</option>
                            <option>متجر إلكتروني</option>
                            <option>Landing Page</option>
                            <option>تطوير موقع</option>
                            <option>UI / UX</option>
                            <option>صيانة وتحديث</option>
                            <option>خدمة أخرى</option>

                        </select>

                    </div>


                    <div class="form-group">

                        <label>الميزانية المتوقعة</label>

                        <select
                            class="form-control"
                            name="budget"
                        >

                            <option value="">
                                اختر الميزانية
                            </option>

                            <option>أقل من 5,000 جنيه</option>
                            <option>5,000 - 10,000 جنيه</option>
                            <option>10,000 - 20,000 جنيه</option>
                            <option>أكثر من 20,000 جنيه</option>
                            <option>غير محددة</option>

                        </select>

                    </div>


                    <div class="form-group">

                        <label>طريقة الدفع</label>

                        <select
                            class="form-control"
                            name="payment"
                            required
                        >

                            <option value="">
                                اختر طريقة الدفع
                            </option>

                            <option>Vodafone Cash</option>
                            <option>InstaPay</option>
                            <option>سيتم الاتفاق لاحقاً</option>

                        </select>

                    </div>


                    <div class="form-group">

                        <label>تفاصيل المشروع</label>

                        <textarea
                            class="form-control"
                            name="details"
                            placeholder="اكتب فكرتك أو التفاصيل المطلوبة..."
                            required
                        ></textarea>

                    </div>


                    <button
                        type="submit"
                        class="btn submit"
                    >
                        إرسال الطلب عبر واتساب 🚀
                    </button>

                </form>

            </div>

        </div>

    </div>

</section>


<footer>

    <div class="container">

        © 2026
        <strong>Webnex</strong>
        — Digital Solutions

    </div>

</footer>


<a
    class="whatsapp"
    href="https://wa.me/201034859496"
    target="_blank"
    aria-label="WhatsApp"
>
    💬
</a>


<script>

function toggleMenu() {

    const menu = document.getElementById("navLinks");

    menu.classList.toggle("active");
}


document.querySelectorAll(".links a").forEach(function(link) {

    link.addEventListener("click", function() {

        document
            .getElementById("navLinks")
            .classList.remove("active");

    });

});

</script>


</body>
</html>
"""


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
