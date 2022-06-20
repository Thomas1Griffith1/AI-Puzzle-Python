#rows divisable by 3!!
import random

# from testing import ActionC_Cube
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
    # path = [state]
    # step = 0
    openStates = []
    openStates.append(state)
    start = [state, 0,]# path] # add path
    open.append(start)
    #goes through all open states that are left
    while len(openStates) >= 1:
        #removes open state from open states as bfs but also in open as it is using that to follow along with my data structure
        node = open.pop(0)
        openStates.pop(0)
        # if node[1] > 362880:
        #     return node
        
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
                # for i in range( len(node[2])):
                #     # print(node[2][i])
                #     travel.append(node[2][i])
                # travel.append(child[0])   
                # print(child[0])
                #create new node for open
                newNode = [child[0], child[1],]# travel]
                # check to see if the child is our lucky winner
                if child[0] == goal:
                    print("total Steps " + str(totalSteps))
                    return newNode #add path
                else:
                    # add past states to path
                    openStates.append(newNode[0])
                    open.append(newNode)

    



def Action_Cube(state):
    cube = [
    ['1','2','3'],
    ['4','5','6'],
    ['7','8','9']
    ]
    cube[1][0] = '1'
    # test1 = '012'

    # print(state.index('0'))
    # print(cube)
    # add = 0
    for i in range(len(cube)):
        for col in range(len(cube)):
            if i == 0:
                cube[i][col] = state[col]
            if i == 1:
                cube[i][col] = state[col+3]
            if i == 2:
                cube[i][col] = state[col+6]
    return cube

state = '724506831'
step = 0
# test = ['0','1','3','4']
# if '5' not in test:
#     print("yes")
result = ActionD(state)
print("done")
print(result)
# print(result[1])
# lis = []
# for i in range(0,4):
#     print(i)
#     lis.append(i)

# print(lis)
# lis.pop(0)
# print(lis)
# print(lis)
# lis.pop(len(lis)-1)
# print(lis)

# tessst = ['123',1,['1','2']]
# tr = []
# # print(tr)
# # print(tessst[2][1])
# # 
# for i in range(0,len(tessst)-1):
#     tr.append(tessst[2][i])
    
# tr.append('0')
# print(tr)
# print(tessst[2])
# for i in range(len(result[2])):
#     print(result[2][i])
# print(random.randint(0,1))
cube = Action_Cube(state)
# state = '724506813'
# path = []
# open = []
# start = ['1234', 0, []]
# open.append(start)
# start = ['1243', 1, ['1234']]
# open.append(start)
# start = ['1423', 2, ['1234', '1243']]
# open.append(start)
# # print(open)
# # if '1243' not in open[1]:
# #     print("not in open")
# # else:
# #     print("in open")
# teest = ['123','132']
# if '132' in teest:
#     print("yay")
