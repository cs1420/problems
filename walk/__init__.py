import check50

@check50.check()
def exists():
    """random_walk.py exists."""
    check50.exists("random_walk.py")
    
@check50.check(exists)
def test_generates_images():
    """generates expected image files"""
    check50.run("python3 random_walk.py").exit(0)
    check50.exists("Chuck_rw.png")
    check50.exists("Daisy_rw.png")
    check50.exists("Chester_rw.png")
