title: Having multiple different banners 
slug: differentbanners
category: posts
date: 2019-03-29
modified: 2019-03-29

This site is generated through Pelican 4.0.1 with the Pelican-Bootstrap3 theme. 

If you want different banners for different parts of your website you can add
some customizability with the following steps:

### - Make sure you have Jinja2 (>=2.10) installed
<br/>

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

### - Adjust some code in your template

In your theme/pelican-bootstrap3/templates/ folder there is a base.html file.
In it you will find the following two snippets of code:

```bash
{% raw %}
# Snippet 1
<!-- Banner -->
{% if BANNER and BANNER_ALL_PAGES %}
    {% include 'includes/bannerhtml' %}
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


fillertext

```html
# Snippet 1
<!-- Banner -->
{.% if BANNER and BANNER_ALL_PAGES %.}
    {.% include 'includes/banner.html' %.}
{.% elif BANNER and not BANNER_ALL_PAGES %.}
    {.% block banner %.}{.% endblock %.}
{.% endif %.}
<!-- End Banner -->

# Snippet 2
{.% if BANNER %.}
    <script src="{.{ SITEURL }.}/{.{ THEME_STATIC_DIR
    }.}/js/bodypadding.js"></script>
{.% endif %.}
```
more fillertext

```bash
# Should update to the most recent version
pip install Jinja2 --upgrade
# Or specify a version
pip install Jinja2==2.10 --upgrade
```
```python
<script>src="{.{ SITEURL }.}/{.{ THEME_STATIC_DIR }.}/js/bodypadding.js"</script>
```
src="{{ SITEURL }}/{.{ THEME_STATIC_DIR }.}/js/bodypadding.js"

texty stuff
<div class="highlight">
    <p>
        <script>src="{" + "{ SITEURL }.}/{.{ THEME_STATIC_DIR }.}/js/bodypadding.js"</script>
    </p>
</div>

<!--script>
//
//    // there is a method to trigger the js code that is much more 
//    // comprehensive than this, but this seems to cover the necessity.
//    document.addEventListener("DOMContentLoaded", function(event) {
//        // Patterns to replace:
//        var regex_flags = 'g'
//        var replaceables = [
//            [/\{\.\{/, '\{\{'], 
//            [/\}\.\}/, '\}\}'],
//            [/\{\.\%/, '\{\%'], 
//            [/\%\.\}/, '\%\}'],
//        ]
//
//        var highlights = document.getElementsByClassName('highlight')
//
//        for (var hl=0;hl<highlights.length;hl++) {
//            for (var p=0;p<replaceables.length;p++) {
//                re = new RegExp(replaceables[p][0], regex_flags)
//                
//                var txt = highlights[hl].innerHTML
//                highlights[hl].innerHTML = txt.replace(re, replaceables[p][1])
//            }
//        }
//    })
//
//</script-->
################

