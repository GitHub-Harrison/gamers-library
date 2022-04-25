# Gamers Library Testing
Return back to the [README.md](README.md)

The testing process has been broken into two sections; one from a users point of view which focuses on how they might interact on the site and the other from an admins point of view and how they might check the site is function as expected.

# Insert am-i-responsive screenshot

## User Focused Testing
This section consists of all testing done regarding the users features and how a user might interact on the site.

### User Story Testing
Testing user stories required me to take a user first approach to the website and think solely about what a user would want to be able to do while on the site. Below are the user stories I Testing for:

* Account Creation
* Viewing the Library
* Adding a Game
* Commenting
* Pagination

## Admin Focused Testing
This section focuses more on how an admin might interact with the site and what features they might use.

### Admin User Story Testing
Testing admin user stories required me to look at the site solely as an admin and to focus more on the admin page rather than the actual site. Below are the stories I tested for:

* Moderating the library
* Approving new games
* Approving/Removing comments

## Feature/Function Testing
I have manually tested this project by doing the following:
* Passed the code through different validators
* Testing all navigation and links work as intended
* Testing the user can submit a new game to be added
* Testing the user can create an account
* Testing the user can freely login/logout
* Testing the user can view the library
* Testing the pagination works correctly
* Testing the image carousel works correctly
* Testing each game has its own post detail page
* Testing the user can post comments on each games detail page
* Testing the admins can approve both games and comments

I also created a few tests within the project to help automate some of the process.
![Django Tests](documentation/testing/django-tests.png)

Below is a video from both the Admins and Users point of view.

## Final Testing Videos

### [Users Point of View]()
- insert screenshot with link to video

### [Admins Point of View]()
- insert screenshot with link to video

## Bugs
While coding my project I have come across a few issues/bugs which I believe all have been fixed. I took note of some of the bugs through the GitHub issue tab and have linked them below.

### Solved Bugs
- Insert link to each issue with description

### Remaining Bugs
* Currently there are no bugs that I am aware of.

## Validator Testing

* PEP8
    * The only errors shown by the PEP8 Validator were relating to line too long as shown:
    ![library Models](documentation/testing/library-models.png)
    ![addgame Forms](documentation/testing/addgame-forms.png)

    * The rest of the python files came back with no errors:
    ![addgame Views](documentation/testing/addgame-views.png)
    ![library Views](documentation/testing/library-views.png)
    ![library Forms](documentation/testing/library-forms.png)
    ![home Views](documentation/testing/home-views.png)

HTML - to be done on the live site / security issues on heroku read docs on other deployment
* CSS 
    * The CSS file passed the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/validator) with no errors:
        ![CSS Validator](documentation/testing/css-validator.png)

## Browser Compatibility