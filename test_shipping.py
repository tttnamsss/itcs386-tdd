import pytest
from shipping import shipping_fee

@pytest.mark.parametrize("weight_kg, expected", [ 
    (1, 40),    # up to 1 kg costs 40 baht
    (3.5, 60),   # > 1 kg and up to 5 kg costs 60 baht
    (7.3, 90),    # > 5 kg costs 60 baht plus 10 baht for every started kilogram above 5 kg
    ]) 

def test_shipping_fee(weight_kg, expected): 
    assert shipping_fee(weight_kg) == expected 
    
def test_weight_is_zero_rejected(): 
    with pytest.raises(ValueError): 
        shipping_fee(0)