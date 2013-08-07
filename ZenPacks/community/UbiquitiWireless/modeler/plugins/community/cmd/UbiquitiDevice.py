import re

from Products.DataCollector.plugins.CollectorPlugin import CommandPlugin
from Products.DataCollector.plugins.DataMaps import ObjectMap, RelationshipMap

mcaStatusParser = re.compile(r"""(([^,='\r\n]+)[,=]([^,='\r\n]+))""")

class UbiquitiDevice(CommandPlugin):
    command = "/usr/bin/ubntbox mca-status"

    def process(self, device, results, log):
        log.info("Modeler %s processing data for device %s",
            self.name(), device.id)

	ubiquitiProperties = {'distance' : 'ubnt_distance',
                              'longitude' : 'ubnt_longitude',
                              'latitude' : 'ubnt_latitude',
                              'freq' : 'ubnt_freq',
                              'essid' : 'ubnt_essid',
                              'apMac' : 'ubnt_apmac',
                              'deviceId' : 'ubnt_deviceid',
                              }

        objectmaps = []

        mcaStatusData = {}

        for label, quote_label, value in mcaStatusParser.findall(results):
            if quote_label:
                label = quote_label
            mcaStatusData[label] = value

        for key in ubiquitiProperties:
            if key in mcaStatusData:
                objectmaps.append(ObjectMap({
                    ubiquitiProperties[key] : mcaStatusData[key],
                    }))

        return objectmaps
