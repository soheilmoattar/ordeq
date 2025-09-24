







    country = Match(ev).Case("NL", s1).Case("BE", s2)
    assert country.references == {"io": [ev], "cases": [s1, s2]}





    small_or_large = Match().Case("S", small).Case("L", large)



    assert small_or_large.references == {"cases": [small, large]}
