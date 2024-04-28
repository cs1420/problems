import check50
import doctest

@check50.check()
def exists():
    """library.py exists."""
    check50.exists("library.py")
    check50.include("ALG.txt","FMP.txt","PNP.txt","TTL.txt","TSL.txt","WOO.txt")
    check50.include("ref_ALG_book.txt","ref_FMP_book.txt","ref_PNP_book.txt","ref_TTL_book.txt","ref_TSL_book.txt","ref_WOO_book.txt")
    
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
def test_nominal_4():
    """handles 4th file correctly"""
    check50.run("python3 library.py FMP.txt").exit(0)
    check50.exists("FMP_book.txt")
    actual = open("FMP_book.txt").read()
    expected = open("ref_FMP_book.txt").read()
    if not actual == expected:
        raise check50.Mismatch(expected, actual, help="Your output file does not match expected output.")

@check50.check(exists)
def test_nominal_5():
    """handles 5th file correctly"""
    check50.run("python3 library.py PNP.txt").exit(0)
    check50.exists("PNP_book.txt")
    actual = open("PNP_book.txt").read()
    expected = open("ref_PNP_book.txt").read()
    if not actual == expected:
        raise check50.Mismatch(expected, actual, help="Your output file does not match expected output.")

@check50.check(exists)
def test_nominal_6():
    """handles 6th file correctly"""
    check50.run("python3 library.py TSL.txt").exit(0)
    check50.exists("TSL_book.txt")
    actual = open("TSL_book.txt").read()
    expected = open("ref_TSL_book.txt").read()
    if not actual == expected:
        raise check50.Mismatch(expected, actual, help="Your output file does not match expected output.")
    
@check50.check(exists)
def test_reject_empty():
    """rejects when no parameters given"""
    status = check50.run("python3 library.py").exit()
    if status == 0:
        raise check50.Failure(f"missing input file name")

@check50.check(exists)
def test_with_doctest():
    """run doctest"""
    check50.run("python3 -m doctest -v library.py").exit(0)