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

import click

# Importing the modules from the `modules/` directory
from modules import db_module, env_module, svc_module

@click.group()
@click.option('-v', '--verbose', is_flag=True, help='Enable verbose mode.')
@click.option('-b', '--brief', is_flag=True, help='Brief output.')
@click.option('-y', '--yes', is_flag=True, help='Automatic yes to prompts; run non-interactively.')
@click.option('-a', '--all', is_flag=True, help='Apply to all.')
@click.option('-f', '--follow', is_flag=True, help='Follow log output.')
@click.option('-p', '--porcelain', is_flag=True, help='Produce machine-readable output.')
@click.option('-k', '--keep', is_flag=True, help='Keep instead of drop.')
@click.option('-r', '--replace', is_flag=True, help='Replace when already there.')
@click.option('-c', '--checkout', is_flag=True, help='Contextually checkout the environment.')
@click.option('-H', '--network-host', is_flag=True, help="Use host's network.")
@click.option('-n', '--no-gen-certs', is_flag=True, help='Do not generate certificates.')
def cli(verbose, brief, yes, all, follow, porcelain, keep, replace, checkout, network_host, no_gen_certs):
    """Shepherd CLI: A tool to manage your environment, services, and database."""
    pass

# Database commands
@cli.group()
def db():
    """Database related operations."""
    pass

@db.command()
def build():
    """Build dbms image."""
    db_module.build_dbms_image()

@db.command()
def bootstrap():
    """Bootstrap dbms service."""
    db_module.bootstrap_dbms_service()

@db.command()
def up():
    """Start dbms service."""
    db_module.start_dbms_service()

@db.command()
def halt():
    """Halt dbms service."""
    db_module.halt_dbms_service()

@db.command()
def stdout():
    """Show dbms service stdout."""
    db_module.show_dbms_stdout()

@db.command()
def shell():
    """Get a shell session for the dbms service."""
    db_module.get_dbms_shell()

@db.command()
def sql_shell():
    """Get a SQL session for the dbms service."""
    db_module.get_sql_shell()

@db.command()
@click.argument('user')
@click.argument('psw')
def create_user(user, psw):
    """Create a new user in the database."""
    db_module.create_user(user, psw)

@db.command()
@click.argument('user')
@click.argument('directory_name')
def create_dir(user, directory_name):
    """Create a new directory object in the database."""
    db_module.create_directory(user, directory_name)

@db.command()
@click.argument('user')
def drop_user(user):
    """Drop an existing user in the database."""
    db_module.drop_user(user)

# Environment commands
@cli.group()
def env():
    """Environment related operations."""
    pass

@env.command()
@click.argument('db_type')
@click.argument('env_tag')
def init(db_type, env_tag):
    """Init an environment with a dbms type and an environment's tag name."""
    env_module.init_environment(db_type, env_tag)

@env.command()
@click.argument('src_env_tag')
@click.argument('dst_env_tag')
def clone(src_env_tag, dst_env_tag):
    """Clone an environment."""
    env_module.clone_environment(src_env_tag, dst_env_tag)

@env.command()
@click.argument('env_tag')
def checkout(env_tag):
    """Checkout an environment."""
    env_module.checkout_environment(env_tag)

@env.command()
def noactive():
    """Set all environments as non-active."""
    env_module.set_all_non_active()

@env.command()
def list():
    """List all available environments."""
    env_module.list_environments()

@env.command()
def up():
    """Start environment."""
    env_module.start_environment()

@env.command()
def halt():
    """Halt environment."""
    env_module.halt_environment()

@env.command()
def reload():
    """Reload environment."""
    env_module.reload_environment()

@env.command()
def status():
    """Print environment's status."""
    env_module.environment_status()

# Service commands
@cli.group()
def svc():
    """Service related operations."""
    pass

@svc.command()
@click.argument('service_type')
def build(service_type):
    """Build service image."""
    svc_module.build_service_image(service_type)

@svc.command()
@click.argument('service_type')
def bootstrap(service_type):
    """Bootstrap service."""
    svc_module.bootstrap_service(service_type)

@svc.command()
@click.argument('service_type')
def up(service_type):
    """Start service."""
    svc_module.start_service(service_type)

@svc.command()
@click.argument('service_type')
def halt(service_type):
    """Stop service."""
    svc_module.stop_service(service_type)

@svc.command()
@click.argument('service_type')
def reload(service_type):
    """Reload service."""
    svc_module.reload_service(service_type)

@svc.command()
@click.argument('service_id')
def stdout(service_id):
    """Show service stdout."""
    svc_module.show_service_stdout(service_id)

@svc.command()
@click.argument('service_id')
def shell(service_id):
    """Get a shell session for the service."""
    svc_module.get_service_shell(service_id)

if __name__ == "__main__":
    cli()
