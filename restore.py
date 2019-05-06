import os, datetime, gzip, argparse
from sh import psql
from azure.storage.blob import BlockBlobService, PublicAccess


def restore_db():
    try:
        # Define block_blob_service
        block_blob_service = BlockBlobService(account_name=os.environ['ACCOUNT_NAME'], account_key=os.environ['ACCOUNT_KEY'])
        container_name = os.environ['CONTAINER_NAME']

        # Use Argparse to grab file name to pull from azure
        parser = argparse.ArgumentParser()
        parser.add_argument("file_name", help="File you want to restore from Azure")
        args = parser.parse_args()

        # Set local path for file donwload
        local_path = os.getcwd() + '/'

        # Grab file from Azure
        block_blob_service.get_blob_to_path(container_name, args.file_name, local_path + args.file_name)

        with gzip.open(args.file_name, 'rb') as f:
                psql('-h', os.environ['POSTGRESQL_HOST'], '-U', os.environ['DB_USER'], _in=f)

    except Exception as e:
        print(e)

if __name__ == '__main__':
    restore_db()
