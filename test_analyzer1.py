from app_analyzer import collect_class_forest, compute_unimplemented

test_input_path = "./src/"
test_input_path2 = "./src2/"


def test_class_forest():
    expected = {
        "AbstractLinkedList": {
        "Cursor": {
            "SubCursor": {}
        },
        "CursorableLinkedList": {},
        "NodeCachingLinkedList": {}
        }
    }

    result = collect_class_forest(test_input_path)
    assert expected == result


def test_unimplemented():
    expected = {"DoublePredicate"}

    result = compute_unimplemented(test_input_path2)
    assert expected == result
