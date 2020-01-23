from bitcoinrpc.authproxy import AuthServiceProxy
from ip2geotools.databases.noncommercial import DbIpCity
import time

rpc_connection = AuthServiceProxy("http://student:WYVyF5DTERJASAiIiYGg4UkRH@blockchain.oss.unist.hr:8332")

def blokinfo():
    print ("________________________________________________________________________________________________")
    print("Podaci o blockchainu")
    print ("________________________________________________________________________________________________")
    chain=rpc_connection.getblockchaininfo()
    for i in chain:
        if (i=="softforks"):
            print("Softforks:")
            for j in chain[i]:
                print("       ",j)
        elif (i=="bip9_softforks"):
            print("bip9_softforks:")
            for k in chain[i]:
                print("       ",k,":",chain[i][k])
        else:
            print(i,":",chain[i])
    print()
    print("*************************************************************************************************")

def mreza():
    print ("________________________________________________________________________________________________")
    print("Podaci o mrezi")
    print ("________________________________________________________________________________________________")
    total=rpc_connection.getnettotals()
    peer=rpc_connection.getpeerinfo()
    print("Broj spojenih node-ova:",len(peer))
    print("Popis node-ova:")
    for i in (peer):
        print("Node",peer.index(i)+1," ","ID:",i["id"]," ","Adresa i port:",i["addr"])
    print("*************************************************************************************************")
    ip=input("Unesi IP adresu node-a za koji te zanimaju lokacijske informacije:")
    print(DbIpCity.get(ip, api_key='free'))

def blokexplore():
    blok=int(input("Unesi visinu zeljenog bloka:"))
    print ("________________________________________________________________________________________________")
    getblockhash=rpc_connection.getblockhash(blok)
    print("Podaci o bloku:", blok)
    print ("________________________________________________________________________________________________")
    get2=rpc_connection.getblock(str(getblockhash))
    print("Blok hash:",getblockhash)
    print("Vrijeme zapisivanja bloka:",time.ctime(get2["time"]))
    print ("Broj potvrda:",get2["confirmations"])
    print ("Broj transakcija:",get2["nTx"])
    print("Tezina rudarenja:", get2["difficulty"])
    print("Merkle root:",get2["merkleroot"])
    print ("Hash prethodnog bloka:",get2["previousblockhash"])
    print("Hash iduceg bloka:",get2["nextblockhash"])
    print ("________________________________________________________________________________________________")
    print ("________________________________________________________________________________________________")
    print("Popis transakcija u bloku:", blok)
    print ("________________________________________________________________________________________________")
    for i in (get2["tx"]):
        print ("Tx",get2["tx"].index(i)+1,":",i)
    print ("________________________________________________________________________________________________")
    print ("________________________________________________________________________________________________")
    transakcija=str(input("Unesi Txid za transakciju koja te zanima:"))
    gettx=rpc_connection.getrawtransaction(transakcija, 1, getblockhash)
    for i in gettx:
        print(i,":",gettx[i])
        print()
    print ("________________________________________________________________________________________________")

#blokinfo()
mreza()
#blokexplore()
