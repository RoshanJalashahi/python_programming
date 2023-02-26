'''
Create Template
After creating Models, with the fields and data we want in them, it is time to display the data in a web page.

Start by creating an HTML file named all_members.html and place it in the /templates/ folder:

my_tennis_club/members/templates/all_members.html:

<!DOCTYPE html>
<html>
<body>

<h1>Members</h1>

<ul>
  {% for x in mymembers %}
    <li>{{ x.firstname }} {{ x.lastname }}</li>
  {% endfor %}
</ul>

</body>
</html>
Do you see the {% %} brackets inside the HTML document?

They are Django Tags, telling Django to perform some programming logic inside these brackets.

You will learn more about Django Tags in our Django Tags chapter.

Modify View
Next we need to make the model data available in the template. This is done in the view.

In the view we have to import the Member model, and send it to the template like this:

my_tennis_club/members/views.py:

from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
'''