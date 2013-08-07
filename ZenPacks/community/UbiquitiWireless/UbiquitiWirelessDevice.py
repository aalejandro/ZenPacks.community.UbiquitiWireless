from Products.ZenModel.Device import Device

class UbiquitiWirelessDevice(Device):
    ubnt_distance = None
    ubnt_longitude = None
    ubnt_latitude = None
    ubnt_freq = None
    ubnt_essid = None
    ubnt_apmac = None
    ubnt_deviceid = None

    _properties = Device._properties + (
        {'id': 'ubnt_distance', 'type': 'int'},
       	{'id': 'ubnt_longitude', 'type': 'float'},
        {'id': 'ubnt_latitude', 'type': 'float'},
        {'id': 'ubnt_freq', 'type': 'int'},
        {'id': 'ubnt_essid', 'type': 'string'},
        {'id': 'ubnt_apmac', 'type': 'string'},
        {'id': 'ubnt_deviceid', 'type': 'string'},
        )
