**Item Catalog**

Item catalog is a website and a JSON API for a list of category items.
The category here is sports.In order to add, edit or delete the website
needs user authentication using google. Registered users will have the
ability to perform any of the actions mentioned.

**Installations required**

1.  VirtualBox

2.  Vagrant

3.  Python 2.7

**How to install**

-   Install Vagrant and VirtualBox as per the instructions provided in
    Udacity course

-   Download the VM Configuration here
    <https://github.com/udacity/fullstack-nanodegree-vm>

-   Install the dependency libraries by running “pip install –r
    requirements.txt”

-   Signup for google account and set up a client id and secret.

-   Visit <http://console.developers.google.com> for google setup

-   Download file starting with client\_secret\_ from google developers
    console and rename it to client\_secrets.json and copy in the
    project folder.

-   Replace the client\_id in the html files with your client\_id and
    save html files.

**How to run**

-   Have Python 2.7.9 installed and make sure python was added to the
    windows path

-   Navigate to ***cd \\vagrant*** in the VM

-   Create the database using the command “python database\_setup.py”

-   Populate the database using “python populate\_database.py”

-   Run the app using “python project.py”

-   Open the web browser and go to the url “localhost:5000”


