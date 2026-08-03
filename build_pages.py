# Writes the nine static pages. Shared chrome lives here so the header and
# footer can never drift apart between pages.
import os

OUT = "/home/claude/site"

NAV_MAIN = [
    ("index.html",   "Home"),
    ("about.html",   "About"),
    ("__RESEARCH__", "Research"),
    ("gallery.html", "Gallery"),
    ("contact.html", "Contact"),
]

# pages that live under the Research dropdown
NAV_SUB = [
    ("research.html",     "Research overview"),
    ("projects.html",     "Projects"),
    ("publications.html", "Publications"),
    ("experience.html",   "Experience"),
    ("conferences.html",  "Conferences"),
]
SUB_FILES = [f for f, _ in NAV_SUB]

ARROW = '<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 12h15m0 0-5-5m5 5-5 5"/></svg>'
EXT = '<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M14 4h6v6M20 4l-9 9M18 14v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V7a1 1 0 0 1 1-1h5"/></svg>'
DOWNLOAD = '<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3v12m0 0 4-4m-4 4-4-4M4 19h16"/></svg>'
MAIL = '<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>'


def head(title, desc, current):
    def link(href, label):
        cls = ' class="is-current" aria-current="page"' if href == current else ""
        return '<a href="%s"%s>%s</a>' % (href, cls, label)

    sub_items = "\n".join(
        '            <li>%s</li>' % link(f, lbl) for f, lbl in NAV_SUB)

    parent_cls = ' class="is-current"' if current in SUB_FILES else ""
    parent_aria = ' aria-current="page"' if current == "research.html" else ""

    group = """<li class="has-sub">
          <a href="research.html"%s%s>Research</a>
          <button class="sub-toggle" type="button" aria-expanded="false" aria-label="Show research pages">
            <svg viewBox="0 0 24 24" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg>
          </button>
          <ul class="subnav">
%s
          </ul>
        </li>""" % (parent_cls, parent_aria, sub_items)

    links = "\n".join(
        "        " + (group if href == "__RESEARCH__" else "<li>%s</li>" % link(href, label))
        for href, label in NAV_MAIN)

    return """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s</title>
<meta name="description" content="%(desc)s">
<meta name="author" content="Shubha Dixit">
<meta property="og:type" content="website">
<meta property="og:title" content="%(title)s">
<meta property="og:description" content="%(desc)s">
<meta property="og:image" content="assets/img/og-cover.jpg">
<link rel="icon" href="assets/img/favicon.png" type="image/png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;0,6..72,500;1,6..72,300&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
</head>

<body>
<a class="skip-link" href="#main">Skip to content</a>

<header class="site-header" id="siteHeader">
  <div class="shell nav-shell">

    <a class="brand" href="index.html">
      <span class="brand-mark">
        <img src="assets/img/logo.png" alt="">
      </span>
      <span class="brand-text">
        <strong>SHUBHA DIXIT</strong>
        <em>Environmental Microbiologist</em>
        <em>Researcher | Biotechnologist</em>
      </span>
    </a>

    <nav class="nav" id="primaryNav" aria-label="Main">
      <ul>
%(links)s
      </ul>
    </nav>

    <a class="btn btn-outline btn-cv" href="assets/cv/Shubha_Dixit_CV.pdf" download>
      Download CV
      %(dl)s
    </a>

    <button class="nav-toggle" id="navToggle" aria-label="Open menu" aria-expanded="false" aria-controls="primaryNav">
      <span></span><span></span><span></span>
    </button>

  </div>
</header>

<main id="main">
""" % {"title": title, "desc": desc, "links": links, "dl": DOWNLOAD}


def page_head(eyebrow, title, lead, stats=""):
    return """
<section class="page-head">
  <div class="shell">
    <p class="eyebrow">%s</p>
    <h1 class="page-title">%s</h1>
    <p class="page-lead">%s</p>
    %s
  </div>
</section>
""" % (eyebrow, title, lead, stats)


CTA = """
<section class="cta">
  <div class="shell">
    <h2>Working on bioremediation, plant&ndash;microbe systems or water quality?</h2>
    <p>I am always glad to talk with research groups, collaborators and students looking for a way into environmental microbiology.</p>
    <div class="cta-actions">
      <a class="btn btn-solid" href="contact.html">Get in touch %s</a>
      <a class="btn btn-ghost" href="assets/cv/Shubha_Dixit_CV.pdf" download>%s Download CV</a>
    </div>
  </div>
</section>
""" % (ARROW, DOWNLOAD)


FOOT = """
</main>

<footer class="site-footer">
  <div class="shell footer-grid">
    <div>
      <p class="footer-name">Shubha Dixit</p>
      <p class="footer-role">Environmental Microbiologist &middot; Researcher &middot; Biotechnologist</p>
    </div>
    <ul class="footer-links">
      <li><a href="about.html">About</a></li>
      <li><a href="research.html">Research</a></li>
      <li><a href="publications.html">Publications</a></li>
      <li><a href="contact.html">Contact</a></li>
      <li><a href="https://scholar.google.com/citations?user=-epYhrEAAAAJ&amp;hl=en" target="_blank" rel="noopener">Google Scholar</a></li>
      <li><a href="https://orcid.org/0009-0008-8177-6797" target="_blank" rel="noopener">ORCID</a></li>
      <li><a href="https://www.researchgate.net/profile/Shubha-Dixit-2" target="_blank" rel="noopener">ResearchGate</a></li>
      <li><a href="https://www.linkedin.com/in/shubha-dixit-377602171" target="_blank" rel="noopener">LinkedIn</a></li>
      <li><a href="mailto:shubha.dixit.9@gmail.com">Email</a></li>
    </ul>
    <p class="footer-copy">&copy; <span id="year">2026</span> Shubha Dixit. All rights reserved.</p>
  </div>
</footer>

<script src="assets/js/main.js"></script>
</body>
</html>
"""


def write(name, title, desc, body, cta=True):
    html = head(title, desc, name) + body + (CTA if cta else "") + FOOT
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(html)
    print(name)


# ══════════════════════════════════════════════════════════ HOME
HOME = """
<section class="hero" id="home">
  <div class="hero-bg" aria-hidden="true"></div>
  <div class="hero-veil" aria-hidden="true"></div>

  <div class="shell hero-shell">

    <div class="hero-copy reveal">
      <p class="eyebrow">Environmental Microbiology <span>&bull;</span> Biotechnology <span>&bull;</span> Bioremediation</p>

      <h1 class="hero-title">
        Harnessing <em>Microbial Life</em> for<br>
        Cleaner Environments and<br>
        Resilient Agriculture
      </h1>

      <p class="hero-lead">
        I am Shubha Dixit, a PhD researcher exploring the potential of microorganisms
        and fungi to address environmental pollution, arsenic contamination and
        agricultural challenges. My work integrates classical microbiology with
        molecular, genomic and multi-omics approaches to build sustainable
        solutions for a healthier planet.
      </p>

      <div class="hero-actions">
        <a class="btn btn-solid" href="research.html">Explore my research __ARROW__</a>
        <a class="btn btn-ghost" href="publications.html">
          <svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 5h7v14H4zm9 0h7v14h-7z"/></svg>
          View publications
        </a>
      </div>

      <ul class="hero-links">
        <li><a href="https://scholar.google.com/citations?user=-epYhrEAAAAJ&amp;hl=en" target="_blank" rel="noopener">
          <svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3 2 9l10 6 10-6-10-6Zm-6 9v5c0 1.7 2.7 3 6 3s6-1.3 6-3v-5"/></svg>
          Google Scholar</a></li>
        <li><a href="https://orcid.org/0009-0008-8177-6797" target="_blank" rel="noopener">
          <svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M9 9v7m0-10v.01M13 9h2a3.5 3.5 0 0 1 0 7h-2z"/></svg>
          ORCID</a></li>
        <li><a href="https://www.researchgate.net/profile/Shubha-Dixit-2" target="_blank" rel="noopener">
          <svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M7 17V7h3a3 3 0 0 1 0 6H7m4 0 4 4M17 5h.01M17 9h.01"/></svg>
          ResearchGate</a></li>
        <li><a href="https://www.linkedin.com/in/shubha-dixit-377602171" target="_blank" rel="noopener">
          <svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M7 10v7m0-10v.01M11 17v-4a2 2 0 0 1 4 0v4"/></svg>
          LinkedIn</a></li>
        <li><a href="mailto:shubha.dixit.9@gmail.com">__MAIL__ Email</a></li>
      </ul>
    </div>

    <div class="hero-figure reveal">
      <span class="hero-arc" aria-hidden="true"></span>
      <img class="hero-image" src="assets/img/hero-image.png" alt="Shubha Dixit, with imagery of fungal hyphae, plant roots and water">
    </div>

  </div>
</section>

<section class="focus" aria-label="Areas of focus">
  <div class="shell focus-grid">

    <article class="focus-card reveal">
      <span class="focus-icon">
        <svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="8"/><path d="M9 10h.01M15 10h.01M9 15c1.5 1.2 4.5 1.2 6 0"/></svg>
      </span>
      <h3>Environmental Microbiology</h3>
      <p>Microbial ecology, diversity analysis and environmental monitoring for sustainable solutions.</p>
      <svg class="focus-art" viewBox="0 0 120 100" aria-hidden="true" focusable="false">
        <g fill="none" stroke="#2E7D46" stroke-width="1.6" stroke-linecap="round">
          <ellipse cx="38" cy="32" rx="16" ry="10" transform="rotate(-18 38 32)" fill="#DCEEDA"/>
          <path d="M23 38c-6 3-9 8-10 14"/>
          <ellipse cx="78" cy="24" rx="12" ry="8" transform="rotate(12 78 24)" fill="#EFF7EC"/>
          <path d="M90 27c5 2 8 6 9 11"/>
          <circle cx="60" cy="62" r="14" fill="#DCEEDA"/>
          <circle cx="56" cy="58" r="2.4" fill="#2E7D46" stroke="none"/>
          <circle cx="65" cy="64" r="2" fill="#2E7D46" stroke="none"/>
          <circle cx="58" cy="69" r="1.6" fill="#2E7D46" stroke="none"/>
          <ellipse cx="98" cy="62" rx="10" ry="7" transform="rotate(-25 98 62)" fill="#EFF7EC"/>
          <path d="M106 55c4-2 6-5 7-9"/>
        </g>
      </svg>
    </article>

    <article class="focus-card reveal">
      <span class="focus-icon">
        <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 21V11m0 0C12 7 9 5 5 5c0 4 3 6 7 6Zm0 0c0-4 3-6 7-6 0 4-3 6-7 6Z"/></svg>
      </span>
      <h3>Plant&ndash;Microbe Interactions</h3>
      <p>Rhizosphere and endophytic microbes enhancing plant growth and stress tolerance.</p>
      <svg class="focus-art" viewBox="0 0 120 100" aria-hidden="true" focusable="false">
        <g fill="none" stroke="#2E7D46" stroke-width="1.6" stroke-linecap="round">
          <path d="M28 52h64" stroke-dasharray="3 5" opacity=".45"/>
          <path d="M60 52V28"/>
          <path d="M60 40c0-8-6-13-15-13 0 8 6 13 15 13Z" fill="#CFE7C8"/>
          <path d="M60 34c0-8 6-13 15-13 0 8-6 13-15 13Z" fill="#EFF7EC"/>
          <path d="M60 52v28M60 60c-8 2-12 8-14 15M60 66c8 2 12 8 14 15M60 74c-5 3-7 7-8 12M60 76c5 3 7 6 8 11"/>
          <circle cx="40" cy="68" r="4.5" fill="#DCEEDA"/>
          <circle cx="84" cy="62" r="3.5" fill="#DCEEDA"/>
          <circle cx="76" cy="82" r="3" fill="#EFF7EC"/>
        </g>
      </svg>
    </article>

    <article class="focus-card reveal">
      <span class="focus-icon">
        <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3v4m0 14v-4M7 6l3 3m7 9-3-3M4 12h4m12 0h-4"/><circle cx="12" cy="12" r="3"/></svg>
      </span>
      <h3>Arsenic Bioremediation</h3>
      <p>Microbial transformation and immobilization of arsenic for environmental safety.</p>
      <svg class="focus-art" viewBox="0 0 120 100" aria-hidden="true" focusable="false">
        <g fill="none" stroke="#2E7D46" stroke-width="1.6" stroke-linecap="round">
          <circle cx="62" cy="50" r="22" fill="#DCEEDA"/>
          <text x="62" y="57" text-anchor="middle" font-family="Inter, system-ui, sans-serif" font-size="18" font-weight="600" fill="#1F7A42" stroke="none">As</text>
          <ellipse cx="24" cy="30" rx="11" ry="7" transform="rotate(-20 24 30)" fill="#EFF7EC"/>
          <path d="M13 36c-5 2-7 6-8 10"/>
          <ellipse cx="99" cy="78" rx="10" ry="6.5" transform="rotate(-20 99 78)" fill="#EFF7EC"/>
          <path d="M108 71c5-2 8-6 9-11"/>
          <path d="M62 22v-8M84 50h8M62 78v8M40 50h-8" opacity=".5"/>
        </g>
      </svg>
    </article>

    <article class="focus-card reveal">
      <span class="focus-icon">
        <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 20c4-8 10-12 16-13-1 8-6 13-13 13H4Z"/><path d="M4 20c2-4 5-6 8-7"/></svg>
      </span>
      <h3>Sustainable Agriculture</h3>
      <p>Microbial strategies for soil health, contaminant mitigation and crop resilience.</p>
      <svg class="focus-art" viewBox="0 0 120 100" aria-hidden="true" focusable="false">
        <g fill="none" stroke="#2E7D46" stroke-width="1.6" stroke-linecap="round">
          <path d="M14 76c14-11 30-16 48-16s34 5 48 16Z" fill="#DCEEDA"/>
          <path d="M60 60V32"/>
          <path d="M60 46c-2-10-10-15-19-16 1 10 9 16 19 16Z" fill="#CFE7C8"/>
          <path d="M60 42c2-10 10-15 19-16-1 10-9 16-19 16Z" fill="#EFF7EC"/>
          <path d="M22 84h76" opacity=".45"/>
          <path d="M34 91h52" opacity=".28"/>
        </g>
      </svg>
    </article>

  </div>
</section>

<section class="band">
  <div class="shell band-grid">

    <div class="band-col reveal">
      <h2 class="rule-heading">
        <svg class="rule-ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 21c0-6 3-10 8-12-1 7-4 11-8 12Z"/><path d="M12 21c-4-1-7-5-8-12 5 2 8 6 8 12Z"/></svg>
        About me
      </h2>

      <div class="about-inner">
        <figure class="about-photo">
          <img src="assets/img/about-portrait.jpg" alt="Shubha Dixit working at a microscope in the laboratory">
        </figure>

        <div class="about-text">
          <p>PhD researcher in Biological Science at AcSIR and CSIR-IITR, Lucknow.</p>
          <p>My research focuses on environmental microbiology, fungal endophytes, rhizospheric microbiology and arsenic bioremediation.</p>
          <p>I aim to understand microbial functions and translate them into sustainable solutions for environmental and agricultural challenges.</p>
          <a class="btn btn-line" href="about.html">
            Know more about me
            <svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="8" r="3.5"/><path d="M5 20c1.5-4 12.5-4 14 0"/></svg>
          </a>
        </div>
      </div>
    </div>

    <div class="band-col band-col-mid reveal">
      <h2 class="rule-heading">
        <svg class="rule-ico" viewBox="0 0 24 24" aria-hidden="true"><circle cx="6" cy="7" r="2"/><circle cx="18" cy="7" r="2"/><circle cx="12" cy="17" r="2"/><path d="M8 8l3 7m5-7-3 7"/></svg>
        Research highlights
      </h2>

      <div class="tile-grid">
        <a class="tile" href="research.html">
          <img src="assets/img/highlight-fungal-endophytes.jpg" alt="Fungal endophyte hyphae under magnification">
          <span>Fungal endophytes</span>
        </a>
        <a class="tile" href="research.html">
          <img src="assets/img/highlight-microbial-remediation.jpg" alt="Bacterial cells involved in remediation">
          <span>Microbial remediation</span>
        </a>
        <a class="tile" href="research.html">
          <img src="assets/img/highlight-water-treatment.jpg" alt="Water samples in test tubes">
          <span>Water &amp; wastewater treatment</span>
        </a>
        <a class="tile" href="research.html">
          <img src="assets/img/highlight-monitoring.jpg" alt="Fungal colonies growing on a culture plate">
          <span>Environmental monitoring</span>
        </a>
      </div>

      <a class="btn btn-solid btn-wide" href="projects.html">Explore all projects __ARROW__</a>
    </div>

    <div class="band-col reveal">
      <h2 class="rule-heading">
        <svg class="rule-ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M8 4h8v5a4 4 0 0 1-8 0z"/><path d="M8 5H5v2a3 3 0 0 0 3 3m8-5h3v2a3 3 0 0 1-3 3M10 20h4m-2-4v4"/></svg>
        Achievements
      </h2>

      <ul class="badge-row">
        <li>
          <svg class="badge-ico" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="9" r="5"/><path d="m8 14-2 7 6-3 6 3-2-7"/></svg>
          <strong>Gold medallist</strong><span>M.Sc. AMBT</span>
        </li>
        <li>
          <svg class="badge-ico" viewBox="0 0 24 24" aria-hidden="true"><path d="m12 3 2.6 5.6 6 .8-4.4 4.2 1.1 6-5.3-3-5.3 3 1.1-6L3.4 9.4l6-.8z"/></svg>
          <strong>DST&ndash;INSPIRE</strong><span>Fellowship</span>
        </li>
        <li>
          <svg class="badge-ico" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="10" r="6"/><path d="M9 15.5 7 22l5-2.5L17 22l-2-6.5"/></svg>
          <strong>AIR 199</strong><span>ICAR AICE JRF/SRF</span>
        </li>
        <li>
          <svg class="badge-ico" viewBox="0 0 24 24" aria-hidden="true"><rect x="4" y="4" width="16" height="13" rx="1.5"/><path d="M8 9h8M8 12h5m-1 5v3l2-1.5L16 20v-3"/></svg>
          <strong>University merit</strong><span>Certificate</span>
        </li>
      </ul>

      <h2 class="rule-heading rule-heading-split">
        <span>
          <svg class="rule-ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 4h9l5 5v11H5z"/><path d="M14 4v5h5M8 13h8m-8 3h5"/></svg>
          Latest publications
        </span>
        <a class="chip-link" href="publications.html">View all</a>
      </h2>

      <div class="pub-carousel" id="pubCarousel">
        <ul class="pub-track">
          <li class="pub-slide is-active">
            <img class="pub-thumb" src="assets/img/pub-arsenic-serendipita.jpg" alt="First page of the arsenic removal paper">
            <div class="pub-meta">
              <h3>Efficient removal of arsenic from the environment by the endophytic fungus <em>Serendipita indica</em> through bioaccumulation in cells and adsorption on the cell wall</h3>
              <p class="pub-source">Environmental Technology &amp; Innovation, 2025</p>
              <span class="tag">Research article</span>
              <a class="doi" href="https://doi.org/10.1016/j.eti.2025.104229" target="_blank" rel="noopener">https://doi.org/10.1016/j.eti.2025.104229 __EXT__</a>
            </div>
          </li>
          <li class="pub-slide">
            <img class="pub-thumb" src="assets/img/pub-microplastics.jpg" alt="Cover of the microplastics book chapter">
            <div class="pub-meta">
              <h3>Microbes&rsquo; and microplastics&rsquo; interactions in freshwater ecosystems: fate and implications for environmental health</h3>
              <p class="pub-source">Springer Nature Singapore, 2025</p>
              <span class="tag">Book chapter</span>
              <a class="doi" href="https://doi.org/10.1007/978-981-95-0225-7_1" target="_blank" rel="noopener">https://doi.org/10.1007/978-981-95-0225-7_1 __EXT__</a>
            </div>
          </li>
          <li class="pub-slide">
            <img class="pub-thumb" src="assets/img/pub-fungi-polymeric.jpg" alt="Cover of the fungal biodegradation chapter">
            <div class="pub-meta">
              <h3>Applications of fungi in biodegradation of polymeric waste and micropollutants</h3>
              <p class="pub-source">Fungi in Wastewater Treatment, Volume 2 &mdash; Springer Nature Switzerland, 2026</p>
              <span class="tag">Book chapter</span>
              <a class="doi" href="https://doi.org/10.1007/978-3-032-01955-4_5" target="_blank" rel="noopener">https://doi.org/10.1007/978-3-032-01955-4_5 __EXT__</a>
            </div>
          </li>
          <li class="pub-slide">
            <img class="pub-thumb" src="assets/img/pub-fungi-radioactive.jpg" alt="Cover of the radioactive contaminants chapter">
            <div class="pub-meta">
              <h3>Applications of fungi in remediation of radioactive contaminants</h3>
              <p class="pub-source">Fungi in Wastewater Treatment, Volume 2 &mdash; Springer Nature Switzerland, 2026</p>
              <span class="tag">Book chapter</span>
              <a class="doi" href="https://doi.org/10.1007/978-3-032-01955-4_10" target="_blank" rel="noopener">https://doi.org/10.1007/978-3-032-01955-4_10 __EXT__</a>
            </div>
          </li>
        </ul>

        <div class="pub-dots" role="tablist" aria-label="Latest publications">
          <button role="tab" aria-selected="true" aria-label="Publication 1" class="is-active"></button>
          <button role="tab" aria-selected="false" aria-label="Publication 2"></button>
          <button role="tab" aria-selected="false" aria-label="Publication 3"></button>
          <button role="tab" aria-selected="false" aria-label="Publication 4"></button>
        </div>
      </div>
    </div>

  </div>
</section>
"""

# ══════════════════════════════════════════════════════════ ABOUT
ABOUT = page_head(
    "About",
    "Shubha Dixit",
    "PhD researcher in Biological Science at AcSIR and CSIR-Indian Institute of Toxicology "
    "Research, Lucknow, working at the meeting point of environmental microbiology, "
    "biotechnology and sustainable agriculture.",
    """<div class="page-stats">
      <div><strong>9.00</strong> M.Sc. CGPA</div>
      <div><strong>5</strong> Publications</div>
      <div><strong>7</strong> Conference presentations</div>
      <div><strong>2</strong> Years research experience</div>
    </div>"""
) + """
<section class="section">
  <div class="shell">
    <div class="split-grid">
      <figure class="portrait-card reveal">
        <img src="assets/img/about-portrait.jpg" alt="Shubha Dixit at the microscope">
      </figure>

      <div class="reveal">
        <p class="eyebrow eyebrow-dark">Career objective</p>
        <h2 class="section-title">Microbial function, translated into practice</h2>
        <p class="section-lead">
          I want to establish myself as an independent researcher in environmental
          microbiology and biotechnology &mdash; advancing sustainable answers to
          environmental pollution and agricultural challenges through microbial technology.
        </p>
        <p>
          My work centres on plant&ndash;microbe interactions, fungal endophytes,
          rhizospheric microbiology, microbial ecology, and arsenic biotransformation and
          bioremediation, with the aim of building strategies for contaminant remediation
          and stronger plant resilience.
        </p>
        <p>
          I integrate classical microbiology with molecular, genomic and multi-omics
          approaches to unravel what microbes actually do, and how that can be applied in
          environmental and agricultural systems. Interdisciplinary research,
          collaboration and continuous learning are how I want to contribute &mdash;
          through publications, translational work, and a career in academia dedicated to
          sustainable environmental development.
        </p>
      </div>
    </div>
  </div>
</section>

<section class="section section-tint">
  <div class="shell">
    <header class="section-head reveal">
      <p class="eyebrow eyebrow-dark">Education</p>
      <h2 class="section-title">Academic profile</h2>
    </header>

    <div class="table-wrap reveal">
      <table class="data-table">
        <thead>
          <tr><th>Years</th><th>Qualification</th><th>Institute</th><th>Result</th></tr>
        </thead>
        <tbody>
          <tr><td>2024 &ndash; present</td><td>PhD, Biological Science</td><td>AcSIR &middot; CSIR-Indian Institute of Toxicology Research, Lucknow</td><td>Ongoing</td></tr>
          <tr><td>2020 &ndash; 2022</td><td>M.Sc. Applied Microbiology &amp; Biotechnology</td><td>Banasthali Vidyapith</td><td>9.00 CGPA</td></tr>
          <tr><td>2017 &ndash; 2020</td><td>B.Sc. Bioscience</td><td>Banasthali Vidyapith</td><td>7.45 CGPA</td></tr>
          <tr><td>2017</td><td>Intermediate, CBSE</td><td>St. Francis Academy</td><td>70%</td></tr>
          <tr><td>2015</td><td>High School, CBSE</td><td>St. Francis Academy</td><td>7.6 CGPA</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<section class="section">
  <div class="shell">
    <header class="section-head reveal">
      <p class="eyebrow eyebrow-dark">Recognition</p>
      <h2 class="section-title">Fellowships, awards and achievements</h2>
    </header>

    <div class="award-grid">
      <article class="award reveal">
        <svg class="badge-ico" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="9" r="5"/><path d="m8 14-2 7 6-3 6 3-2-7"/></svg>
        <h3>Gold medal and first rank</h3>
        <p>M.Sc. Applied Microbiology &amp; Biotechnology, batch of 2020&ndash;2022, Banasthali Vidyapith.</p>
      </article>
      <article class="award reveal">
        <svg class="badge-ico" viewBox="0 0 24 24" aria-hidden="true"><path d="m12 3 2.6 5.6 6 .8-4.4 4.2 1.1 6-5.3-3-5.3 3 1.1-6L3.4 9.4l6-.8z"/></svg>
        <h3>DST&ndash;INSPIRE Fellowship</h3>
        <p>Awarded in Life Science.</p>
      </article>
      <article class="award reveal">
        <svg class="badge-ico" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="10" r="6"/><path d="M9 15.5 7 22l5-2.5L17 22l-2-6.5"/></svg>
        <h3>All India Rank 199</h3>
        <p>ICAR AICE JRF/SRF, 2023.</p>
      </article>
      <article class="award reveal">
        <svg class="badge-ico" viewBox="0 0 24 24" aria-hidden="true"><rect x="4" y="4" width="16" height="13" rx="1.5"/><path d="M8 9h8M8 12h5m-1 5v3l2-1.5L16 20v-3"/></svg>
        <h3>University Merit Certificate</h3>
        <p>Banasthali Vidyapith, for a scholastic grade point average of 9 CGPA.</p>
      </article>
      <article class="award reveal">
        <svg class="badge-ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 4h14v9a7 7 0 0 1-14 0z"/><path d="M9 20h6"/></svg>
        <h3>NTA PhD entrance, 2024</h3>
        <p>Qualified in both Biotechnology and Microbiology.</p>
      </article>
      <article class="award reveal">
        <svg class="badge-ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 19V7l8-3 8 3v12"/><path d="M9 19v-5h6v5"/></svg>
        <h3>University representative</h3>
        <p>10th Bhartiya Chhatra Sansad, New Delhi, 2020.</p>
      </article>
    </div>
  </div>
</section>

<section class="section section-tint">
  <div class="shell">
    <header class="section-head reveal">
      <p class="eyebrow eyebrow-dark">Beyond the lab</p>
      <h2 class="section-title">Away from the bench</h2>
    </header>
    <ul class="chip-list chip-list-lg reveal">
      <li>Badminton</li>
      <li>Photography</li>
      <li>Poetry writing</li>
      <li>Vedic scriptures</li>
      <li>National Service Scheme volunteering</li>
    </ul>
  </div>
</section>
"""

# ══════════════════════════════════════════════════════════ RESEARCH
RESEARCH = page_head(
    "Research",
    "Four questions my work keeps returning to",
    "Each theme starts in the field &mdash; a contaminated aquifer, a paddy soil, a wetland "
    "outlet &mdash; and ends at the bench, where microbial function is isolated, "
    "characterised and put to work."
) + """
<section class="section">
  <div class="shell">
    <div class="theme-list">

      <article class="theme reveal">
        <h3>How do microbial communities respond to a contaminated environment?</h3>
        <p>
          Environmental microbiology and microbial ecology form the base of my work:
          isolating, culturing and characterising bacterial and fungal communities from
          water, soil and rhizosphere, then reading their diversity and function through
          molecular and multi-omics approaches.
        </p>
        <ul class="chip-list">
          <li>Microbial ecology</li><li>Diversity analysis</li><li>Bacteriology &amp; mycology</li><li>Microbial genetics</li><li>Microbial physiology</li>
        </ul>
      </article>

      <article class="theme reveal">
        <h3>Can endophytes make crops tolerate what the soil throws at them?</h3>
        <p>
          Rhizospheric and endophytic microbes &mdash; <em>Serendipita indica</em> among
          them &mdash; can restrict metal uptake, support growth and buffer plants against
          stress. I study these associations to build biological inputs that work under
          real field contamination.
        </p>
        <ul class="chip-list">
          <li>Plant&ndash;microbe interactions</li><li>Fungal endophytes</li><li>Rhizosphere microbiology</li><li>Plant tissue culture</li><li>Sustainable agriculture</li>
        </ul>
      </article>

      <article class="theme reveal">
        <h3>Where does arsenic go, and can microbes take it out of circulation?</h3>
        <p>
          From arsenic mobilisation in Haridwar groundwater to microbe-assisted
          remediation in the arsenic-impacted agricultural soils of Laksar, this thread
          follows the element through biogeochemical transformation, bioaccumulation and
          cell-wall adsorption.
        </p>
        <ul class="chip-list">
          <li>Arsenic biogeochemistry</li><li>Heavy-metal biotransformation</li><li>Bioremediation</li><li>Groundwater microbiology</li><li>Environmental toxicology</li>
        </ul>
      </article>

      <article class="theme reveal">
        <h3>What does a treatment system actually remove?</h3>
        <p>
          Water quality assessment and environmental monitoring &mdash; constructed
          wetlands, wastewater treatment performance, and the physicochemical parameters
          that decide whether a system removes chemical and bacterial load or merely moves
          it downstream.
        </p>
        <ul class="chip-list">
          <li>Water quality assessment</li><li>Constructed wetlands</li><li>Environmental monitoring</li><li>Pollution control</li><li>QA/QC &amp; method validation</li>
        </ul>
      </article>

    </div>
  </div>
</section>

<section class="section section-tint">
  <div class="shell">
    <header class="section-head reveal">
      <p class="eyebrow eyebrow-dark">Areas of interest</p>
      <h2 class="section-title">Where the disciplines meet</h2>
    </header>

    <div class="interest-grid">
      <div class="interest reveal">
        <h3>Microbiology</h3>
        <p>Environmental microbiology, microbial ecology, rhizosphere and endophytic microbiology, microbial genetics, mycology, bacteriology, microbial physiology.</p>
      </div>
      <div class="interest reveal">
        <h3>Biotechnology</h3>
        <p>Environmental biotechnology, bioremediation, plant&ndash;microbe interactions, molecular and cellular biology, environmental toxicology, sustainable agriculture.</p>
      </div>
      <div class="interest reveal">
        <h3>Environmental sciences</h3>
        <p>Water quality assessment, groundwater microbiology, arsenic biogeochemistry, heavy-metal biotransformation, environmental monitoring, pollution control.</p>
      </div>
      <div class="interest reveal">
        <h3>Research techniques</h3>
        <p>Molecular microbiology, microbial genomics, multi-omics, microbial diversity analysis, bioinformatics, analytical instrumentation.</p>
      </div>
    </div>
  </div>
</section>
"""

# ══════════════════════════════════════════════════════════ PROJECTS
PROJECTS = page_head(
    "Projects",
    "Field campaigns and laboratory studies",
    "Four bodies of work, from an arsenic-affected aquifer in Haridwar to fungal cultures "
    "at CSIR-IITR."
) + """
<section class="section">
  <div class="shell">
    <div class="project-grid">

      <article class="project-card reveal">
        <img src="assets/img/project-arsenic-groundwater.jpg" alt="Groundwater sampling in the field">
        <div class="project-body">
          <p class="project-tag">National Institute of Hydrology, Roorkee &middot; 2022&ndash;2024</p>
          <h3>Understanding arsenic mobilisation in the groundwater of Haridwar and formulating remediation measures</h3>
          <p>
            Groundwater quality assessment across an arsenic-affected belt: field sampling
            and collection, physicochemical and environmental analysis, instrument
            operation under QA/QC protocols, and statistical interpretation feeding into
            remediation strategy and technical reporting.
          </p>
        </div>
      </article>

      <article class="project-card reveal">
        <img src="assets/img/project-constructed-wetland.jpg" alt="Constructed wetland treatment system">
        <div class="project-body">
          <p class="project-tag">M.Sc. dissertation &middot; NIH Roorkee &middot; 2022</p>
          <h3>Evaluation of constructed wetland in chemical and bacterial removal</h3>
          <p>
            How well does a constructed wetland actually clean water? The study paired
            physicochemical parameter analysis with isolation, cultivation and
            identification of the bacterial communities driving pollutant degradation
            inside the system.
          </p>
        </div>
      </article>

      <article class="project-card reveal">
        <img src="assets/img/project-laksar-soils.jpg" alt="Agricultural soil sampling at Laksar">
        <div class="project-body">
          <p class="project-tag">Ongoing &middot; CSIR-IITR, Lucknow</p>
          <h3>From arsenic hotspots to biological solutions: agricultural soils of Laksar, Uttarakhand</h3>
          <p>
            Mapping heavy-metal contamination across Laksar&rsquo;s agricultural fields,
            then testing the microbe-assisted remediation potential of the communities
            already living in those soils.
          </p>
        </div>
      </article>

      <article class="project-card reveal">
        <img src="assets/img/project-serendipita.jpg" alt="Fungal culture plate in the laboratory">
        <div class="project-body">
          <p class="project-tag">Ongoing &middot; CSIR-IITR, Lucknow</p>
          <h3>Endophytic fungi as metal sinks</h3>
          <p>
            Characterising how <em>Serendipita indica</em> and its endofungal bacterial
            partners take up and immobilise arsenic and cadmium &mdash; bioaccumulation
            inside cells, adsorption on the cell wall, and what that means for crop
            protection.
          </p>
        </div>
      </article>

    </div>
  </div>
</section>
"""

# ══════════════════════════════════════════════════════════ PUBLICATIONS
PUBLICATIONS = page_head(
    "Publications",
    "Peer-reviewed articles and book chapters",
    "Journal articles and invited chapters on arsenic bioremediation, fungal applications "
    "in wastewater treatment, and microbe&ndash;microplastic interactions.",
    """<div class="page-stats">
      <div><strong>1</strong> Journal article</div>
      <div><strong>4</strong> Book chapters</div>
      <div><strong>2025&ndash;26</strong> Publication years</div>
    </div>"""
) + """
<section class="section">
  <div class="shell">
    <ol class="pub-list">

      <li class="pub-row reveal">
        <span class="pub-year">2025</span>
        <div>
          <h3>Efficient removal of arsenic from the environment by endophytic fungus <em>Serendipita indica</em> through bioaccumulation in cells and adsorption on the cell wall</h3>
          <p class="pub-authors">Shukla, J., Singh, S., <strong>Dixit, S.</strong>, Kushwaha, A. S., Mohd, S., Saji, J., &amp; Kumar, M.</p>
          <p class="pub-source">Environmental Technology &amp; Innovation, 104229</p>
          <span class="tag">Research article</span>
          <a class="doi" href="https://doi.org/10.1016/j.eti.2025.104229" target="_blank" rel="noopener">doi.org/10.1016/j.eti.2025.104229 __EXT__</a>
        </div>
      </li>

      <li class="pub-row reveal">
        <span class="pub-year">2025</span>
        <div>
          <h3>Microbes&rsquo; and microplastics&rsquo; interactions in freshwater ecosystems: fate and implications for environmental health</h3>
          <p class="pub-authors"><strong>Dixit, S.</strong>, Maurya, A., Singh, A., Verma, S., Singh, R., &amp; Kumar, M.</p>
          <p class="pub-source">In <em>Occurrence, Detection, and Fate of Microplastics in Freshwater Ecosystems</em> (pp. 1&ndash;39). Springer Nature Singapore</p>
          <span class="tag">Book chapter</span>
          <a class="doi" href="https://doi.org/10.1007/978-981-95-0225-7_1" target="_blank" rel="noopener">doi.org/10.1007/978-981-95-0225-7_1 __EXT__</a>
        </div>
      </li>

      <li class="pub-row reveal">
        <span class="pub-year">2026</span>
        <div>
          <h3>Applications of fungi in biodegradation of polymeric waste and micropollutants</h3>
          <p class="pub-authors">Maurya, A., <strong>Dixit, S.</strong>, Nayak, S., Singh, S., &amp; Kumar, M.</p>
          <p class="pub-source">In <em>Fungi in Wastewater Treatment: Volume 2</em> (pp. 101&ndash;123). Springer Nature Switzerland</p>
          <span class="tag">Book chapter</span>
          <a class="doi" href="https://doi.org/10.1007/978-3-032-01955-4_5" target="_blank" rel="noopener">doi.org/10.1007/978-3-032-01955-4_5 __EXT__</a>
        </div>
      </li>

      <li class="pub-row reveal">
        <span class="pub-year">2026</span>
        <div>
          <h3>Applications of fungi in wastewater and innovative approaches to residual waste processing</h3>
          <p class="pub-authors">Singh, S., Nayak, S., Maurya, A., <strong>Dixit, S.</strong>, &amp; Kumar, M.</p>
          <p class="pub-source">In <em>Fungi in Wastewater Treatment: Volume 2</em> (pp. 283&ndash;308). Springer Nature Switzerland</p>
          <span class="tag">Book chapter</span>
          <a class="doi" href="https://doi.org/10.1007/978-3-032-01955-4_13" target="_blank" rel="noopener">doi.org/10.1007/978-3-032-01955-4_13 __EXT__</a>
        </div>
      </li>

      <li class="pub-row reveal">
        <span class="pub-year">2026</span>
        <div>
          <h3>Applications of fungi in remediation of radioactive contaminants</h3>
          <p class="pub-authors">Nayak, S., Singh, S., Maurya, A., <strong>Dixit, S.</strong>, &amp; Kumar, M.</p>
          <p class="pub-source">In <em>Fungi in Wastewater Treatment: Volume 2</em> (pp. 217&ndash;242). Springer Nature Switzerland</p>
          <span class="tag">Book chapter</span>
          <a class="doi" href="https://doi.org/10.1007/978-3-032-01955-4_10" target="_blank" rel="noopener">doi.org/10.1007/978-3-032-01955-4_10 __EXT__</a>
        </div>
      </li>

    </ol>

    <p class="note reveal">
      Conference abstracts are listed separately on the <a href="conferences.html">conferences page</a>.
    </p>
  </div>
</section>
"""

# ══════════════════════════════════════════════════════════ EXPERIENCE
EXPERIENCE = page_head(
    "Experience",
    "Positions, skills and training",
    "Two years of applied hydrology and groundwater research at NIH Roorkee, and the "
    "laboratory and analytical skill set built alongside it."
) + """
<section class="section">
  <div class="shell">
    <div class="exp-grid">

      <div class="reveal">
        <h3 class="col-title">Research positions</h3>
        <ol class="timeline">
          <li>
            <span class="tl-date">2024 &mdash; present</span>
            <h4>PhD researcher, Biological Science</h4>
            <p>AcSIR &middot; CSIR-Indian Institute of Toxicology Research, Lucknow. Microbe-assisted remediation of arsenic-impacted agricultural soils, endophytic fungi and metal restriction in plants.</p>
          </li>
          <li>
            <span class="tl-date">Jan 2022 &mdash; Jan 2024</span>
            <h4>Resource Person</h4>
            <p>National Institute of Hydrology, Roorkee &mdash; research project on arsenic mobilisation in Haridwar groundwater. Field sampling and groundwater collection, physicochemical and environmental analysis, experiment design, analytical instrumentation under QA/QC protocols, statistical interpretation, technical reporting and project documentation.</p>
          </li>
          <li>
            <span class="tl-date">Jan &mdash; Jul 2022</span>
            <h4>M.Sc. dissertation</h4>
            <p>National Institute of Hydrology, Roorkee &mdash; evaluation of constructed wetland in chemical and bacterial removal, combining water quality analysis with bacterial isolation and identification.</p>
          </li>
        </ol>

        <h3 class="col-title col-title-gap">Training and workshops</h3>
        <ul class="plain-list">
          <li>Water and wastewater treatment &mdash; 5-day training, NIH Roorkee</li>
          <li>Water quality monitoring &amp; management &mdash; 5-day hands-on training, NIH Roorkee</li>
          <li>Environment data processing &mdash; 5-day hands-on training, NIH Roorkee</li>
          <li>2nd Roorkee Water Conclave 2022 &mdash; IIT Roorkee</li>
        </ul>
      </div>

      <div class="reveal">
        <h3 class="col-title">Skills</h3>

        <div class="skill-block">
          <h4>Research &amp; laboratory</h4>
          <ul class="chip-list">
            <li>Microbial isolation &amp; characterisation</li><li>Fungal &amp; bacterial culturing</li>
            <li>Aseptic technique</li><li>Plant tissue culture</li><li>DNA extraction</li><li>PCR</li>
            <li>Agarose gel electrophoresis</li><li>ELISA</li><li>Cell-based assays</li><li>Microscopy</li>
            <li>Water quality analysis</li><li>Spectrophotometry</li><li>TOC analysis</li>
            <li>TKN estimation</li><li>Ion chromatography</li><li>Biochemical characterisation</li>
            <li>Media preparation</li><li>Experimental design</li>
          </ul>
        </div>

        <div class="skill-block">
          <h4>Analytical &amp; technical</h4>
          <ul class="chip-list">
            <li>Research methodology</li><li>Scientific writing</li>
            <li>Data analysis &amp; interpretation</li><li>Statistical analysis</li>
            <li>Environmental monitoring</li><li>Laboratory QA/QC</li><li>Method validation</li>
            <li>Documentation</li>
          </ul>
        </div>

        <div class="skill-block">
          <h4>Software &amp; bioinformatics</h4>
          <ul class="chip-list">
            <li>Origin</li><li>BLAST</li><li>ArcGIS</li><li>QGIS</li><li>Google Earth Pro</li>
            <li>Microsoft Office Suite</li><li>Reference managers</li>
          </ul>
        </div>

        <div class="skill-block">
          <h4>Professional</h4>
          <ul class="chip-list">
            <li>Scientific problem-solving</li><li>Hypothesis development</li>
            <li>Experimental planning</li><li>Collaboration</li><li>Leadership</li>
            <li>Project management</li><li>Scientific communication</li>
          </ul>
        </div>
      </div>

    </div>
  </div>
</section>
"""

# ══════════════════════════════════════════════════════════ CONFERENCES
CONFERENCES = page_head(
    "Conferences",
    "Presentations and symposia",
    "Three international conferences, a national symposium, and abstracts presented at "
    "EGU, the Roorkee Water Conclave and CSIR-IITR.",
    """<div class="page-stats">
      <div><strong>3</strong> International conferences</div>
      <div><strong>1</strong> National symposium</div>
      <div><strong>1</strong> Oral presentation</div>
    </div>"""
) + """
<section class="section">
  <div class="shell">
    <ul class="conf-list">

      <li class="conf reveal">
        <span class="conf-when">May 2026</span>
        <div>
          <h3>Microbe-assisted remediation potential in arsenic-impacted agricultural soils of Laksar, Uttarakhand</h3>
          <p>Dixit, S., Maurya, A., Singh, R., Singh, S., &amp; Kumar, M. &mdash; EGU General Assembly 2026 &middot; Vienna, Austria &middot; 3&ndash;8 May 2026 &middot; EGU26-811</p>
          <a class="doi" href="https://doi.org/10.5194/egusphere-egu26-811" target="_blank" rel="noopener">doi.org/10.5194/egusphere-egu26-811 __EXT__</a>
        </div>
      </li>

      <li class="conf reveal">
        <span class="conf-when">May 2026</span>
        <div>
          <h3>From arsenic hotspots to biological solutions: microbial remediation of contaminated agricultural soils of Laksar</h3>
          <p>Dixit, S., Maurya, A., Nayak, S., Singh, S., Singh, R., &amp; Kumar, M. &mdash; International Symposium on Emerging Contaminants in Water with Special Focus on Arsenic and Fluoride Contamination (ECWAF 2026) &middot; IIT Roorkee &middot; 29&ndash;30 May 2026</p>
        </div>
      </li>

      <li class="conf reveal">
        <span class="conf-when">Feb 2026</span>
        <div>
          <h3>Spatial distribution and mapping of heavy metals in agricultural fields of Laksar, Uttarakhand</h3>
          <p>Dixit, S., Maurya, A., Singh, R., &amp; Kumar, M. &mdash; Roorkee Water Conclave 2026 &middot; IIT Roorkee &amp; NIH Roorkee &middot; 23&ndash;25 February 2026</p>
        </div>
      </li>

      <li class="conf reveal">
        <span class="conf-when">Nov 2025</span>
        <div>
          <h3>Assessment of heavy metal contamination in agricultural soils of Laksar, Uttarakhand</h3>
          <p>Dixit, S., Maurya, A., Singh, R., &amp; Kumar, M. &mdash; Emerging Approaches in Risk Analysis and Translational Aspects of Health and Environment (EARTH 2025) &middot; CSIR-IITR, Lucknow &middot; 12&ndash;15 November 2025</p>
        </div>
      </li>

      <li class="conf reveal">
        <span class="conf-when">Nov 2025</span>
        <div>
          <h3>Investigating the role of <em>Serendipita indica</em> and endofungal bacterium 06_IITR association in cadmium restriction in tobacco</h3>
          <p>Nayak, S., Dixit, S., &amp; Kumar, M. &mdash; EARTH 2025 &middot; CSIR-IITR, Lucknow &middot; 12&ndash;15 November 2025 &middot; co-author</p>
        </div>
      </li>

      <li class="conf reveal">
        <span class="conf-when">Mar 2024</span>
        <div>
          <h3>Evaluation of constructed wetland for chemical and bacterial removal <span class="conf-flag">Oral presentation</span></h3>
          <p>3rd Roorkee Water Conclave &middot; IIT Roorkee &middot; 3&ndash;6 March 2024</p>
        </div>
      </li>

      <li class="conf reveal">
        <span class="conf-when">Jan 2024</span>
        <div>
          <h3>Evaluation of constructed wetland for chemical and bacterial removal</h3>
          <p>Dixit, S., &amp; Singh, R. &mdash; International Conference on Future of Water Resources (ICFWR 2024) &middot; IIT Roorkee &middot; 18&ndash;20 January 2024</p>
        </div>
      </li>

      <li class="conf reveal">
        <span class="conf-when">Feb 2020</span>
        <div>
          <h3>University representative</h3>
          <p>10th Bharatiya Chhatra Sansad &middot; MIT World Peace University &middot; 20&ndash;23 February 2020</p>
        </div>
      </li>

    </ul>
  </div>
</section>
"""

# ══════════════════════════════════════════════════════════ GALLERY
labels = [
    ("gallery-01.jpg", "Field sampling"),
    ("gallery-02.jpg", "At the bench"),
    ("gallery-03.jpg", "Culture plates"),
    ("gallery-04.jpg", "Conference presentation"),
    ("gallery-05.jpg", "Instrumentation"),
    ("gallery-06.jpg", "Research group"),
    ("gallery-07.jpg", "Gold medal, M.Sc. AMBT"),
    ("gallery-08.jpg", "Poster session"),
]
figs = "\n".join(
    '      <figure class="reveal"><img src="assets/img/%s" alt="%s"><figcaption>%s</figcaption></figure>'
    % (f, cap, cap) for f, cap in labels)

GALLERY = page_head(
    "Gallery",
    "Field, bench and podium",
    "Sampling campaigns, laboratory work, conferences and the moments in between."
) + """
<section class="section">
  <div class="shell">
    <div class="gallery-grid">
%s
    </div>
  </div>
</section>
""" % figs

# ══════════════════════════════════════════════════════════ CONTACT
CONTACT = page_head(
    "Contact",
    "Open to collaboration",
    "I am glad to hear from research groups working on bioremediation, plant&ndash;microbe "
    "systems and water quality &mdash; and from students looking for a way into "
    "environmental microbiology."
) + """
<section class="section">
  <div class="shell contact-grid">

    <div class="reveal">
      <h2 class="section-title">Get in touch</h2>
      <ul class="contact-list">
        <li>
          __MAIL__
          <a href="mailto:shubha.dixit.9@gmail.com">shubha.dixit.9@gmail.com</a>
        </li>
        <li>
          <svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 21s7-6.2 7-11a7 7 0 1 0-14 0c0 4.8 7 11 7 11Z"/><circle cx="12" cy="10" r="2.5"/></svg>
          CSIR-Indian Institute of Toxicology Research, Lucknow, India
        </li>
        <li>
          __DL__
          <a href="assets/cv/Shubha_Dixit_CV.pdf" download>Download full CV (PDF)</a>
        </li>
      </ul>

      <h3 class="col-title col-title-gap">Profiles</h3>
      <ul class="contact-list">
        <li><a href="https://scholar.google.com/citations?user=-epYhrEAAAAJ&amp;hl=en" target="_blank" rel="noopener">Google Scholar</a></li>
        <li><a href="https://orcid.org/0009-0008-8177-6797" target="_blank" rel="noopener">ORCID</a></li>
        <li><a href="https://www.researchgate.net/profile/Shubha-Dixit-2" target="_blank" rel="noopener">ResearchGate</a></li>
        <li><a href="https://www.linkedin.com/in/shubha-dixit-377602171" target="_blank" rel="noopener">LinkedIn</a></li>
      </ul>
    </div>

    <form class="contact-form reveal" action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
      <label>
        <span>Name</span>
        <input type="text" name="name" required placeholder="Your name">
      </label>
      <label>
        <span>Email</span>
        <input type="email" name="email" required placeholder="you@institute.edu">
      </label>
      <label>
        <span>Message</span>
        <textarea name="message" rows="5" required placeholder="What would you like to discuss?"></textarea>
      </label>
      <button class="btn btn-solid" type="submit">Send message __ARROW__</button>
      <p class="form-note">The form posts through Formspree &mdash; replace <code>YOUR_FORM_ID</code> with your own endpoint, or delete the form and keep the email link.</p>
    </form>

  </div>
</section>
"""

pages = [
    ("index.html", "Shubha Dixit &mdash; Environmental Microbiologist | Researcher | Biotechnologist",
     "Shubha Dixit, PhD researcher in environmental microbiology and biotechnology: plant-microbe interactions, fungal endophytes, rhizospheric microbiology and arsenic bioremediation.", HOME, False),
    ("about.html", "About &mdash; Shubha Dixit",
     "Career objective, academic profile, fellowships and awards of Shubha Dixit, PhD researcher at AcSIR and CSIR-IITR Lucknow.", ABOUT, True),
    ("research.html", "Research &mdash; Shubha Dixit",
     "Research themes: microbial ecology, plant-microbe interactions, arsenic bioremediation and water quality assessment.", RESEARCH, True),
    ("projects.html", "Projects &mdash; Shubha Dixit",
     "Field campaigns and laboratory studies on arsenic mobilisation, constructed wetlands and microbe-assisted remediation.", PROJECTS, True),
    ("publications.html", "Publications &mdash; Shubha Dixit",
     "Peer-reviewed articles and book chapters on arsenic bioremediation, fungal applications in wastewater treatment and microplastics.", PUBLICATIONS, True),
    ("experience.html", "Experience &mdash; Shubha Dixit",
     "Research positions, laboratory and analytical skills, software and training of Shubha Dixit.", EXPERIENCE, True),
    ("conferences.html", "Conferences &mdash; Shubha Dixit",
     "Conference presentations and symposia including EGU General Assembly 2026 and the Roorkee Water Conclave.", CONFERENCES, True),
    ("gallery.html", "Gallery &mdash; Shubha Dixit",
     "Photographs from field sampling, laboratory work and conferences.", GALLERY, True),
    ("contact.html", "Contact &mdash; Shubha Dixit",
     "Contact Shubha Dixit for collaboration in environmental microbiology, bioremediation and water quality research.", CONTACT, False),
]

for name, title, desc, body, cta in pages:
    body = body.replace("__ARROW__", ARROW).replace("__EXT__", EXT) \
               .replace("__MAIL__", MAIL).replace("__DL__", DOWNLOAD)
    write(name, title, desc, body, cta)

print("all pages written")
