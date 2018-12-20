import sqlite3

with sqlite3.connect("database.db") as db:
	cursor=db.cursor()

cursor.execute('''
DROP TABLE IF EXISTS user;

	''')

cursor.execute('''
DROP TABLE IF EXISTS ratings;

	''')

cursor.execute('''
DROP TABLE IF EXISTS books;

	''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS user(
User_ID INTEGER  PRIMARY KEY , 
username VARCHAR(20) NOT NULL,
email VARCHAR(20) NOT NULL,
password VARCHAR(20) NOT NULL,
confirm VARCHAR(20) NOT NULL,
Age INT  DEFAULT 0,
Location VARCHAR(20) NOT NULL DEFAULT ' ',
Past_Purchase INT DEFAULT 0);
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS ratings(
User_ID INT NOT NULL ,
ISBN VARCHAR(20) NOT NULL ,
BOOK_RATING INT NOT NULL DEFAULT 0);
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS books(
ISBN VARCHAR(20) NOT NULL DEFAULT ' ' PRIMARY KEY,
BOOK_TITLE VARCHAR(20) DEFAULT NULL,
BOOK_AUTHOR VARCHAR(20) DEFAULT NULL,
YEAR_OF_PUBLICATION INT DEFAULT NULL,
PUBLISHER VARCHAR(20) DEFAULT NULL,
Image_URL_S varchar(255)  default NULL,
Image_URL_M varchar(255)  default NULL);
''')

cursor.execute('''

INSERT INTO user(username,email,password,confirm,Age,Location,Past_Purchase)
VALUES ("Swayam","sw@gmail.com","pal","pal",21,"Bhubaneshwar",10),
("Atul","xyz@gmail.com","singh","singh",21, "Noida",75),
--------------------------------------------------------------
 ("Nyc","nyc@gmail.com","nyc","nyc",NULL,"delhi",15),
 ("Stockton","stockton@gmail.com","stockton","stockton",18,"Noida",0),
 ("Moscow","moscow@gmail.com","moscow","moscow",NULL,"delhi",51),
 ("Porto","porto@gmail.com","porto","porto",17,"Bhubaneshwar",25),
 ("Farn","farnborough@gmail.com","farn","farn",NULL,"Bhubaneshwar",78),
 ("Santa","santamonica@gmail.com","santa","santa",61,"gaziabad",1),
 ("Washington","washing@gmail.com","washington","washington",NULL,"delhi",65),
 ("Timmins","timmins@gmail.com","timmins","timmins",NULL,"Noida",35),
 ("German","germantown@gmail.com","german","german",NULL,"Bhubaneshwar",20),
 ("Albace","albacete@gmail.com","albace","albace",26,"Noida",5),
 ("Melbourne","melbourne@gmail.com","melbourne","melbourne",14,"delhi",0),
 ("Fort","fort@gmail.com","fort","fort",NULL,"Bhubaneshwar",9),
 ("Barci","barcelona@gmail.com","barci","barci",26,"gaziabad",69),
 ("Polis","mediapolis@gmail.com","polis","polis",NULL,"gaziabad",49),
 ("Calgary","calgary@gmail.com","calgary","calgary",NULL,"Noida",10),
 ("Albu","albuquerque@gmail.com","albu","albu",NULL,"delhi",91),
 ("Chesa","chesapeake@gmail.com","chesa","chesa",NULL,"gaziabad",21),
 ("Rio","rio@gmail.com","rio","rio",25,"gaziabad",49);



	''')
cursor.execute('''
	INSERT INTO ratings(User_ID,ISBN,BOOK_RATING)
    VALUES (1 , '00001' ,8),
 ---------------------------------------------
 (1 , '00002' ,0),  
 (1 , '00003' ,0),
 (1 , '00004' ,0),
 (1 , '00005' ,0),
 (1 , '00006' ,0),
 (1 , '00007' ,0),
 (1 , '00008' ,0),
 (1 , '00009' ,0),
 (1 , '00010' ,0),
 (2 , '00001' ,0),
 (2 , '00002' ,7),
 (2 , '00003' ,0),
 (2 , '00004' ,0),
 (2 , '00005' ,0),
 (2 , '00006' ,0),
 (2 , '00007' ,0),
 (2 , '00008' ,0),
 (2 , '00009' ,0),
 (2 , '00010' ,0),
 (3 , '00001' ,0),
 (3 , '00002' ,9),
 (3 , '00003' ,0),
 (3 , '00004' ,0),
 (3 , '00005' ,0),
 (3 , '00006' ,0),
 (3 , '00007' ,0),
 (3 , '00008' ,0),
 (3 , '00009' ,0),
 (3 , '00010' ,0),
 (4 , '00001' ,0),
 (4 , '00002' ,0),
 (4 , '00003' ,0),
 (4 , '00004' ,10),
 (4 , '00005' ,0),
 (4 , '00006' ,0),
 (4 , '00007' ,0),
 (4 , '00008' ,0),
 (4 , '00009' ,0),
 (4 , '00010' ,0),
 (5 , '00001' ,0),
 (5 , '00002' ,0),
 (5 , '00003' ,6),
 (5 , '00004' ,0),
 (5 , '00005' ,0),
 (5 , '00006' ,0),
 (5 , '00007' ,0),
 (5 , '00008' ,0),
 (5 , '00009' ,0),
 (5 , '00010' ,3),
 (6 , '00001' ,0),
 (6 , '00002' ,0),
 (6 , '00003' ,0),
 (6 , '00004' ,0),
 (6 , '00005' ,4),
 (6 , '00006' ,0),
 (6 , '00007' ,0),
 (6 , '00008' ,0),
 (6 , '00009' ,0),
 (6 , '00010' ,7),
 (7 , '00001' ,0),
 (7 , '00002' ,0),
 (7 , '00003' ,0),
 (7 , '00004' ,0),
 (7 , '00005' ,0),
 (7 , '00006' ,0),
 (7 , '00007' ,0),
 (7 , '00008' ,0),
 (7 , '00009' ,5),
 (7 , '00010' ,0),
 (8 , '00001' ,0),
 (8 , '00002' ,0),
 (8 , '00003' ,0),
 (8 , '00004' ,0),
 (8 , '00005' ,0),
 (8 , '00006' ,0),
 (8 , '00007' ,0),
 (8 , '00008' ,8),
 (8 , '00009' ,0),
 (8 , '00010' ,0),
 (9 , '00001' ,6),
 (9 , '00002' ,0),
 (9 , '00003' ,0),
 (9 , '00004' ,0),
 (9 , '00005' ,0),
 (9 , '00006' ,0),
 (9 , '00007' ,0),
 (9 , '00008' ,0),
 (9 , '00009' ,0),
 (9 , '00010' ,6),
 (10 , '00001' ,0),
 (10 , '00002' ,0),
 (10 , '00003' ,7),
 (10 , '00004' ,0),
 (10 , '00005' ,0),
 (10 , '00006' ,0),
 (10 , '00007' ,0),
 (10 , '00008' ,0),
 (10 , '00009' ,0),
 (10 , '00010' ,0),
 (11 , '00001' ,0),
 (11 , '00002' ,0),
 (11 , '00003' ,9),
 (11 , '00004' ,0),
 (11 , '00005' ,0),
 (11 , '00006' ,0),
 (11 , '00007' ,0),
 (11 , '00008' ,0),
 (11 , '00009' ,0),
 (11 , '00010' ,0),
 (12 , '00001' ,8),
 (12 , '00002' ,0),
 (12 , '00003' ,0),
 (12 , '00004' ,0),
 (12 , '00005' ,0),
 (12 , '00006' ,0),
 (12 , '00007' ,0),
 (12 , '00008' ,0),
 (12 , '00009' ,0),
 (12 , '00010' ,0),
 (13 , '00001' ,0),
 (13 , '00002' ,0),
 (13 , '00003' ,0),
 (13 , '00004' ,0),
 (13 , '00005' ,0),
 (13 , '00006' ,0),
 (13 , '00007' ,0),
 (13 , '00008' ,3),
 (13 , '00009' ,0),
 (13 , '00010' ,0),
 (14 , '00001' ,0),
 (14 , '00002' ,0),
 (14 , '00003' ,0),
 (14 , '00004' ,0),
 (14 , '00005' ,0),
 (14 , '00006' ,0),
 (14 , '00007' ,0),
 (14 , '00008' ,0),
 (14 , '00009' ,8),
 (14 , '00010' ,0),
 (15 , '00001' ,0),
 (15 , '00002' ,0),
 (15 , '00003' ,0),
 (15 , '00004' ,0),
 (15 , '00005' ,0),
 (15 , '00006' ,0),
 (15 , '00007' ,0),
 (15 , '00008' ,0),
 (15 , '00009' ,9),
 (15 , '00010' ,0),
 (16 , '00001' ,0),
 (16 , '00002' ,0),
 (16 , '00003' ,1),
 (16 , '00004' ,0),
 (16 , '00005' ,0),
 (16 , '00006' ,0),
 (16 , '00007' ,0),
 (16 , '00008' ,0),
 (16 , '00009' ,0),
 (16 , '00010' ,0),
 (17 , '00001' ,0),
 (17 , '00002' ,5),
 (17 , '00003' ,0),
 (17 , '00004' ,0),
 (17 , '00005' ,0),
 (17 , '00006' ,0),
 (17 , '00007' ,0),
 (17 , '00008' ,0),
 (17 , '00009' ,0),
 (17 , '00010' ,0),
 (18 , '00001' ,0),
 (18 , '00002' ,0),
 (18 , '00003' ,0),
 (18 , '00004' ,0),
 (18 , '00005' ,1),
 (18 , '00006' ,0),
 (18 , '00007' ,0),
 (18 , '00008' ,0),
 (18 , '00009' ,0),
 (18 , '00010' ,0),
 (19 , '00001' ,0),
 (19 , '00002' ,0),
 (19 , '00003' ,0),
 (19 , '00004' ,0),
 (19 , '00005' ,0),
 (19 , '00006' ,0),
 (19 , '00007' ,0),
 (19 , '00008' ,9),
 (19 , '00009' ,0),
 (19 , '00010' ,0),
 (20 , '00001' ,0),
 (20 , '00002' ,0),
 (20 , '00003' ,0),
 (20 , '00004' ,0),
 (20 , '00005' ,0),
 (20 , '00006' ,0),
 (20 , '00007' ,0),
 (20 , '00008' ,0),
 (20 , '00009' ,9),
 (20 , '00010' ,0);
 ''')


cursor.execute('''
	INSERT INTO books(ISBN,BOOK_TITLE,BOOK_AUTHOR,YEAR_OF_PUBLICATION,PUBLISHER,Image_URL_S,Image_URL_M)
    VALUES 
 ('00001',"Classical Mythology",'Mark P. O. Morford',2002,'Oxford University Press','http://images.amazon.com/images/P/0195153448.01.THUMBZZZ.jpg','http://images.amazon.com/images/P/0195153448.01.MZZZZZZZ.jpg'),
 ('00002','Clara Callan','Richard Bruce Wright',2001,'HarperFlamingo Canada','http://images.amazon.com/images/P/0002005018.01.THUMBZZZ.jpg','http://images.amazon.com/images/P/0002005018.01.MZZZZZZZ.jpg'),
 ('00003','Timeline','MICHAEL CRICHTON',2000,'Ballantine Books','http://images.amazon.com/images/P/0345417623.01.THUMBZZZ.jpg','http://images.amazon.com/images/P/0345417623.01.MZZZZZZZ.jpg'),
 ('00004','Flu: The Story of the Great Influenza Pandemic of 1918 and the Search for the Virus That Caused It','Gina Bari Kolata',1999,'Farrar Straus Giroux','http://images.amazon.com/images/P/0374157065.01.THUMBZZZ.jpg','http://images.amazon.com/images/P/0374157065.01.MZZZZZZZ.jpg'),
 ('00005','The Mummies of Urumchi','E. J. W. Barber',1999,'W. W. Norton &amp; Company','http://images.amazon.com/images/P/0393045218.01.THUMBZZZ.jpg','http://images.amazon.com/images/P/0393045218.01.MZZZZZZZ.jpg'),
 ('00006','Icebound','Dean R. Koontz',2000,'Bantam Books','http://images.amazon.com/images/P/0553582909.01.THUMBZZZ.jpg','http://images.amazon.com/images/P/0553582909.01.MZZZZZZZ.jpg'),
 ('00007',"What If?: The World's Foremost Military Historians Imagine What Might Have Been",'Robert Cowley',2000,'Berkley Publishing Group','http://images.amazon.com/images/P/0425176428.01.THUMBZZZ.jpg','http://images.amazon.com/images/P/0425176428.01.MZZZZZZZ.jpg'),
 ('00008','PLEADING GUILTY','Scott Turow',1993,'Audioworks','http://images.amazon.com/images/P/0671870432.01.THUMBZZZ.jpg','http://images.amazon.com/images/P/0671870432.01.MZZZZZZZ.jpg'),
 ('00009','Harry Potter','J.K Rowling',1993,'Audioworks','http://images.amazon.com/images/P/0439136350.01.THUMBZZZ.jpg','http://images.amazon.com/images/P/0439136350.01.MZZZZZZZ.jpg'),
 ('00010','Harry Potter and the Goblet of Fire (Book 4)','J.K Rowling',2000,'Scholastic','http://images.amazon.com/images/P/0439139597.01.THUMBZZZ.jpg','http://images.amazon.com/images/P/0439139597.01.MZZZZZZZ.jpg');
 ''')



db.commit()

db.close()