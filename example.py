import etcd

client = etcd.Client(host='127.0.0.1', port=2379)

print('write')
client.write('foo', 1)

print('read')
print(client.read('foo').value)

print('done')
