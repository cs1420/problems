import check50

@check50.check()
def exists():
    """simulation.py exists."""
    check50.exists("simulation.py")
    check50.include("1.txt","2.txt")

@check50.check(exists)
def test_reject_negative():
    """rejects a negative population percent"""
    status = check50.run("python3 simulation.py -0.5 2.5 20 output.txt").exit()
    if status == 0:
        raise check50.Failure(f"expected to reject negative population")

@check50.check(exists)
def test_pop_0():
    """rejects a population percent of 0"""
    status = check50.run("python3 simulation.py 0 2.5 20 output.txt").exit()
    if status == 0:
        raise check50.Failure(f"expected to reject 0 population")

@check50.check(exists)
def test_nominal_1():
    """handles nominal input values correctly"""
    check50.run("python3 simulation.py 0.1 2.5 20 output.txt").exit(0)
    check50.exists("output.txt")
    actual = open("output.txt").read()
    expected = open("1.txt").read()
    if not actual == expected:
        raise check50.Mismatch(expected, actual, help="Your output file does not match expected output.")

@check50.check(exists)
def test_nominal_2():
    """handles other nominal values correctly"""
    check50.run("python3 simulation.py 0.1 1.2  80 output.txt").exit(0)
    check50.exists("output.txt")
    actual = open("output.txt").read()
    expected = open("2.txt").read()
    if not actual == expected:
        raise check50.Mismatch(expected, actual, help="Your output file does not match expected output.")
        
@check50.check(exists)
def test_non_numeric_rate():
    """reject non-numeric rate"""
    status = check50.run("python3 simulation.py 0 pippy 20 output.txt").exit()
    if status == 0:
        raise check50.Failure(f"expected to reject non-numeric rate")

@check50.check(exists)
def test_reject_negative_rate():
    """rejects a negative rate"""
    status = check50.run("python3 simulation.py 0 -1 20 output.txt").exit()
    if status == 0:
        raise check50.Failure(f"expected to reject non-numeric rate")

@check50.check(exists)
def test_reject_large_rate():
    """rejects a rate > 4"""
    status = check50.run("python3 simulation.py 0 5 20 output.txt").exit()
    if status == 0:
        raise check50.Failure(f"expected to reject non-numeric rate")
    
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
    """rejects a negative rate"""
    status = check50.run("python3 simulation.py 0.1 2.5 -1 output.txt").exit()
    if status == 0:
        raise check50.Failure(f"expected to reject non-positive iteration values")
