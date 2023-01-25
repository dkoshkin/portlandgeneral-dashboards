from decimal import Decimal
import json
import os

from portlandgeneral import OPowerApi


def json_lambda(x): return str(x) if type(x) is Decimal else x.__dict__

username = os.getenv('PGE_EMAIL')
password = os.getenv('PGE_PASSWORD')

client = OPowerApi(verbose=True)
client.login(
    username=username,
    password=password
)

current_customers = client.current_customers()
print('getting customer info')
print(json.dumps(current_customers, indent=2, default=json_lambda))

opower_uuid = current_customers.uuid
utility_account_uuid = current_customers.utility_accounts[0].uuid

print('downloading file ...')
client.download_usage(opower_uuid, start_date='2023-01-22', end_date='2023-01-23')
