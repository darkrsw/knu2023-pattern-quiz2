from app_analyzer import collect_class_forest, compute_unimplemented

test_input_path = "./src/"
test_input_path2 = "./src2/"
test_input_path3 = "./core"
test_input_path4 = "./controller"
test_input_path5 = "./part01"
test_input_path6 = "./message"
test_input_path7 = "./parser"
test_input_path8 = "./email"

def test1_class_forest():
    # expected = {
    #     "AbstractLinkedList": {
    #     "Cursor": {
    #         "SubCursor": {}
    #     },
    #     "CursorableLinkedList": {},
    #     "NodeCachingLinkedList": {}
    #     }
    # }

    expected = {'AbstractLinkedList': {'NodeCachingLinkedList': {}, 'CursorableLinkedList': {}, 'Cursor': {'SubCursor': {}}},
     'LinkedListIterator': {'LinkedSubListIterator': {}}}

    result = collect_class_forest(test_input_path)
    assert expected == result


def test2_unimplemented():
    expected = {"DoublePredicate"}

    result = compute_unimplemented(test_input_path2)
    assert expected == result


def test3_class_forest():
    expected = {'Attachment'}

    result = compute_unimplemented(test_input_path8)
    assert expected == result

def test4_unimplemented():
    expected = {'Plugin', 'ScanningResultCallback', 'ScanningProgressCallback', 'WinIpHlpDll'}

    result = compute_unimplemented(test_input_path3)
    assert expected == result


def test5_class_forest():
    expected = {}

    result = collect_class_forest(test_input_path4)
    assert expected == result


def test6_unimplemented():
    expected = {'OnFragmentInteractionListener'}

    result = compute_unimplemented(test_input_path4)
    assert expected == result

def test7_class_forest():
    expected = {'DiscountPolicy': {'AmountDiscountPolicy': {}, 'PercentDiscountPolicy': {}}}

    result = collect_class_forest(test_input_path5)
    assert expected == result


def test8_unimplemented():
    expected = set()

    result = compute_unimplemented(test_input_path5)
    assert expected == result


def test9_class_forest():
    expected = {'AISMessageParser': {'AISMessage21Parser': {}, 'AISPositionReportParser': {'AISMessage02Parser': {}, 'AISMessage03Parser': {}, 'AISMessage01Parser': {}}, 'AISPositionReportBParser': {'AISMessage19Parser': {}, 'AISMessage18Parser': {}}, 'AISMessage24Parser': {}, 'AISMessage05Parser': {}, 'AISUTCParser': {'AISMessage04Parser': {}}, 'AisMessage27Parser': {}, 'AISMessage09Parser': {}}}

    result = collect_class_forest(test_input_path7)
    assert expected == result


def test10_unimplemented():
    expected = {'AISMessage01', 'AISMessage03', 'AISMessage24', 'AISUTCReport', 'AISMessage05', 'AISMessage09', 'AISPositionReport', 'AISMessage02', 'AISPositionInfo', 'AISMessage27', 'AISMessage19', 'AISMessage04', 'AISMessage18', 'AISMessage', 'AISMessage21', 'AISPositionReportB'}

    result = compute_unimplemented(test_input_path6)
    assert expected == result
