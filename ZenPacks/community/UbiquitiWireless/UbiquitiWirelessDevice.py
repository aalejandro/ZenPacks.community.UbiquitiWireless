from Products.ZenModel.Device import Device

class UbiquitiWirelessDevice(Device):
    temp_sensor_count = None

    _properties = Device._properties + (
        {'id': 'temp_sensor_count', 'type': 'int'},
        )
