import check50

@check50.check()
def exists():
    """library.py exists."""
    check50.exists("library.py")
    check50.include("ALG.txt","FMP.txt","PNP.txt","TTL.txt","TSL.txt","WOO.txt")
    check50.include("ref_ALG.txt","ref_FMP.txt","ref_PNP.txt","ref_TTL.txt","ref_TSL.txt","ref_WOO.txt")
    
@check50.check(exists)
def test_nominal_1():
    """handles ALG file correctly"""
    check50.run("python3 library.py ALG.txt").exit(0)
    check50.exists("ALG_book.txt")
    actual = open("ALG_book.txt").read()
    expected = open("ref_ALG_book.txt").read()
    if not actual == expected:
        raise check50.Mismatch(expected, actual, help="Your output file does not match expected output.")

@check50.check(exists)
def test_nominal_2():
    """handles TTL file correctly"""
    check50.run("python3 library.py TTL.txt").exit(0)
    check50.exists("TTL_book.txt")
    actual = open("TTL_book.txt").read()
    expected = open("ref_TTL_book.txt").read()
    if not actual == expected:
        raise check50.Mismatch(expected, actual, help="Your output file does not match expected output.")

@check50.check(exists)
def test_nominal_3():
    """handles WOO file correctly"""
    check50.run("python3 library.py WOO.txt").exit(0)
    check50.exists("WOO_book.txt")
    actual = open("WOO_book.txt").read()
    expected = open("ref_WOO_book.txt").read()
    if not actual == expected:
        raise check50.Mismatch(expected, actual, help="Your output file does not match expected output.")
    
@check50.check(exists)
def test_reject_empty():
    """rejects when no parameters given"""
    status = check50.run("python3 simulation.py").exit()
    if status == 0:
        raise check50.Failure(f"expected to provide parameters")

@check50.check(exists)
def test_non_numeric_iterations():
    """reject non-numeric iteration value"""
    status = check50.run("python3 simulation.py 0.1 2.5 pippy output.txt").exit()
    if status == 0:
        raise check50.Failure(f"expected to reject non-numeric iteration value")

@check50.check(exists)
def test_reject_negative_iterations():
    """rejects a negative iteration value"""
    status = check50.run("python3 simulation.py 0.1 2.5 -1 output.txt").exit()
    if status == 0:
        raise check50.Failure(f"expected to reject non-positive iteration values")
