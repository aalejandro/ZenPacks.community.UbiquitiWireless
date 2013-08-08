from Products.Zuul.form import schema
from Products.Zuul.interfaces.device import IDeviceInfo
from Products.Zuul.utils import ZuulMessageFactory as _t

class IUbiquitiDeviceInfo(IDeviceInfo):
    ubnt_distance = schema.Int(title=_t('Distance to the AP'))
    ubnt_longitude = schema.Float(title=_t('Longitude'))
    ubnt_latitude = schema.Float(title=_t('Latitude'))
    ubnt_freq = schema.Int(title=_t('Frequency in MHz'))
    ubnt_essid = schema.Text(title=_t('ESSID'))
    ubnt_apmac = schema.Text(title=_t('Access Point MAC Address'))
    ubnt_deviceid = schema.Text(title=_t('Device MAC Address'))
