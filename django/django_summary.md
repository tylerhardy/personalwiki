# Django 18 Summary
- Build web applications using the Django framework.
  - Write a brief project spec.
    - A full spec details the project goals, describes the project's functionality, and discusses its appearance and user interface.
    - A spec should keep you focused and help keep your project on track.
      - State the project name and what it will do.
      - Go into brief detail of what the app will do.
  - Setup a virtual environment 
  - Install and setup Django.
  - Verify that the project was set up correctly.
  - Create and setup an app.
  - Define models to represent the data for your app.
    - Migrate the app database after changes to models.
  - Create superuser for the admin site.
  - Use admin site to setup initial data.
- Use the Django shell to work with the project's data in a terminal session.
- Define URLs, create view functions, write templates to make pages for the site.
  - Use template inheritance to simplify the structure of individual templates.
  - Use templates to easily modify the site as the project evolves.

# Django 19 Summary
- In this chapter you learned to use forms to allow users to add new topics and entries, and edit existing entries. 
  - You then learned how to implement user accounts. 
  - You allowed existing users to log in and out, and you learned how to use Django’s default UserCreationForm to let people create new ccounts.
- After building a simple user authentication and registration system, you restricted access to logged-in users for certain pages using the @login_required decorator. 
  - You then attributed data to specific users through a foreign key relationship.
  - You also learned to migrate the database when the migration requires you to specify some default data.
- Finally, you learned how to make sure a user can see only data that belongs to them by modifying the view functions.
  - You retrieved appropriate data using the filter() method, and you learned to compare the owner of the requested data to the currently logged-in user.
- It may not always be immediately obvious what data you should make available and what data you should protect, but this skill will come with practice.
  - The decisions we’ve made in this chapter to secure our users’ data illustrate why working with others is a good idea when building a project: 
    - having someone else look over your project makes it more likely that you’ll spot vulnerable areas.
- We now have a fully functioning project running on our local machine.
- In the final chapter we’ll style Learning Log to make it visually appealing, and we’ll deploy the project to a server so anyone with Internet access can register and make an account.

# Django 20 Summary
