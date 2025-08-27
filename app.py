from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'

PHONE = "(847) 322-5748"
COMPANY = "Spring Rain"

REVIEWS = [
    {"author": "Renee · Lake Bluff", "text": "Scheduling is simple and they arrive on time."},
    {"author": "Mous · Winnetka", "text": "Professional, courteous, attentive team."},
    {"author": "Michael · Highland Park", "text": "First‑rate service—very efficient."},
    {"author": "Gail · Chicago", "text": "Reliable and professional—highly recommend."},
]

FAQS = [
    {
        "q": "Why certify the RPZ (backflow device) every year?",
        "a": (
            "Annual certification ensures the device is functioning properly "
            " and prevents contamination of the water supply."
        ),
    },
    {
        "q": "When should I winterize my sprinkler system?",
        "a": (
            "It's best to winterize your sprinkler system before the first hard freeze. "
            "This usually means late October to early November in most areas."
        ),
    },
]

SERVICE_AREAS = [
    "Arlington Heights", "Barrington", "Chicago", "Deerfield", "Downers Grove", "Elmhurst", "Evanston",
    "Glencoe", "Glen Ellyn", "Grayslake", "Gurnee", "Hinsdale", "Highland Park", "Kenilworth",
    "Lake Bluff", "Lake Forest", "Libertyville", "Lincolnshire", "Northbrook", "Palatine", "Skokie",
    "Vernon Hills", "Wilmette", "Winnetka"
]

SERVICES = [
    {
        "slug": "installations",
        "title": "New Installations",
        "desc": "Water‑efficient systems using modern nozzles, emitters, and smart controllers.",
        "img": "service1.jpg",
    },
    {
        "slug": "startup",
        "title": "System Startup",
        "desc": "Spring activation and alignment so all zones are ready to water.",
        "img": "service2.jpg",
    },
    {
        "slug": "rpz",
        "title": "RPZ Certification",
        "desc": "Annual testing to stay compliant with local rules and protect your water.",
        "img": "service3.jpg",
    },
    {
        "slug": "midseason",
        "title": "Mid‑Season Check",
        "desc": "Adjust coverage once plants are in full growth to keep water use efficient.",
        "img": "service1.jpg",
    },
    {
        "slug": "expansion",
        "title": "System Expansion",
        "desc": "Add zones or extend coverage as your landscape evolves.",
        "img": "service2.jpg",
    },
    {
        "slug": "repairs",
        "title": "Repairs",
        "desc": "Fast diagnosis and fixes when something isn’t working right.",
        "img": "service3.jpg",
    },
    {
        "slug": "winterization",
        "title": "Shutdown / Winterization",
        "desc": "Seasonal blow‑outs and shut‑off to prevent freeze damage.",
        "img": "service1.jpg",
    },
]

PORTFOLIO = [
    {"title": "Residential · Large", "img": "gallery1.jpg"},
    {"title": "Residential · City", "img": "gallery2.jpg"},
    {"title": "Residential · Small", "img": "placeholder.jpg"},
    {"title": "Working City Garden", "img": "placeholder.jpg"},
    {"title": "Elawa Farm", "img": "placeholder.jpg"},
    {"title": "Commercial", "img": "placeholder.jpg"},
    {"title": "Condo", "img": "placeholder.jpg"},
]

@app.context_processor
def inject_globals():
    return dict(company=COMPANY, phone=PHONE, year=datetime.now().year)


@app.route("/")
def index():
    return render_template("index.html", services=SERVICES[:4], reviews=REVIEWS[:3])


@app.route("/services")
def services():
    return render_template("services.html", services=SERVICES)


@app.route("/resources")
def resources():
    return render_template("resources.html")


@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html", items=PORTFOLIO)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/service-areas")
def service_areas():
    return render_template("service_areas.html", areas=SERVICE_AREAS)


@app.route("/reviews")
def reviews():
    return render_template("reviews.html", reviews=REVIEWS)


@app.route("/faqs")
def faqs():
    return render_template("faqs.html", faqs=FAQS)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        subject = request.form.get("subject")
        message = request.form.get("message")
        # In a real app, send an email or store the inquiry.
        flash("Thanks! We received your message and will follow up.")
        return redirect(url_for("contact"))
    return render_template("contact.html")  


if __name__ == "__main__":
    app.run(debug=True)
