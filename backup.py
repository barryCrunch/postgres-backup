import os
import datetime
import gzip
from sh import pg_dumpall
from azure.storage.blob import BlockBlobService, PublicAccess

def backup_db():
    try:
        # Create the BlockBlobService that is used to call the Blob service for the storage account
        block_blob_service = BlockBlobService(account_name=os.environ['ACCOUNT_NAME'], account_key=os.environ['ACCOUNT_KEY'])
        container_name = os.environ['CONTAINER_NAME']
        file_name = 'netbox-backup - ' + str(datetime.datetime.now()) + '.gz'
        with gzip.open(file_name, 'wb') as f:
            pg_dumpall('-h', os.environ['POSTGRESQL_HOST'], '-U', os.environ['DB_USER'],  _out=f)

        # Upload database backup
        block_blob_service.create_blob_from_path(container_name, 'netbox_backup - '+str(datetime.datetime.now()), file_to_upload)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    backup_db()
