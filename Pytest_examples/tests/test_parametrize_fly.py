from pytest import mark


@mark.parametrize("simple_tv_brand", [("Sansung"), ("Sony"), ("LG")])
def test_simple_television_turns_on(simple_tv_brand):
    print(f"{simple_tv_brand} turns on as expected")
