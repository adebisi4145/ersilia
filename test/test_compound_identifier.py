import pytest
from ersilia.utils.identifiers.compound import CompoundIdentifier

@pytest.fixture
def compound_identifier():
    return CompoundIdentifier()

@pytest.mark.parametrize("header", ["smiles", "input", "SMILES", "INPUT"])
def test_is_input_header_positive(compound_identifier, header):
    """Test that valid input headers return True."""
    assert compound_identifier.is_input_header(header) is True

@pytest.mark.parametrize("header", ["key", "inchiKey", "KEY", "INCHIKEY"])
def test_is_key_header_positive(compound_identifier, header):
    """Test that valid key headers return True."""
    assert compound_identifier.is_key_header(header) is True

@pytest.mark.parametrize("inchikey", [
    "BSYNRYMUTXBXSQ-UHFFFAOYSA-N",
    "BQJCRHHNABKAKU-KBQPJGBKSA-N",
    "ZJPODVODJYKFHM-UHFFFAOYSA-N"
])
def test_is_inchikey_positive(compound_identifier, inchikey):
    """Test that valid InChIKeys return True."""
    assert compound_identifier._is_inchikey(inchikey) is True