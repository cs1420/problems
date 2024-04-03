import check50

@check50.check()
def exists():
    """Dessert Shop 1 files exist."""
    check50.exists("desserts.py")
    check50.exists("test_desserts.py")

@check50.check(exists)
def test_candy_default():
   pass

def check_expect(targets):
  for expected, actual, help in targets:
    if not match(expected, actual): 
      raise check50.Mismatch(expected, actual, help=help)
 
