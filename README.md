- This is demonstration of django restframework
- This is support login
- Serializing of One-to-Many and Many-to-Many relationship models
- Providing **JWT** Authentication for accessing internal API


# Installation
- Create a virtualenv `virtualenv env`
- Activate virtualenv `source env/bin/activate`
- Install requirements `pip install -r requirements.txt`


# Run Project
- `python manage.py runserver`

# End-Points
- URI: `/api/v1/login/`  *Guide: This will Create Token for further Requests*
- URI: `/api/v1/groups/`  *Guide: Return all the groups that below to the user*
- URI: `/api/v1/group/ID`  *Guide: Return all the photos belonging to the group*
- URI: `/api/v1/photos/ID` *Guide: Return details of the Photo*
