# Automated Software Defined Networking (ASDN) Platform

**Filip Nikolic**

### Initial Project Planning (01/10/17)

This is my first blog entry I wil briefly outline the progress I have made thus far:
  - Researched the areas the project will most affect (Computer Networking & Assisted Machine Learning)
  - Met with my potential project supervisor Mr. Brian Stone
  - Developed and submitted my Project Proposal Form
  - Carried out further research on scripting platforms such as Ansible and Puppet
  - Crated a simple System Design Diagram
![sytem-design](https://gitlab.computing.dcu.ie/nikolif2/2018-ca400-nikolif2/raw/master/docs/blog/images/system-design.png)

### Functional Specification Completion (15/10/17) 

I have completed most of my functional specification, with only some diagrams left to be done.
Furthermore these are some additional comments on my progress:
  - I have set up my virtual development environment, by depoyin a dell server running ESXi 6.5.
  - On it I have depolyed a Windows 2016 Server running Web Services.
  - Remote VPN access has been set up to the server over a Juniper Networks SRX300 Firewall. 
  - I have been regularly meting with my supervisor each week.
  - Currently I have migrated to using trello as a project planning and Scrum Development Platform.
![trello](https://gitlab.computing.dcu.ie/nikolif2/2018-ca400-nikolif2/raw/master/docs/blog/images/trello.png)


### Application UI Designed (31/10/17)

  - I have completed the design of the responsive Web-UI.  
  - The Functional Specification has been submitted.
  - I am meeting with my supervisor on a weekly basis. 
  - I deployed the Andular front-end platform to the web-server.
![sytem-design](https://gitlab.computing.dcu.ie/nikolif2/2018-ca400-nikolif2/raw/master/docs/blog/images/ui.png)
    
### Website Deployment (31/10/17)
  - I have deployed an Angular webite on the server.
  - The login and registration screens have been created.
  - The site-to-site VPN connection between Agile Networks and my local network have been built.
![vpn](https://gitlab.computing.dcu.ie/nikolif2/2018-ca400-nikolif2/raw/master/docs/blog/images/VPN.png)

### Website Development (20/11/17)
  - The website has been mostly developed.
  - It has been developed using Angular 4, Bootstrap and many other dependencies. 
  - As it is still in development, the compiled version of it has not been pushed to GitHub. 
![net](https://gitlab.computing.dcu.ie/nikolif2/2018-ca400-nikolif2/raw/master/docs/blog/images/build.png)

### Reconfiguring the test network (12/12/17)
  - I have had to reconfigure the VPN connection to the test network, as it would not allow some types of traffic through.
  - I have also expanded the lab to include devices from different networks. 
  - The automated VPN build script had to be changed to accomodate the above changes. 
![vpn](https://gitlab.computing.dcu.ie/nikolif2/2018-ca400-nikolif2/raw/master/docs/blog/images/net.jpg)

### Website Testing (30/01/18)
  - The website front-end is mostly complete.
  - I have deployed and used the sonarqube test server, and ran some code coverage and unit tests. 
  - Only the final version of website design has been pushed to Git. 
![sonar](https://gitlab.computing.dcu.ie/nikolif2/2018-ca400-nikolif2/raw/master/docs/blog/images/sonar.png)

### Core Application Development and Testing (08/02/18)
  - I have changed the platform architecture to run on Tomcat, using Maven as well as Swagger.
  - Integration between the database, front end and is done in Java (using Spring).
  - This process will allow for data to be passed between Angular and Spring (where they are turned into Java Classes).
![swagger](https://gitlab.computing.dcu.ie/nikolif2/2018-ca400-nikolif2/raw/master/docs/blog/images/swagger.png)

### Core dependency changes (20/03/18)
  - After extensive research, I have decided to change some of the core dependencies I am using to communicate with the network devices as well as to generate configuration files. Instead of developing my own solution for this problem, I have found a library called [Jinja2](http://jinja.pocoo.org/docs/2.10/), that can be integrated with Ansible. 
  - I have started doing unit tests on some of the complete modules used for generating the device hierarchy. 
  - On the server side, I have moved from a Windows Server 2016 VM to a Ubuntu Server VM. There are a number of reasons for the change, some include a much more lightweight and portable OS, increased default security parameters as well as being able to provide more services, such as being an POP3 or SMTP server. 
  - I have also registered a [domain name](https://asdn.ie) which is secured using an SSL certificate. 