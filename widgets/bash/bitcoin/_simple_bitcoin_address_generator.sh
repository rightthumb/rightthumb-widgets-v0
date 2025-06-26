pip install bitcoin
python3 -c "
from bitcoin import *
priv = random_key()
pub = privtopub(priv)
addr = pubtoaddr(pub)
print('Private Key:', priv)
print('Bitcoin Address:', addr)
"