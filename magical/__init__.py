from check50 import *

class Magical(Checks):

    @check()
    def exists(self):
        """simulation.py exists"""
        self.require("magical/simulation.py")

    @check("exists")
    def compiles(self):
        """simulation.py compiles"""
        self.spawn("python3 -m py_compile magical/simulation.py")

    @check("compiles")
    def correct(self):
        """Check that simulation.py produces correct output"""
        self.spawn("python3 magical/simulation.py 0.1 2.5 20 output.txt").stdout("0\t0.100\n1\t0.225\n2\t0.436\n3\t0.615\n4\t0.592\n5\t0.604\n6\t0.598\n7\t0.601\n8\t0.600\n9\t0.600\n10\t0.600\n11\t0.600\n12\t0.600\n13\t0.600\n14\t0.600\n15\t0.600\n16\t0.600\n17\t0.600\n18\t0.600\n19\t0.600\n20\t0.600\n", "0\t0.100\n1\t0.225\n2\t0.436\n3\t0.615\n4\t0.592\n5\t0.604\n6\t0.598\n7\t0.601\n8\t0.600\n9\t0.600\n10\t0.600\n11\t0.600\n12\t0.600\n13\t0.600\n14\t0.600\n15\t0.600\n16\t0.600\n17\t0.600\n18\t0.600\n19\t0.600\n20\t0.600\n")
