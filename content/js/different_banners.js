    var snippets_unused = "# snippet 1:" +
        "<br/>" + 
        "{% if BANNER and BANNER_ALL_PAGES %}"
        "    {% include 'includes/banner.html' %}"
        "{% elif BANNER and not BANNER_ALL_PAGES %}"
        "    {% block banner %}{% endblock %}"
        "{% endif %}"
        "## snippet 2:"
        "{% if BANNER %}"
        '    <script src="{{ SITEURL }}/{{'
        '    THEME_STATIC_DIR}}/js/bodypadding.js"></script>'
        "{% endif %}"

var snippets = "<pre>" +
    "<span class='c1'># Snippet 1</span>" +
    "<br/>" +
    "{% if BANNER and BANNER_ALL_PAGES %}" +
    "<br/>" +
    "    {% include 'includes/banner.html' %}" +
    "<br/>" +
    "{% elif BANNER and not BANNER_ALL_PAGES %}" +
    "<br/>" +
    "    {% block banner %}{% endblock %}" +
    "<br/>" +
    "{% endif %}" +
    "<br/>" +
    "<br/>" +
    "<span class='c1'># Snippet 2</span>" +
    "<br/>" +
    "{% if BANNER %}" +
    "<br/>" +
    '    &lt;<span class="ent">script</span> <span class="e">src</span>=<span class="s2"><span class="pds">"</span>{{ SITEURL }}/{{ THEME_STATIC_DIR }}/js/bodypadding.js<span class="pds">"</span></span>&gt;&lt;/<span class="ent">script</span>&gt;' +
    "<br/>" +
    "{% endif %}</pre>" 

    function place_snippet(snippets) {
        var placing_point = document.getElementById('code_snippets_1')
        placing_point.innerHTML = snippets
    }

    // there is a method much more comprehensive than this,
    // but this does seem to cover the necessity.
    document.addEventListener("DOMContentLoaded", function(event) {
        place_snippet(snippets)
    });
