"""hi this is isnpector tools for python"""
x= [1,2,3]
print(dir(x))
attr_of_empty = x.__getattribute__
print(f"""
      
     1-now empty 
      {dir()}  
      
      2- now the none just to see if the none and emoty are same
      {dir(None)}
      
      3- lets try something form the empty dir run and to see whats that
      {__package__}
      {__annotations__}
      {__builtins__}
      {__doc__}
      {type(__annotations__)}
      
      """)
