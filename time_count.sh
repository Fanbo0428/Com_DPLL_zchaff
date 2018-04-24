python cnf_generator.py
cd DPLL-master
time python cnf_text_generator.py|python dpll.py
cd ../zchaff
./zchaff test.cnf