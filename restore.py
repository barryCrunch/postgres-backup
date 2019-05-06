import os, datetime, gzip, argparse
from sh import psql
from azure.storage.blob import BlockBlobService, PublicAccess


def restore():
    try:
        # Use Argparse to grab file name to pull from azure
        parser = argparse.ArgumentParser()
        parser.add_argument("file_name", help="File you want to restore from Azure")
        args = parser.parse_args()

        # Set local path for file donwload
        local_path = os.getcwd() + '/'

        # Grab file from Azure
        block_blob_service.get_blob_to_path(container_name, args.file_name, local_path + args.file_name)

        # Unzip File
        f = gzip.open(args.file_name, 'rb')
        unzipped_backup = f.read()
        f.close

        # Restore Database
        psql('-h', os.environ['POSTGRESQL_HOST'], '-U', os.environ['DB_USER'], '-f', unzipped_backup)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    backup_db()
