import  random 
def  generate_k_sat ( k ,  m ,  n ): 
    if  not  ( 1  <= k <= n): 
        raise  ValueError ( "Error: k should be between  1 and n (inclusive)." ) 
    if  m <  1 : 
        raise  ValueError ( "Error: Number of clauses  (m) must be at least 1." ) 
    variables =  list  (  range  (  1  , n+  1  )) 
    clauses = [] 
    
    
    for  _  in  range  (m): 
        clause = [] 
        clause_variables =  list  (variables) 
        for  _  in  range  (k): 
            if  not  clause_variables: 
                raise  ValueError  (  "Error: Not enough  variables available."  ) 
            variable = random.choice(clause_variables) 
            is_positive = random.choice([  True  ,  False  ]) 
            clause.append(variable  if  is_positive  else  -variable) 
            clause_variables.remove(variable) 
        clauses.append(clause) 
    return  clauses 

def  print_k_sat  (  clauses  ): 
    super_final_clause =  " & "  .join([  "("  +  " | "  .join(  map  (  str  ,  clause)) +  ")"  for  clause  in  clauses]) 
    print  (  "Expression Generated is: "  + super_final_clause) 

if  __name__  ==  "__main__"  : 
    try  : 
        # Get user input for k, m, and n 
        k =  int  (  input  (  "Enter the number of variables  in one clause: "  )) 
        m =  int  (  input  (  "Enter the number of clauses:  "  )) 
        n =  int  (  input  (  "Enter the total number of variables:  "  )) 
        # Generate and print k-SAT problem 
        k_sat_problem = generate_k_sat(k, m, n) 
        print  (  "  \n  Randomly Generated k-SAT Problem:"  ) 
        print_k_sat(k_sat_problem) 
    except ValueError  as  e: 
        print(e)
