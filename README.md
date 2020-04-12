# About Bytely

<font color='red'>NOTE:</font> This is not a "real" website, it's not hosted anywhere, maybe in the future. If I decide to host it somewhere it will probably not be at ``.com`` but in this README I'll be using it for examples.

This project is *heavily* inspired by [Bitly](https://bitly.com/), hence the name Bytely. The reason as to why I decided to go with that name is because I'm planning to add some additional features, including, but not limited to:

 - **Statistics**: Clicks, percentage by country, how many clicks for every day.
 - **Charts**: Using the above statistics for pie charts, line charts and possibly more.
 - **Custom Links**: Registered users can create custom shortened links  (e.g. `Bytely.com/MyCustomLink`).

# Want to help?
**Backend:**
At the moment I'm not looking for any help with the Backend, if you notice any significant flaws or some improvements, sure go ahead and create a pull request, but I want to figure out the backend feature implementation by myself. If you have any suggestions / ideas make a pull request, I'll always e reading them.

**Frontend:**
Go nuts! This is not API based so I'm using the Jinja2 templating engine. If you know how to use it and want to write some HTML, CSS, JS feel free to make a pull request and I'll take a look at it!

# How to install

 - Download the files from the github repository.
 **or**
 - use git - ``git clone https://www.github.com/vincent-gustafsson/bytely``
 - Make sure you have all the libraries installed.
# How to run

 1. Open the terminal.
 2. Make sure you are in the directory that contains the ``run.py`` file.
 3. Type ``python run.py´´
 4. The Flask app will now run on a development server at ``http://127.0.0.1:5000``
