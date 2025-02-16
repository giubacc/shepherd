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

from dataclasses import dataclass, field
from typing import List, Optional

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
    registry: str
    sys_user: str
    sys_psw: str
    user: str
    psw: str
    upstreams: List[Upstream] = field(default_factory=list)

@dataclass
class ServiceProperty:
    key: str = ""
    value: str = ""

@dataclass
class ServicePort:
    http: str = ""

@dataclass
class ServiceEnvVar:
    key: str
    value: str

@dataclass
class Service:
    type: str
    tag: str
    registry: str
    ingress: Optional[bool] = None
    envvars: List[ServiceEnvVar] = field(default_factory=list)
    ports: List[ServicePort] = field(default_factory=list)
    properties: List[ServiceProperty] = field(default_factory=list)
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
    registry: str
    empty_env: str
    pump_dir_name: str
    root_db_name: str
    plug_db_name: str
    net_listener_port: str

@dataclass
class PostgresConfig:
    registry: str
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
