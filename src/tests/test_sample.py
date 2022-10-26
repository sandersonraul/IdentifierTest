import sys
sys.path.append('src/')

from identifier import identifier

class TestIdentifier:

    def test1(self):
        assert identifier.identifier("a19763") == "Valid"
    
    def teste2(self):
        assert identifier.identifier("b") == "Valid"
    
    def teste3(self):
        assert identifier.identifier("") == "Invalid"

    def teste4(self):
        assert identifier.identifier("4") == "Invalid"

    def teste5(self):
        assert identifier.identifier("c123546") == "Invalid"

    def teste6(self):
        assert identifier.identifier("b*&34") == "Invalid"