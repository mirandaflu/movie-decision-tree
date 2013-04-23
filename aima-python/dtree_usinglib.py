from learning import *

learner = DecisionTreeLearner()

filename = ''

while 1:
    if filename != '':
        print '\n(type exit to exit)'
        
    filename = raw_input("which movie survey?")
    
    if filename == 'exit':
        break
    
    movies = DataSet(name='movies'+filename, #for display, csv file matches
                     target='like_movie', #attr trying to predict
                     
                     #list of attributes to predict on
                     attrnames="like_movie like_director like_actors dislike_actors series_seen_previous trailer positive_rating recommended access remake_seen_original subscribe_online theater_close like_theater with_whom cost opening_weekend")

    learner.train(movies)
    learner.dt.display()
	
    verbose = 1 # 0=none, 1=only negative outcomes, 2=all

    print 'accuracy: '
    print test(learner, movies, None, verbose)

    print 'done'

#2A gives list index out of range error
