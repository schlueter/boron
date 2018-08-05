# Copyright 2017 Brandon Schlueter
# This file is part of boron.
#
# Ghh is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from __future__ import print_function

import argparse
import sys

import bjoern

from boron import description, default_config_file, WSGIApp


def parse_args(description, default_config_file):
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('host_or_socket',
                        type=str,
                        help='A hostname or socket to listen on.')
    parser.add_argument('-p', '--port',
                        type=int,
                        help='A port to listen on.')
    parser.add_argument('-r', '--reuse-port',
                        action='store_true',
                        help='Enables SO_REUSEPORT if available.')
    parser.add_argument('-c', '--config-file',
                        type=argparse.FileType('r'),
                        help='Specify the path to a configuration file.')
    return parser.parse_args()

def main():
    args = parse_args(description, default_config_file)
    try:
        app = WSGIApp()
        bjoern.listen(app, args.host_or_socket, args.port, reuse_port=args.reuse_port)
        listen_address = args.host_or_socket + (':' + str(args.port)) if args.port else ''
        print('Listening at {listen_address}'.format(listen_address=listen_address) , file=sys.stderr)
        bjoern.run()
    except KeyboardInterrupt:
        print('\rExit requested', file=sys.stderr)
        exit()

if __name__ == '__main__':
    main()
