'''
Do you see Django block Tag inside the <title> element, and the <body> element?

They are placeholders, telling Django to replace this block with content from other sources.

Modify Templates
Now the two templates (all_members.html and details.html) can use this master.html template.

This is done by including the master template with the {% extends %} tag, and inserting a title block and a content block:

MembersGet your own Django Server
my_tennis_club/members/templates/all_members.html:

{% extends "master.html" %}

{% block title %}
  My Tennis Club - List of all members
{% endblock %}


{% block content %}
  <h1>Members</h1>

  <ul>
    {% for x in mymembers %}
      <li><a href="details/{{ x.id }}">{{ x.firstname }} {{ x.lastname }}</a></li>
    {% endfor %}
  </ul>
{% endblock %}
DetailsGet your own Django Server
my_tennis_club/members/templates/details.html:

{% extends "master.html" %}

{% block title %}
  Details about {{ mymember.firstname }} {{ mymember.lastname }}
{% endblock %}


{% block content %}
  <h1>{{ mymember.firstname }} {{ mymember.lastname }}</h1>

  <p>Phone {{ mymember.phone }}</p>
  <p>Member since: {{ mymember.joined_date }}</p>

  <p>Back to <a href="/members">Members</a></p>

{% endblock %}
If you have followed all the steps on your own computer, you can see the result in your own browser: 127.0.0.1:8000/members/.

If the server is down, you have to start it again with the runserver command:

py manage.py runserver
'''