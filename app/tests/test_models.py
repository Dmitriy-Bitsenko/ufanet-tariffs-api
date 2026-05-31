
from sqlmodel import Session, SQLModel, create_engine
from app.models.tariffs import Tariff
import pytest


@pytest.fixture
def session():
    engine = create_engine("sqlite://")
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session
    SQLModel.metadata.drop_all(engine)
    




def test_create_and_read_tariff(session: Session):
    dictionary_test = {
            "name": "Игровой", "price": 450.00, "city": "Уфа", "speed_mbps": 120,
            "description": "Для тех кто любит поиграть"
            }

    tariff_1 = Tariff(**dictionary_test)
    session.add(tariff_1)
    session.commit()
    session.refresh(tariff_1)
    retrieved_tariff = session.get(Tariff, tariff_1.id)

    assert retrieved_tariff.id is not None
    assert retrieved_tariff.name == "Игровой"
    assert retrieved_tariff.price == 450.00
    assert retrieved_tariff.city == "Уфа"
    assert retrieved_tariff.speed_mbps == 120
    assert retrieved_tariff.description == "Для тех кто любит поиграть"

    


