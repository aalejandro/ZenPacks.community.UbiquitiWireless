import re

from Products.ZenUtils.Utils import getExitMessage
from Products.ZenRRD.CommandParser import CommandParser

perfParser = re.compile(r"""(([^,='\r\n]+)[,=]([^,='\r\n]+))""")


class _BadData(Exception):
    """
    Raised by splitMultLine when plugin output is not parseable.
    """

class McaStatus(CommandParser):
    def processPerfData(self, rawPerfData):
        perfData = {}

        for label, quote_label, value in perfParser.findall(rawPerfData):
            if quote_label:
                label = quote_label
            try:
                value = float(value.strip())
            except:
                value = 'U'
            perfData[label] = value

        return perfData

    def processResults(self, cmd, result):
        output = cmd.result.output
        exitCode = cmd.result.exitCode
        severity = cmd.severity
        if exitCode == 0:
            severity = 0
        elif exitCode == 2:
            severity = min(severity + 1, 5)

        evt = {
                "device": cmd.deviceConfig.device,
                "message": output,
                "severity": severity,
                "component": cmd.component,
                "eventKey": cmd.eventKey,
                "eventClass": cmd.eventClass,
            }

        perfData = self.processPerfData(output)
        evt.update({
                   "performanceData": perfData,
                   "summary": 'mca-status'
        })

        for dp in cmd.points:
            if dp.id in perfData:
                result.values.append((dp, perfData[dp.id]))

        result.events.append(evt)
