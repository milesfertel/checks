from check50 import *


class Vigenere(Checks):

    @check()
    def exists(self):
        """vigenere.c exists."""
        self.require("vigenere.c")

    @check("exists")
    def compiles(self):
        """vigenere.c compiles."""
        self.spawn("clang -o vigenere vigenere.c -lcs50 -lm").exit(0)

    @check("compiles")
    def aa(self):
        """encrypts "a" as "a" using "a" as keyword"""
        self.spawn("./vigenere a").stdin("a").stdout("ciphertext:\s*a\n", "ciphertext: a\n").exit(0)

    @check("compiles")
    def bazbarfoo_caqgon(self):
        """encrypts "barfoo" as "caqgon" using "baz" as keyword"""
        self.spawn("./vigenere baz").stdin("barfoo").stdout("ciphertext:\s*caqgon\n", "ciphertext: caqgon\n").exit(0)

    @check("compiles")
    def mixedBaZBARFOO(self):
        """encrypts "BaRFoo" as "CaQGon" using "BaZ" as keyword"""
        self.spawn("./vigenere BaZ").stdin("BaRFoo").stdout("ciphertext:\s*CaQGon\n", "ciphertext: CaQGon\n").exit(0)

    @check("compiles")
    def allcapsBAZBARFOO(self):
        """encrypts "BARFOO" as "CAQGON" using "BAZ" as keyword"""
        self.spawn("./vigenere BAZ").stdin("BARFOO").stdout("ciphertext:\s*CAQGON\n", "ciphertext: CAQGON\n").exit(0)

    @check("compiles")
    def bazworld(self):
        """encrypts "world!$?" as "xoqmd!$?" using "baz" as keyword"""
        self.spawn("./vigenere baz").stdin("world!$?").stdout("ciphertext:\s*xoqmd!\$\?\n", "ciphertext: xoqmd!$?\n").exit(0)

    @check("compiles")
    def CSFiftyBrianyu28(self):
        """encrypts "Brianyu28" as "Djnisrs28" using "CSFifty" as keyword"""
        self.spawn("./vigenere CSFifty").stdin("Brianyu28").stdout("ciphertext:\s*Djnisrs28\n", "ciphertext: Djnisrs28\n").exit(0)

    @check("compiles")
    def ThisisCSFiftyMilesDanielFertel(self):
        """encrypts "Miles Daniel Fertel" as "Fptwa Fssqje Ylzlmd" using "ThisisCSFifty" as keyword"""
        self.spawn("./vigenere ThisisCSFifty").stdin("Miles Daniel Fertel").stdout("ciphertext:\s*Fptwa Fssqje Ylzlmd\n", "ciphertext: Fptwa Fssqje Ylzlmd\n").exit(0)

    @check("compiles")
    def noarg(self):
        """handles lack of argv[1]"""
        self.spawn("./vigenere").exit(1)

    @check("compiles")
    def toomanyargs(self):
        """handles argc > 2"""
        self.spawn("./vigenere 1 2 3").exit(1)

    @check("compiles")
    def reject(self):
        """rejects "Hax0r2" as keyword"""
        self.spawn("./vigenere Hax0r2").exit(1)
