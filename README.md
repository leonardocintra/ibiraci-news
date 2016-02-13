News - Articles
================================

A simple web application that allows you to uploads photos, maintain a database with references to them, list them with their metadata, and display them using various cloud-based transformations.


## Installation

Run the following commands from your shell.

Project cloning and dependent package installation: 

    git clone https://github.com/leonardocintra/news.git
    cd news
    pip install -r requirements.txt

### Start with virtualenv

We recommend and support the usage of **virtualenv**. All you need to do is create a new virtualenv (if necessary):

    virtualenv venv

And then just activate it:

    source venv/bin/activate


### Usage

    - Add, update and remove articles
    - Articles supports images
    - RSS Feed
    - Users can comment on articles with [Disqus](https://disqus.com/)