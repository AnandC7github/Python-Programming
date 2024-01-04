#in this, a new file lib is created under which the file dog.py is inserted. now to run the file we have to include a file named "__init__.py" in the folder and then import the folder name 
from lib import dog

dog.bark()


#or 

from lib.dog import bark

dog.bark()
