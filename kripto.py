from bitcoinrpc.authproxy import AuthServiceProxy
import time

rpc_connection = AuthServiceProxy("http://student:WYVyF5DTERJASAiIiYGg4UkRH@blockchain.oss.unist.hr:8332")
#blok=int(input("Unesi blok:"))
get5=rpc_connection.getblockchaininfo()
print(get5)
#getinfo = rpc_connection.getnetworkinfo()
#getmempool=rpc_connection.getrawmempool()
#print (getinfo)
#print (getmempool)
#get=rpc_connection.getnodeaddresses(2)
#get=rpc_connection.validateaddress ("03fissjcsuvsjkavk")
#get=rpc_connection.getmempoolentry("74a6902a64471b65e2e536cc58663eae8d26ce1a5262c39dd2528c703ade05c0")
#getblockcount=rpc_connection.getblockcount()
#print (getblockcount)
print ("________________________________________________________________________________________________")
"""

getblockhash=rpc_connection.getblockhash(blok)
print("Blok hash:",getblockhash)
#getchaintxstats=rpc_connection.getchaintxstats(1660330)
#print(getchaintxstats)
print ("________________________________________________________________________________________________")
get2=rpc_connection.getblock(str(getblockhash))
print(get2)

print ("________________________________________________________________________________________________")
print ("Confirmations:",get2["confirmations"])
print ("Broj transakcija u bloku:",len(get2["tx"]))
print ("________________________________________________________________________________________________")

for i in (get2["tx"]):
    print ("Tx:",i)
print ("________________________________________________________________________________________________")

transakcija=str(input("Unesi Txid:"))
print (transakcija)
get3=rpc_connection.getrawtransaction(transakcija, 1, get2["hash"])
print(get3)
#print(get2["tx"])
print ("________________________________________________________________________________________________")

readable = time.ctime(get3["time"])
print("Vrijeme transakcije:",readable)

get4=rpc_connection.getpeerinfo()
for i in (get4):
    print ("id:",i["id"])
    print ("adresa:",i["addr"])
    print ("________________________________________________________________________________________________")
"""
#print (get4[0])
#get3=rpc_connection.gettxout("b38dd468087d58a43c80e6733f1e42eaa4289833ab476b831b1a6506b617dbf9")
#print (get3)
#get=rpc_connection.getblockheader("0000000000023d8b3bb168398fd56c98e786fa926356a09266bd92963c62d17c")
#get1=rpc_connection.getblockheader("0000000000033e147a5067eb851833dd875039493593fda466ae50f44473f941")
#print (get)
#print (get1)

#decoderawtransaction=rpc_connection.decoderawtransaction("e1c6a0a55563570c6a4faea67e4a000e5039103e2588f4de713dfd3da958e70b")
#print (decoderawtransaction)

#print (rpc_connection.uptime())
