import pytest
from django.contrib.auth.models import User
from mixer.backend.django import mixer

from apps.trades.models import Balance, Currency, Item, Offer


@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    """Function for enable db access for pytest"""

    pass


@pytest.fixture()
def user_instance():
    """User instance without balance"""

    return mixer.blend(User)


@pytest.fixture()
def item_instance():
    """Item instance"""

    return mixer.blend(Item)


@pytest.fixture()
def currency_instance():
    """Currency with code, which is different from USD"""

    return mixer.blend(Currency)


@pytest.fixture()
def offer_purchase_instance(user_instance, item_instance):
    """Purchase offer instance without entry_quantity"""

    return mixer.blend(
        Offer,
        status="PURCHASE",
        user=user_instance,
        item=item_instance,
        price=10,
        entry_quantity=60,
        quantity=0,
    )


@pytest.fixture()
def offer_sell_instance(user_instance, item_instance):
    """Sell offer instance with entry_quantity"""

    return mixer.blend(
        Offer,
        status="SELL",
        user=user_instance,
        item=item_instance,
        price=11,
        entry_quantity=70,
        quantity=34,
    )


@pytest.fixture()
def user_instances():
    """Return two users instances for making trade between them"""

    return [mixer.blend(User), mixer.blend(User), mixer.blend(User)]


@pytest.fixture()
def item_instances():
    """Return two items instance"""

    return [mixer.blend(Item), mixer.blend(Item)]


@pytest.fixture()
def offer_instances(user_instances, item_instances):
    """Return six different offer instances"""

    buyer = user_instances[0]
    seller = user_instances[1]

    item_1 = item_instances[0]
    item_2 = item_instances[1]

    return [
        mixer.blend(
            Offer,
            status="PURCHASE",
            user=buyer,
            item=item_1,
            price=10,
            entry_quantity=43,
            quantity=6,
            is_active=True,
        ),
        mixer.blend(
            Offer,
            status="SELL",
            user=seller,
            item=item_2,
            entry_quantity=1,
            quantity=0,
            price=50,
            is_active=True,
        ),
        mixer.blend(
            Offer,
            status="SELL",
            user=seller,
            item=item_1,
            price=15,
            entry_quantity=56,
            quantity=6,
            is_active=True,
        ),
        mixer.blend(
            Offer,
            status="SELL",
            user=seller,
            item=item_1,
            price=7,
            entry_quantity=10,
            quantity=3,
            is_active=True,
        ),
        mixer.blend(
            Offer,
            status="SELL",
            user=seller,
            item=item_1,
            price=9,
            entry_quantity=25,
            quantity=5,
            is_active=False,
        ),
        mixer.blend(
            Offer,
            status="SELL",
            user=seller,
            item=item_1,
            price=8,
            entry_quantity=60,
            quantity=7,
            is_active=True,
        ),
        mixer.blend(
            Offer,
            status="SELL",
            user=seller,
            item=item_1,
            price=8,
            entry_quantity=44,
            quantity=7,
            is_active=True,
        ),
        mixer.blend(
            Offer,
            status="PURCHASE",
            user=user_instances[2],
            item=item_1,
            price=10,
            entry_quantity=43,
            quantity=6,
            is_active=True,
        ),
        mixer.blend(
            Offer,
            status="SELL",
            user=buyer,
            item=item_1,
            price=5,
            entry_quantity=42,
            quantity=6,
            is_active=True,
        ),
    ]
