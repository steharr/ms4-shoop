# **[Shoop](https://ms4-shoop.herokuapp.com/)**
<img src="docs/mockup/mockup-shoop.png" alt="mockup of the shoop website" width="500"/> 

Shoop is a fictional online eCommerce website for shoes where users can buy and review a variety of different shoe types

This project was completed for my **Code Institute Milestone 4 Project**. The site is built using **HTML, CSS, Bootstrap & Javascript** for the front end and **Python, Django, Postgres and AWS S3** for the back end. It is deployed on **Heroku** at the following location: **https://ms4-shoop.herokuapp.com/**

## **UX**
The **five planes of user experience design** developed by Jesse James Garrett was used as the conceptual framework for the development process of this site

### **Strategy Plane**

The overall objective of Shoop is to be a easy-to-use eCommerce website that offers a wide variety of trendy designer shoes for site viewers. A unique feature of Shoop that sets it apart from other shoe sellers is its review functionality. Users can write reviews and give ratings on shoes that they have bought. Review data is visible on the site for all viewers to see and allows them to make educated decisions on purchases. The site owners also occasionally will run flash sales to encourage users to buy. They therefore require these sales to be visible to the viewers on the site's landing page. With these objectives in mind, a list of user stories was created to facilitate the development of the site. 

### **User Stories**

#### Site Owners
1. As a site viewer, I want to browse products in the store
2. As a site viewer, I want to view specific products in the store
3. As a site viewer, I want to search for specific items by text
4. As a site viewer, I want to search for specific items by category
5. As a site viewer, I want to sort items in the store
6. As a site viewer, I want to add products to a cart in the store
7. As a site viewer, I want to purchase products in the cart
8. As a site viewer, I want to review items in the store
9. As a site viewer, I want to see other peoples reviews and what the overall score for an item is


#### Site Viewers
1. As I site owner, I want to edit specific products in the store
2. As I site owner, I want to add new products to the store
3. As I site owner, I want to update current products in the store
4. As I site owner, I want to delete current products in the store
5. As I site owner, I want to add sale banners to the store
6. As I site owner, I want to delete sale banners to the store
7. As I site owner, I want to update sale banners to the store

### **Scope Plane**
To plan out the scope of the site, a list of minimum viable product features were compiled to help with development. A second list of 'nice-to-have' features were compiled that would be worked on if 

<!-- **Group 1: Minimum Viable Product Features**  

**Group 2: Nice to Have Features**   -->


<!-- ### **Structure Plane** -->

<!-- ##### **Database Schema**  -->
<!-- diagram   -->

<!-- #### **Front End Design:**  -->
<!-- list of pages -->
 
<!-- #### **Front and Back End Relationship:** -->
<!-- site plan -->

<!-- #### **Final Key Design Decisions** -->


<!-- ### **Skeleton Plane** -->

<!-- ### **Surface Plane** -->

<!-- **Color Palette**   -->

<!-- **Font**   -->

<!-- ### **Features** -->

<!-- #### **Existing Features** -->

<!-- #### **Features Left to Implement** -->


<!-- ### **Technologies Used**
* [Visual Studio Code](https://code.visualstudio.com/)  
Code editor I used to write my code
* [HTML](https://en.wikipedia.org/wiki/HTML5)  
For markup
* [CSS](https://en.wikipedia.org/wiki/CSS)  
For styling the site
* [Bootstrap](https://getbootstrap.com/)  
Framework used to create and style components on the front end
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)  
For programming certain dynamic elements in the review section of the site
* [Python](https://www.python.org/)  
For programming the back end of the site
* [Flask](https://flask.palletsprojects.com/en/2.0.x/)  
Used as a web framework for the site
* [MongoDB](https://www.mongodb.com/)  
The database for the site
* [Heroku](https://id.heroku.com/login)  
Platform where the site is deployed
* [DiceBear Avatars](https://avatars.dicebear.com/)  
An avatar library that provides the site avatars via a HTTP API
* [Font Awesome](https://fontawesome.com/)  
Used for icons throughout the site
* [Git](https://git-scm.com/)  
For version control
* [GitHub](https://github.com/)  
For storing my files and for hosting the site on Github Pages
* [Canva](https://www.canva.com/)  
I used a premium version of this tool to create the fake affiliate logo for the site
* [favicon-generator.org](https://www.favicon-generator.org/)  
Used to generate a favicon for the site
* [Balsamiq](https://balsamiq.com/)  
Used to create wireframes
* [dbdiagram](https://dbdiagram.io/home)  
Used to create the database schema diagram for this readme
* [Coolors](https://dbdiagram.io/home)  
Used to create the color palette of the site -->

***

<!-- ### **Testing**
Please see **** for details on the testing carried out for this project -->


<!-- ### **Version Control**
* To begin the project, I created a remote repository on Github by choosing the **New Repository** button and following the on screen steps.
* I then created a local repository using Git:
   *  I created a directory on my computer called **MS3**
   *  I opened the directory using VS code and started a terminal
   *  I initialized the directory as a Git repository using the command `git init`
   *  I added a README to the file using the command `git add README.md`
   *  I then created an `app.py` file in the directory and started working on the site
   *  When I was ready to commit my first set of changes, I used the `git add .` and the `git commit -m "Initial commit"` commands in my terminal
   
* In order to store my commits remotely on Github, I linked my local repository to the remote repository:
   * In my VS code terminal, I used the command `git remote add origin https://github.com/steharr/ms2-holiday-review` and `git remote -v`

* Throughout the development process, I would regularly push my commits to Github using the `git push` command 

* For this project, there were some environment variables I needed to keep hidden so that they werent pushed publicly to Github. For example, the **MONGO_URI** that I was using to connect to my database and the **SECRET_KEY** needed for flashing messages in flask. For this I created an `env.py` which was stored on my local machine. All variables which needed to be hidden were stored in this file. I then added the file to a `.gitignore` file so that whenever I was committing files, the `env.py` file would never be included. In order to access these environment variables when the app was running on a development server on my computer, my code would import the `env.py` module. On the deployed app, these variables are stored and extracted from Heroku. Details of how this was setup are in the next section

* In order to help me better manage the dependencies of my project, I created a virtual environment in the **MS3** directory I was working from. I did this by using the python terminal command `python -m venv .venv`. In VSCode I then selected this virtual environment as my python interpreter. This enabled me to have a better overview of exactly what the dependencies were being used by my project since I already had multiple uneccessary modules installed on my computer. If I did not take this step, certain uneccessary modules may have been included in the `requirments.txt` file I created while deploying my website to Heroku. I then added this `.venv` environment that was created to my `.gitignore` file so that it wouldnt be commited to github.

### **Deployment**
This website is deployed on [Heroku](https://id.heroku.com/login). The steps taken to deploy the site are detailed below:

1. In order to prepare my website before it was deployed to Heroku, I first created a `requirements.txt` file using the pip command `pip freeze > requirements.txt` in a terminal in VSCode. This extracted all the dependencies of my project that were installed in my virtual environment into a .txt file which Heroku could use to build my project when it is being deployed.

2. I also created a `Procfile` which contained the instruction: `web: python app.py`. This instructs my applications dynos on Heroku to build a web server powered by python and use the `app.py` as the file which is to be run on this server.

3. Then in Heroku, I created a new app called **ms3-holiday-review** and selected Europe as the region.

4. I then connected my Heroku app to my previously created GitHub repository by choosing the **Connect to GitHub** option in the **Deploy** section of the Heroku dahsboard. I searched for my GitHub repo by name using the search box provided.  
<img src="documents/deployment/deployment-1.png" alt="linking heroku app to github repo" width="400"/> 

5. At this point I set up **config vars** in the **Settings** section of Heroku dahsboard. These are the environment variables that my code needs to work. As mentioned previously, on my local machine these are stored in `env.py` and never pushed to GitHub.  
<img src="documents/deployment/deployment-2.png" alt="setting up config vars in heroku" width="400"/> 

6. Once the app setup was complete, I set up **automatic deploys** for my app. I did this by choosing the **Enable Automatic Deploys** option in the **Deploy** section of the Heroku dashboard. This meant that anytime I pushed code to GitHub, Heroku would automatically build my app. It is also possible to manually deploy a branch in Heroku by using the **Manual deploy** options in the same section on the dashboard  
<img src="documents/deployment/deployment-3.png" alt="setting up automatic deploys in heroku" width="400"/> 

**NOTE:** *Normally for a deployed website, it is important that `debug` parameter for the `app.run` flask method is set to False. Since this was a study project, I kept it equal to True up until the point where I was submitting the project for assessment, where it was then changed to False* -->

<!-- ### **Credits** -->

<!-- #### **Code** -->

<!-- ### **Acknowledgments** -->
