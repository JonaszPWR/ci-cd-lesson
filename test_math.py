import pytest
import math_functions

@pytest.mark.parameterize("a, b, expected", [(1,2,3), (2,3,5), (3,4,7), (4,5,9)])

def test_add(a, b, expected):
    result = math_functions.add(a,b)
    assert result == expected

@pytest.mark.parameterize("a, b, expected",[ (1 , 2 , - 1 ), (2 , 3, - 1 ),
                                             (3 , 4 , - 1 ), (4 , 5 , - 1 ) ])
def test_subtract (a , b , expected ):
    result = math_functions.subtract (a , b)
    assert result == expected

@pytest . mark . parametrize ( "a , b , expected " , [ (1 , 2 , 2 ), (2 , 3 ,6 ),
                                                       (3 , 4 , 12 ), (4 , 5 , 20 ) ])

def test_multiply (a , b , expected ):
    result = math_functions.multiply (a , b)
    assert result == expected
@pytest . mark . parametrize ( "a , b , expected " , [ (1 , 2 , 0.5 ), (3 ,4 , 0.75 ),
                                                       (4 , 5 , 0.8 ) ])

def test_divide (a , b , expected ) :
    result = math_functions.divide (a , b)
    assert result == expected
