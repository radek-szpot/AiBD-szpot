from bubble import bubble_sort

def test_bubble_sort():
    got = bubble_sort([14, 33, 27, 35, 10])
    want = [10, 14, 27, 33, 35]
    assert got == want