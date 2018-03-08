# apt-get install python3-pytest for check if all test are ok

import random
#This test check all functions of this module
import RandScript

#Test if function "delete_first" delete name of script, 
#pruebav2.py in this case.
def test_del_First_none():
	main_script =  ["pruebav2.py"]
	ref         =  []
	res         =  RandScript.delete_first(main_script)
	assert res  == ref

#Test if function "delete_first" copy arguments without name of script,
#pruebav2.py in this case
def test_del_First_copy():
	linecom        =  ["pruebav2.py", "a","b"]
	ref            =  ["a","b"]
	res            =  RandScript.delete_first(linecom)
	assert linecom == ["pruebav2.py","a","b"]
	assert res     == ref

#Test if function "comprueba_cero" assert that length of 0 
#params are equal to 0
def test_comprueba_cero():
	params      = []
	zero_params = RandScript.comprueba_cero(params)
	assert zero_params

#Test if function "check" choose a random param between an array of params
#and an exit code.
#This test check function "choose" too, because function "check" uses it.
def test_check():
	words      = ["a","b","c"]
	zero       = (len(words)==0)
	ref_chosen = "a"
	ref_error  = 0
	random.seed(1)
	
	res_error, res_chosen =  RandScript.check(zero, words)
	assert res_error      == ref_error
	assert res_chosen     == ref_chosen
	




	
