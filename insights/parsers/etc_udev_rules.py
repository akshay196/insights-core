"""
EtcUdevRules - file ``/etc/udev/rules.d/``
==========================================

This module is similar to the :py:mod:`insights.parsers.udev_rules`
but parse .rules files under ``/etc/ude/rules.d/`` directory instead.

The parsers included in this module are:

UdevRules40Redhat - file ``/etc/udev/rules.d/40-redhat.rules``
--------------------------------------------------------------

"""
from insights import parser
from insights.core import LogFileOutput
from insights.specs import Specs


@parser(Specs.udev_40_redhat_rules)
class UdevRules40Redhat(LogFileOutput):
    """
    Read the content of ``/etc/udev/rules.d/40-redhat.rules`` file.

    .. note::

        The syntax of the `.rules` file is complex, and no rules require to
        get the serialized parsed result currently.  An only existing rule's
        supposed to check the syntax of some specific line, so here the
        :class:`insights.core.LogFileOutput` is the base class.

    Sample input::

        # do not edit this file, it will be overwritten on update
        # CPU hotadd request
        SUBSYSTEM=="cpu", ACTION=="add", TEST=="online", ATTR{online}=="0", ATTR{online}="1"

        # Memory hotadd request
        SUBSYSTEM!="memory", ACTION!="add", GOTO="memory_hotplug_end"
        PROGRAM="/bin/uname -p", RESULT=="s390*", GOTO="memory_hotplug_end"

        LABEL="memory_hotplug_end"

    Examples:
        >>> 'LABEL="memory_hotplug_end"' in udev_rules.lines
        True
    """
    pass
