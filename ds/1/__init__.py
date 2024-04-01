import check50

@check50.check()
def exists():
    """Dessert Shop 1 files exist."""
    check50.exists("desserts.py")
    check50.exists("test_desserts.py")

@check50.check(exists)
def test_candy_default():
  candy = Candy()
  values = (candy.name, candy.weight, candy.price_per_pound)
  expected_values = ("",0,0)
  help_msgs = (
    r"default name should be the empty string.",
    r"default weight should be 0.",
    r"default price per pound should be 0."
  )
  check_expect(zip(expected_values,values,help_msgs))
               
@check50.check(exists)
def test_candy_nominal():
  candy = Candy("peanut brittle", 3, 12.00)
  values = (candy.name, candy.weight, candy.price_per_pound)
  expected_values = ("peanut brittle", 3, 12.00)
  help_msgs = (
    r"the name was not set to expected nominal value.",
    r"the name was not set to expected nominal value..",
    r"price per pound was not set to nominal value."
  )
  check_expect(zip(expected_values,values,help_msgs))

@check50.check(exists)
def test_candy_modify():
  candy = Candy()
  candy.name = "peanut brittle"
  candy.weight = 3.0
  candy.price_per_pound = 12.00
  values = (candy.name, candy.weight, candy.price_per_pound)
  expected_values = ("peanut brittle", 3, 12.00)
  help_msgs = (
    r"the name was not modified to expected nominal value.",
    r"the name was not modified to expected nominal value..",
    r"price per pound was not modified to nominal value."
  )
  check_expect(zip(expected_values,values,help_msgs))

@check50.check(exists)
def test_cookie_default():
  cookie = Cookie()
  values = (cookie.name, cookie.quantity, cookie.price_per_dozen)
  expected_values = ("",0,0)
  help_msgs = (
    r"default name should be the empty string.",
    r"default quantity should be 0.",
    r"default price per dozen should be 0."
  )
  check_expect(zip(expected_values,values,help_msgs))

@check50.check(exists)
def test_cookie_nominal():
  cookie = Cookie("mini dounut", 12.0, 5.00)
  values = (cookie.name, cookie.quantity, cookie.price_per_dozen)
  expected_values = ("mini dounut", 12.0, 5.00)
  help_msgs = (
   r"name should be non-empty.",
    r"quantity should not be 0.",
    r"price per dozen should not be 0."
  )
  check_expect(zip(expected_values,values,help_msgs))
	
@check50.check(exists)
def test_cookie_modify():
  cookie = Cookie()
  cookie.name = "mini dounut"
  cookie.quantity = 12.0
  cookie.price_per_dozen = 5.00
  values = (cookie.name, cookie.quantity, cookie.price_per_dozen)
  expected_values = ("mini dounut", 12.0, 5.00)
  help_msgs = (
   r"modified name should be non-empty.",
    r"modified quantity should not be 0.",
    r"modified price per dozen should not be 0."
  )
  check_expect(zip(expected_values,values,help_msgs))

@check50.check(exists)
def test_ice_cream_default():
  ice_cream = IceCream()
  values = (ice_cream.name,ice_cream.scoop_count, ice_cream.price_per_scoop)
  expected_values = ("", 0, 0)
  help_msgs = (
   r"name should be empty.",
    r"scoop count should be 0.",
    r"price per scoop should be 0."
  )
  check_expect(zip(expected_values,values,help_msgs))

@check50.check(exists)
def test_ice_cream_nominal():
  ice_cream = IceCream("moose tracks", 2, 1.30)
  values = (ice_cream.name,ice_cream.scoop_count, ice_cream.price_per_scoop)
  expected_values = ("moose tracks", 2, 1.30)
  help_msgs = (
   r"name should be not be empty.",
    r"scoop count should not be 0.",
    r"price per scoop should not be 0."
  )
  check_expect(zip(expected_values,values,help_msgs))

@check50.check(exists)
def test_ice_cream_modify():
  ice_cream = IceCream()
  ice_cream.name = "moose tracks"
  ice_cream.scoop_count = 2 
  ice_cream.price_per_scopp = 1.30
  values = (ice_cream.name,ice_cream.scoop_count, ice_cream.price_per_scoop)
  expected_values = ("moose tracks", 2, 1.30)
  help_msgs = (
   r"modified name should be not be empty.",
    r"modified scoop count should not be 0.",
    r"modified price per scoop should not be 0."
  )
  check_expect(zip(expected_values,values,help_msgs))
@check50.check(exists)
def test_sundae_default():
  sundae = Sundae()
  values = (sundae.name,sundae.scoop_count, sundae.price_per_scoop, sundae.topping_name, sundae.topping_price)
  expected_values = ("", 0,0,"",0)
  help_msgs = (
   r"name should be empty.",
    r"scoop count should be 0.",
    r"price per scoop should be 0."
    r"topping name should be empty."
    r"topping price should be 0."
  )
  check_expect(zip(expected_values,values,help_msgs))

@check50.check(exists)
def test_sundae_nominal():
  sundae = Sundae("banana split", "chocolate", 1.50)
  values = (sundae.name,sundae.scoop_count, sundae.price_per_scoop, sundae.topping_name, sundae.topping_price)
  expected_values = ("banana split", 0, 0, "chocolate", 1.50)
  help_msgs = (
   r"name should not be empty.",
    r"scoop count should be 0.",
    r"price per scoop should be 0."
    r"topping name should not be empty."
    r"topping price should not be 0."
  )
  check_expect(zip(expected_values,values,help_msgs))
...
@check50.check(exists)
def test_sundae_modify():
  sundae = Sundae()
  sundae.name = "banana split"
  sundae.topping_name = "chocolate"
  sundae.topping_price = 1.50
  values = (sundae.name,sundae.scoop_count, sundae.price_per_scoop, sundae.topping_name, sundae.topping_price)
  expected_values = ("banana split", 0, 0, "chocolate", 1.50)
  help_msgs = (
   r"name should not be empty.",
    r"scoop count should be 0.",
    r"price per scoop should be 0."
    r"topping name should not be empty."
    r"topping price should not be 0."
  )
  check_expect(zip(expected_values,values,help_msgs))
'''
def check_expect(targets):
  for expected, actual, help in targets:
    if not match(expected, actual): 
      raise check50.Mismatch(expected, actual, help=help)
  
