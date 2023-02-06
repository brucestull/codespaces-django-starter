# Commands and Links

## Questions and Concepts

### Questions

* How to get the CodeSpaces environment variables?
  * `printenv`
* What is involved in deploying this to Heroku?

### Concepts

* Can use this repository as a 'starter' for other projects in GitHub's CodeSpaces.
* `python manage.py shell` seems to work as expected:

  ```bash
  @brucestull ➜ /workspaces/codespaces-django (main) $ python manage.py shell
  Python 3.10.4 (main, Jan 25 2023, 00:13:50) [GCC 9.4.0]
  Type 'copyright', 'credits' or 'license' for more information
  IPython 8.8.0 -- An enhanced Interactive Python. Type '?' for help.
  
  In [1]: from django.conf import settings as s
  
  In [2]: s.DEBUG
  Out[2]: True
  
  In [3]:
  ```

## Commands

* Start the development server:
  * `python manage.py runserver`

## Links
