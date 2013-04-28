from learning import *

def printMenu_returnChoice(hasbeentrained):
    unavailable = ''
    if (hasbeentrained == False):
        unavailable = '  *'
    print ''
    print '1 train on file'
    print '2 train as an average of all the data'
    print unavailable+'3 test on file'
    print unavailable+'4 test on typed input'
    print unavailable+'5 display tree'
    print '6 exit'
    print ''
    if (hasbeentrained == False):
        print '  (* unavailable, train first)'
    response = ''
    while (response.isdigit() == False) or (int(response) > 6) or (int(response) < 1) or (int(response) > 2 and int(response) < 6 and hasbeentrained == False):
        response = raw_input("What would you like to do?")
    return int(response)

learner = DecisionTreeLearner()
hasbeentrained = False
verbose = 1 # 0=none, 1=only negative outcomes, 2=all

while 1:
    c = printMenu_returnChoice(hasbeentrained)

    if c == 6:
        #exit
        break

    elif c == 5:
        #display tree
        if (str(learner.dt) == learner.dt):
            print 'always answers '+learner.dt
        else:
            learner.dt.display()

    elif c == 4:
        #test on typed input
        #not implemented yet
        break

    elif c == 3:
        #test on file
        filename = raw_input("Which file?")
        testset = DataSet(name=filename, #for display, csv file matches
                         target='like_movie', #attr trying to predict
                         #list of attributes to predict on, matches columns in csv
                         attrnames="like_movie like_director like_actors dislike_actors series_seen_previous trailer positive_rating recommended access remake_seen_original subscribe_online theater_close like_theater with_whom cost opening_weekend")
        print 'accuracy: '
        print test(learner, testset, None, 2)

    elif c == 2:
        #train as average of all the data
        #not implemented yet
        break

    elif c == 1:
        #train on file
        filename = raw_input("Which file?")
        trainingset = DataSet(name='movies'+filename, #for display, csv file matches
                         target='like_movie', #attr trying to predict
                         #list of attributes to predict on, matches columns in csv
                         attrnames="like_movie like_director like_actors dislike_actors series_seen_previous trailer positive_rating recommended access remake_seen_original subscribe_online theater_close like_theater with_whom cost opening_weekend")
        learner.train(trainingset)
        hasbeentrained = True
