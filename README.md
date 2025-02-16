# Shepherd

![Lint](https://github.com/LunaticFringers/shepherd/actions/workflows/lint.yaml/badge.svg)

Shepherd implements an orchestrator tool capable of quickly provisioning
fully operational  development platforms using **Docker**.

> **Note:** Should a bug be found and not expected to be related with
> [known issues][issues], one should feel encouraged to file a new issue.

## Key Concepts

**Shepherd** utilizes two types of images,
each serving distinct and complementary purposes:

1. **Docker Images**
2. **Environment Images**

### Docker Images

Docker images are stateless by design, functioning much like executables
that can be deployed consistently across any environment platform.
They encapsulate the application and its dependencies but do not include
any runtime data, making them versatile and reusable in various contexts.

### Environment Images

Environment images, on the other hand, capture a snapshot of a specific
reference platform at a given point in time.
These images are more comprehensive, including:

- **Database State**: The complete state of the database is embedded within
  the environment image, allowing it to be immediately consumed by the
  corresponding database Docker image with no additional processing required.

- **Service Deployments**: The snapshot can also include the deployment state
  of services which are ready for immediate use upon consumption.

All of this state information is packaged into a `tar.gz` archive, which
can be optionally stored in a shared repository for easy access and
distribution among developers.

Once an environment image is pulled and imported into shepherd,
the corresponding environment state will evolve privately.

## Requirements

To ensure optimal performance and efficiency when working with shepherd
and managing multiple environments, certain hardware specifications
are recommended:

### Hardware

- **Memory**: A modern machine equipped with at least **32 GB of RAM**.
  This amount of memory is essential for running resource-intensive
  services like databases and for handling multiple containers simultaneously
  without performance degradation.

- **Storage**: A **large-capacity disk** is highly recommended,
  especially if you plan to store multiple environments locally.
  Each environment's database snapshot can consume significant
  storage space.

### OS & System Services

- **Linux platforms**
  - Ubuntu 22.04 LTS
  - Ubuntu 24.04 LTS

- **Windows platforms**
  - Windows 10/11
    - [WSL](https://learn.microsoft.com/en-us/windows/wsl/install)
    - [Ubuntu 22.04 LTS][ubuntu-22-04-wsl]
    - [Ubuntu 24.04 LTS][ubuntu-24-04-wsl]
    - [Docker](https://docs.docker.com/desktop/install/windows-install)

## Installation

> **Note:** It is highly recommended to use the tool having
> `NOPASSWD` option set for `sudo`.

To set the `NOPASSWD` option, execute:

```shell
sudo visudo
```

Add the following line replacing `$USER` with the actual username.

```text
$USER ALL=(ALL) NOPASSWD:ALL
```

> **Note:** If you do not have the `NOPASSWD` option set for `sudo`, you must
  prepend commands with `sudo` to run them with the necessary permissions.

Install the latest tool's version with the following command.

```text
sh -c "$(curl -sfL ftp://to-change/shp/shpdctli.sh)"
```

Use `VER` env variable to install the desired tool's version.

```text
VER=0.0.0 sh -c "$(curl -sfL ftp://to-change/shp/shpdctli.sh)"
```

## Quick Start

Once installed, query the environment registry for available images:

```text
$ shpdctl reg list
Environment        Size
-----------        ----
Env-Tag-1          7.22    (G)
Env-Tag-2          671.25  (M)
Env-Tag-3          53.78   (M)
...
```

Pull an environment:

```text
shpdctl --checkout env pull Env-Tag-2
```

Start it:

```text
shpdctl env up
```

Stop it:

```text
shpdctl env halt
```

## Consuming Environment Images

An environment image is typically created once, then pushed to the registry,
where it can be pulled and consumed countless times by any developer.
This ensures uniformity across different instances and reduces setup time.

Refer to documentation for [Consuming Environment Images].

## Authoring Environment Images

For creating, maintaining and pushing environment images to the registry refer
to [Authoring Environment Images].

## Full Commands and Options Documentation

Refer to the specific documentation for the currently supported commands
and options of [shpdctl].

## Database Service's Documentation

The database is provided as a containerized service with the status persisted
on an host's path.

Refer to the specific documentation for currently supported database services:

1. [Oracle]
2. Postgres

## Contributing

This section provides instructions for setting up the development environment
for contributors.

## Prerequisites

Ensure you have the following installed on your system:

- Python 3.10 or later
- `pip` (Python package installer)
- `virtualenv` (optional but recommended for managing dependencies)

To install these on Ubuntu, run:

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv -y
```

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone git@github.com:LunaticFringers/shepherd.git
   cd shepherd
   ```

2. **Create a Virtual Environment**

   Use a virtual environment to isolate dependencies:

   ```bash
   cd src
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**

   Install the required Python packages from `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

4. **Verify Installation**

   Test the CLI to ensure it works:

   ```bash
   python shpdctl.py --help
   ```

   You should see the list of available commands and options.

5. **Run the CLI**

   You can now use the CLI:

   ```bash
   python shpdctl.py <command> [options]
   ```

[issues]: https://github.com/LunaticFringers/shepherd/issues
[ubuntu-22-04-wsl]: https://apps.microsoft.com/detail/9pn20msr04dw?hl=en-us&gl=US
[ubuntu-24-04-wsl]: https://apps.microsoft.com/detail/9nz3klhxdjp5?hl=en-us&gl=US
[Consuming Environment Images]: docs/env-consume.md
[Authoring Environment Images]: docs/env-auth.md
[shpdctl]: docs/shpdctl.md
[Oracle]: docs/ORACLE.md
