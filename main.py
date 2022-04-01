import unittest


def solution(a, b):
    # Implementar
    dif = a-b
    str=""
    while a>0 | b>0:
        dif = a - b
        if dif>0:
            for i in range(2):
                str=str+"a"
                a -= 1
            str=str+"b"
            b -= 1
        elif dif==0:
            for i in range(a):
                str=str+"ab"
                a -= 1
                b -= 1
        elif dif<0:
            for i in range(2):
                str= str+"b"
                b-=1
            str= str+"a"
            a -= 1

    return str


class Test(unittest.TestCase):
    def test_solution(self):
        self.assertNotIn("aaa", solution(5, 3))
        self.assertNotIn("bbb", solution(5, 3))
        self.assertNotIn("aaa", solution(3, 3))
        self.assertNotIn("bbb", solution(3, 3))
        self.assertNotIn("aaa", solution(1, 4))
        self.assertNotIn("bbb", solution(1, 4))


unittest.main()