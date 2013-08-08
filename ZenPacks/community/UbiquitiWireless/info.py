from zope.interface import implements

from Products.Zuul.infos import ProxyProperty
from Products.Zuul.infos.device import DeviceInfo

from ZenPacks.community.UbiquitiWireless.interfaces import IUbiquitiDeviceInfo

class UbiquitiDeviceInfo(DeviceInfo):
    implements(IUbiquitiDeviceInfo)

    ubnt_distance = ProxyProperty('ubnt_distance')
    ubnt_longitude = ProxyProperty('ubnt_longitude')
    ubnt_latitude = ProxyProperty('ubnt_latitude')
    ubnt_freq = ProxyProperty('ubnt_freq')
    ubnt_essid = ProxyProperty('ubnt_essid')
    ubnt_apmac = ProxyProperty('ubnt_apmac')
    ubnt_deviceid = ProxyProperty('ubnt_deviceid')
