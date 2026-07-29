# Udacity Projects Portfolio

A collection of four projects completed across different Udacity courses, ranging from static HTML/CSS websites to a Python-based resume analysis tool and a JavaScript card game with automated testing.

## Projects

### UD1 — Udacity Website Project (`udacity-projects/udacity-website-project/UD1/`)

A static multi-page website built with HTML and CSS. Contains an `index.html`, a `css/` directory, an `images/` directory, and a `pages/` subdirectory.

**To run:** Open `UD1/index.html` directly in a browser.

---

### UD3 — Portfolio Site (`udacity-projects/udacity-portfolio-site/Portfolio Site-UD3/`)

A personal portfolio website built with SCSS and the BEM methodology. Sass is compiled to a single compressed CSS file in `dist/`.

**Tech:** HTML, SCSS (Sass 1.69.5), BEM

```bash
cd "udacity-projects/udacity-portfolio-site/Portfolio Site-UD3"
npm install
npm run dev       # watch and compile SCSS
npm run build-css # one-off compile
```

---

### UD4 — Resume Optimization Project (`udacity-projects/resume-optimization-project/Resume Optimization Project-UD4/UD3/`)

A Python tool for analysing and enhancing resumes. Reads PDF and DOCX files, performs NLP-based text analysis, and produces scoring or suggestions. Contains `docs/`, `examples/`, `submission/`, and `tools/` subdirectories.

**Tech:** Python 3.8+, NLTK, spaCy, textstat, PyPDF2, python-docx, pandas, numpy, BeautifulSoup4, Click

```bash
pip install -r requirements.txt
```

---

### UD7 — Card Game with Shuffle (`udacity-projects/udacity-project-ud7/UD-7/`)

A browser-based card game application built with vanilla JavaScript (ES modules). Implements a shuffle algorithm (`Shuffle.js`), card rendering utilities (`utilityRenderFunctions.js`), and a full game loop (`app.js`). Includes a Mocha/Chai unit-test suite and Cypress end-to-end tests, all orchestrated with Gulp and bundled with Parcel.

**Tech:** JavaScript (ES modules), Parcel 2.16.4, Gulp 5, Mocha 11, Chai 6, Cypress 15, TypeScript 5.9

```bash
cd "udacity-projects/udacity-project-ud7/UD-7"
npm install
npm run dev       # gulp watch (Parcel dev build)
npm run build     # production build
npm test          # Mocha unit tests
npm run test:cypress  # Cypress e2e tests
```

---

## Clone

```bash
git clone https://github.com/ali-yaqoup/udacity-projects.git
```
