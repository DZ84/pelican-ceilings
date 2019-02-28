title: Dynamic movement and collision handling
slug: projects-flying-dots
category: projects
date: 2019-02-14
modified: 2019-02-14
Sortorder: 001

<div class="container-for-dots">
	<div class="ref_point"></div>
</div>

This project is part of a larger project, which involves creating an alive version of a drawing I saw. But to be able to achieve this, the dots involved have to be able to detect eachother and handle collisions accordingly. This turned out to be quite challenging.

Although this version is not finished, it is fully functioning. As explained in the repository one could even make adjustments in the options to see what type of effect this will have the dots behavior and their interaction with eachother.

Some challenges in this projects were:

* maths, getting a grip on calculating new paths after collisions,
* finding decent ways of keeping track of situations (how does this collision effect future collisions),
* discovering the profileris in both Chrome and Firefox to help create more efficient code,
* and discovering the Firefox profiler is more informative/less buggy,
* finding out that modifying arrays takes *waaaaay* more cpu power than collision calculations do
.

<br>
To visit the site click [here](https://dzet.github.io).
The repository can be found [here](https://github.com/DZet/flying-dots).

{% from 'flying_dots.html' import flying_dots %}
{{ flying_dots() }}

<script>

	var el = document.getElementById("together")

    var ref_point = document.getElementsByClassName("ref_point")[0]
    ref_point.parentNode.insertBefore(el, null)

</script>
