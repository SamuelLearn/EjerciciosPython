# -*- coding: utf-8 -*-
import re

def password (p):
    if len(p) > 8 and  not(' ' in p):
        formato = "^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$"
        f = lambda x: True if re.findall(formato, x) else False
	return f(p)
        
