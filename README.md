# Shubha Dixit — personal research website

A static site (plain HTML, CSS and vanilla JS — no build step, no framework), ready to
publish on GitHub Pages.

```
.
├── index.html          ← Home: hero, focus cards, about / highlights / achievements band
├── about.html          ← Career objective, academic profile, awards, interests
├── research.html       ← Four research themes + areas of interest
├── projects.html       ← Field campaigns and laboratory studies
├── publications.html   ← Articles and book chapters, with DOIs
├── experience.html     ← Positions, skills, training
├── conferences.html    ← Conference and symposium presentations
├── gallery.html        ← Photographs
├── contact.html        ← Contact details and message form
├── .nojekyll           ← stops GitHub running Jekyll on the folder
├── README.md
└── assets/
    ├── css/style.css   ← all styling; design tokens at the top
    ├── js/main.js      ← sticky header, mobile menu, reveal, carousel
    ├── cv/Shubha_Dixit_CV.pdf
    └── img/            ← every image, names listed below
```

Nine pages, one shared header and footer. Every inner page opens with a dark masthead so
the navigation stays readable, and closes with a call to action back to Contact.

**Navigation:** Home · About · **Research ▾** · Gallery · Contact. The Research item is a
dropdown holding *Research overview, Projects, Publications, Experience, Conferences* —
it opens on hover on desktop, on tap on mobile (where it becomes an indented accordion),
and the chevron button is keyboard-operable. All five remain ordinary standalone pages
with their own URLs; only the way you reach them changed. Whenever you are on one of
them, the Research tab shows the active dot and the matching item is highlighted in the
menu.

---

## 1. Publishing on GitHub Pages

Put everything above at the **root** of the repository (not inside a subfolder), then:

```bash
git add .
git commit -m "Add personal research website"
git push origin main
```

Repository → **Settings → Pages → Build and deployment**
→ Source: *Deploy from a branch* → Branch: `main` → Folder: `/ (root)` → **Save**.

The site appears in a minute or two at:

- `https://<username>.github.io/` if the repository is named `<username>.github.io`
- `https://<username>.github.io/<repo-name>/` for any other repository name

Both work unchanged, because every path is relative.

**Custom domain (optional):** add a file named `CNAME` at the root containing only your
domain, then point a CNAME DNS record at `<username>.github.io`.

---

## 2. Images — what goes where

Every image lives in `assets/img/`. Placeholder files with the right names and aspect
ratios are already there, so nothing renders broken. **Replace each file with a real one,
keeping the same filename** — no HTML editing needed.

### The two you are supplying

| Filename | Where | Suggested size | Notes |
|---|---|---|---|
| `logo.png` | Header on every page | 512 × 512, **transparent PNG** | Your SD monogram, with the surrounding transparent padding trimmed off so the mark fills the frame. It renders at 68 px on desktop (56 px once the header shrinks on scroll), 56 px on tablets, 52 px on phones. The untrimmed upload is kept as `logo-original.png`; if you replace `logo.png`, crop it tight to the artwork for the same effect. `favicon.png` is generated from it. |
| `hero-image.png` | Right side of the home hero | ~1100 × 1300, **transparent PNG** | The complete composite — portrait, fungal imagery, roots, water, all in one. Transparent background so it blends into the dark hero. The bottom edge fades out automatically. |

### The rest

| Filename | Where | Size | Subject |
|---|---|---|---|
| `hero-bg.jpg` | Behind the hero, and faintly behind every inner-page masthead | 1920 × 1080 | Dark microbial texture. Sits under a heavy veil, so a busy image is fine. |
| ~~`focus-*.png`~~ | — | — | **No longer used.** The four ribbon cards below the hero now carry inline SVG line art (microbe cluster, seedling with roots, "As" badge, sprout in soil) drawn in the site palette, so it scales crisply and blends with the card instead of sitting on it as a pasted box. The art lives in the `<svg class="focus-art">` block inside each card in `index.html`. |
| `about-portrait.jpg` | Home band + About page | 750 × 1000 (3:4) | At the microscope, white coat. |
| `highlight-fungal-endophytes.jpg` | Home, tile 1 | 900 × 620 | Fungal endophyte micrograph. |
| `highlight-microbial-remediation.jpg` | Home, tile 2 | 900 × 620 | Bacterial cells / SEM. |
| `highlight-water-treatment.jpg` | Home, tile 3 | 900 × 620 | Water samples in test tubes. |
| `highlight-monitoring.jpg` | Home, tile 4 | 900 × 620 | Culture plate with colonies. |
| `pub-arsenic-serendipita.jpg` | Home carousel, slide 1 | 450 × 600 (3:4) | First page of the ETI paper. |
| `pub-microplastics.jpg` | Slide 2 | 450 × 600 | Book or chapter cover. |
| `pub-fungi-polymeric.jpg` | Slide 3 | 450 × 600 | Book or chapter cover. |
| `pub-fungi-radioactive.jpg` | Slide 4 | 450 × 600 | Book or chapter cover. |
| `project-arsenic-groundwater.jpg` | Projects | 1200 × 675 (16:9) | Groundwater sampling. |
| `project-constructed-wetland.jpg` | Projects | 1200 × 675 | Constructed wetland site. |
| `project-laksar-soils.jpg` | Projects | 1200 × 675 | Agricultural soil sampling. |
| `project-serendipita.jpg` | Projects | 1200 × 675 | Fungal cultures on plates. |
| `gallery-01.jpg` … `gallery-08.jpg` | Gallery | 900 × 675 (4:3) | Field, bench, conference and award photos. |
| `og-cover.jpg` | Link preview on WhatsApp / LinkedIn / X | 1200 × 630 | Name, title, one strong image. |
| `favicon.png` | Browser tab icon | 128 × 128 | The monogram on a dark square. |

Tips:
- Keep photos under ~400 KB. [Squoosh](https://squoosh.app) does this in a browser.
- Filenames are case-sensitive on GitHub Pages. `Gallery-01.JPG` will **not** load.
- More gallery photos: copy a `<figure>` block in `gallery.html` and add `gallery-09.jpg`, etc.

---

## 3. Fill in before going live

Search the HTML files for these:

1. **Profile links** — `https://scholar.google.com/`, `https://orcid.org/`,
   `https://www.researchgate.net/`, `https://www.linkedin.com/`. They appear in the hero
   (`index.html`), the footer of every page, and `contact.html`. Replace with the real
   URLs, or delete the `<li>` for any profile that doesn't exist yet.
2. **Contact form** — `action="https://formspree.io/f/YOUR_FORM_ID"` in `contact.html`.
   Create a free form at [formspree.io](https://formspree.io) and paste the endpoint, then
   delete the `.form-note` paragraph. Or delete the whole `<form>` — the email link
   beside it still works.
3. **CV** — replace `assets/cv/Shubha_Dixit_CV.pdf` when it is updated, keeping the name.

Deliberately **not** on the site, though they are on the CV: phone numbers, home address,
date of birth and parents' names. Those belong off a public page — the email address and
institutional affiliation are enough.

---

## 4. Editing content

Each page is a plain HTML file you can edit directly. The header and footer blocks are
identical in all nine — if you change the navigation, change it in every file (or ask for
the generator script that writes them all from one template).

All colours, fonts and spacing live in the `:root` block at the top of
`assets/css/style.css`:

```css
--leaf:      #7CC96A;  /* bright accent — "Microbial Life", eyebrows, hover */
--leaf-deep: #1F7A42;  /* solid buttons, DOIs, timeline dots */
--ink:       #07160E;  /* hero, mastheads, footer */
--cream:     #F7F5EE;  /* page background */
```

Type is **Newsreader** (display serif) + **Inter** (body), loaded from Google Fonts in
each `<head>`.

---

## 5. Previewing locally

```bash
python3 -m http.server 8000
```

Then open `http://localhost:8000`.
