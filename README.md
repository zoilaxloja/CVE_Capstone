# CVE_Capstone
- This is my CVE_Capstone GitHub repository where all the project files can be found: https://github.com/zoilaxloja/CVE_Capstone 

- To get the NVD CVE data, the user can download a zip from https://github.com/CVEProject/cvelistV5 or manually clone the repository. 
      •	To download, the user will need to click the green “<> Code” button and select the download zip option.
      •	I recommend to manually clone it. To do this, follow the steps below to see how this step will look like:
            1.	git clone https://github.com/CVEProject/cvelistV5
            2.	cd cvelistV5 

-	To always have the CVE database list maintain updated with the latest CVE’s and new changes, download the repo_update bash script from the CVE_Capstone Github. Below are the steps on how to make this code an executable, so the user can enter one command and it will automatically update. 
        1.	Go to the directory where the bash script is located ex: cd Desktop
        2.	Make the bash script an executable with chmod +x repo_update.sh
        3.	Run the script with ./repo_update.sh. This is the command the user will need to run evertime to get the latest CVE updates.   
 

- For the backend, app.py, the user will need to install flask to the their environment. Below are two command options the user can take to accomplish this:
     •	User can directly download it through the command:
        	 pip install flask 
    •	Sometimes depending on your system, this won’t work and the user will get “ModuleNotFoundError: No module named flask.” In that case, I recommend       creating a virtual environment and installing Flask within it. Follow the steps below to fix this issue and get Flask up and running on the       
       system:
            1.	pip install virtualenv
            2.	virtualenv venv
            3.	venv\Scripts\activate (on windows) or source venv/bin/activate (on MacOs/Linux)
            4.	pip install flask

- For the frontend, the user will need to create a templates folder and input the index.html file inside the folder “templates”. 
