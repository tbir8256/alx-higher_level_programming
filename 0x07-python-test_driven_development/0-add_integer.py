Skip to content

Search or jump to…

Pull requests

Issues

Marketplace

Explore

 

 @tbir8256 

 monoprosito

 /

 holbertonschool-higher_level_programming

 Public

 Code

 Issues

 Pull requests

 Actions

 Projects

 Security

 Insights

 holbertonschool-higher_level_programming/0x07-python-test_driven_development/0-add_integer.py /

 @monoprosito

 monoprosito Refactor some conditions

 Latest commit 9ee20de on Jan 14, 2020

  History

   1 contributor

   Executable File  50 lines (33 sloc)  1018 Bytes



   #!/usr/bin/python3

   """A module to add two numbers

   This module performs the addition operation between two numbers,

   these numbers can be integers or floats.

   """





   def add_integer(a, b=98):

           """Adds two numbers

               Performs the addition between two numbers.

                   Args:

                           a (:obj:`int, float`): The first number.

                                   b (:obj:`int, float`, optional): The second number.

                                       Returns:

                                               int: The result of the addition.

                                                   """

                                                       if type(a) not in (int, float):

                                                                   raise TypeError('a must be an integer')



                                                                   if type(b) not in (int, float):

                                                                               raise TypeError('b must be an integer')



                                                                               a = convert_to_int(a)

                                                                                   b = convert_to_int(b)

                                                                                       return a + b





                                                                                   def convert_to_int(num):

                                                                                           """Cast the data type of num parameter

                                                                                               Convert a float number to a integer number

                                                                                                   Args:

                                                                                                           num (:obj:`int, float`): The number to cast.

                                                                                                               Returns:

                                                                                                                       int: The number casted to integer.

                                                                                                                           """

                                                                                                                               if type(num) is float:

                                                                                                                                           num = int(num)

                                                                                                                                                   return num



                                                                                                                                                   return num
