import numpy as np
import os
import random


no_variable=500#a test read from input
no_clause=1000#a test read from input
clause_length=1



#generate all forms of literals given number of variables
variables=[str(x) for x in range(1,no_variable+1)]
variables_not=['-'+str(x) for x in range(1,no_variable+1)]
all_variables=variables+variables_not 
#make title for cnf file
cnf_title=list(['p cnf'])+[' ',str(no_variable),' ',str(no_clause),'\n']
cnf_title=''.join(cnf_title)
cnf_list=list([cnf_title])

#randomly generate clauses
for i in range(no_clause):
     clause_length=random.randint(1,no_variable)
     clause = random.sample(all_variables,clause_length)
     clause.append('0\n')
     clause = ' '.join(clause)
     cnf_list.append(clause)

cnf_txt=''.join(cnf_list)
#write the results into cnf file
with open('./zchaff/test.cnf','w') as f:
     f.write(cnf_txt)

with open('./DPLL-master/test.cnf','w') as f:
     f.write(cnf_txt)
     

          
