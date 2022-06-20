
def ActionG(state):
    totalSteps = 0
    goal = '724560831'

    if state == goal:
        return [state,0,[]]

    final = []

    path = [state]

    # openStates is only the list of states that are in the open list 
    openStates = []

    # openStates is only the list of states that are in the open list 
    closedStates = []
    #start the open States with state
    openStates.append(state)

    #   state, steps, path taken, total cost 
    info = [state, 0, path, 0.0]
    # lists of lists seperated by the diff cost values 
    open = [ []  ,  []   ,  []   ]
    open[0].append(info)
    # print(open)
    #goes through all open states that are left
    while len(open[0]) >0 or len(open[1]) > 0 or len(open[2]) > 0:
        if len(open[0]) >= 1:
            
            node = open[0].pop(0)
            openStates.remove(node[0])
            closedStates.append(node[0])
            # print(node[0])
            # node = open[0].pop(0)

        elif len(open[1]) >= 1:
            node = open[1].pop(0)
            openStates.remove(node[0])
            closedStates.append(node[0])
            # node = open[1].pop(0)

        else:
            node = open[2].pop(0)
            openStates.remove(node[0])
            closedStates.append(node[0])
            # node = open[2].pop(0)
        # print(node[0])
        #now go through the children and see if it is goal or add to open
        # current = node
        # print(node[0])
        if (node[0].index('0') >2):# can go up for child
            #set up values for child

            steps = node[1] + 1
            cost = 1.0

            
            childState = []
            zeroLoc = state.index('0')
            movedNumLoc = state.index(state[state.index('0') -3])

            if movedNumLoc < zeroLoc: # return the outcome of move using current state as a reference of each section of new state
                childState = state[:movedNumLoc] + state[zeroLoc] +state[movedNumLoc+1 : zeroLoc] + state[movedNumLoc] + state[zeroLoc+1:]
            
            if movedNumLoc > zeroLoc:# return the outcome of move using current state as a reference of each section of new state
                childState = state[:zeroLoc] + state[movedNumLoc] +state[zeroLoc+1 : movedNumLoc] + state[zeroLoc] + state[movedNumLoc+1:]


            if childState not in closedStates and childState not in openStates:
                print()
                totalSteps = totalSteps+1
                travel = []
                # gets path so far from past node
                for i in range( len(node[2])):
                    # print(node[2][i])
                    travel.append(node[2][i])
                travel.append(childState)   
                # print(child[0])
                #create new node for open
                newNode = [childState, node[1]+1, travel, node[3] + cost]
                # check to see if the child is our lucky winner
                if childState == goal:
                    print(childState)
                    print("^it")
                    print("total Steps " + str(totalSteps))
                    return newNode #add path
                else:
                    print(childState)
                    print("^ not it")
                    # add past states to path
                    openStates.append(newNode[0])
                    open[1].append(newNode)






        if (state.index('0') < 6): #can go down for child
            steps = node[1] + 1
            cost = 1.0

            
            childState = []
            zeroLoc = state.index('0')
            movedNumLoc = state.index(state[state.index('0') +3])

            if movedNumLoc < zeroLoc: # return the outcome of move using current state as a reference of each section of new state
                childState = state[:movedNumLoc] + state[zeroLoc] +state[movedNumLoc+1 : zeroLoc] + state[movedNumLoc] + state[zeroLoc+1:]
            
            if movedNumLoc > zeroLoc:# return the outcome of move using current state as a reference of each section of new state
                childState = state[:zeroLoc] + state[movedNumLoc] +state[zeroLoc+1 : movedNumLoc] + state[zeroLoc] + state[movedNumLoc+1:]


            if childState not in closedStates and childState not in openStates:
                print()
                totalSteps = totalSteps+1
                travel = []
                # gets path so far from past node
                for i in range( len(node[2])):
                    # print(node[2][i])
                    travel.append(node[2][i])
                travel.append(childState)   
                # print(child[0])
                #create new node for open
                newNode = [childState, node[1]+1, travel, node[3] + cost]
                # check to see if the child is our lucky winner
                if childState == goal:
                    print("total Steps " + str(totalSteps))
                    print(childState)
                    print("^it")
                    return newNode #add path
                else:
                    # add past states to path
                    print(childState)
                    print("^ not it")
                    openStates.append(newNode[0])
                    open[1].append(newNode)





        if ((state.index('0') != 0) and state.index('0') != 3 and state.index('0') != 6): #left action to get movement number
            steps = node[1] + 1
            cost = 2.0

            
            childState = []
            zeroLoc = state.index('0')
            movedNumLoc = state.index(state[state.index('0') -1])

            if movedNumLoc < zeroLoc: # return the outcome of move using current state as a reference of each section of new state
                childState = state[:movedNumLoc] + state[zeroLoc] +state[movedNumLoc+1 : zeroLoc] + state[movedNumLoc] + state[zeroLoc+1:]
            
            if movedNumLoc > zeroLoc:# return the outcome of move using current state as a reference of each section of new state
                childState = state[:zeroLoc] + state[movedNumLoc] +state[zeroLoc+1 : movedNumLoc] + state[zeroLoc] + state[movedNumLoc+1:]


            if childState not in closedStates and childState not in openStates:
                print()
                totalSteps = totalSteps+1
                travel = []
                # gets path so far from past node
                for i in range( len(node[2])):
                    # print(node[2][i])
                    travel.append(node[2][i])
                travel.append(childState)   
                # print(child[0])
                #create new node for open
                newNode = [childState, node[1]+1, travel, node[3] + cost]
                # check to see if the child is our lucky winner
                if childState == goal:
                    print(childState)
                    print("^it")
                    print("total Steps " + str(totalSteps))
                    return newNode #add path
                else:
                    # add past states to path
                    print(childState)
                    print("^ not it")
                    openStates.append(newNode[0])
                    open[2].append(newNode)


        if (state.index('0') != 2 and state.index('0') != 5 and state.index('0') != 8): #can go right for child
            steps = node[1] + 1
            cost = 0.5

            
            childState = []
            zeroLoc = state.index('0')
            movedNumLoc = state.index(state[state.index('0') +1])

            if movedNumLoc < zeroLoc: # return the outcome of move using current state as a reference of each section of new state
                childState = state[:movedNumLoc] + state[zeroLoc] +state[movedNumLoc+1 : zeroLoc] + state[movedNumLoc] + state[zeroLoc+1:]
            
            if movedNumLoc > zeroLoc:# return the outcome of move using current state as a reference of each section of new state
                childState = state[:zeroLoc] + state[movedNumLoc] +state[zeroLoc+1 : movedNumLoc] + state[zeroLoc] + state[movedNumLoc+1:]

            # print(closedStates)
            # print(openStates)
            if childState not in closedStates and childState not in openStates:
                totalSteps = totalSteps+1
                travel = []
                # gets path so far from past node
                for i in range( len(node[2])):
                    # print(node[2][i])
                    travel.append(node[2][i])
                travel.append(childState)   
                # print(child[0])
                #create new node for open
                newNode = [childState, node[1]+1, travel, node[3] + cost]
                print(newNode[0])
                # print("last leg")
                # print(childState)
                # print("total Steps ")
                # check to see if the child is our lucky winner
                # print(childState)
                # print(goal)
                if childState[0] == goal:
                    # print("total Steps " + str(totalSteps))
                    final = newNode
                    print(childState)
                    print("^it")
                    return newNode #add path
                else:
                    print(childState)
                    print("^ not it")
                    # add past states to path
                    openStates.append(newNode[0])
                    open[0].append(newNode)






state = '724056831'
returns = ActionG(state)
print(returns)
