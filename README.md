# postgres-backup
A very simple docker container that connects to a postgresql database, performs a pg_dumpall, and then pushes the backup into an Azure blob storage on a cron schedule. The backup takes place every 30 minutes. I will probably make this variable in the future but it is what is is for now.

---

## Primary Functions
#### Backup
The container if started with the `./startup.sh` command will automaticlaly start taking backups of the postgresql database every half hour on the hour. Manual backups can be taken by execing into the container and running the commands below. The backup is a `pg_dumpall` and will grab all databases in a cluster.

#### Restore
There is also the ability to restore from any backup located in the Aure Blob storage container by exec-ing into the container and running the restore command. The how-to is listed below.

---

## How to run the container
```docker run -d -t --env-file env.file mkbarry/postgres-backup:latest ./startup.sh```
This will start the cron job and kick off the backup schedule of every 30 minutes on the hour/half hour. If you would like to just peform a manual backup then just exec into the container and execute the python script.
```
docker exec -it {container-name} /bin/bash
python3 backup.py
```
To restore a backup all you have to do is call the restore script and pass the name of the backup that you would like to restore.
```
python3 restore.py {backup-file-name}
```
This will pull the backup down from Azure and restore it to the postgresql host specified in the environment variable. BE CAREFUL - don't restore this to an existing database. The restore should be done to an empty database.

---

## Environment Variables
| Variable        | Purpose       | 
| -------------   | :-------------|
| ACCOUNT_NAME    | This is your azure storage account name.       |
| COINTAINER_NAME | The name of the storage container on Azure.    |
| ACCOUNT_KEY     | The account key to access the storage account. |
| POSTGRESQL_HOST | The host containing the postgresql database.   |
| DB_USER         | User to authenticate to the database.          |
| PGPASSWORD      | Password for the database.                     |
