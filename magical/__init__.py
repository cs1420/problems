centimport check50

@check50.check()
def exists():
    """simulation.py exists."""
    check50.exists("simulation.py")
    check50.include("1.txt")

@check50.check(exists)
def test_reject_negative():
    """rejects a negative population percent"""
    check50.run("python3 simulation.py -0.5 2.5 20 output.txt").reject()

@check50.check(exists)
def test_pop_0():
    """rejects a population percent of 0"""
    check50.run("python3 simulation.py 0 2.5 20 output.txt").reject()

@check50.check(exists)
def test_nominal_1():
    """handles nominal input values correctly"""
    check50.run("python3 simulation.py 0 2.5 20 output.txt").exit(0)
    check50.exists("output.txt")
    actual = open("output.txt").read()
    expected = open("1.txt").read()
    if not actual == expected:
        raise check50.Mismatch(expected, actual, help="Your output file does not match expected output.")

@check50.check(exists)
def test2():
    """handles a height of 2 correctly"""
    out = check50.run("python3 mario.py").stdin("2").stdout()
    check_pyramid(out, open("2.txt").read())

@check50.check(exists)
def test23():
    """handles a height of 8 correctly"""
    out = check50.run("python3 mario.py").stdin("8").stdout()
    check_pyramid(out, open("8.txt").read())

@check50.check(exists)
def test24():
    """rejects a height of 9, and then accepts a height of 2"""
    (check50.run("python3 mario.py").stdin("9").reject()
            .stdin("2").stdout(open("2.txt")).exit(0))

@check50.check(exists)
def test_reject_foo():
    """rejects a non-numeric height of "foo" """
    check50.run("python3 mario.py").stdin("foo").reject()

@check50.check(exists)
def test_reject_empty():
    """rejects a non-numeric height of "" """
    check50.run("python3 mario.py").stdin("").reject()


def check_pyramid(output, correct):
    if output == correct:
        return

    output = [line for line in output.splitlines() if line != ""]
    correct = correct.splitlines()

    help = None
    if len(output) == len(correct):
        if all(ol.rstrip() == cl for ol, cl in zip(output, correct)):
            help = "Did you add too much trailing whitespace to the end of your pyramid?"
        elif all(ol[1:] == cl for ol, cl in zip(output, correct)):
            help = "Are you printing an additional character at the beginning of each line?"

    raise check50.Mismatch(correct, output, help=help)
