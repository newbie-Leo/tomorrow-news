#!/usr/bin/env python
import os
import sys

import mimetypes
mimetypes.types_map['.svg'] = 'image/svg+xml'

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "news_collector.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
