# Ruijing (Chandler) Yang — Academic Website

Source repository for the personal academic website of Ruijing (Chandler) Yang, Assistant Professor in Finance at the University of Macau. The site presents research, teaching, conference presentations, and a curriculum vitae.

**Website:** [https://ruijingyang.github.io](https://ruijingyang.github.io)

Built with Jekyll and hosted on GitHub Pages. Current build and deployment information is available in this repository's [GitHub Actions](https://github.com/RuijingYANG/RuijingYANG.github.io/actions).

## Repository structure

- [`_pages/`](_pages/): main website pages.
- [`_research/`](_research/): working paper entries.
- [`_data/`](_data/): navigation, career, and presentation data.
- [`_config.yml`](_config.yml): site settings.
- `_includes/`, `_layouts/`, `_sass/`, and `assets/`: templates and styling.

## Local preview

With Ruby and Bundler installed, run from the repository root:

```bash
bundle install
bundle exec jekyll serve
```

Open `http://localhost:4000` to preview the site.

## Template attribution and license

Adapted from [Academic Pages](https://github.com/academicpages/academicpages.github.io), originally forked by Stuart Geiger from [Minimal Mistakes](https://github.com/mmistakes/minimal-mistakes) by Michael Rose. The underlying theme is released under the MIT License. The original copyright and permission notice are retained in [LICENSE](LICENSE).
