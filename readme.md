# Final Project - InstaClone

Web Programming with Python and JavaScript

### Requirements

See [here](https://docs.cs50.net/ocw/web/projects/3/project3.html).

## Initialization

To run the website following things need to be done:

- Install dependencies with `pip install -r requirements.txt`. Besides Django it contains Pillow library and django-optimized-image to work with images.
- Make migrations with `python manage.py makemigrations`.
- Apply migrations with `python manage.py migrate`.
- Create superuser with `python manage.py createsuperuser`.
- (Optionally) You can populate the database with menu items from http://www.pinocchiospizza.net/menu.html page by running `python create_db.py`.

## Models for db-interaction

- `Post`. Users can create Posts
- `Comment`. Posts can contain Comments
- `Like`. Posts can contain Likes

## Files and directories description

- `media`. A directory for storing items images. 'Default.img' is initally used for all items.
- `orders/static/orders` directory contains all static files used in project.

  - `scss`. It contains source SCSS file name `style.scss`.
  - `css`. Compiled CSS file, `style.css` and `style.css.map`.
  - `js`. A directory for JavaScript files.

- `orders/templates/orders`. A directory to store templates files.
  - `base.html`. Base HTML template.
  - `index.html`. Feed with newest posts
  - `post_detail.html`. Containing infos about a post
  - `post_form.html`. Create new posts with a form
  - `order_history.html`. All orders of a user
    The file "index.js" contains all code for sending requests to the backend. The other js-files were created for animations and styling.

The app "user" was created to manage the authentification for the user. All urls regarding the user can be found in the pizza/urls-file

- `orders`. Some notable files in this application directory:
  - `admin.py`. Contains admin classes for orders application.
  - `models.py`. This file includes all orders models, some of them were listed above.
  - `urls.py`. Here I included all URLs of orders application.
  - `views.py`. Includes all the views from orders application.
  - `create_db.py`. This script populates DB with items taken from http://www.pinocchiospizza.net/menu.html page.
