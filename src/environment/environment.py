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


class EnvironmentMng:
    def init_environment(self, db_type: str, env_tag: str) -> None:
        """Stub for initializing an environment."""
        pass

    def clone_environment(self, src_env_tag: str, dst_env_tag: str) -> None:
        """Stub for cloning an environment."""
        pass

    def checkout_environment(self, env_tag: str) -> None:
        """Stub for checking out an environment."""
        pass

    def set_all_non_active(self) -> None:
        """Stub for setting all environments as non-active."""
        pass

    def list_environments(self) -> None:
        """Stub for listing all available environments."""
        pass

    def start_environment(self) -> None:
        """Stub for starting an environment."""
        pass

    def halt_environment(self) -> None:
        """Stub for halting an environment."""
        pass

    def reload_environment(self) -> None:
        """Stub for reloading an environment."""
        pass

    def environment_status(self) -> None:
        """Stub for getting environment status."""
        pass
