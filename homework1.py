from functions import *

print("please enter the state:")
# check to see if state is valid 9 digits

state = str(input())

print("hello, please type the letter of the following options aka: a")
print("a)  Lists all states")
print("b)  Make a move on the current state by moving 0")
print("c)  make three rows % 3")
print("d)  BFS search for 012345678")
print("e)  DFS search for 012345678")
print("f)  BFS search for 123804765")
print("g)  unit cost search (UCS)")


inputs = str(input())
# state = '123456789'
current = ''
solution = []
if inputs == 'a':
    print("you chose the option to Lists all states:")
    print(recursionA(state,current,solution))

if inputs == 'b':
    print("current state: " + state + ", please select action")
    
    print("moving up:1")
    print("down:2")
    print("left:3")
    print("right:4")
    input = input()
    print("current state: " + state + ", Action: " + str(input))
    outcomeB = ActionB(state,input)
    print("outcome: " + outcomeB)
if inputs == 'c':
    # print("you typed c, thanks")
    ActionC(state, 0)
if inputs == 'd':
    print("dong BFS, return is final state, best steps to get there and path there:")
    print(ActionD(state))
if inputs == 'e':
    print("dong DFS, return is final state, best steps to get there and path there:")
    print(ActionE(state))
if inputs == 'f':
    print("dong BFS, return is final state, best steps to get there and path there:")
    print(ActionD(state))
if inputs == 'g':
    print("dong UCS, return is final state, best steps to get there and path there:")
    print(ActionG(state))


