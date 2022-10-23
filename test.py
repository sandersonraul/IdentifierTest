from identifier import identifier

class TestIdentifier:

    def test1(self):
        assert identifier("a19763") == "Valid"
    
    def teste2(self):
        assert identifier("b") == "Valid"
    
    def teste3(self):
        assert identifier("") == "Invalid"

    def teste4(self):
        assert identifier("4") == "Invalid"

    def teste5(self):
        assert identifier("c123546") == "Invalid"

    def teste6(self):
        assert identifier("b*&34") == "Invalid"