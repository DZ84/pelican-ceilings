// - This is to circumvent the current problem with the
// Jinja2content plugin for Pelican, which doesn't allow for
// escaping Jinja2 template tags. All Jinja2 tags placed inside
// article files are automatically processed by the plugin and
// can not easily be made visible on a Pelican page.
//
// - Usage: 
//
//      Escapes the following Jinja2 template tags: 
//          {% tag %}
//          {{ tag }}
//
//      in the following way:
//          {.% tag %.}
//          {.{ tag }.}
//
// - Concerning code highlights, it is only successfully tested 
// for code that is highlighted as HTML in a markdown file. For 
// example:
//
//  ```html
//      {.% if BANNER %.}
//          {.{ BANNER }.}
//      {.% endif %.}
//  ```
//
// will show a code highlight with the syntax of the template
// tags in place.
//
// - It can also be used with template tags that are escaped in
// other elements, like for example in paragraphs.
//
// - There is a method to trigger the js code that is much more 
// comprehensive than the "DOMContentLoaded" method, but this seems
// to cover the necessity.

document.addEventListener("DOMContentLoaded", function(event) {
    function replace_occurrences(els, replaceables, regex_flags) {
        for (var hl=0;hl<els.length;hl++) {
            for (var p=0;p<replaceables.length;p++) {
                re = new RegExp(replaceables[p][0], regex_flags)
                
                var txt = els[hl].innerHTML
                els[hl].innerHTML = txt.replace(re, replaceables[p][1])
            }
        }
    }

    // Patterns to replace:
    var regex_flags = 'g'
    var replaceables = [
        [/\{\.\{/, '\{\{'], 
        [/\}\.\}/, '\}\}'],
        [/\{\.\%/, '\{\%'], 
        [/\%\.\}/, '\%\}'],
    ]

    var highlights = document.getElementsByClassName('highlight')
    replace_occurrences(highlights, replaceables, regex_flags)

    var paragraphs= document.getElementsByTagName('p')
    replace_occurrences(paragraphs, replaceables, regex_flags)

})
