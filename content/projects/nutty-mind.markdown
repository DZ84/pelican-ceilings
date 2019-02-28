title: Nutty-Mind: CSS practice
slug: projects-nutty-mind
category: projects
date: 2019-02-14
modified: 2019-02-14
stylesheets: nutty-mind.css
Sortorder: 001

Eventhough I'm more interested in backend development, I still felt I needed to practice my CSS skills. It can be fun, and comes in handy all the time. As practice I tried to copy a certain style I saw in a painting, which resulted in:

<script>
<!--
	// This is pure padding that pelican won't execute but does consider when
	// determining the size of the article in the homepage/index overview.
//-->
</script>	

<div class="nutty-mind-container" style="
			width: 100%;
			min-height: 450px;
			text-align; center;
			background: black;
			">
	<div style="float: left; width: 50%; height: 10px;"></div>
	{% from 'nutty-mind.html' import fig_wrap %}
	{{ fig_wrap() }}
</div>
<br/>

The example I had seen before was drawn on a wall in a hostel:

<img src="./images/projects/nutty-mind/example.jpg">

Obviously CSS is not the best technique to create such an image, it is too fragile. But it was interesting none the less.

As usual, different browsers may give different results, but this can break outside of Firefox or Chrome, and zoomlevels can have varying effects. I expect also that SASS would have made the process of creating this easier.

The repository can be found [here](https://github.io/dzet/nutty_mind).

