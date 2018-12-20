# Premier Experience for Loyal eCommerce Customers
## dell_hackathon_iiitb_2018_aksit

### About
- This project is a simple illustration of a Recommendation System to enhance the Premier Experience of Loyal eCommerce Customers
- For simplicity we have worked only on books rating dataset
- Soul intention of this project was to develop __*Recommendation System*__ and not the Front End

### Layout
- Identify the user as guest or existing user
- If new user, promote for signup
- For new users recommendations are based on popularity index i.e. He/She will be recommended most popular items
- For existing users recommendations are based on **Item-Based & User-Based Collabrative Filtering** 
- **Item-Based Collabrative Filtering** is recommending items baased on *Item Similarity Index* i.e. items which user has purchased or                                             liked in past.
- **User-Based Collabrative Filtering** is recommending items based on *User Similarity Index* i.e. items which other customers similar to                                         user likes.

### Tools & Libraries Required
- Flask
- SQLAlchemy
- Sqlite3
- Pandas
- Matplotlib
- Sklearn
- KNN
### How to run
- Run __*save.py*__ and copy paste the URL in your browser.
- __*data.py*__ contains the SQL commands to generate the database.
- __*recommendation_engine.py*__ contains the Recommendation Engine.
