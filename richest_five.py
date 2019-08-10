#! /usr/bin/env python
# This script should read the accounts.json file and print out the five
# wealthiest accounts at the bank, in order from highest to lowest balance.
# Output should take the following form:
# <last name>, <first name>: $<balance>
import json

with open('accounts.json') as jsonfile:
    accounts = json.load(jsonfile)
    accounts_sorted = sorted(accounts, key=lambda account : account['balance'], reverse=True)
    accounts_out = json.dumps(accounts_sorted, indent=4, separators=(", ", ": "))
    with open('accounts.tmp', 'w') as outfile:
        outfile.write(accounts_out)
    for account in accounts_sorted[0:5]:
        print('{}, {}: ${}'.format(account['name']['last'],
                                   account['name']['first'],
                                   account['balance']))
