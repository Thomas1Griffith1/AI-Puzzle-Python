#Thomas Griffith
import random



def recursionA(state,current,solutions):
    #this if statement checks to see if the state still has values in it for recursion
    if len(state) >= 1:  
        #this for loop selects each number left in state and adds it to the current list 
        #this loop uses recursion to place each number left into the next spot while
        # the rest of the numbers are cycled back into state excluding it until it is empty
        for i in range(len(state)):
            newstate = state[i+1:]+state[:i] #new state excluding position selected
            recursionA(newstate, current + state[i],solutions) # recursion to add to new current
    else: # this catches the end of the recursion and adds each current with no more states to list of outcomes
        # and returns the list of solutions
        solutions.append(current+state)
        return solutions
    return solutions

###################################################################
###################################################################
###################################################################
def ActionB(state,action):
    action = int(action)
    movement = 0
    outcome = ''
    not_Possible = False # check to see if move if valid

    if (action == 1) and (state.index('0') >2): #up action to get movement number
        movement = -3

    elif (action == 2) and (state.index('0') < 6): #down action to get movement number
        movement = 3

    elif (action == 3) and ((state.index('0') != 0) and state.index('0') != 3 and state.index('0') != 6): #left action to get movement number
        movement = -1

    elif (action == 4) and (state.index('0') != 2 and state.index('0') != 5 and state.index('0') != 8): #right action to get movement number
        movement = 1

    else:# move is invalid 
        not_Possible = True
    
    #get the location of the soon to be swapped numbers
    zeroLoc = state.index('0')
    movedNumLoc = state.index(state[state.index('0') + movement])

    # print invald move
    if not_Possible == True:
        print("out of place move from current location: " + state)
        outcome = state
    elif movedNumLoc < zeroLoc: # return the outcome of move using current state as a reference of each section of new state
        outcome = state[:movedNumLoc] + state[zeroLoc] +state[movedNumLoc+1 : zeroLoc] + state[movedNumLoc] + state[zeroLoc+1:]
    
    elif movedNumLoc > zeroLoc:# return the outcome of move using current state as a reference of each section of new state
        outcome = state[:zeroLoc] + state[movedNumLoc] +state[zeroLoc+1 : movedNumLoc] + state[zeroLoc] + state[movedNumLoc+1:]

    return outcome
###################################################################
###################################################################
###################################################################

def ActionC(state, step):
    print("state: " + state + "    action: initial state")
    row1 = int(state[0]) + int(state[1]) + int(state[2])
    row2 = int(state[3]) + int(state[4]) + int(state[5])
    row3 = int(state[6]) + int(state[7]) + int(state[8])

    while row1%3 != 0 or row2%3 != 0 or row3%3 != 0:


        action = random.randint(1,4)

        if (action == 1) and (state.index('0') >2):# move it up
            step = step +1
            zeroLoc = state.index('0')
            movedNumLoc = state.index(state[state.index('0') -3])

            if movedNumLoc < zeroLoc: # return the outcome of move using current state as a reference of each section of new state
                state = state[:movedNumLoc] + state[zeroLoc] +state[movedNumLoc+1 : zeroLoc] + state[movedNumLoc] + state[zeroLoc+1:]

            if movedNumLoc > zeroLoc:# return the outcome of move using current state as a reference of each section of new state
                state = state[:zeroLoc] + state[movedNumLoc] +state[zeroLoc+1 : movedNumLoc] + state[zeroLoc] + state[movedNumLoc+1:]
            print("state: " + state + "    action: up")

        if (action == 2) and (state.index('0') < 6): # move it down
            step = step +1
            zeroLoc = state.index('0')
            movedNumLoc = state.index(state[state.index('0') + 3])

            if movedNumLoc < zeroLoc: # return the outcome of move using current state as a reference of each section of new state
                state = state[:movedNumLoc] + state[zeroLoc] +state[movedNumLoc+1 : zeroLoc] + state[movedNumLoc] + state[zeroLoc+1:]

            if movedNumLoc > zeroLoc:# return the outcome of move using current state as a reference of each section of new state
                state = state[:zeroLoc] + state[movedNumLoc] +state[zeroLoc+1 : movedNumLoc] + state[zeroLoc] + state[movedNumLoc+1:]
            print("state: " + state + "    action: down")

        if (action == 3) and ((state.index('0') != 0) and state.index('0') != 3 and state.index('0') != 6): #move left
            step = step +1
            zeroLoc = state.index('0')
            movedNumLoc = state.index(state[state.index('0') -1])

            if movedNumLoc < zeroLoc: # return the outcome of move using current state as a reference of each section of new state
                state = state[:movedNumLoc] + state[zeroLoc] +state[movedNumLoc+1 : zeroLoc] + state[movedNumLoc] + state[zeroLoc+1:]

            if movedNumLoc > zeroLoc:# return the outcome of move using current state as a reference of each section of new state
                state = state[:zeroLoc] + state[movedNumLoc] +state[zeroLoc+1 : movedNumLoc] + state[zeroLoc] + state[movedNumLoc+1:]
            print("state: " + state + "    action: left")

        if (action == 4) and (state.index('0') != 2 and state.index('0') != 5 and state.index('0') != 8): # move right
            step = step +1
            zeroLoc = state.index('0')
            movedNumLoc = state.index(state[state.index('0') + 1])

            if movedNumLoc < zeroLoc: # return the outcome of move using current state as a reference of each section of new state
                state = state[:movedNumLoc] + state[zeroLoc] +state[movedNumLoc+1 : zeroLoc] + state[movedNumLoc] + state[zeroLoc+1:]

            if movedNumLoc > zeroLoc:# return the outcome of move using current state as a reference of each section of new state
                state = state[:zeroLoc] + state[movedNumLoc] +state[zeroLoc+1 : movedNumLoc] + state[zeroLoc] + state[movedNumLoc+1:]
            print("state: " + state + "    action: right")
        
        row1 = int(state[0]) + int(state[1]) + int(state[2])
        row2 = int(state[3]) + int(state[4]) + int(state[5])
        row3 = int(state[6]) + int(state[7]) + int(state[8])








###################################################################
###################################################################
###################################################################
def Action_Move(state, action, step):
    returns = []
    steps = 0
    act = ''
    not_Possible = False

    if (action == 1) and (state.index('0') >2): #up action to get movement number
        # print("move up")
        movement = -3
        steps = step + 1
        act = 'up'

    elif (action == 2) and (state.index('0') < 6): #down action to get movement number
        movement = 3
        # print("move down")
        steps = step + 1
        act = 'down'

    elif (action == 3) and ((state.index('0') != 0) and state.index('0') != 3 and state.index('0') != 6): #left action to get movement number
        movement = -1
        # print("move left")
        steps = step + 1
        act = 'left'

    elif (action == 4) and (state.index('0') != 2 and state.index('0') != 5 and state.index('0') != 8): #right action to get movement number
        movement = 1
        # print("move right")
        steps = step + 1
        act = 'right'
    

    else:# move is invalid 
        returns.append(state)
        returns.append(step)
        returns.append(act)
        return returns
    #get the location of the soon to be swapped numbers
    zeroLoc = state.index('0')
    movedNumLoc = state.index(state[state.index('0') + movement])


    if movedNumLoc < zeroLoc: # return the outcome of move using current state as a reference of each section of new state
        outcome = state[:movedNumLoc] + state[zeroLoc] +state[movedNumLoc+1 : zeroLoc] + state[movedNumLoc] + state[zeroLoc+1:]
    
    if movedNumLoc > zeroLoc:# return the outcome of move using current state as a reference of each section of new state
        outcome = state[:zeroLoc] + state[movedNumLoc] +state[zeroLoc+1 : movedNumLoc] + state[zeroLoc] + state[movedNumLoc+1:]
    returns.append(outcome)
    returns.append(steps)
    returns.append(act)
    return returns




def ActionD(state):
    totalSteps = 0
    open = []
    goal = '012345678'
    if state == goal:
        return [state,0,[]]
    # goal = '74506831'
    closed = []
    start = []
    path = [state]
    # step = 0
    openStates = []
    openStates.append(state)
    start = [state, 0, path] # add path
    open.append(start)
    #goes through all open states that are left
    while len(openStates) >= 1:
        #removes open state from open states as bfs but also in open as it is using that to follow along with my data structure
        node = open.pop(0)
        openStates.pop(0)
        
        closed.append(node[0])
        
        #goes through all the children it has
        for i in range(1,5):
            # child has [state , step ] get all childs
            child = Action_Move(node[0],i,node[1])
            
            # check to see if child state is not in the closed or open lists
            if child[0] not in closed and child[0] not in openStates:
                totalSteps = totalSteps+1
                travel = []
                # gets path so far from past node
                for i in range( len(node[2])):
                    # print(node[2][i])
                    travel.append(node[2][i])
                travel.append(child[0])   
                # print(child[0])
                #create new node for open
                newNode = [child[0], child[1], travel]
                # check to see if the child is our lucky winner
                if child[0] == goal:
                    print("total Steps " + str(totalSteps))
                    return newNode #add path
                else:
                    # add past states to path
                    openStates.append(newNode[0])
                    open.append(newNode)








###################################################################
###################################################################
###################################################################

def ActionE(state):
    totalSteps = 0
    open = []
    goal = '012345678'
    if state == goal:
        return [state,0,[]]
    # goal = '74506831'
    closed = []
    start = []
    path = [state]
    # step = 0
    openStates = []
    openStates.append(state)
    start = [state, 0, path] # add path
    open.append(start)
    #goes through all open states that are left
    while len(openStates) >= 1:
        #removes open state from open states as Dfs but also in open as it is using that to follow along with my data structure
        # pops from the back of the list first in last out
        node = open.pop(len(open)-1)
        openStates.pop(len(open)-1)
        
        closed.append(node[0])
        #goes through all the children it has
        for i in range(1,5):
            # child has [state , step ] get all childs
            child = Action_Move(node[0],i,node[1])
            
            # check to see if child state is not in the closed or open lists
            if child[0] not in closed and child[0] not in openStates:
                totalSteps = totalSteps+1
                travel = []
                # gets path so far from past node
                for i in range( len(node[2])):
                    # print(node[2][i])
                    travel.append(node[2][i])
                travel.append(child[0])   
                # print(child[0])
                #create new node for open
                newNode = [child[0], child[1], travel]
                # check to see if the child is our lucky winner
                if child[0] == goal:
                    print("total Steps " + str(totalSteps))
                    return newNode #add path
                else:
                    # add past states to path
                    openStates.append(newNode[0])
                    open.append(newNode)




###################################################################
###################################################################
###################################################################

def ActionF(state):
    totalSteps = 0
    open = []
    goal = '123804765'
    if state == goal:
        return [state,0,[]]
    # goal = '74506831'
    closed = []
    start = []
    path = [state]
    # step = 0
    openStates = []
    openStates.append(state)
    start = [state, 0, path] # add path
    open.append(start)
    #goes through all open states that are left
    while len(openStates) >= 1:
        #removes open state from open states as bfs but also in open as it is using that to follow along with my data structure
        node = open.pop(0)
        openStates.pop(0)
        
        closed.append(node[0])
        #goes through all the children it has
        for i in range(1,5):
            # child has [state , step ] get all childs
            child = Action_Move(node[0],i,node[1])
            
            # check to see if child state is not in the closed or open lists
            if child[0] not in closed and child[0] not in openStates:
                totalSteps = totalSteps+1
                travel = []
                # gets path so far from past node
                for i in range( len(node[2])):
                    # print(node[2][i])
                    travel.append(node[2][i])
                travel.append(child[0])   
                # print(child[0])
                #create new node for open
                newNode = [child[0], child[1], travel]
                # check to see if the child is our lucky winner
                if child[0] == goal:
                    print("total Steps " + str(totalSteps))
                    return newNode #add path
                else:
                    # add past states to path
                    openStates.append(newNode[0])
                    open.append(newNode)





###################################################################
###################################################################
###################################################################

def ActionG(state):
    totalSteps = 0
    goal = '123804765'

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



