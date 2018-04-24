import numpy as np

#read cnf file into a list
with open('./test.cnf') as f:
     cnf_list = [line for line in f.readlines()]
#delete the comment part
for line in cnf_list:
     if line[0] == 'c':
          cnf_list.remove(line)

config = None          
#fetch the config file
for line in cnf_list:
     if line[0] == 'p':
          config=line
          break

config=list(config)[6:len(config)-1]
seg=config.index(' ')

variable_no = int(''.join(config[:seg]))
clause_no = int(''.join(config[seg+1:]))
#print variable_no,clause_no

var_list=[str(i) for i in range(1,variable_no+1)]


input_string=list(['and']) #A and infront of the list, indicating the CNF form
for clause in cnf_list[1:]:
     clause_string=list(['or'])
     clause = clause.split()
     clause.remove('0')
     for literal in clause:
          if literal[0] == '-':
               literal_not=['not',literal.lstrip('-')]#converse negation literals such as -A to not
               clause.append(literal_not)
     for l in clause:
          if l[0]!='-':
               clause_string.append(l)           
     input_string.append(clause_string)
     
print input_string
