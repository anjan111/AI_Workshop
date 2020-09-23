##### Applicatio.py
import sample
sample.user_fun1()
sample.user_fun2()
sample.user_fun3()

import sample as sam
sam.user_fun1()
sam.user_fun2()
sam.user_fun3()

from sample  import user_fun1, user_fun2, user_fun3
user_fun1()
user_fun2()
user_fun3()
from sample  import *
user_fun1()
user_fun2()
user_fun3()
