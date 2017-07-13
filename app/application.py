from app.provider.iam_provider_raw_v2 import IamProvider4RawV2
from app.provider.iam_provider_raw_v3 import IamProvider4RawV3
from app.provider.iam_provider_private import IamProvider4Private


CFG_PROVIDER_IP = '10.62.60.161'
# CFG_PROVIDER_IP = '10.62.97.18'
CFG_PROVIDER_PORT = '8089'
CFG_PROVIDER_PROTOCOL = 'http'

app_raw_v2 = IamProvider4RawV2(CFG_PROVIDER_IP, CFG_PROVIDER_PORT, CFG_PROVIDER_PROTOCOL)
app_raw_v3 = IamProvider4RawV3(CFG_PROVIDER_IP, CFG_PROVIDER_PORT, CFG_PROVIDER_PROTOCOL)
app_private = IamProvider4Private(CFG_PROVIDER_IP, CFG_PROVIDER_PORT, CFG_PROVIDER_PROTOCOL)



