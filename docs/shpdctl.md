# shpdctl

## Database Service

```sh
shpdctl db build
```

Build the database management system (DBMS) image.

```sh
shpdctl db bootstrap
```

Bootstrap the database management system (DBMS) service.

---

```sh
shpdctl db up
```

Start the DBMS service.

---

```sh
shpdctl db halt
```

Stop the DBMS service.

---

```sh
shpdctl db reload
```

Reload the DBMS service.

---

```sh
shpdctl db stdout
```

Show DBMS service stdout.

---

```sh
shpdctl db shell
```

Open a shell session within the DBMS service container.

---

```sh
shpdctl db sql-shell
```

Open a `sql-shell` session for the DBMS service.

---

```sh
shpdctl db create user [user] [psw]
```

Create a new user in the database with the specified username and password.

---

```sh
shpdctl db create dir [user] [directory-name]
```

Create a new directory object in the database for the specified user.

---

```sh
shpdctl db drop user [user]
```

Delete an existing user from the database.

---

> **NOTE** This parameter setting is valid only for Oracle.

```sh
shpdctl db import dump [user] [dump-file] [schema]
                    [dump-file] [schema]
                    [import-config-file]
```

Import an existing schema into the database from a dump file or import
configuration file.

---

> **NOTE** This parameter setting is valid only for PostgreSQL.

```sh
shpdctl db import dump [dump-file]
```

Import a dump in the database.

---

```sh
shpdctl db exec script [sql-file]
                    [sql-file] [user] [pwd]
```

Execute a `sql` script as a sys user or a specified user with password.

---

```sh
shpdctl db list users
```

List all users in the DBMS.

---

```sh
shpdctl db upstream [remote]
```

Use an upstream DBMS.

---

```sh
shpdctl db downstream
```

Set DBMS to the local (downstream) service

---

```sh
shpdctl db sync [upstream]
```

Sync the DBMS local service's status with an upstream DBMS.

## Environment Management

```sh
shpdctl env init [db-type] [env-tag]
```

Initialize a new environment with a specified DBMS type and environment tag name.

---

```sh
shpdctl env clone [src-env-tag] [dst-env-tag]
```

Clone an existing environment (requires root privileges).

---

```sh
shpdctl env checkout [env-tag]
```

Checkout an environment.

---

```sh
shpdctl env noactive
```

Set all environments as non-active.

---

```sh
shpdctl env list
```

List all available environments.

---

```sh
shpdctl env up
```

Start the environment.

---

```sh
shpdctl env halt
```

Stop the environment.

---

```sh
shpdctl env reload
```

Reload the environment.

---

```sh
shpdctl env status
```

Display the status of the specified environment.

---

```sh
shpdctl env clean
```

Clean up the specified environment.

---

```sh
shpdctl env archive [env-tag]
```

Archive the specified environment (requires root privileges).

---

```sh
shpdctl env restore [env-tag]
```

Restore an archived environment (requires root privileges).

---

```sh
shpdctl env push [env-tag]
```

Push an environment image to the environment registry.

---

```sh
shpdctl env fetch [env-tag]
```

Fetch an environment image from the environment registry.

---

```sh
shpdctl env pull [env-tag]
```

Fetch an environment image from the environment registry and import it.

## Environment Registry

```sh
shpdctl reg list
```

List all the environment images on the environment registry.

## System

```sh
shpdctl [--all] sys prune
```

Delete all the archived environments and their archived images.

## Available Env-Vars

### SHPD_CFG_PATH

Specify shpdctl's config file (default: ~/.shpdctl.json).

### SHPD_DB_CONTAINER_NAME

Specify the dbms docker container name.

### SHPD_ENVS_BASE_DIR

Specify the base directory to use for storing the environments.

### SHPD_ENV_TAG

Specify the environment's tag to use.

### SHPD_ENV_DB_TYPE

Specify the environment's dbms to use: Oracle or Postgres.

### SHPD_ENV_DB_DATA_REL_DIR

Specify the relative directory used by dbms to store its data.

### SHPD_ENV_DB_SHARED_REL_DIR

Specify the relative directory used by dbms to mount its directory objects.

### SHPD_DB_REGISTRY

Specify the dbms docker upstream registry.

### SHPD_DB_TAG

Specify the dbms docker image tag.

### SHPD_ENV_DB_SYS_USER

Specify the dbms sys user to use.

### SHPD_ENV_DB_SYS_PSW

Specify the dbms sys password to use.

### SHPD_ENV_DB_APP_USER

Specify the dbms user to use for the environment.

### SHPD_ENV_DB_APP_PSW

Specify the dbms user password to use for the environment.

### SHPD_ENV_ORA_PUMP_DIR_NAME

Specify the Oracle's pump directory name.

### SHPD_ENV_ORA_ROOT_DB_NAME

Specify the Oracle's container database (CDB) name.

### SHPD_ENV_DB_NAME

Specify the database name.

### SHPD_ENV_DB_NET_LST_PORT_HOST

1. Specify the Oracle-host port mapping for the Oracle Net
Listener Port (1521).
2. Specify the Postgres-host port mapping for the Postgres Net
Listener Port (5432).
