Django Blog Tutorial from Corey Schafer: https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p

# Setup

Install django
```
pip install -r requirements.txt
```

Create project
```
django-admin startproject django_project
```

Launch the server
```
python manage.py runserver
```

Site becomes available at http://localhost:8000/

# Start a new app

```
python manage.py startapp blog
```

# Bootstrap Starter Template
https://getbootstrap.com/docs/4.0/getting-started/introduction/#starter-template

# Admin Page

Create the super user
```
python manage.py makemigrations  # This will show "No changes detected"
python manage.py migrate
python manage.py createsuperuser
```
Access the admin page: http://localhost:8000/admin/

# Migrations

## Changing models

You must run the migration whenever models are changed.

```
python manage.py makemigrations
python manage.py migrate
```

## Real world

Based on [Django Migrations Documentation](https://docs.djangoproject.com/en/5.0/topics/migrations/), it looks like `makemigrations` would normally be run on a pre-prod system. The generated migration file **should** be committed to source control. Then in production you would only need to run `migrate`.

> You should think of migrations as a version control system for your database schema. makemigrations is responsible for packaging up your model changes into individual migration files - analogous to commits - and migrate is responsible for applying those to your database.
>
> The migration files for each app live in a “migrations” directory inside of that app, and are designed to be committed to, and distributed as part of, its codebase. You should be making them once on your development machine and then running the same migrations on your colleagues’ machines, your staging machines, and eventually your production machines.

## Debugging Migrations

Lets say you run the makemigrations and get the following output:
```
➜  django_project git:(tutorial_part_05) ✗ python manage.py makemigrations
Migrations for 'blog':
  blog/migrations/0001_initial.py
    - Create model Post
```

You can see the actual sql that will be run during the `migrate` step by running
```
python manage.py sqlmigrate blog 0001
```
Be sure to fill in the appropriate app name and migration number.

Here is the example output:
```
➜  django_project git:(tutorial_part_05) ✗ python manage.py sqlmigrate blog 0001
BEGIN;
--
-- Create model Post
--
CREATE TABLE "blog_post" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(100) NOT NULL, "content" text NOT NULL, "date_posted" datetime NOT NULL, "author_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "blog_post_author_id_dd7a8485" ON "blog_post" ("author_id");
COMMIT;
```

# Debugging
You can enter an interactive python shell that has access to all the Django models
```
python manage.py shell
```

Sample:
```
➜  django_project git:(tutorial_part_05) ✗ python manage.py shell
Python 3.12.1 (main, Jan  5 2024, 10:51:10) [Clang 15.0.0 (clang-1500.1.0.2.5)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
```

# Create a post from the interactive shell
```
>>> from blog.models import Post
>>> from django.contrib.auth.models import User
>>> User.objects.all()
<QuerySet [<User: dottey>, <User: testuser>]>

>>> User.objects.first()
<User: dottey>

>>> User.objects.last()
<User: testuser>

>>> User.objects.filter(username='dottey').first()
<User: dottey>

>>> user = User.objects.filter(username='dottey').first()

>>> Post.objects.all()
<QuerySet []>

>>> post_1 = Post(title='Blog 1', content='First Post Content!', author=user)
>>> post_1.save()
>>> Post.objects.all()
<QuerySet [<Post: Post object (1)>]>
```
After adding a `__str__` method to the Post class:
```
>>> from blog.models import Post
>>> from django.contrib.auth.models import User
>>> Post.objects.all()
<QuerySet [<Post: Blog 1>]>
```
Get details about the post
```
>>> post = Post.objects.first()
>>> post
<Post: Blog 1>

>>> post.date_posted
datetime.datetime(2024, 2, 6, 19, 13, 53, 733767, tzinfo=datetime.timezone.utc)
```
Using post_set to access and create posts:
```
>>> user.post_set.all()
<QuerySet [<Post: Blog 1>, <Post: Blog 2>]>

>>> user.post_set.create(title='Blog 3', content='Third Post Content!')
<Post: Blog 3>
```

# Crispy Forms

* https://django-crispy-forms.readthedocs.io/en/latest/install.html
* https://pypi.org/project/crispy-bootstrap4/

Add the two requirements
```
crispy-bootstrap4
django-crispy-forms
```

Update settings.py
```
    INSTALLED_APPS = (
        ...
        "crispy_forms",
        "crispy_bootstrap4",
        ...
    )

    CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"

    CRISPY_TEMPLATE_PACK = "bootstrap4"
```
