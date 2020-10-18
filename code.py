# --------------
from csv import reader
from numpy import array

def explore_data(dataset, start, end, rows_and_columns=False):
    """Explore the elements of a list.
    
    Print the elements of a list starting from the index 'start'(included) upto the index 'end'         (excluded).
    
    Keyword arguments:
    dataset -- list of which we want to see the elements
    start -- index of the first element we want to see, this is included
    end -- index of the stopping element, this is excluded 
    rows_and_columns -- this parameter is optional while calling the function. It takes binary          values, either True or False. If true, print the dimension of the list, else dont.
    """
    for data in dataset[start:end]:
        print(data,'\n')
    if rows_and_columns:
        listarray = array(dataset[start:end])
        print(listarray.shape)
    
        
     


def duplicate_and_unique_movies(dataset, index_):
    """Check the duplicate and unique entries.
    
    We have nested list. This function checks if the rows in the list is unique or duplicated based     on the element at index 'index_'.
    It prints the Number of duplicate entries, along with some examples of duplicated entry.
    
    Keyword arguments:
    dataset -- two dimensional list which we want to explore
    index_ -- column index at which the element in each row would be checked for duplicacy 
    
    """
    columnlist = [index_]
    newlist = [[each_list[i] for i in columnlist] for each_list in dataset]
        # intilize a null list 
    unique_list = [] 
    duplicate_list = []
    # traverse for all elements 
    for x in newlist: 
        # check if exists in unique_list or not 
        if x not in unique_list: 
            unique_list.append(x) 
        else:
            duplicate_list.append(x)
    # print list 
    # print ('number of unique records ',str(len(unique_list)))
    print ('number of duplicate records ',str(len(duplicate_list)))
    for x in duplicate_list: 
        print (x) 


def movies_lang(dataset, index_, lang_):
    """Extract the movies of a particular language.
    
    Of all the movies available in all languages, this function extracts all the movies in a            particular laguage.
    Once you ahve extracted the movies, call the explore_data() to print first few rows.

    Keyword arguments:
    dataset -- list containing the details of the movie
    index_ -- index which is to be compared for langauges
    lang_ -- desired language for which we want to filter out the movies
    
    Returns:
    movies_ -- list with details of the movies in selected language
    
    """
    movies_ = [x for x in dataset if x[index_] == lang_]
    return movies_
    



def rate_bucket(dataset, rate_low, rate_high):
    """Extract the movies within the specified ratings.
    
    This function extracts all the movies that has rating between rate_low and high_rate.
    Once you ahve extracted the movies, call the explore_data() to print first few rows.
    
    Keyword arguments:
    dataset -- list containing the details of the movie
    rate_low -- lower range of rating
    rate_high -- higher range of rating
    
    Returns:
    rated_movies -- list of the details of the movies with required ratings
    """
    rated_movies =[]
    for movie in dataset:
        if float(movie[11]) >= rate_low and float(movie[11]) <= rate_high:
            rated_movies.append(movie)
    return rated_movies




# Read the data file and store it as a list 'movies'
opened_file = open(path, encoding="utf8")
read_file = reader(opened_file)
movies = list(read_file)



# The first row is header. Extract and store it in 'movies_header'.
movies_header = movies.pop(0)

# Subset the movies dataset such that the header is removed from the list and store it back in movies




# Delete wrong data

# Explore the row #4553. You will see that as apart from the id, description, status and title, no other information is available.
# Hence drop this row.
movies.pop(4553)


# Using explore_data() with appropriate parameters, view the details of the first 5 movies.

explore_data(movies,0,5,True)


# Our dataset might have more than one entry for a movie. Call duplicate_and_unique_movies() with index of the name to check the same.
duplicate_and_unique_movies(movies,13)



# We saw that there are 3 movies for which the there are multiple entries. 
# Create a dictionary, 'reviews_max' that will have the name of the movie as key, and the maximum number of reviews as values.
columnlist = [13,12]
newlist = [[each_list[i] for i in columnlist] for each_list in movies]
def str_list_to_int_list(str_list):
    n = 0
    while n < len(str_list):
        str_list[n][1] = int(str_list[n][1])
        n += 1
    return(str_list)
newlist = str_list_to_int_list(newlist)
from operator import itemgetter
sorted_data = sorted(newlist, key=itemgetter(1), reverse = True)
test_keys = [[each_list[i] for i in [0]][0] for each_list in sorted_data]
test_values = [[each_list[i] for i in [1]][0] for each_list in sorted_data]
review_max = dict(zip(test_keys, test_values))

# Create a list 'movies_clean', which will filter out the duplicate movies and contain the rows with maximum number of reviews for duplicate movies, as stored in 'review_max'. 
movies_clean = []
for x in movies:
    if review_max[x[13]]== int(x[12]):
        movies_clean.append(x)
print(len(movies_clean))



# Calling movies_lang(), extract all the english movies and store it in movies_en.

movies_en = movies_lang(movies_clean, 3, 'en')


# Call the rate_bucket function to see the movies with rating higher than 8.
high_rated_movies = rate_bucket(movies_en, 8, 100)


