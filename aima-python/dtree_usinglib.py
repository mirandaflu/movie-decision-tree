from learning import *

learner = DecisionTreeLearner()

movies = DataSet(name='movies_formatted', #for display, csv file matches
                 target='like_movie', #attr trying to predict
                 
                 #list of attributes to predict on
                 attrnames="like_movie like_director like_actors dislike_actors series_seen_previous trailer positive_rating recommended access remake_seen_original blank1 blank2 subscribe_online blank3 blank4 theater_close like_theater blank5 blank6 with_whom blank7 blank8 cost opening_weekend")

learner.train(movies)

verbose = 2 # 0=none, 1=only negative outcomes, 2=all

test(learner, movies, None, verbose)

print 'done'
