from typing import List

import pytest

from proto_parser.proto_parser import ProtoFile, MessageField, ScopedSection, WORD_PROTO_FILE, WORD_ROOT
from simple_expected import EXPECTED_SIMPLE_ENUM, EXPECTED_SIMPLE_SERVICE
from t1_expected import T1_LINES, T1_BASKET_SERVICE, T1_SCOPED_SECTION_EXPECTED

lines1 = [
    ""
]


@pytest.mark.parametrize("file, expected", [
    ("t1.proto", T1_LINES),
])
def test_get_wraped_text(file: str, expected: List[str]):
    with open(file) as f:
        lines = f.read().splitlines()
        result = ProtoFile.get_wraped_text(lines)
        assert result == expected


@pytest.mark.parametrize("line, expected", [
    ("service BasketService {", "BasketService"),
    ("message UpdateBasketReq {", "UpdateBasketReq"),
])
def test_extract_type_name_from_line(line, expected):
    result = ProtoFile.extract_type_name_from_line(line)
    assert result == expected


@pytest.mark.parametrize("file, expected", [
    ("simple_enum.proto", EXPECTED_SIMPLE_ENUM),
])
def test_extract_enum(file, expected):
    with open(file) as f:
        lines = f.read().splitlines()
        result, _ = ProtoFile.extract_enum(lines)
        assert result == expected


@pytest.mark.parametrize("file, expected", [
    ("simple_service.proto", EXPECTED_SIMPLE_SERVICE),
])
def test_extract_service(file, expected):
    result, _ = ProtoFile.extract_service(T1_BASKET_SERVICE)
    assert result == expected


@pytest.mark.parametrize("line, expected", [
    ("  Basket basket = 1;", MessageField(name="basket", data_type="Basket")),
])
def test_extract_field_from_line(line, expected):
    result = ProtoFile.extract_field_from_line(line)
    assert result == expected


@pytest.mark.parametrize("file, expected", [
    ("t1.proto", T1_SCOPED_SECTION_EXPECTED),
])
def test_extract_scope(file, expected):
    with open(file) as f:
        lines = f.read().splitlines()
        sc = ScopedSection(name=WORD_ROOT, data_type=WORD_PROTO_FILE)
        result, idx = ProtoFile.extract_scope(lines, sc)
        assert result == expected
