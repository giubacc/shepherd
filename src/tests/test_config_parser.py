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

import unittest

from config import parse_config


class TestConfigParser(unittest.TestCase):

    def test_parse_config(self):
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

        self.assertEqual(config.ora.image, "OracleImage")
        self.assertEqual(config.pg.image, "PostgresImage")
        self.assertEqual(config.shpd_registry.ftp_server, "ftp.example.com")
        self.assertEqual(config.envs[0].tag, "sample-1")
        self.assertEqual(config.envs[0].db.type, "pg")
        self.assertEqual(config.db_default.sys_user, "sysuser")
        self.assertEqual(config.envs[0].services[0].type, "traefik")
        self.assertEqual(
            config.envs[0].services[2].subject_alternative_name,
            "DNS:poke-192.168.1.2.example.com",
        )
        print("Test passed successfully!")


if __name__ == "__main__":
    unittest.main()
