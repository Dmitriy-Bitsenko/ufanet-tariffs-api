from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine
from models.tariffs import Tariff
from datetime import date
import pytest


@pytest.fixture
def create_db():
    engine = create_engine("sqlite://")
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session
    SQLModel.metadata.drop_all(engine)
    




def test_tariff(session: Session, client: TestClient):
    

    assert id == 1
    assert name == "Игровой"
    assert price == 450.00
    assert city == "Уфа"
    assert speed_mbps == 120 
    assert description == "Тариф"
    assert created_at == date.datetime()
