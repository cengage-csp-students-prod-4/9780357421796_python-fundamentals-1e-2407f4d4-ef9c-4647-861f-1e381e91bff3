import ipaddress
import random
import re

import pytest

try:
    from functions import AccessApi as mws
except ImportError:
    from accessApi import AccessApi as mws

base_url: str = "https://raw.githubusercontent.com/cengage-ide-content/"
billing_end_point: str = "APItesting/main/getBillingInfo.json"
customer_end_point: str = "APItesting/main/getCustomers.json"
site_end_point: str = "APItesting/main/getSites.json"

api: mws = mws(base_url)

billing_schema: dict = {
    "id": int,
    "FirstName": str,
    "LastName": str,
    "city": str,
    "state": str,
    "Lang": str,
    "SSN": str,
}

customer_schema: dict = {
    "id": int,
    "first_name": str,
    "last_name": str,
    "email": str,
    "ip_address": str,
    "address": str,
}

site_schema: dict = {
    "id": int,
    "address": str,
    "ThirdParty": str,
    "admin": str,
}


def random_record(end_point: str) -> dict:
    """Return one random record from the endpoint's JSON list."""
    data: list = api.get_end_point(end_point)
    assert isinstance(data, list) and len(data) > 0
    return random.choice(data)


def check_schema(record: dict, schema: dict) -> None:
    """Assert the record has exactly the schema's keys with matching value types."""
    assert set(record.keys()) == set(schema.keys())
    for key, expected_type in schema.items():
        assert isinstance(record[key], expected_type), f"{key} is not {expected_type}"


# TASK 2

# billing
def test_billing_status_code():
    assert api.get_status_code(billing_end_point) == 200


def test_billing_validate_schema():
    check_schema(random_record(billing_end_point), billing_schema)


def test_billing_validate_ssn():
    record: dict = random_record(billing_end_point)
    assert re.fullmatch(r"\d{3}-\d{2}-\d{4}", record["SSN"])


def test_billing_validate_time():
    assert api.get_elapsed_time(billing_end_point) < 60


# customers
def test_customers_status_code():
    assert api.get_status_code(customer_end_point) == 200


def test_customers_validate_schema():
    check_schema(random_record(customer_end_point), customer_schema)


def test_customers_validate_ssn():
    # Customers have no SSN; validate the IP address and email format instead.
    record: dict = random_record(customer_end_point)
    ipaddress.ip_address(record["ip_address"])  # raises ValueError if invalid
    assert re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", record["email"])


def test_customers_validate_time():
    assert api.get_elapsed_time(customer_end_point) < 60


# site
def test_site_status_code():
    assert api.get_status_code(site_end_point) == 200


def test_site_validate_schema():
    check_schema(random_record(site_end_point), site_schema)


def test_site_validate_ssn():
    # Sites have no SSN; validate the id and that text fields are non-empty.
    record: dict = random_record(site_end_point)
    assert record["id"] > 0
    assert record["address"].strip()
    assert record["admin"].strip()


def test_site_validate_time():
    assert api.get_elapsed_time(site_end_point) < 60


# TASK 3 - parametrized refactor
@pytest.mark.parametrize(
    "end_point",
    [billing_end_point, customer_end_point, site_end_point],
    ids=["billing", "customers", "sites"],
)
def test_status_code(end_point: str):
    assert api.get_status_code(end_point) == 200


@pytest.mark.parametrize(
    "end_point",
    [billing_end_point, customer_end_point, site_end_point],
    ids=["billing", "customers", "sites"],
)
def test_validate_time(end_point: str):
    assert api.get_elapsed_time(end_point) < 60