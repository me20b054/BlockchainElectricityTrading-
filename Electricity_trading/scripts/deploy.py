from brownie import accounts, config, ElectricityTrading_test, network
import os
import time


def deploy_electricity_trading():
    # account = accounts.add(os.getenv("private_key1"))
    # electricity_trading = ElectricityTrading_test.deploy({"from": account})
    # print(account)
    account1 = accounts.add(config["wallets"]["from_key1"])
    electricity_trading = ElectricityTrading_test.deploy(
        {"from": account1}, publish_source=True
    )
    # time.sleep(1)
    # account2 = accounts.add(config["wallets"]["from_key2"])
    # time.sleep(1)
    # account3 = accounts.add(config["wallets"]["from_key3"])
    # time.sleep(1)
    # account4 = accounts.add(config["wallets"]["from_key4"])
    # time.sleep(1)
    # # print(account1, account2, account3)
    # electricity_trading.sendToContract(account1, {"from": account1})


def main():
    deploy_electricity_trading()
