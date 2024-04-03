"""
Pytest test code for the instructor reference implementation
of desert shop part 1. This code IS NOT to be shared
with students.

To run from teriminal: python3 -m pytest test_desserts.py

Author: George Rudolph
Date: 2 Apr 2024
Version: 2
"""
import pytest
from desserts import Candy, Cookie, IceCream, Sundae

#
# Default value test cases
#
def test_candy_default():
	candy = Candy()
	assert candy.name == ""
	assert candy.weight == 0
	assert candy.price_per_pound == 0

def test_cookie_default():
	cookie = Cookie()
	assert cookie.name == ""
	assert cookie.quantity == 0
	assert cookie.price_per_dozen == 0

def test_ice_cream_default():
	ice_cream = IceCream()
	assert ice_cream.name == ""
	assert ice_cream.scoop_count == 0
	assert ice_cream.price_per_scoop == 0

def test_sundae_default():
	sundae = Sundae()
	assert sundae.name == ""
	assert sundae.topping_name == ''
	assert sundae.topping_price == 0

#
# Nominal value test cases
#

def test_candy_nominal():
	candy = Candy("peanut brittle", 3, 12.00)
	assert candy.name == "peanut brittle"
	assert candy.weight == 3.0
	assert candy.price_per_pound == 12.00

def test_cookie_nominal():
	cookie = Cookie("mini dounut", 12.0, 5.00)
	assert cookie.name == "mini dounut"
	assert cookie.quantity == 12.0
	assert cookie.price_per_dozen == 5.00

def test_ice_cream_nominal():
	ice_cream = IceCream("moose tracks", 2, 1.30)
	assert ice_cream.name == "moose tracks"
	assert ice_cream.scoop_count == 2
	assert ice_cream.price_per_scoop == 1.30

def test_sundae_nominal():
	sundae = Sundae("banana split", "chocolate", 1.50)
	assert sundae.name == "banana split"
	assert sundae.topping_name == "chocolate"
	assert sundae.topping_price == 1.50

#
# Modify attributes test cases
#

def test_candy_modify():
	candy = Candy()

	candy.name = "peanut brittle"
	assert candy.name == "peanut brittle"


	candy.weight = 3.0
	assert candy.weight == 3.0

	candy.price_per_pound = 12.00
	assert candy.price_per_pound == 12.00

def test_cookie_modify():
  cookie = Cookie()
  cookie.name = "mini dounut"
  assert cookie.name == "mini dounut"

  cookie.quantity = 12.0
  assert cookie.quantity == 12.0

  cookie.price_per_dozen = 5.00
  assert cookie.price_per_dozen == 5.00

def test_ice_cream_modify():
	ice_cream = IceCream()

	ice_cream.name = "moose tracks"
	assert ice_cream.name == "moose tracks"

	ice_cream.scoop_count = 2
	assert ice_cream.scoop_count == 2

	ice_cream.price_per_scoop = 1.30
	assert ice_cream.price_per_scoop == 1.30

def test_sundae_modify():
	sundae = Sundae()

	sundae.name = "banana split"
	assert sundae.name == "banana split"

	sundae.topping_name = "chocolate"
	assert sundae.topping_name == "chocolate"

	sundae.topping_price = 1.50
	assert sundae.topping_price == 1.50
