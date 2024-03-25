import check50

@check50.check()
def happy_day_1():
    """happy day 1"""
    check50.run("python3 yondu.py").stdin("20\n1000\n", prompt=False).stdout("How many pirates:\nHow many units:\n\nYondu's share: 159.60\nPeter's share: 127.15\nCrew's share: 39.62\n", regex=False).exit(0)

@check50.check()
def happy_day_2():
    """happy day 2"""
    check50.run("python3 yondu.py").stdin("35\n100000\n", prompt=False).stdout("How many pirates:\nHow many units:\n\nYondu's share: 15197.23\nPeter's share: 11770.63\nCrew's share: 2213.10\n", regex=False).exit(0)

@check50.check()
def happy_day_3():
    """happy day 3"""
    check50.run("python3 yondu.py").stdin("49\n39481\n", prompt=False).stdout("How many pirates:\nHow many units:\n\nYondu's share: 5735.85\nPeter's share: 4386.49\nCrew's share: 624.65\n", regex=False).exit(0)