from learning import *

def printMenu_returnChoice(hasbeentrained):
    unavailable = ''
    if (hasbeentrained == False):
        unavailable = '  *'
    print ''
    print '1 train on file'
    print '2 train over all the data'
    print unavailable+'3 test on file'
    print unavailable+'4 test on typed input'
    print unavailable+'5 display tree'
    print '6 exit'
    if (hasbeentrained == False):
        print '  (* unavailable, train first)'
    print ''
    response = ''
    while (response.isdigit() == False) or (int(response) > 6) or (int(response) < 1) or (int(response) > 2 and int(response) < 6 and hasbeentrained == False):
        response = raw_input("What would you like to do?")
    return int(response)

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

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
        tree = learner.dt
        while str(tree) != tree:
            print tree.attrname+"?"
            print '  options:'
            i = trainingset.attrnames.index(tree.attrname)
            for val in trainingset.values[i]:
                print '    '+val
            ans = raw_input('choice: ')
            tree = tree.branches[ans]
        print tree

    elif c == 3:
        #test on file
        filename = raw_input("Which file?")
        testset = DataSet(name=filename, #for display, csv file matches
                         target='like_movie', #attr trying to predict
                         #list of attributes to predict on, matches columns in csv
                         attrnames="like_movie like_director like_actors dislike_actors series_seen_previous trailer positive_rating recommended access remake_seen_original subscribe_online theater_close like_theater with_whom cost opening_weekend")
        print test(learner, testset, None, 2)

    elif c == 2:
        #train over all the data
        import os
        if os.path.exists('../data/all_data.csv') == False:
            f = file('../data/all_data.csv','w')
            for survey in ['1A','1B','2A','2B','3A','3B','4A','4B','5A','6A','6B','7A','8A','9A','9B','10A','10B','11A','11B','12A','12B']:
                f2 = open('../data/movies'+survey+'.csv','r')
                lines = f2.readlines()
                for line in lines:
                    props = line.split(',')
                    for i in range(0,16):
                        props[i] = props[i].strip()

                    #categorize prices
                    if is_number(props[14]):
                        cost = float(props[14])
                        if cost < 1:
                            props[14] = 'free'
                        elif cost < 10:
                            props[14] = 'low'
                        elif cost < 20:
                            props[14] = 'medium'
                        elif cost < 50:
                            props[14] = 'high'

                    #categorize opening weekend
                    if props[15] != 'Y':
                        props[15] = 'N'
                    
                    line = ','.join(props[0:15]) + '\n'
                    f.write(line)
                f2.close()
            f.close()
        trainingset = DataSet(name='all_data', #for display, csv file matches
                              target='like_movie', #attr trying to predict
                             #list of attributes to predict on, matches columns in csv
                             attrnames="like_movie like_director like_actors dislike_actors series_seen_previous trailer positive_rating recommended access remake_seen_original subscribe_online theater_close like_theater with_whom cost opening_weekend")
        learner.train(trainingset)
        hasbeentrained = True
        print 'trained'
        

    elif c == 1:
        #train on file
        filename = raw_input("Which file?")
        trainingset = DataSet(name='movies'+filename, #for display, csv file matches
                         target='like_movie', #attr trying to predict
                         #list of attributes to predict on, matches columns in csv
                         attrnames="like_movie like_director like_actors dislike_actors series_seen_previous trailer positive_rating recommended access remake_seen_original subscribe_online theater_close like_theater with_whom cost opening_weekend")
        learner.train(trainingset)
        hasbeentrained = True
        print 'trained'

    raw_input("Press enter to continue...")
