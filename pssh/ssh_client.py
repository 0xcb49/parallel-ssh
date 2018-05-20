# This file is part of parallel-ssh.

# Copyright (C) 2014-2018 Panos Kittenis.

# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation, version 2.1.

# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

# flake8: noqa: F401

from warnings import warn

warn("Importing from pssh.ssh2_client is deprecated. Please update to "
     "from pssh.clients import SSHClient for the default client, or "
     "from pssh.clients.miko import SSHClient to continue using the paramiko "
     "client only.")

from .clients.miko import SSHClient, logger
