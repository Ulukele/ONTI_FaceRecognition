#!/usr/bin/env python

### Put your code below this comment ###
#print("Show must go on")

from eth_account import Account
from web3 import Web3, HTTPProvider, IPCProvider, WebsocketProvider
from py_ecc import secp256k1

def GetPerson():
    with open('person.json') as file:
    	infor = json.load(file)
        return infor['id']

def HashIt(ident, pin):
    ident = (ident[:8] + ident[9:13] + ident[14:18] + ident[19:23] + ident[24:])

    pin = str(pin)
    pin = [('0'+pin[0]), ('0'+pin[1]), ('0'+pin[2]), ('0'+pin[3])]

    #Calculate privateKey
    data = b''
    for i in range(4):
        data = (w3.sha3(data).hex())[2:]
        data = data + ident + pin[i]
        #print(i, data)
        data = bytes.fromhex(data)
    data = (w3.sha3(data).hex())[2:]
    privateKey = data
    return privateKey

def HashCodeWithPinCodeAndPerson(PINcode):
    personInfo = GetPerson()
    key = HashIt(GetPerson, PINcode)
    return key

def BalanceAll(balance):
    currency = ["wei", "kwei", "mwei", "gwei", "szabo", "finney", "poa"]
    ind = 0
    while (balance > 10):
        balance /= 1000
        ind += 1
    if balance < 1:
        balance *= 1000
        ind -= 1
    balance = str(round(balance, 6))
    if balance[-1] == '0':
        balance = balance[:-2]
    return (balance, currency[ind])

def IGetAdress(privateKey):
    adress = Account.privateKeyToAccount("0x"+privateKey)
    return adress

def PrintBalance(privateKey):
    adress = IGetAdress(privateKey)
    balance = BalanceAll(web3.eth.getBalance(adress))
    print("Balance on {0} is {1} {2}".format('"'+ adress[2:] +'"', balance[0], balance[1]))

args = (sys.argv)[1:]
sizeM = len(args)

if args[0] == "--balance":
    if sizeM == 2:
        PINcode = arg[1]
        Key = HashCodeWithPinCodeAndPerson(PINcode)
        PrintBalance(Key)
