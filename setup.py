#!/usr/bin/env python
from web3 import Web3, HTTPProvider
import json
import sys
import requests
from eth_account import Account
import DI_Transactions as dit

args = (sys.argv)[1:]

with open('network.json') as file:
    infor = json.load(file)
    privateKey = infor["privKey"]
    RecURL = infor["rpcUrl"]
    GasURL = infor["gasPriceUrl"]
    defGas = infor["defaultGasPrice"]

adres = dit.get_adress(privateKey)

web3 = Web3(HTTPProvider(RecURL))

def GetContractAddress():
    with open('registrar.json') as file:
        infor = json.load(file)
        return infor["registrar"]["address"]

def GetOwner():
    contract_by_address = web3.eth.contract(address = GetContractAddress(), abi = abiKYC)
    return contract_by_address.functions.GetOwner().call()

if args[0] == '--deploy':
    TX1 = dit.deploy_contract(person=adres, file_name="KYC_Registrar")
    TX2 = dit.deploy_contract(person=adres, file_name="Payment_Handler")
    print("KYC Registrar:", TX1['contractAddress'])
    print("Payment Handler:", TX2['contractAddress'])
    with open('registrar.json', 'w') as file:
        file.write(json.dumps({"registrar": {"address": TX1['contractAddress'], "startBlock": TX1['blockNumber']}, "payments": {"address": TX2['contractAddress'], "startBlock": TX2['blockNumber']}}))

if args[0] == '--owner' and args[1] == 'registrar':
    print("Admin account:", GetOwner())

if args[0] == '--chown' and args[1] == 'registrar' and len(args) == 3:
    newOwner = args[2]
    contract_by_address = web3.eth.contract(address = GetContractAddress(), abi = abiKYC)
    newAddress = web3.toChecksumAddress(newOwner[2:])
    senderAddress = dit.get_adress(privateKey)
    if(GetOwner() != senderAddress.address):
        print("Request cannot be executed")

    else:
        tx_wo_sign = contract_by_address.functions.RedactOwner(newAddress).buildTransaction({
    		'from': senderAddress.address,
    		'nonce': web3.eth.getTransactionCount(senderAddress.address),
    		'gas': 8000000,
    		'gasPrice': dit.get_gas_price(GasURL, defGas)
        })
        signed_tx = senderAddress.signTransaction(tx_wo_sign)

        txId = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        TX = web3.eth.waitForTransactionReceipt(txId)
        print("New admin account:", newOwner)
