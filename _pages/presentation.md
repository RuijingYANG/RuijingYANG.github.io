---
layout: archive
title: "Presentations"
permalink: /presentation/
author_profile: true
---

<p class="section-note">* by coauthor</p>
{% assign presentation_years = site.data.presentations.presentations | group_by: 'year' %}
{% for year in presentation_years %}
<section class="presentation-year" aria-labelledby="presentations-{{ year.name }}">
<h2 id="presentations-{{ year.name }}">{{ year.name }}</h2>
<ul>
{% for event in year.items %}
<li>
<p class="event-name">{{ event.name | escape }}{% if event.by_coauthor %}<sup class="coauthor-marker">*</sup>{% endif %}</p>
{% if event.location %}<p class="event-place">{{ event.location | escape }}</p>{% endif %}
</li>
{% endfor %}
</ul>
</section>
{% endfor %}

<h2>Discussions</h2>
<ul class="discussion-list">
{% for event in site.data.presentations.discussions %}
<li>
<h3 class="discussion-title">{{ event.title | escape }}</h3>
<p class="discussion-meta">{{ event.conference | escape }}, {{ event.year }}</p>
<p class="discussion-authors">by {{ event.authors | escape }}</p>
</li>
{% endfor %}
</ul>
