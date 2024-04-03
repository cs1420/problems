import re
import check50

@check50.check()
def exists():
    """Dessert Shop 1 files exist."""
    check50.exists("desserts.py")
    check50.exists("test_desserts.py")

@check50.check(exists)
def test_candy_default():
    out = check50.run("pytest test_desserts.py").stdout()
    pattern = r"(collected \d+ items|\d+ passed)"
    matches = re.findall(pattern, output)
    
    if "collected 12 items" not in matches:
        raise check50.Failure(f"Expected 'collected 12 items' in output, but not found.")
    
    if "12 passed" not in matches:
        raise check50.Failure(f"Expected '12 passed' in output, but not found.")
    
def check_expect(targets):
  for expected, actual, help in targets:
    if not match(expected, actual): 
      raise check50.Mismatch(expected, actual, help=help)
 
