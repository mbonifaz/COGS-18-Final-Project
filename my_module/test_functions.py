from my_module.functions import addition
from my_module.functions import subtraction
from my_module.functions import multiplication
from my_module.functions import division
from my_module.functions import squares
from my_module.functions import square_root
 
    
def addition_test():
    out1, out2 = addition()
    assert 1 <= out1 <= 100
    assert 1 <= out2 <= 100

    
def subtraction_test():
    out1, out2 = subtraction()
    assert 1 <= out1 <= 100
    assert 1 <= out2 <= 100
 
   
def multiplication_test():
    out1, out2 = multiplication()
    assert 1 <= out1 <= 100
    assert 1 <= out2 <= 100
    
    
def division_test():
    out1, out2 = division()
    assert 1 <= out1 <= 100
    assert 1 <= out2 <= 100
    
    
def squares_test():
    out1 = squares()
    assert 1 <= out1 <= 25
    
    
def square_root_test():
    out = square_root()
    assert 1 <= out1 <= 49
                 
    
