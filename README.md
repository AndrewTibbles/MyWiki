# <center>Django 2.2 project for unit 27 by Andrew Tibbles</center>

### The company that i work for are having some of its websites moved away from the use of ASP.NET in order to provide more choices about Linux vs Windows servers. We understand how Django works on Linux systems, but less so using Django on Windows. I am required to produece a dynamic wiki with the following requirements.
- Be using django 2.2 + and python 3.6 +
- Have the ability to upload text or images to the website.
- Upload files which can be stored and then downloaded.
- Create, edit and save pages from the browser.
- User login which has been intergrated to restrict modification.
- Add a method to log 404 and 500 errors filtering out trivial errors.
- Apply a url to display simple statistics. These statistics must persist across a server reboot.
- Aesthetically pleasing design for use with the company. Minimal CSS used so bootstrap is required.
- Use an SQLite for the backend database.
- Providing user login to be assessed.
- Comments throughout the source code
- Unit tests to prove I know how they work.
---
## <center>Setup</center>
---
### Navigate to the directory `.\MyWiki\`
### Run the command `pip install -r requirements.txt` to install any dependencies. If you are an unprivileged user use `pip install --user -r requirements.txt` and it will be installed for your local user.
### Start the server with `Python manage.py runserver` 
### To view the site in your browser navigate to `http://localhost:8000/` or `http://127.0.0.1:8000/`
---
## <center>Test User Admin Login Credentials</center>
--- 
### <center>Username: `Admin`</center>
### <center>Password: `Admin`</center>
---
## <center>Error Logging</center>
---
### To test 404 and 500 errors on the site, use the extension '/errors/407', '/errors/404' and '/errors/500'
### This will log only 404 and 500 errors to the MyWiki/MyWiki/logs/debug.log.
### I have also styled the file to look more prosentable and readable including the use of a timestamp.

### This site is stored on an SCCS through my Github repository which can be located here: `https://github.com/AndrewTibbles/MyWiki`