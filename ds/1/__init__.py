import re
import check50
import check50.py

@check50.check()
def exists():
    """Dessert Shop 1 files exist."""
    check50.exists("desserts.py")
    check50.exists("test_desserts.py")

@check50.check(exists)
def student_test():
    """Student test_dessert file runs."""
    out = check50.run("pytest test_desserts.py").stdout()
    check_expect(out,12)

@check50.check(student_test)
def setup(self):
   """Setup"""
   # Replace the student's test file with your own
   #check50.include("./staff_test_desserts.py")
   #check50.py.append_code("test_desserts.py", "./staff_test_desserts.py")

@check50.check(setup)
def test_candy_default():
	"""Test Candy default constructor."""
	out = check50.run("pytest test_desserts.py::test_candy_default").stdout()
	check_expect(out,1)
	
@check50.check(setup)
def test_candy_nominal():
	"""Test Candy constructor with nominal values."""
	out = check50.run("pytest staff_test_desserts.py::test_candy_nominal").stdout()
	check_expect(out,1)

@check50.check(setup)
def test_candy_modify():
	"""Test Candy modify values."""
	out = check50.run("pytest staff_test_desserts.py::test_candy_modify").stdout()
	check_expect(out,1)

@check50.check(exists)
def test_cookie_default():
	"""Test Cookie default constructor."""
	out = check50.run("pytest staff_test_desserts.py::test_cookie_default").stdout()
	check_expect(out,1)

@check50.check(exists)
def test_cookie_nominal():
	"""Test Cookie constructor with nominal values."""
	out = check50.run("pytest staff_test_desserts.py::test_cookie_nominal").stdout()
	check_expect(out,1)

	
@check50.check(exists)
def test_cookie_modify():
	"""Test Cookie modify values."""
	out = check50.run("pytest staff_test_desserts.py::test_cookie_modify").stdout()
	check_expect(out,1)

@check50.check(exists)
def test_ice_cream_default():
	"""Test Ice Cream default constructor."""
	out = check50.run("pytest staff_test_desserts.py::test_ice_cream_default").stdout()
	check_expect(out,1)

@check50.check(exists)
def test_ice_cream_nominal():
	"""Test Ice Cream constructor with nominal values."""
	out = check50.run("pytest staff_test_desserts.py::test_ice_cream_nominal").stdout()
	check_expect(out,1)

@check50.check(exists)
def test_ice_cream_modify():
	"""Test Ice Cream modify values."""
	out = check50.run("pytest staff_test_desserts.py::test_ice_cream_modify").stdout()
	check_expect(out,1)

@check50.check(exists)
def test_sundae_default():
	"""Test Sundae default constructor."""
	out = check50.run("pytest staff_test_desserts.py::test_sundae_default").stdout()
	check_expect(out,1)

@check50.check(exists)
def test_sundae_nominal():
	"""Test Sundae constructor with nominal values."""
	out = check50.run("pytest staff_test_desserts.py::test_sundae_nominal").stdout()
	check_expect(out,1)
	
@check50.check(exists)
def test_sundae_modify():
	"""Test Sundae modify values."""
	out = check50.run("pytest staff_test_desserts.py::test_sundae_modify").stdout()
	check_expect(out,1)

def check_expect(out, count):
	pattern = r"(collected \d+ items|\d+ passed)"
	matches = re.findall(pattern, out)
    
	if f"collected {count} items" not in matches:
		raise check50.Failure(f"Expected 'collected {count} items' in output, but {matches} found.")
    
	if f"{count} passed" not in matches:
		raise check50.Failure(f"Expected '{count} passed' in output, but not found.")
  
