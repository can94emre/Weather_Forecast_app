# Weather_Forecast_app

We parse the json data from this application api with the python service. We fetch the parse according to the name of the city that the user wrote on the html page. The application displays the temperature of the city selected by the user.


### Prerequisites


There are some necessary software to run the application. Some programs are needed when loading.

```
Ubuntu 16.0.4
python 3.5
python pip 3
python flask module
python requests module
python render_template module
apache tomcat
apache2
html
Vim


```

### Installing

The linux based Ubuntu 16.0.4 operating system is required for the operation of the program first.

  Linux da ilk olarak apache tomcat yüklüyoruz.
```
sudo apt-get update
sudo apt-get install default-jdk
sudo apt-get install tomcat8

```
  Then, install apache2.
```
sudo apt-get install apache2
```
  Install python3.5 for for service work
```
sudo apt-get install python3.5
```
  And python pip
```
sudo apt-get install python3-pip
pip3 -V
```

  We need python flask module and requests module
```
sudo pip3 install flask
sudo pip3 install requests

```
 In order to run our service, in ubuntu terminal, we enter the file that is in our python service. We're running our service.
 ```
 python3.5 weather.py
 
 ```

At the terminal after service run

 ```
  http://127.0.0.1:5000/
  
 ```

Click here to open a link.

## Running the tests

The application is debugging while it is running.


### Break down into end to end tests

We are writing our city index.html'de and show the temperature values of our city.


## Built With

* [Flask](http://flask.pocoo.org/) - The web api microframework used
* [HTML](https://www.w3schools.com/html/) - Interface used
* [PYTHON](https://www.python.org/) - Web service used


