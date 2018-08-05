# Copyright 2018 Brandon Schlueter
# This file is part of boron.
#
# Boron is free software: you can redistribute it and/or modify
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
    parser.add_argument('-a', '--host',
                        type=str,
                        default='0.0.0.0',
                        help='A host listen on.')
    parser.add_argument('-s', '--socket',
                        type=str,
                        help='A socket to listen on.')
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

    if args.port:
        listen_address = ':'.join([args.host, str(args.port)])
    else:
        listen_address = args.socket

    try:
        bjoern.listen(WSGIApp(), args.host or args.socket, args.port, reuse_port=args.reuse_port)
        print('Listening at {listen_address}'.format(listen_address=listen_address), file=sys.stderr)
        bjoern.run()
    except KeyboardInterrupt:
        print('\rExit requested', file=sys.stderr)
        exit()


if __name__ == '__main__':
    main()
