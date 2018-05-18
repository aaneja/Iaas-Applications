
#sudo pip install msrestazure
#sudo pip install azure-datalake-store
import argparse
from msrestazure.azure_active_directory import AADTokenCredentials
from azure.datalake.store import core, lib, multithread

parser = argparse.ArgumentParser()
parser.add_argument('--tenant', '-t', help="AAD Tenant id linked to the ADLS account. Eg: contoso.onmicrosoft.com", type= str, required=True)
parser.add_argument('--adlsAccountName', '-a', help="Short name of ADLS account", type= str, required=True)
parser.add_argument('--dir', '-d', help="Directory to ls", type= str, default= '/')

args=parser.parse_args()

adlCreds = lib.auth(tenant_id=args.tenant, resource = 'https://datalake.azure.net/')

## Create a filesystem client object
adl = core.AzureDLFileSystem(adlCreds, store_name=args.adlsAccountName)

print adl.ls(args.dir)