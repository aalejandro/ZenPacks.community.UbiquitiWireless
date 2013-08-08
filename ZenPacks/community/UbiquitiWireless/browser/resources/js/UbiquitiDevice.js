(function(){

Ext.onReady(function() {
    // Add information to the device overview system summary
    var DEVICE_OVERVIEW_ID = 'deviceoverviewpanel_summary';
    Ext.ComponentMgr.onAvailable(DEVICE_OVERVIEW_ID, function(){
        var overview = Ext.getCmp(DEVICE_OVERVIEW_ID);
        overview.removeField('memory');

        overview.addField({
            name: 'ubnt_deviceid',
            fieldLabel: _t('Device MAC')
        });
    });

    // Add information to the device overview page.
    var PANEL_ID = 'deviceoverviewpanel_systemsummary';
    Ext.ComponentMgr.onAvailable(PANEL_ID, function(){
        var panel = Ext.getCmp(PANEL_ID);

        items = [
        {
            name: 'ubnt_essid',
            fieldLabel: _t('ESSID')
        },
        {
            name: 'ubnt_apmac',
            fieldLabel: _t('AP Mac')
        },
        {
            name: 'ubnt_freq',
            fieldLabel: _t('Frequency')
        },
        {
            name: 'ubnt_distance',
            fieldLabel: _t('Distance')
        },
        {
            name: 'ubnt_latitude',
            fieldLabel: _t('Latitude')
        },
        {
            name: 'ubnt_longitude',
            fieldLabel: _t('Longitude')
        }
        ];

        panel.insert(0, items);
    });
});

})();
