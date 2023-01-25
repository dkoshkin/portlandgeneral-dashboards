from decimal import Decimal
import json
import os

from portlandgeneral import OPowerApi


def json_lambda(x): return str(x) if type(x) is Decimal else x.__dict__

username = os.getenv('PGE_EMAIL')
password = os.getenv('PGE_PASSWORD')

client = OPowerApi(verbose=False)
client.login(
    username=username,
    password=password
)

current_customers = client.current_customers()
opower_uuid = current_customers.uuid
utility_account_uuid = current_customers.utility_accounts[0].uuid
utility_usage_hourly = client.utility_usage_hourly(utility_account_uuid, start_date='2023-01-22', end_date='2023-01-23')

print(json.dumps(utility_usage_hourly, indent=2, default=json_lambda))