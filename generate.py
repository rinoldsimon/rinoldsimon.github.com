#!/usr/bin/env python3
from pathlib import Path

SITE = {
    "email": "crisrinold@gmail.com",
    "phone_display": "+91 72995 44052",
    "phone_href": "+917299544052",
    "github": "https://github.com/rinoldsimon",
    "linkedin": "https://www.linkedin.com/in/rinoldsimon/",
    "x": "https://x.com/crisrinold",
    "stackoverflow": "https://stackoverflow.com/users/2480797/rinold-simon",
    "wordpress": "https://learnrubyblog.wordpress.com/",
    "elitecoders": "https://portfolio.elitecoders.co/",
    "elitecoders_site": "https://elitecoders.co/",
    "socialrails": "https://socialrails.onrender.com",
    "resume_pdf": "/files/Rinold-Simon-Resume.pdf",
    "description": (
        "Senior Full-Stack Engineer in Chennai. Ten years with Ruby on Rails and React, "
        "remote teams, and lately Python, FastAPI, and AI-assisted development."
    ),
}

EXPERIENCE = [
    {
        "company": "EliteCoders",
        "location": "Remote",
        "dates": "Apr 2022 – Present",
        "url": "https://portfolio.elitecoders.co/",
        "note": "Building EliteCoders — a product studio. Client work and our own platforms.",
        "roles": [
            {
                "title": "Senior Software Engineer",
                "subtitle": "Consultant for GUILDHOUSE Group",
                "dates": "Dec 2022 – Present",
                "bullets": [
                    "Built AE Connect, a student information system used by 300+ K-12 schools and about 15,000 students.",
                    "React portals on Rails, with PostgreSQL, Sidekiq, and AWS carrying the heavy reporting.",
                ],
            },
            {
                "title": "Senior Software Engineer",
                "subtitle": "Core Platform",
                "dates": "Apr 2022 – Nov 2022",
                "bullets": [
                    "Part of the founding team that launched elitecoders.co — a US platform connecting developers with recruiters.",
                    "Shipped the core Rails app and the client work on the EliteCoders portfolio.",
                ],
            },
        ],
    },
    {
        "company": "Maxiom Technology",
        "location": "Remote",
        "roles": [
            {
                "title": "Senior Full Stack Developer",
                "subtitle": "Consultant for FiscalNote",
                "dates": "Jun 2021 – Mar 2022",
                "bullets": [
                    "Migrated FiscalNote — including auth and identity — from microservices into one Rails app.",
                    "Cleaned up the data model so the new system loaded faster than what it replaced.",
                ],
            },
            {
                "title": "Full Stack Developer",
                "subtitle": "Internal · Hyperlogs",
                "dates": "Jan 2021 – May 2021",
                "bullets": [
                    "Built time-tracking and timesheets for Hyperlogs, an internal Ember.js app.",
                    "Flutter prototype so people could log hours on iOS and Android.",
                ],
            },
            {
                "title": "Full Stack Developer",
                "subtitle": "E-Commerce Automation",
                "dates": "Jun 2019 – Dec 2020",
                "bullets": [
                    "Electron app on Node that ran Amazon seller accounts — thousands of orders a day, replacing a 10-person manual process.",
                ],
            },
        ],
    },
    {
        "company": "Digiryte Ltd",
        "location": "Chennai, India",
        "roles": [
            {
                "title": "Lead Frontend Developer",
                "subtitle": "",
                "dates": "Jun 2016 – May 2019",
                "bullets": [
                    "Led frontend for a HIPAA-compliant healthcare app for UK and Germany clients.",
                    "Ran a team of six — standups, mentoring, shipping.",
                ],
            },
        ],
    },
]

PROJECTS = [
    {
        "title": "EliteCoders",
        "context": "Core Platform",
        "period": "2022",
        "url": "https://portfolio.elitecoders.co/",
        "tags": ["Rails", "React"],
        "summary": "Part of the founding team that launched elitecoders.co — a US hiring platform connecting developers with recruiters. More of the studio’s work lives on the portfolio.",
    },
    {
        "title": "AE Connect",
        "context": "GUILDHOUSE Group · EliteCoders",
        "period": "2022 – Present",
        "tags": ["React", "Rails", "PostgreSQL"],
        "summary": "Student information system for 300+ K-12 schools and about 15,000 students — onboarding, grading, scheduling. React portals, Rails APIs, Sidekiq for the heavy reports.",
    },
    {
        "title": "FiscalNote, rebuilt",
        "context": "Maxiom Technology",
        "period": "2021 – 2022",
        "tags": ["Rails", "Architecture"],
        "summary": "Folded a sprawling microservices setup — including auth — into one Ruby on Rails application. Fewer moving parts, and it held up better than what it replaced.",
    },
    {
        "title": "Amazon seller automation",
        "context": "Maxiom Technology",
        "period": "2019 – 2020",
        "tags": ["Electron", "Node.js"],
        "summary": "An Electron app that ran Amazon seller accounts on its own — thousands of orders a day, replacing a 10-person manual process.",
    },
]

SKILLS = [
    ("Frontend", ["React", "JavaScript", "TypeScript", "Tailwind CSS", "HTML/CSS"]),
    ("Backend", ["Ruby on Rails", "Node.js", "REST APIs"]),
    ("Data", ["PostgreSQL", "MySQL", "Redis"]),
    ("Cloud & ops", ["AWS", "Docker", "Git", "Sidekiq", "Sentry"]),
    ("Automation", ["Electron", "Flutter", "Puppeteer", "Zapier"]),
    ("AI", ["Cursor", "Claude", "ChatGPT", "Gemini"]),
    ("Learning", ["Python", "FastAPI"]),
    ("Also", ["Ember.js", "Elixir"]),
]


def icons():
    return """
<svg xmlns="http://www.w3.org/2000/svg" style="display:none">
  <symbol id="icon-github" viewBox="0 0 24 24" fill="currentColor"><path d="M12 .5C5.73.5.5 5.73.5 12.02c0 5.1 3.29 9.42 7.86 10.95.58.1.79-.25.79-.56 0-.28-.01-1.02-.02-2-3.2.7-3.88-1.54-3.88-1.54-.53-1.33-1.28-1.69-1.28-1.69-1.05-.72.08-.7.08-.7 1.16.08 1.77 1.2 1.77 1.2 1.03 1.77 2.7 1.26 3.36.96.1-.75.4-1.26.73-1.55-2.55-.29-5.23-1.28-5.23-5.7 0-1.26.45-2.29 1.19-3.1-.12-.29-.52-1.46.11-3.05 0 0 .97-.31 3.18 1.18a11.1 11.1 0 0 1 2.9-.39c.98 0 1.97.13 2.9.39 2.2-1.49 3.17-1.18 3.17-1.18.63 1.59.23 2.76.12 3.05.74.81 1.18 1.84 1.18 3.1 0 4.43-2.69 5.4-5.25 5.69.41.36.78 1.07.78 2.16 0 1.56-.01 2.81-.01 3.2 0 .31.21.67.8.56A10.52 10.52 0 0 0 23.5 12C23.5 5.73 18.27.5 12 .5Z"/></symbol>
  <symbol id="icon-linkedin" viewBox="0 0 24 24" fill="currentColor"><path d="M20.45 20.45h-3.55v-5.57c0-1.33-.03-3.04-1.85-3.04-1.85 0-2.14 1.45-2.14 2.94v5.67H9.35V9h3.41v1.56h.05c.47-.9 1.63-1.85 3.36-1.85 3.59 0 4.26 2.36 4.26 5.44v6.3ZM5.34 7.43a2.06 2.06 0 1 1 0-4.12 2.06 2.06 0 0 1 0 4.12ZM7.12 20.45H3.56V9h3.56v11.45ZM22.23 0H1.77C.79 0 0 .77 0 1.73v20.54C0 23.23.79 24 1.77 24h20.46c.98 0 1.77-.77 1.77-1.73V1.73C24 .77 23.21 0 22.23 0Z"/></symbol>
  <symbol id="icon-x" viewBox="0 0 24 24" fill="currentColor"><path d="M18.24 2H21.5l-7.54 8.62L22.5 22h-6.59l-5.16-6.74L4.9 22H1.62l8.06-9.21L1.5 2h6.76l4.66 6.17L18.24 2Zm-1.16 18h1.81L7 3.89H5.06L17.08 20Z"/></symbol>
  <symbol id="icon-stackoverflow" viewBox="0 0 24 24" fill="currentColor"><path d="M17.24 19.22v-5.39h1.8V21H3.01v-7.17h1.8v5.39h12.43ZM7.22 17.43h8.99v-1.8H7.22v1.8Zm.22-3.27 8.8 1.84.37-1.76-8.8-1.84-.37 1.76Zm1.15-3.36 8.15 3.8.76-1.63-8.15-3.81-.76 1.64Zm2.24-3.2 6.91 5.76 1.16-1.39-6.91-5.76-1.16 1.39Zm4.4-3.4-1.48 1.1 5.36 7.2 1.48-1.1-5.36-7.2Z"/></symbol>
  <symbol id="icon-wordpress" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.49 2 2 6.49 2 12s4.49 10 10 10 10-4.49 10-10S17.51 2 12 2zm-1.41 16.53-.04-.01 2.38-6.51c.22.02.55.06.87.06.35 0 .46-.04.72-.04.16 0 .4.01.6.04l-2.4 6.57c-.56-.03-1.16-.09-1.73-.11zm-1.65-.3C6.9 17.39 5.53 15.38 5.53 13c0-.8.17-1.54.47-2.23l3.8 10.43a6.1 6.1 0 0 1-1.86-2.97zm7.33-.85c.39-.8.62-1.7.62-2.65 0-1.03-.38-1.97-.62-2.31-.38-.55-.74-.55-1.03-.55-.64 0-.95.12-1.46.12-.35 0-.77-.05-1.08-.09L12 6.56c.41-.02.82-.06.82-.06.37-.04.32-.58-.05-.56 0 0-1.1.09-1.81.09-.67 0-1.8-.09-1.8-.09-.37-.02-.41.55-.05.57 0 0 .39.04.8.06l1.17 3.22-1.65 4.95-2.73-8.17c.41-.02.8-.06.8-.06.37-.04.32-.58-.04-.56 0 0-1.1.09-1.81.09-.13 0-.28 0-.43-.01A8.47 8.47 0 0 1 12 3.53c1.78 0 3.4.68 4.62 1.79-.03 0-.06 0-.1 0-.64 0-1.1.56-1.1 1.17 0 .54.31 1 .64 1.54.25.44.54.99.54 1.8 0 .55-.15 1.24-.35 2.17l-.15.65z"/></symbol>
  <symbol id="icon-mail" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m4 7 8 6 8-6"/></symbol>
  <symbol id="icon-phone" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M6.5 3.8h2.4l1.3 3.3-1.7 1.1a12.4 12.4 0 0 0 5.3 5.3l1.1-1.7 3.3 1.3v2.4c0 .9-.7 1.7-1.6 1.8-2.4.3-7-1-10.3-4.3C3.7 10.2 2.4 5.6 2.7 3.2c.1-.9.9-1.6 1.8-1.6Z"/></symbol>
  <symbol id="icon-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="4"/><path d="M12 3v2M12 19v2M4.2 4.2l1.4 1.4M18.4 18.4l1.4 1.4M3 12h2M19 12h2M4.2 19.8l1.4-1.4M18.4 5.6l1.4-1.4"/></symbol>
  <symbol id="icon-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M16.5 13.2A7 7 0 0 1 10.8 5 7.2 7.2 0 1 0 19 14.8a7 7 0 0 1-2.5-1.6Z"/></symbol>
</svg>
"""


def social(compact=False):
    klass = "social-row social-row--compact" if compact else "social-row"
    links = [
        (SITE["github"], "GitHub", "icon-github"),
        (SITE["linkedin"], "LinkedIn", "icon-linkedin"),
        (SITE["x"], "X", "icon-x"),
        (SITE["stackoverflow"], "Stack Overflow", "icon-stackoverflow"),
    ]
    items = "".join(
        f'<a href="{href}" target="_blank" rel="noopener noreferrer" aria-label="{label}"><svg><use href="#{icon}"></use></svg></a>'
        for href, label, icon in links
    )
    return f'<div class="{klass}">{items}</div>'


def nav(active=""):
    resume_current = ' aria-current="page"' if active == "resume" else ""
    return f"""
<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap header-inner">
    <a class="wordmark" href="/">Rinold Simon</a>
    <nav id="site-nav" class="site-nav">
      <a href="/#about">About</a>
      <a href="/#work">Work</a>
      <a href="/#experience">Experience</a>
      <a href="/resume/"{resume_current}>Resume</a>
      <a href="{SITE["wordpress"]}" target="_blank" rel="noopener noreferrer">Articles</a>
      <a href="/#contact">Contact</a>
    </nav>
    <div class="header-tools">
      <button class="theme-toggle" type="button" aria-label="Switch to light theme">
        <svg class="icon-sun" aria-hidden="true"><use href="#icon-sun"></use></svg>
        <svg class="icon-moon" aria-hidden="true"><use href="#icon-moon"></use></svg>
      </button>
      <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav">
        <span class="sr-only">Menu</span>
        <span></span><span></span>
      </button>
    </div>
  </div>
</header>
"""


def experience_list():
    blocks = []
    for job in EXPERIENCE:
        roles = []
        for role in job["roles"]:
            subtitle = f"<span>{role['subtitle']}</span>" if role["subtitle"] else ""
            bullets = "".join(f"<li>{b}</li>" for b in role["bullets"])
            roles.append(
                f"""
        <div class="role">
          <div class="role-meta">
            <h4>{role["title"]}{subtitle}</h4>
            <p class="dates">{role["dates"]}</p>
          </div>
          <ul>{bullets}</ul>
        </div>"""
            )
        company = job["company"]
        if job.get("url"):
            company = f'<a href="{job["url"]}" target="_blank" rel="noopener noreferrer">{company}</a>'
        place = job["location"]
        if job.get("dates"):
            place = f'{job["location"]} · {job["dates"]}'
        note = f'<p class="job-note">{job["note"]}</p>' if job.get("note") else ""
        blocks.append(
            f"""
    <article class="job">
      <div class="job-head">
        <h3>{company}</h3>
        <p class="job-place">{place}</p>
      </div>
      {note}
      {"".join(roles)}
    </article>"""
        )
    return f'<div class="timeline">{"".join(blocks)}</div>'


def project_grid():
    cards = []
    for project in PROJECTS:
        tags = "".join(f"<li>{t}</li>" for t in project["tags"])
        title = project["title"]
        if project.get("url"):
            title = f'<a href="{project["url"]}" target="_blank" rel="noopener noreferrer">{title}</a>'
        cards.append(
            f"""
    <article class="project-card">
      <p class="project-meta">{project["context"]} · {project["period"]}</p>
      <h3>{title}</h3>
      <p>{project["summary"]}</p>
      <ul class="tags">{tags}</ul>
    </article>"""
        )
    return f'<div class="project-grid">{"".join(cards)}</div>'


def skill_groups():
    groups = []
    for name, items in SKILLS:
        tags = "".join(f"<li>{i}</li>" for i in items)
        groups.append(f"<div><h3>{name}</h3><ul class=\"tags\">{tags}</ul></div>")
    return f'<div class="skill-groups">{"".join(groups)}</div>'


THEME_BOOTSTRAP = """
    <script>
      (function () {
        var theme = "dark";
        try {
          var forced = new URLSearchParams(location.search).get("theme");
          var saved = localStorage.getItem("theme");
          if (forced === "light" || forced === "dark") theme = forced;
          else if (saved === "light" || saved === "dark") theme = saved;
          else if (window.matchMedia("(prefers-color-scheme: light)").matches) theme = "light";
        } catch (e) {}
        document.documentElement.setAttribute("data-theme", theme);
      })();
    </script>
"""


def layout(title, description, body, extra_title=False, path="/"):
    full_title = f"{title} · Rinold Simon" if extra_title else "Rinold Simon"
    canonical = f"https://rinoldsimon.github.io{path}"
    return f"""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{full_title}</title>
    <meta name="description" content="{description}">
    <link rel="canonical" href="{canonical}">
    <link rel="icon" type="image/png" sizes="32x32" href="/images/favicon-32.png">
    <link rel="icon" type="image/x-icon" href="/favicon.ico">
    <link rel="apple-touch-icon" href="/images/apple-touch-icon.png">
    <meta property="og:type" content="website">
    <meta property="og:title" content="{full_title}">
    <meta property="og:description" content="{description}">
    <meta property="og:url" content="{canonical}">
    <meta property="og:image" content="https://rinoldsimon.github.io/images/rinold.jpg">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{full_title}">
    <meta name="twitter:description" content="{description}">
    <meta name="twitter:image" content="https://rinoldsimon.github.io/images/rinold.jpg">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=Outfit:wght@380;450;560&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/stylesheets/site.css">
    {THEME_BOOTSTRAP}
  </head>
  <body>
    {icons()}
    {nav("resume" if title == "Resume" else "")}
    <main id="main">
      {body}
    </main>
    <footer class="site-footer">
      <div class="wrap footer-inner">
        <p>© 2026 Rinold Simon · Chennai</p>
        {social(compact=True)}
      </div>
    </footer>
    <script src="/javascripts/site.js"></script>
  </body>
</html>
"""


def home():
    body = f"""
<section class="hero">
  <div class="wrap hero-grid">
    <div class="hero-copy">
      <p class="eyebrow">Chennai · Full-stack · Remote-friendly</p>
      <h1>Rinold Simon</h1>
      <p class="lede">Senior engineer with a decade of Rails and React. I’m building <a href="{SITE["elitecoders"]}" target="_blank" rel="noopener noreferrer">EliteCoders</a>, and poking at Python, FastAPI, and AI-assisted workflows for whatever comes next.</p>
      <div class="hero-actions">
        <a class="btn btn-primary" href="mailto:{SITE["email"]}">Say hello</a>
        <a class="btn btn-ghost" href="/resume/">Resume</a>
        <a class="btn btn-ghost" href="{SITE["wordpress"]}" target="_blank" rel="noopener noreferrer">Articles</a>
      </div>
      {social()}
    </div>
    <figure class="hero-photo">
      <img src="/images/rinold.jpg" alt="Rinold Simon, smiling outdoors at the beach" width="720" height="900">
    </figure>
  </div>
</section>

<section id="about" class="section">
  <div class="wrap split">
    <div>
      <p class="eyebrow">About</p>
      <h2>Still building. Still curious.</h2>
    </div>
    <div class="prose">
      <p>I’m a Senior Full-Stack Engineer based in Chennai, with ten years of shipping web apps and distributed systems. Rails and React are home base. These days I’m also leaning into Python and FastAPI — using tools like Cursor, Claude, and Gemini to write cleaner code and move through hard bugs faster.</p>
      <p>Most of my recent work has been with remote US teams: student systems, hiring products, platform migrations. I’m also building <a href="{SITE["elitecoders"]}" target="_blank" rel="noopener noreferrer">EliteCoders</a>, a product studio. When I’m away from the keyboard I’m at the gym, and a proud dad to two kids.</p>
      <p>I write about Rails on my <a href="{SITE["wordpress"]}" target="_blank" rel="noopener noreferrer">tech blog</a>, and I hang around <a href="{SITE["stackoverflow"]}" target="_blank" rel="noopener noreferrer">Stack Overflow</a> — about 3,000 reputation, mostly Rails and the old Ember.js days.</p>
    </div>
  </div>
  <div class="wrap facts">
    <div><strong>10</strong><span>years shipping</span></div>
    <div><strong>3k+</strong><span>Stack Overflow reputation</span></div>
    <div><strong>M.Sc</strong><span>IT, College of Engineering Guindy</span></div>
    <div><strong>Remote</strong><span>US clients, Indian timezone</span></div>
  </div>
</section>

<section id="work" class="section">
  <div class="wrap">
    <p class="eyebrow">Selected work</p>
    <h2>A few things worth talking about</h2>
    <p class="section-lead">Not a dump of every repo. Just the work that still feels interesting — a studio we’re building, school systems, a platform rewrite, a bot that ran Amazon accounts on its own.</p>
    {project_grid()}
    <p class="aside">More studio work on the <a href="{SITE["elitecoders"]}" target="_blank" rel="noopener noreferrer">EliteCoders portfolio</a>. There’s also <a href="{SITE["socialrails"]}" target="_blank" rel="noopener noreferrer">SocialRails</a> — feeds, follows, and chat in Rails.</p>
  </div>
</section>

<section id="experience" class="section">
  <div class="wrap">
    <p class="eyebrow">Experience</p>
    <h2>Where the years went</h2>
    {experience_list()}
    <p class="aside"><a href="/resume/">Full resume</a> · <a href="{SITE["resume_pdf"]}">Download PDF</a></p>
  </div>
</section>

<section id="skills" class="section">
  <div class="wrap">
    <p class="eyebrow">Stack</p>
    <h2>What I reach for</h2>
    {skill_groups()}
  </div>
</section>

<section id="contact" class="section contact">
  <div class="wrap contact-card">
    <p class="eyebrow">Contact</p>
    <h2>If you want to talk, I’m easy to find.</h2>
    <p>Collaborate, talk shop, or just say hello. Email is best. Phone works too.</p>
    <div class="contact-lines">
      <a href="mailto:{SITE["email"]}"><svg><use href="#icon-mail"></use></svg>{SITE["email"]}</a>
      <a href="tel:{SITE["phone_href"]}"><svg><use href="#icon-phone"></use></svg>{SITE["phone_display"]}</a>
    </div>
    {social()}
  </div>
</section>
"""
    return layout("Home", SITE["description"], body, path="/")


def resume():
    body = f"""
<article class="page">
  <div class="wrap page-head">
    <p class="eyebrow">Resume</p>
    <h1>Rinold Simon</h1>
    <ul class="resume-meta">
      <li>Senior Full-Stack Engineer</li>
      <li>Chennai</li>
      <li><a href="mailto:{SITE["email"]}">{SITE["email"]}</a></li>
      <li><a href="tel:{SITE["phone_href"]}">{SITE["phone_display"]}</a></li>
    </ul>
    <div class="hero-actions">
      <a class="btn btn-primary" href="{SITE["resume_pdf"]}">Download PDF</a>
      <a class="btn btn-ghost" href="mailto:{SITE["email"]}">Email</a>
      <a class="btn btn-ghost" href="{SITE["linkedin"]}" target="_blank" rel="noopener noreferrer">LinkedIn</a>
    </div>
  </div>
  <div class="wrap resume-block">
    <h2>Summary</h2>
    <p>Senior Full-Stack Engineer with 10 years of building reliable web applications. Strong in Ruby on Rails and React. Used to remote international teams and the full path from database design to frontend deploy. Lately I’m expanding into Python and FastAPI, and I use Cursor, Claude, ChatGPT, and Gemini to write tighter code and debug faster.</p>
  </div>
  <div class="wrap resume-block">
    <h2>Experience</h2>
    {experience_list()}
  </div>
  <div class="wrap resume-block">
    <h2>Skills</h2>
    {skill_groups()}
  </div>
  <div class="wrap resume-split">
    <div class="resume-block">
      <h2>Education</h2>
      <p class="edu-title">Master of Science (M.Sc) in Information Technology</p>
      <p>College of Engineering Guindy, Anna University · Chennai · 2016</p>
    </div>
    <div class="resume-block">
      <h2>Languages</h2>
      <p>English (professional) · Tamil (native)</p>
    </div>
  </div>
  <div class="wrap resume-block">
    <h2>Elsewhere</h2>
    <ul class="plain-list">
      <li><a href="{SITE["github"]}">GitHub</a> — projects and samples</li>
      <li><a href="{SITE["elitecoders"]}">EliteCoders</a> — studio portfolio</li>
      <li><a href="{SITE["stackoverflow"]}">Stack Overflow</a> — 3,000+ reputation</li>
      <li><a href="{SITE["wordpress"]}">Tech blog</a> — Rails writing</li>
      <li><a href="{SITE["socialrails"]}">SocialRails</a> — open-source social app in Rails</li>
    </ul>
  </div>
</article>
"""
    return layout("Resume", "Resume for Rinold Simon, Senior Full-Stack Engineer in Chennai.", body, extra_title=True, path="/resume/")


def projects():
    body = f"""
<article class="page">
  <div class="wrap page-head">
    <p class="eyebrow">Selected work</p>
    <h1>A few things worth talking about</h1>
    <p class="lede">Brief notes on products and systems I’ve actually shipped — not a GitHub inventory.</p>
  </div>
  <div class="wrap">
    {project_grid()}
    <p class="aside">More on <a href="{SITE["github"]}" target="_blank" rel="noopener noreferrer">GitHub</a>, including <a href="{SITE["socialrails"]}" target="_blank" rel="noopener noreferrer">SocialRails</a>.</p>
  </div>
</article>
"""
    return layout("Work", "Selected work by Rinold Simon.", body, extra_title=True, path="/projects/")


def not_found():
    body = """
<article class="page">
  <div class="wrap page-head">
    <p class="eyebrow">404</p>
    <h1>That page isn’t here.</h1>
    <p class="lede">Try the <a href="/">home page</a> or the <a href="/resume/">resume</a>.</p>
  </div>
</article>
"""
    return layout("Not found", SITE["description"], body, extra_title=True, path="/404.html")


def write(path, html):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html.strip() + "\n", encoding="utf-8")
    print("wrote", path)


if __name__ == "__main__":
    root = Path(__file__).resolve().parent
    write(root / "index.html", home())
    write(root / "resume" / "index.html", resume())
    write(root / "projects" / "index.html", projects())
    write(root / "404.html", not_found())
    write(root / ".nojekyll", "")
