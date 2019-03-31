title: Differing banners with Pelican-Bootstrap3
slug: differing-banners
category: posts
date: 2019-03-31
modified: 2019-03-31


This site is generated through Pelican 4.0.1 with the Pelican-Bootstrap3 theme. 

If you want different banners for different parts of your website you can
do so by making the following adjustments:

<script>
<!--
	// This is pure padding that pelican won't execute but does consider when
	// determining the size of the article in the homepage/index overview.
-->
</script>

<br/>
### **- Make sure you have Jinja2 (>=2.10) installed**

The .10 stands for ten, so 2.9 will not be up to date. Check your version with:


```bash
# The capitals matter
pip freeze | grep Jinja2
```

And update accordingly with:


```bash
# Should update to the most recent version
pip install Jinja2 --upgrade
# Or specify a version
pip install Jinja2==2.10 --upgrade
```
<br/>
### **- Adjust some code in your template**

In your **theme/pelican-bootstrap3/templates/** folder there is a **'base.html'** file.
In it you will find the following two snippets of code:

```bash
{% raw %}
# Snippet 1
<!-- Banner -->
{% if BANNER and BANNER_ALL_PAGES %}
    {% include 'includes/banner.html' %}
{% elif BANNER and not BANNER_ALL_PAGES %}
    {% block banner %}{% endblock %}
{% endif %}
<!-- End Banner -->


# Snippet 2
{% if BANNER %}
    <script src="{{ SITEURL }}/{{ THEME_STATIC_DIR
    }}/js/bodypaddingjs"></script>
{% endif %}

{% endraw %}
```

Which you can replace with:

```bash

{% raw %}
# Snippet 1
<!-- Banner -->
{% set banner = namespace(found=false) %}
{% for category, banner_url in CUSTOM_BANNERS %}
    {% if category == output_file and not found %}
        {% set banner.found = true %}
        {% set BANNER = banner_url %}
        {% include 'includes/banner.html' %}
    {% endif %}
{% endfor %}
<!-- End Banner -->

# Snippet 2
{% if banner.found %}
    <script src="{{ SITEURL }}/{{ THEME_STATIC_DIR
    }}/js/bodypadding.js"></script>
{% endif %}

{% endraw %}
```

There is also some banner related clutter in **'index.html'** that you can remove if you want to do
it correctly. And, if you're somehow bothered by the **sitename** appearing on your banner,
you can remove the **{% raw %} '{{ sitename }}' {% endraw %}** tag from the **'includes/banner.html'** file.


<br/>
### **- Alter your pelicanconf.py**

Remove the following options completely from your **'pelicanconf.py'** file:

* BANNER
* BANNER_ALL_PAGES

<br/>
And you can now add the following code for some more options concerning you
banners:

```bash

CUSTOM_BANNERS = (
    ('index.html', './images/banners/gg_aligned_cropped.jpg'),
    ('category/posts.html', './images/banners/my_own_picture.jpg'),
    ('category/projects.html', './images/banners/some_other_picture.jpg'),
    ('pages/About.html', './images/banners/some_picture_about_you.JPG'),
    ('differing-banners.html', './images/banners/picture_for_article.jpg'),
)

```

There is the index, categories, pages, and individual articles.

<br/>
Enjoy

