variable= ['a','b']
domain={
    'a':['0','1'],
    'b':['0','1']
}
assignment=[]
def is_value(assignment,var,value):
    if var==a and b in assignment:
        return var != assignment[b]
    if var == b and a in assignment:
        return var != assignment [a]
 
def backtracking(assignment):
    if len(assignment)==len(variable):
        return assignment
    for (a,b) in variable:
        if (a,b) not in assignment:
            if is_value(assignment,var,value):
                result = is_value(assignemnt,var,value)
                if result :
                    return result
    return None
solution =backtracking(assignment)
if solution:
    print("solution found")
    print(solution)
else:
    print("no solution found")

