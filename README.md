# WebTransfer
#### a privacy-respecting file sharing service
---

### Frequently Asked Questions

*What is WebTransfer?*
> WebTransfer is a fast and free file sharing service designed to be privacy-respecting.

*Is WebTransfer public?*
> Yes! WebTransfer is publicly available [here](https://wt.iipython.cf).

*How much space does WebTransfer give you?*
> Each user gets a set amount of storage (by default, 6 gigabytes), and can upload files upto 2 gigabytes in size. After you upload a file, it expires in 24 hours to save storage space.

*Do I have to pay to use WebTransfer?*
> No. WebTransfer is and always will be completely free, no strings attached.

---

###  Design

WebTransfer is built on top of the Python Flask framework, utilizing public routes for HTML-serving pages and API routes for everything else. The frontend is designed using [Bootstrap](https://getbootstrap.com), [Bootstrap Icons](https://icons.getbootstrap.com), [JQuery](https://jquery.com) and AJAX.  

For example, when you load **/user/dashboard**, you get the dashboard HTML containing the template and a loading spinner. In the background, an AJAX request is made to **/user/api/files**, which populates the template and displays it.

---

###  Installation

Before you setup WebTransfer, you should have the following:
- Python 3.10+ ([download](https://python.org))
- Python Requirements (`python3 -m pip install -r reqs.txt`)
- Git SCM* ([download](https://git-scm.com))

If you built Python from source (Linux only):
- Python SQlite Extension (install sqlite libraries before building)
    - Debian: `sudo apt install libsqlite3-dev`
    - Fedora: `sudo dnf install sqlite-devel`

Begin setting up WebTransfer:
```bash
git clone https://github.com/ii-Python/webtransfer
cd webtransfer
python3 -m pip install -r reqs.txt
```

Before you attempt to launch WebTransfer, see [Configuration](#configuration) and then [Launching](#launching)

---

### Configuration

In order for Flask to use sessions properly, you require a secret key.  
To pass this to WebTransfer, either use the `SECRET_KEY` environment variable or use a `.env` file.  

> If you're using a `.env` file, place the following in it:
> `SECRET_KEY="hopefully a long and secure string"`

> If you're running via command line:
> `SECRET_KEY="hopefully a long and secure string" python3 ...`

For security reasons, a quite important thing to do is migrate from the built-in Flask sessions to the open-source [Flask-Session](https://redis.io/) module. This however will require an installation of [Redis](https://redis.io/), and could potentially slow down your instance (though by milliseconds).  
To set this up, follow these steps:
- Install Redis ([link](https://redis.io/)):
    - Debian: `sudo apt install redis`
    - Fedora: `sudo dnf install redis`
- Set the `redis-server` binary location:
    - If on your PATH, it will automatically be picked up
    - Otherwise, set the `REDIS_BINARY` environment variable
- Install Flask-Session (`python3 -m pip install Flask-Session`)
- Relaunch WebTransfer

Another **very** important thing to do (for both security and performance) is to switch to [uWSGI](https://uwsgi-docs.readthedocs.io/en/latest/) if you plan on making your instance public. The built-in Werkzeug server will perform terribly compared to something as basic as [gunicorn](https://gunicorn.org).

In the event that you do use gunicorn you could run the following:
> python3 -m gunicorn -b 0.0.0.0:8080 -w 1 launch:app

---

### Launching

Before you launch, ensure the following:
    - You have [Redis](https://redis.io/) installed on your system (if using [Flask-Session](https://flask-session.readthedocs.io/en/latest/))
    - You have enough space for uploads on the current drive

If you are launching with any form of uWSGI server, make sure you **only have 1 worker**.  
The threads that WebTransfer uses for Redis and reaper will unfortunately break and likely corrupt your database when running from more than 1 worker.

To launch with Gunicorn (**recommended**):
> python3 -m gunicorn -b 0.0.0.0:8080 -w 1 launch:app

To launch with the Werkzeug server:
> python3 launch.py
