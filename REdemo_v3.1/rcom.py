#Making necesarry imports
import pandas as pd
import matplotlib.pyplot as plt
import sklearn.metrics as metrics
import numpy as np
from sklearn.neighbors import NearestNeighbors
from scipy.spatial.distance import correlation
from sklearn.metrics.pairwise import pairwise_distances
from IPython.display import display, clear_output
from contextlib import contextmanager
import warnings
warnings.filterwarnings('ignore')
import numpy as np
import re
import os
import sys
import seaborn as sns
books = pd.read_csv('data/books.csv', sep=';', error_bad_lines=False, encoding="latin-1",dtype=object)
books.columns = ['ISBN', 'bookTitle', 'bookAuthor', 'yearOfPublication', 'publisher']
users = pd.read_csv('data/users.csv', sep=';', error_bad_lines=False, encoding="latin-1")
users.columns = ['userID', 'Location', 'Age']
ratings = pd.read_csv('data/ratings.csv', sep=';', error_bad_lines=False, encoding="latin-1",dtype=object)
ratings.columns = ['userID', 'ISBN', 'bookRating']

#checking shapes of the datasets
print(books.shape)
print(users.shape)
print(ratings.shape)
books.head()

pd.set_option('display.max_colwidth', -1)

#However, the value 0 is invalid and as this dataset was published in 2004, I have assumed the the years after 2006 to be 
#invalid keeping some margin in case dataset was updated thereafer
#setting invalid years as NaN
books.loc[(books.yearOfPublication.astype(np.int32) > 2006 )| (books.yearOfPublication.astype(np.int32) == 0),'yearOfPublication'] = np.NAN

#replacing NaNs with mean value of yearOfPublication
books.yearOfPublication.fillna(round(books.yearOfPublication.mean()), inplace=True)

#rechecking
books.yearOfPublication.isnull().sum()
#No NaNs

#resetting the dtype as int32
books.yearOfPublication = books.yearOfPublication.astype(np.int32)
print(books.dtypes)

#exploring 'publisher' column
books.loc[books.publisher.isnull(),:]
#two NaNs

print(users.shape)
users.head()


users.dtypes

#In my view values below 5 and above 90 do not make much sense for our book rating case...hence replacing these by NaNs
users.loc[(users.Age > 90) | (users.Age < 5), 'Age'] = np.nan

#replacing NaNs with mean
users.Age = users.Age.fillna(users.Age.mean())

#setting the data type as int
users.Age = users.Age.astype(np.int32)

#ratings dataset will have n_users*n_books entries if every user rated every item, this shows that the dataset is very sparse
n_users = users.shape[0]
n_books = books.shape[0]
print(n_users * n_books)


ratings.userID=ratings.userID.astype(np.int64)
ratings.bookRating=ratings.bookRating.astype(np.int64)
print(ratings.dtypes)
ratings.head(5)


#ratings dataset should have books only which exist in our books dataset, unless new books are added to books dataset
ratings_new = ratings[ratings.ISBN.isin(books.ISBN)]


#ratings dataset should have ratings from users which exist in users dataset, unless new users are added to users dataset
ratings = ratings[ratings.userID.isin(users.userID)]



print("number of users: " + str(n_users))
print("number of books: " + str(n_books))

#Sparsity of dataset in %
sparsity=1.0-len(ratings_new)/float(n_users*n_books)
print('The sparsity level of Book Crossing dataset is ' +  str(sparsity*100) + ' %')

#Hence segragating implicit and explict ratings datasets
ratings_explicit = ratings_new[ratings_new.bookRating != 0]
ratings_implicit = ratings_new[ratings_new.bookRating == 0]

#plotting count of bookRating
sns.countplot(data=ratings_explicit , x='bookRating')
#plt.show()
#It can be seen that higher ratings are more common amongst users and rating 8 has been rated highest number of times

#At this point , a simple popularity based recommendation system can be built based on count of user ratings for different books
def new_user_recommendation():
	    ratings_count = pd.DataFrame(ratings_explicit.groupby(['ISBN'])['bookRating'].sum())
	    top10 = ratings_count.sort_values('bookRating', ascending = False).head(3)
	    print("Following books are recommended")
	    top=top10.merge(books, left_index = True, right_on = 'ISBN')
	    return top

	#Given below are top 10 recommendations based on popularity. It is evident that books authored by J.K. Rowling are most popular


#Similarly segregating users who have given explicit ratings from 1-10 and those whose implicit behavior was tracked
users_exp_ratings = users[users.userID.isin(ratings_explicit.userID)]
users_imp_ratings = users[users.userID.isin(ratings_implicit.userID)]

#To cope up with computing power I have and to reduce the dataset size, I am considering users who have rated atleast 100 books
#and books which have atleast 100 ratings
counts1 = ratings_explicit['userID'].value_counts()
ratings_explicit = ratings_explicit[ratings_explicit['userID'].isin(counts1[counts1 >= 1].index)]
counts = ratings_explicit['bookRating'].value_counts()
ratings_explicit = ratings_explicit[ratings_explicit['bookRating'].isin(counts[counts >= 1].index)]


#Generating ratings matrix from explicit ratings table
ratings_matrix = ratings_explicit.pivot(index='userID', columns='ISBN', values='bookRating')
userID = ratings_matrix.index
ISBN = ratings_matrix.columns
print(ratings_matrix.shape)
ratings_matrix.head()
#Notice that most of the values are NaN (undefined) implying absence of ratings

n_users = ratings_matrix.shape[0] #considering only those users who gave explicit ratings
n_books = ratings_matrix.shape[1]
print(n_users, n_books)


#since NaNs cannot be handled by training algorithms, replacing these by 0, which indicates absence of ratings
#setting data type
ratings_matrix.fillna(0, inplace = True)
ratings_matrix = ratings_matrix.astype(np.int32)


#rechecking the sparsity
sparsity=1.0-len(ratings_explicit)/float(users_exp_ratings.shape[0]*n_books)
print('The sparsity level of Book Crossing dataset is ' +  str(sparsity*100) + ' %')



	#setting global variables
global metric,k
k=3
metric='cosine'

#This function finds k similar users given the user_id and ratings matrix 
#These similarities are same as obtained via using pairwise_distances
def findksimilarusers(user_id, ratings, metric = metric, k=k):
    similarities=[]
    indices=[]
    model_knn = NearestNeighbors(metric = metric, algorithm = 'brute') 
    model_knn.fit(ratings)
    loc = ratings.index.get_loc(user_id)
    distances, indices = model_knn.kneighbors(ratings.iloc[loc, :].values.reshape(1, -1), n_neighbors = k+1)
    similarities = 1-distances.flatten()
            
    return similarities,indices


#This function predicts rating for specified user-item combination based on user-based approach
def predict_userbased(user_id, item_id, ratings, metric = metric, k=k):
	prediction=0
	user_loc = ratings.index.get_loc(user_id)
	item_loc = ratings.columns.get_loc(item_id)
	similarities, indices=findksimilarusers(user_id, ratings,metric, k) #similar users based on cosine similarity
	mean_rating = ratings.iloc[user_loc,:].mean() #to adjust for zero based indexing
	sum_wt = np.sum(similarities)-1
	product=1
	wtd_sum = 0 
	
	for i in range(0, len(indices.flatten())):
	    if indices.flatten()[i] == user_loc:
	        continue;
	    else: 
	        ratings_diff = ratings.iloc[indices.flatten()[i],item_loc]-np.mean(ratings.iloc[indices.flatten()[i],:])
	        product = ratings_diff * (similarities[i])
	        wtd_sum = wtd_sum + product
	
	#in case of very sparse datasets, using correlation metric for collaborative based approach may give negative ratings
	#which are handled here as below
	if sum_wt==0.0:
		sum_wt=0.1
	
	prediction = int(round(mean_rating + (wtd_sum/sum_wt)))
	if prediction <= 0:
	    prediction = 1   
	elif prediction >10:
	    prediction = 10
	
	print('\nPredicted rating for user {0} -> item {1}: {2}'.format(user_id,item_id,prediction))
	return prediction


print(books.dtypes)
print()
print(ratings.dtypes)
print()
print(users.dtypes)

def predicting_user_based_rating(uid,iid):
	return predict_userbased(uid,iid,ratings_matrix);
uid=5
iid='00003'
predicting_user_based_rating(uid,iid)

	


#This function finds k similar items given the item_id and ratings matrix

def findksimilaritems(item_id, ratings, metric=metric, k=k):
    similarities=[]
    indices=[]
    ratings=ratings.T
    loc = ratings.index.get_loc(item_id)
    model_knn = NearestNeighbors(metric = metric, algorithm = 'brute')
    model_knn.fit(ratings)
    
    distances, indices = model_knn.kneighbors(ratings.iloc[loc, :].values.reshape(1, -1), n_neighbors = k+1)
    similarities = 1-distances.flatten()
    return similarities,indices



#This function predicts the rating for specified user-item combination based on item-based approach
def predict_itembased(user_id, item_id, ratings, metric = metric, k=k):
    prediction= wtd_sum =0
    user_loc = ratings.index.get_loc(user_id)
    item_loc = ratings.columns.get_loc(item_id)
    similarities, indices=findksimilaritems(item_id, ratings) #similar users based on correlation coefficients
    sum_wt = np.sum(similarities)-1
    product=1
    for i in range(0, len(indices.flatten())):
        if indices.flatten()[i] == item_loc:
            continue;
        else:
            product = ratings.iloc[user_loc,indices.flatten()[i]] * (similarities[i])
            wtd_sum = wtd_sum + product  
    if sum_wt==0.0 :
        sum_wt=0.1
#     print(wtd_sum,sum_wt," ",wtd_sum/sum_wt," ",int(round(wtd_sum/sum_wt)))
    prediction = int(round(wtd_sum/sum_wt))
    
    #in case of very sparse datasets, using correlation metric for collaborative based approach may give negative ratings
    #which are handled here as below //code has been validated without the code snippet below, below snippet is to avoid negative
    #predictions which might arise in case of very sparse datasets when using correlation metric
    if prediction <= 0:
        prediction = 1   
    elif prediction >10:
        prediction = 10

    print('\nPredicted rating for user {0} -> item {1}: {2}'.format(user_id,item_id,prediction) )     
    
    return prediction

def predicting_item_based_rating(uid,iid):
    return predict_itembased(uid,iid,ratings_matrix);
uid=5
iid='00003'
predicting_item_based_rating(uid,iid)


@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:  
            yield
        finally:
            sys.stdout = old_stdout




#This function utilizes above functions to recommend items for item/user based approach and cosine/correlation. 
#Recommendations are made if the predicted rating for an item is >= to 6,and the items have not been rated already
def recommendItem2(user_id, ratings, metric=metric,recommendtype=1):    
    if (user_id not in ratings.index.values) or type(user_id) is not int:
        print("User id should be a valid integer from this list :")
    else:    
#                     ids = ['Item-based (correlation)','Item-based (cosine)','User-based (correlation)','User-based (cosine)']
#                     select = widgets.Dropdown(options=ids, value=ids[0],description='Select approach', width='1000px')
                    
                    clear_output(wait=True)
                    prediction = []                                  
                    metric = 'cosine'   
                    with suppress_stdout():
                        if(recommendtype==1):    
                        #if (select.value == 'Item-based (correlation)') | (select.value == 'Item-based (cosine)'):
                            for i in range(ratings.shape[1]):
                                if (ratings[str(ratings.columns[i])][user_id] !=0): #not rated already
                                    prediction.append(predict_itembased(user_id, str(ratings.columns[i]) ,ratings, metric))
                                else:                    
                                    prediction.append(-1) #for already rated items
                        else:
                            for i in range(ratings.shape[1]):
                                if (ratings[str(ratings.columns[i])][user_id] !=0): #not rated already
                                    prediction.append(predict_userbased(user_id, str(ratings.columns[i]) ,ratings, metric))
                                else:                    
                                    prediction.append(-1) #for already rated items
                    prediction = pd.Series(prediction)
                    prediction = prediction.sort_values(ascending=False)
                    recommended = prediction[:3]
#                     print("---------------------------------------------Hello------------------------------" )
                    print("As per  approach....Following books are recommended...")
#                     print(recommended,recommended.dtypes)
#                     print("---------------------------------------------Hello------------------------------" )
#                     print(recommended.index[1],"len-",len(recommended))
#                     print("---------------------------------------------Hello------------------------------" )
#                     print("As per {0} approach....Following books are recommended...")
                    recomend=''
#                     print(books.bookTitle[recommended.index[1]].dtypes)
                    for i in range(len(recommended)):
#                          print("{0}. {1}".format(i+1,books.bookTitle[recommended.index[i]].encode('utf-8')))
                         recomend=recomend+books.bookTitle[recommended.index[i]]+' , '
                         #recomend=recomend.append(recommended.index[i])
                    return recomend
	                

def duplicate(words1,words2):
    words=[]
    for i in range(len(words1)):
        chk=1
        for j in range(len(words2)):
            if(words1[i]==words2[j]):
                del words2[j]
                chk=0
                break;
#         if(chk==1):
        words.append(words1[i])
    for j in range(len(words2)):
        words.append(words2[j])
#     print(words)
    return words

def new_user_recom():
    top=new_user_recommendation()
    top=top['ISBN']
    top=top.values
    return top


def recom(userid):
    recomend=[]
    recomend.append(recommendItem2(userid, ratings_matrix))
    
    recomend.append(recommendItem2(userid, ratings_matrix,2))
#     recomend=pd.DataFrame(recomend)
#     recomend.astype(int64)
#     recomend=recomend.unique()
#     print(recomend.shape)
#     rec=tostring(recomend)
    words1=recomend[0].split(",")
    words2=recomend[1].split(",")
#     if (words1[0]==words2[0]):
#         print("yes",len(words1)," ",len(words2))
    words=duplicate(words1,words2)
    #str1=''.join(str(e) for e in words)
    
    return words
	    
#=========================================================================================
userID=5
# userID=21
str1=[]
str2=[]
chk=1
recomendi=''
if (userID not in ratings.userID.values) or type(userID) is not int:
    str12=new_user_recom()
    str12=str12.astype(int)
    chk=0
    for i in range(len(str12)):
        print(books.bookTitle[str12[i]])
        recomendi=recomendi+books.bookTitle[str12[i]]+','
    words1=recomendi.split(",")
    str1=words1
    print(words1)
    
else:
    
    str1=recom(userID)