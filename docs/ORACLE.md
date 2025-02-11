# Containerized Oracle Database

The Oracle database is provided as a containerized service running within its
private Docker container.

Oracle's state persists across executions by utilizing a host directory
mounted on `/opt/oracle/oradata` within the container.

Additionally, users can specify a host directory to be used by Oracle as an
import directory.

## Oracle Container Registry

**shepherd** utilizes Oracle's database images pulled from the
[Oracle Container Registry][oracle-registry-web].

To download images directly from this registry, you'll need a valid Oracle
account, which you can create for free on the
[Oracle Container Registry site][oracle-registry-web].

### Accept Oracle Standard Terms and Restrictions

To pull Oracle images from the Oracle Container Registry, you must accept the
Oracle Standard Terms and Restrictions for the enterprise section
of the registry.

To do so, follow these steps:

1. Visit the [Oracle Container Registry][oracle-registry-web].
2. Click on the **Database** button.
3. Click the **continue** button for the **enterprise** row in the Repository
   table (usually the first row).

### Obtain the Auth Token

You need an authentication token to access the registry.

1. From the top-down menu on the Oracle web page, select **Auth Token**.
2. Copy the generated **Secret Key** from the new page and save it for the
   next step.

### Docker Login to Oracle Registry

Authenticate to the Oracle Container Registry using Docker:

```bash
docker login container-registry.oracle.com
```

Use `your-email@example.com` as the username and the previously copied
Secret Key as the password.

Once authenticated, Docker saves the auth token in `~/.docker/config.json`,
eliminating the need for repeated logins.

### Pull an Oracle Database Image

By default, **shepherd** uses the following image:

```text
container-registry.oracle.com/database/enterprise:19.3.0.0
```

To pull this image, execute:

```text
docker pull container-registry.oracle.com/database/enterprise:19.3.0.0
```

For specific requirements, browse available images on the
[Oracle Container Registry site][oracle-registry-web].

[oracle-registry-web]: https://container-registry.oracle.com
