# -*- coding: utf-8 -*-
"""python_project_age_vote.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Mtb43fF9SXnU_BVVtSjjbnl_IYHl69u5
"""

try:
  name =input('Enter your name ')
  name=str(name)
  age =int(input('Enter your age ' ))
  if age>=18:
      print(f'congrates, {name} you are eligible to vote')
  else:
     print('OOPs, you are not eligible to vote')


except:
    print('Enter name name as text and age as number')



