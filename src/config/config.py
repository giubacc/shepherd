# MIT License
#
# Copyright (c) 2025 Lunatic Fringers
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import json
import os
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class Upstream:
    tag: str
    type: str
    user: str
    psw: str
    host: str
    port: str
    database: str
    unix_user: str
    dump_dir: str
    enabled: bool


@dataclass
class Database:
    type: str
    image: Optional[str]
    sys_user: str
    sys_psw: str
    user: str
    psw: str
    upstreams: List[Upstream] = field(default_factory=list)


@dataclass
class Service:
    type: str
    tag: str
    image: str
    ingress: Optional[bool] = None
    envvars: Optional[dict[str, str]] = field(default_factory=dict)
    ports: Optional[dict[str, str]] = field(default_factory=dict)
    properties: Optional[dict[str, str]] = field(default_factory=dict)
    subject_alternative_name: Optional[str] = None


@dataclass
class Environment:
    tag: str
    db: Database
    services: List[Service]
    archived: bool
    active: bool


@dataclass
class OracleConfig:
    image: str
    empty_env: str
    pump_dir_name: str
    root_db_name: str
    plug_db_name: str
    net_listener_port: str


@dataclass
class PostgresConfig:
    image: str
    empty_env: str
    net_listener_port: str


@dataclass
class ShpdRegistry:
    ftp_server: str
    ftp_user: str
    ftp_psw: str
    ftp_shpd_path: str
    ftp_env_imgs_path: str


@dataclass
class CAConfig:
    country: str
    state: str
    locality: str
    organization: str
    organizational_unit: str
    common_name: str
    email: str
    passphrase: str


@dataclass
class CertConfig:
    country: str
    state: str
    locality: str
    organization: str
    organizational_unit: str
    common_name: str
    email: str
    subject_alternative_names: List[str] = field(default_factory=list)


@dataclass
class DbDefault:
    sys_user: str
    sys_psw: str
    user: str
    psw: str


@dataclass
class Config:
    ora: OracleConfig
    pg: PostgresConfig
    shpd_registry: ShpdRegistry
    host_inet_ip: str
    domain: str
    dns_type: str
    ca: CAConfig
    cert: CertConfig
    envs_dir: str
    db_default: DbDefault
    envs: List[Environment] = field(default_factory=list)


def parse_config(json_str: str) -> Config:
    data = json.loads(json_str)

    def parse_upstream(item: Any) -> Upstream:
        return Upstream(
            tag=item["tag"],
            type=item["type"],
            user=item["user"],
            psw=item["psw"],
            host=item["host"],
            port=item["port"],
            database=item["database"],
            unix_user=item["unix_user"],
            dump_dir=item["dump_dir"],
            enabled=item["enabled"],
        )

    def parse_database(item: Any) -> Database:
        return Database(
            type=item["type"],
            image=item["image"],
            sys_user=item["sys_user"],
            sys_psw=item["sys_psw"],
            user=item["user"],
            psw=item["psw"],
            upstreams=[
                parse_upstream(upstream) for upstream in item["upstreams"]
            ],
        )

    def parse_service(item: Any) -> Service:
        return Service(
            type=item["type"],
            tag=item["tag"],
            image=item["image"],
            ingress=item.get("ingress"),
            envvars=item.get("envvars", {}),
            ports=item.get("ports", {}),
            properties=item.get("properties", {}),
            subject_alternative_name=item.get("subject_alternative_name"),
        )

    def parse_environment(item: Any) -> Environment:
        return Environment(
            tag=item["tag"],
            db=parse_database(item["db"]),
            services=[parse_service(service) for service in item["services"]],
            archived=item["archived"],
            active=item["active"],
        )

    def parse_oracle_config(item: Any) -> OracleConfig:
        return OracleConfig(
            image=item["image"],
            empty_env=item["empty_env"],
            pump_dir_name=item["pump_dir_name"],
            root_db_name=item["root_db_name"],
            plug_db_name=item["plug_db_name"],
            net_listener_port=item["net_listener_port"],
        )

    def parse_postgres_config(item: Any) -> PostgresConfig:
        return PostgresConfig(
            image=item["image"],
            empty_env=item["empty_env"],
            net_listener_port=item["net_listener_port"],
        )

    def parse_shpd_registry(item: Any) -> ShpdRegistry:
        return ShpdRegistry(
            ftp_server=item["ftp_server"],
            ftp_user=item["ftp_user"],
            ftp_psw=item["ftp_psw"],
            ftp_shpd_path=item["ftp_shpd_path"],
            ftp_env_imgs_path=item["ftp_env_imgs_path"],
        )

    def parse_ca_config(item: Any) -> CAConfig:
        return CAConfig(
            country=item["country"],
            state=item["state"],
            locality=item["locality"],
            organization=item["organization"],
            organizational_unit=item["organizational_unit"],
            common_name=item["common_name"],
            email=item["email"],
            passphrase=item["passphrase"],
        )

    def parse_cert_config(item: Any) -> CertConfig:
        return CertConfig(
            country=item["country"],
            state=item["state"],
            locality=item["locality"],
            organization=item["organization"],
            organizational_unit=item["organizational_unit"],
            common_name=item["common_name"],
            email=item["email"],
            subject_alternative_names=item.get("subject_alternative_names", []),
        )

    def parse_db_default(item: Any) -> DbDefault:
        return DbDefault(
            sys_user=item["sys_user"],
            sys_psw=item["sys_psw"],
            user=item["user"],
            psw=item["psw"],
        )

    return Config(
        ora=parse_oracle_config(data["ora"]),
        pg=parse_postgres_config(data["pg"]),
        shpd_registry=parse_shpd_registry(data["shpd_registry"]),
        host_inet_ip=data["host_inet_ip"],
        domain=data["domain"],
        dns_type=data["dns_type"],
        ca=parse_ca_config(data["ca"]),
        cert=parse_cert_config(data["cert"]),
        envs_dir=data["envs_dir"],
        db_default=parse_db_default(data["db_default"]),
        envs=[parse_environment(env) for env in data["envs"]],
    )


def load_user_values(file_path: str) -> Dict[str, str]:
    """
    Loads a file holding the user's values in key=value format
    into a dictionary.

    Args:
        file_path (str): Path to the user's values file.

    Returns:
        Dict[str, str]: A dictionary containing the key-value pairs
        from the file.

    Raises:
        FileNotFoundError: If the configuration file does not exist.
        ValueError: If the file is improperly formatted.
    """
    user_values: Dict[str, str] = {}

    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"The configuration file '{file_path}' does not exist."
        )

    try:
        with open(file_path, "r") as file:
            for line in file:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue

                if "=" in line:
                    key, value = line.split("=", 1)
                    user_values[key.strip()] = value.strip()
                else:
                    raise ValueError(
                        f"Invalid line format in config file: '{line}'"
                    )
    except Exception as e:
        raise ValueError(f"Error reading configuration file: {e}")

    return user_values
