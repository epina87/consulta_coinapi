# 15913 de 16132 (219)

from criptoexchange.models import TodoCoinApiIO, Cambio,ModelError 
from config import apiKey
import pytest

def test_todocoinapiio():
    todas = TodoCoinApiIO()
    assert isinstance(todas,TodoCoinApiIO)
    todas.trae(apiKey)

    assert len(todas.criptos) == 15913
    assert len(todas.no_criptos) == 220


def test_cambio_OK():
    btcEur = Cambio("BTC")
    assert btcEur.tasa is None
    assert btcEur.horafecha is None
    btcEur.actualiza(apiKey)

    assert btcEur.tasa > 0
    assert isinstance(btcEur.horafecha, str)

def test_cambio_no_OK():
    noOK = Cambio("KKTUA")
    assert noOK.tasa is None
    assert noOK.horafecha is None

    with pytest.raises(ModelError) as  exceptionInfo:
        noOK.actualiza(apiKey)

    assert str(exceptionInfo.value) == "550: You requested specific single item that we don't have at this moment."


