'''
The extends Tag
In the previous pages we created two templates, one for listing all members, and one for details about a member.

The templates have a set of HTML code that are the same for both templates.

Django provides a way of making a "parent template" that you can include in all pages to for the stuff that are the same in all pages.

Start by creating a template called master.html, with all the necessary HTML elements:

MasterGet your own Django Server
my_tennis_club/members/templates/master.html:

<!DOCTYPE html>
<html>
<head>
  <title>{% block title %}{% endblock %}</title>
</head>
<body>

{% block content %}
{% endblock %}

</body>
</html>
Do you see Django block Tag inside the <title> element, and the <body> element?

They are placeholders, telling Django to replace this block with content from other sources.

'''