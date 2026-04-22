---
permalink: /
title: "Ruijing (Chandler) Yang"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

Welcome! I am an Assistant Professor in Finance at the University of Macau. My research focuses on empirical asset pricing, derivatives, and machine learning methods for financial prediction.

## Quick links
- [Research](/research/)
- [Teaching](/teaching/)
- [Presentations](/presentation/)
- [CV](/cv/)
- [Data](/research_data/)

## Employment
- **2025–Present**: Assistant Professor in Finance, University of Macau
- **2024–2025**: Postdoctoral Fellow, The Hong Kong Polytechnic University
  Supervisor: Jie (Jay) Cao

## Education
- **Ph.D. in Finance**, The Chinese University of Hong Kong, 2024
- **M.Sc. in Finance**, Nanyang Technological University, 2019
- **B.Eng. in Civil Engineering**, Southeast University, 2017

## Selected Working Papers
{% include base_path %}
{% assign selected_research = site.research | reverse %}
{% for post in selected_research limit:4 %}
- **{{ post.title }}**
  - {{ post.authors }}
{% endfor %}

## Research Interests
- Empirical Asset Pricing: derivatives, return predictability, investments
- Machine Learning in Finance: textual analysis, large language models
