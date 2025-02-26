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

import os
from typing import Dict

import pytest

from config import load_user_values, parse_config


def create_temp_config_file(file_path: str, content: str) -> None:
    with open(file_path, "w") as file:
        file.write(content)


def test_parse_config():
    mock_data = {
        "${ora_image}": "OracleImage",
        "${ora_empty_env}": "empty",
        "${ora_pump_dir}": "pump_dir",
        "${ora_root_db_name}": "root_db",
        "${ora_plug_db_name}": "plug_db",
        "${ora_listener_port}": "1521",
        "${pg_image}": "PostgresImage",
        "${pg_empty_env}": "empty",
        "${pg_listener_port}": "5432",
        "${shpd_registry}": "ftp.example.com",
        "${shpd_registry_ftp_usr}": "ftpuser",
        "${shpd_registry_ftp_psw}": "ftppassword",
        "${shpd_registry_ftp_shpd_path}": "/shpd/path",
        "${shpd_registry_ftp_imgs_path}": "/env/imgs/path",
        "${host_inet_ip}": "192.168.1.1",
        "${domain}": "example.com",
        "${dns_type}": "DNS",
        "${ca_country}": "US",
        "${ca_state}": "State",
        "${ca_locality}": "Locality",
        "${ca_org}": "Org",
        "${ca_org_unit}": "Unit",
        "${ca_cn}": "common.name",
        "${ca_email}": "email@example.com",
        "${ca_passphrase}": "passphrase",
        "${cert_country}": "US",
        "${cert_state}": "State",
        "${cert_locality}": "Locality",
        "${cert_org}": "Org",
        "${cert_org_unit}": "Unit",
        "${cert_cn}": "common.name",
        "${cert_email}": "email@example.com",
        "${env_base_dir}": "/path/to/envs",
        "${db_sys_usr}": "sysuser",
        "${db_sys_psw}": "syspassword",
        "${db_usr}": "dbuser",
        "${db_psw}": "dbpassword",
        "${ingress_ip}": "192.168.1.2",
    }

    json_str = """{
        "ora": {
            "image": "${ora_image}",
            "empty_env": "${ora_empty_env}",
            "pump_dir_name": "${ora_pump_dir}",
            "root_db_name": "${ora_root_db_name}",
            "plug_db_name": "${ora_plug_db_name}",
            "net_listener_port": "${ora_listener_port}"
        },
        "pg": {
            "image": "${pg_image}",
            "empty_env": "${pg_empty_env}",
            "net_listener_port": "${pg_listener_port}"
        },
        "shpd_registry": {
            "ftp_server": "${shpd_registry}",
            "ftp_user": "${shpd_registry_ftp_usr}",
            "ftp_psw": "${shpd_registry_ftp_psw}",
            "ftp_shpd_path": "${shpd_registry_ftp_shpd_path}",
            "ftp_env_imgs_path": "${shpd_registry_ftp_imgs_path}"
        },
        "host_inet_ip": "${host_inet_ip}",
        "domain": "${domain}",
        "dns_type": "${dns_type}",
        "ca": {
            "country": "${ca_country}",
            "state": "${ca_state}",
            "locality": "${ca_locality}",
            "organization": "${ca_org}",
            "organizational_unit": "${ca_org_unit}",
            "common_name": "${ca_cn}",
            "email": "${ca_email}",
            "passphrase": "${ca_passphrase}"
        },
        "cert": {
            "country": "${cert_country}",
            "state": "${cert_state}",
            "locality": "${cert_locality}",
            "organization": "${cert_org}",
            "organizational_unit": "${cert_org_unit}",
            "common_name": "${cert_cn}",
            "email": "${cert_email}",
            "subject_alternative_names": []
        },
        "envs_dir": "${env_base_dir}",
        "db_default": {
            "sys_user": "${db_sys_usr}",
            "sys_psw": "${db_sys_psw}",
            "user": "${db_usr}",
            "psw": "${db_psw}"
        },
        "envs": [
            {
                "tag": "sample-1",
                "db": {
                    "type": "pg",
                    "image": "",
                    "sys_user": "",
                    "sys_psw": "",
                    "user": "",
                    "psw": "",
                    "upstreams": [
                        {
                            "tag": "upstream",
                            "type": "pg",
                            "user": "",
                            "psw": "",
                            "host": "",
                            "port": "5432",
                            "database": "",
                            "unix_user": "",
                            "dump_dir": "",
                            "enabled": false
                        }
                    ]
                },
                "services": [
                    {
                        "type": "traefik",
                        "ingress": true,
                        "tag": "traefik-1",
                        "image": "",
                        "envvars": null
                    },
                    {
                        "type": "custom-1",
                        "tag": "primary",
                        "image": "",
                        "envvars": null,
                        "ports": null,
                        "properties": {
                            "instance.name": "primary",
                            "instance.id": 1
                        }
                    },
                    {
                        "type": "nodejs",
                        "tag": "poke",
                        "image": "",
  "subject_alternative_name": "DNS:poke-${ingress_ip}.${domain}",
                        "ports": {
                            "http": "3000:3000"
                        },
                        "envvars": {
                            "USER": "user",
                            "PSW": "psw"
                        }
                    }
                ],
                "archived": false,
                "active": false
            }
        ]
    }"""

    for placeholder, value in mock_data.items():
        json_str = json_str.replace(placeholder, value)

    config = parse_config(json_str)

    assert config.ora.image == "OracleImage"
    assert config.pg.image == "PostgresImage"
    assert config.shpd_registry.ftp_server == "ftp.example.com"
    assert config.envs[0].tag == "sample-1"
    assert config.envs[0].db.type == "pg"
    assert config.db_default.sys_user == "sysuser"
    assert config.envs[0].services[0].type == "traefik"
    assert (
        config.envs[0].services[2].subject_alternative_name
        == "DNS:poke-192.168.1.2.example.com"
    )


def test_load_user_values_file_not_found() -> None:
    """Test handling of a non-existent file."""
    file_path = "non_existent_config.properties"
    with pytest.raises(FileNotFoundError):
        load_user_values(file_path)


def test_load_user_values_invalid_format() -> None:
    """Test handling of an improperly formatted file."""
    file_path = "invalid_config.properties"
    config_content = """
    key1=value1
    key2
    key3=value3
    """
    create_temp_config_file(file_path, config_content)

    with pytest.raises(ValueError):
        load_user_values(file_path)

    os.remove(file_path)


def test_load_user_values_empty_file() -> None:
    """Test handling of an empty file."""
    file_path = "empty_config.properties"
    config_content = ""
    create_temp_config_file(file_path, config_content)

    expected: Dict[str, str] = {}
    result = load_user_values(file_path)
    assert result == expected, "Failed to handle empty configuration file."

    os.remove(file_path)


def test_load_user_values_full_config() -> None:
    """Test loading a full configuration file with all key-value pairs."""
    file_path = "full_config.properties"
    config_content = """
    # Oracle (ora) Configuration
    ora_image=ghcr.io/lunaticfringers/shepherd/oracle:19.3.0.0_TZ40
    ora_empty_env=fresh-ora-19300
    ora_pump_dir=PUMP_DIR
    ora_root_db_name=ORCLCDB
    ora_plug_db_name=ORCLPDB1
    ora_listener_port=1521

    # PostgreSQL (pg) Configuration
    pg_image=ghcr.io/lunaticfringers/shepherd/postgres:17-3.5
    pg_empty_env=fresh-pg-1735
    pg_listener_port=5432

    # SHPD Registry Configuration
    shpd_registry=
    shpd_registry_ftp_usr=
    shpd_registry_ftp_psw=
    shpd_registry_ftp_shpd_path=shpd
    shpd_registry_ftp_imgs_path=imgs

    # Host and Domain Configuration
    host_inet_ip=127.0.0.1
    domain=sslip.io
    dns_type=autoresolving

    # Certificate Authority (CA) Configuration
    ca_country=IT
    ca_state=MS
    ca_locality=Carrara
    ca_org=LunaticFringe
    ca_org_unit=Development
    ca_cn=sslip.io
    ca_email=lf@sslip.io
    ca_passphrase=test

    # Certificate Configuration
    cert_country=IT
    cert_state=MS
    cert_locality=Carrara
    cert_org=LunaticFringe
    cert_org_unit=Development
    cert_cn=sslip.io
    cert_email=lf@sslip.io
    cert_subject_alternative_names=

    # Environment Directory Configuration
    env_base_dir=~/shpdenvs

    # Database Default Configuration
    db_sys_usr=sys
    db_sys_psw=sys
    db_usr=docker
    db_psw=docker
    """
    create_temp_config_file(file_path, config_content)

    expected: Dict[str, str] = {
        "ora_image": "ghcr.io/lunaticfringers/shepherd/oracle:19.3.0.0_TZ40",
        "ora_empty_env": "fresh-ora-19300",
        "ora_pump_dir": "PUMP_DIR",
        "ora_root_db_name": "ORCLCDB",
        "ora_plug_db_name": "ORCLPDB1",
        "ora_listener_port": "1521",
        "pg_image": "ghcr.io/lunaticfringers/shepherd/postgres:17-3.5",
        "pg_empty_env": "fresh-pg-1735",
        "pg_listener_port": "5432",
        "shpd_registry": "",
        "shpd_registry_ftp_usr": "",
        "shpd_registry_ftp_psw": "",
        "shpd_registry_ftp_shpd_path": "shpd",
        "shpd_registry_ftp_imgs_path": "imgs",
        "host_inet_ip": "127.0.0.1",
        "domain": "sslip.io",
        "dns_type": "autoresolving",
        "ca_country": "IT",
        "ca_state": "MS",
        "ca_locality": "Carrara",
        "ca_org": "LunaticFringe",
        "ca_org_unit": "Development",
        "ca_cn": "sslip.io",
        "ca_email": "lf@sslip.io",
        "ca_passphrase": "test",
        "cert_country": "IT",
        "cert_state": "MS",
        "cert_locality": "Carrara",
        "cert_org": "LunaticFringe",
        "cert_org_unit": "Development",
        "cert_cn": "sslip.io",
        "cert_email": "lf@sslip.io",
        "cert_subject_alternative_names": "",
        "env_base_dir": "~/shpdenvs",
        "db_sys_usr": "sys",
        "db_sys_psw": "sys",
        "db_usr": "docker",
        "db_psw": "docker",
    }
    result = load_user_values(file_path)
    assert result == expected, "Failed to load full configuration file."

    os.remove(file_path)
