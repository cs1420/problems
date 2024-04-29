import check50

@check50.check()
def exists():
    """random_walk.py exists."""
    check50.exists("fact_check.py")
    check50.exists("BLS_private.csv")
    check50.exists("presidents.txt")
    
    
@check50.check(exists)
def test_generates_images():
    """generates conclusions.md"""
    check50.run("python3 fact_check.py").exit(0)
    check50.exists("conclusions.md")
    