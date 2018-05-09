'''
AceProxy default configuration script
DO NOT EDIT THIS FILE!
Copy this file to aceconfig.py and change only needed options.
'''

import logging
import platform
from aceclient.acemessages import AceConst


class AceDefConfig(object):
    acespawn = False
    acecmd = "acestreamengine --client-console"
    acekey = 'n51LvQoTlJzNGaFxseRK-uvnvX-sD4Vm5Axwmc4UcoD-jruxmKsuJaH0eVgE'
    acehost = '127.0.0.1'
    aceport = 62062
    aceage = AceConst.AGE_18_24
    acesex = AceConst.SEX_MALE
    acestartuptimeout = 10
    aceconntimeout = 5
    aceresulttimeout = 10
    debug = logging.DEBUG
    #
    httphost = '0.0.0.0'
    httpport = 8000
    aceproxyuser = ''
    firewall = False
    firewallblacklistmode = False
    firewallnetranges = (
        '127.0.0.1',
        '192.168.0.0/16',
        )
    maxconns = 10
    loggingtoafile = False
    logpath = ''
    vlcuse = False
    vlcuseaceplayer = False
    vlcspawn = False
    vlccmd = "vlc -I telnet --clock-jitter -1 --network-caching -1 --sout-mux-caching 2000 --telnet-password admin --telnet-port 4212"
    vlcspawntimeout = 5
    vlchost = '127.0.0.1'
    vlcport = 4212
    vlcoutport = 8081
    vlcpass = 'admin'
    vlcpreaccess = ''
    vlcmux = 'ts'
    vlcforceffmpeg = False
    videodelay = 2
    videoobey = True
    videopausedelay = 2
    videoseekback = 0
    videodestroydelay = 3
    videotimeout = 40
    fakeuas = ('Mozilla/5.0 IMC plugin Macintosh', )
    fakeheaderuas = ('HLS Client/2.0 (compatible; LG NetCast.TV-2012)',
                     'Mozilla/5.0 (DirectFB; Linux armv7l) AppleWebKit/534.26+ (KHTML, like Gecko) Version/5.0 Safari/534.26+ LG Browser/5.00.00(+mouse+3D+SCREEN+TUNER; LGE; 42LM670T-ZA; 04.41.03; 0x00000001;); LG NetCast.TV-2012 0'
                     )

    osplatform = platform.system()
