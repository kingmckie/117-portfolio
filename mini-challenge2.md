Create the Projects section

1. Create an app named projects:
    python3 manage.py startapp projects 

2. Install the app in setting.py under config folder
    INSTALLED_APPD = [
        'pages',
        'projects',
    ]

3. Create a folder named projects under templates folder


4. Create a template named list.html
    4.1 Add the projecs section of the old version of the porfolio (use the about.html as example)

5. Create a view named projects_list
    5.1 Render the list.html

6. Create the urls.py file under projects app

7. Create the urlpattern to for the projects_list view

8. Include the urls of the projects app to the urls under config folder


app name: experience
<h2> My experience is here! </h>