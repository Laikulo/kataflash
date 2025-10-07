"""
The interface between kataflash and katapult's flashtool.
Only this module should import or interact with kataflash.upstream and children
"""

import asyncio
import argparse
import sys
import runpy

from typing import Sequence


def invoke_raw():
    """
    Invoke the main of flashtool. This will not return. Args will be read from sys.argv.
    """
    runpy.run_module(
        "kataflash.upstream.flashtool", run_name="__main__", alter_sys=True
    )


def invoke_args(*args: Sequence[str]):
    """
    Invoke the main of flashtool with the given args. This will not return.
    """
    arg0 = sys.argv[0]
    sys.argv = [arg0, *args]
    invoke_raw()


def invoke(*args):
    old_argv = sys.argv.copy()
    try:
        invoke_args(*args)
    except SystemExit as e:
        # invoke_args will overwrite the args to get argparse to do what we want, this is needed to restore it
        # We do this inplace just in case something else has a ref to this around
        sys.argv.clear()
        sys.argv += old_argv
        return e.args[0]


def get_version():
    """
    Return a human-grokable version string for the katapult embedded within
    returns <missing> if it cannot be found
    """
    try:
        from .upstream.info import KATAPULT_REF
    except Exception as e:
        print(e)
        return "<missing>"
    else:
        return KATAPULT_REF
