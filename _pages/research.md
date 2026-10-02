---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
---

{% if site.author.googlescholar %}
You can also find my publications on [Google Scholar]({{ site.author.googlescholar }}).
{% endif %}

{% include base_path %}

{% assign ordered_research = site.research | sort: 'working_paper_order' %}
{% for post in ordered_research %}
  {% include archive-single.html %}
{% endfor %}
