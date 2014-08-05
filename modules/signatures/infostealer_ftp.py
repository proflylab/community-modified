# Copyright (C) 2012-2014 Claudio "nex" Guarnieri (@botherder), Accuvant Inc. (bspengler@accuvant.com)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from lib.cuckoo.common.abstracts import Signature

class FTPStealer(Signature):
    name = "infostealer_ftp"
    description = "Harvests credentials from local FTP client softwares"
    severity = 3
    categories = ["infostealer"]
    authors = ["nex", "Accuvant"]
    minimum = "1.0"

    def run(self):
        file_indicators = [
            ".*\\\\CuteFTP\\\\sm\.dat$",
            ".*\\\\FlashFXP\\\\.*\\\\Sites\.dat$",
            ".*\\\\FileZilla\\\\sitemanager\.xml$",
            ".*\\\\FileZilla\\\\recentservers\.xml$",
            ".*\\\\VanDyke\\\\Config\\\\Sessions\\\\.*",
            ".*\\\\Far\\ Manager\\\\.*",
            ".*\\\\FTP\\ Explorer\\\\.*"
            ".*\\\\FTP\\ Commander.*"
            ".*\\\\SmartFTP\\\\.*",
            ".*\\\\TurboFTP\\\\.*",
            ".*\\\\FTPRush\\\\.*",
            ".*\\\\LeapFTP\\\\.*",
            ".*\\\\FTPGetter\\\\.*",
            ".*\\\\ALFTP\\\\.*",
            ".*\\\\Ipswitch\\\\WS_FTP\\\\.*",
        ]
        registry_indicators = [
            ".*\\\\Software\\\\Far.*\\\\Hosts$",
            ".*\\\\Software\\\\Far.*\\\\FTPHost$",
            ".*\\\\Software\\\\GlobalSCAPE\\\\CuteFTP.*",
            ".*\\\\Software\\\\Ghisler\\\\Windows Commander.*",
            ".*\\\\Software\\\\Ghisler\\\\Total Commander.*",
            ".*\\\\Software\\\\BPFTP\\\\.*",
            ".*\\\\Software\\\\FileZilla.*",
            ".*\\\\Software\\\\TurboFTP.*",
            ".*\\\\Software\\\\Sota\\\\FFFTP.*",
            ".*\\\\Software\\\\FTPWare\\\\CoreFTP\\\\.*",
            ".*\\\\Software\\\\FTP\\ Explorer\\\\.*",
            ".*\\\\Software\\\\FTPClient\\\\.*",
            ".*\\\\Software\\\\LinasFTP\\\\.*",
            ".*\\\\Software\\\\Robo-FTP.*",
            ".*\\\\Software\\\\MAS-Soft\\\\FTPInfo\\\\.*",
            ".*\\\\Software\\\\SoftX\.org\\\\FTPClient\\\\.*",
            ".*\\\\Software\\\\NCH\\ Software\\\\CoreFTP\\\\.*",
            ".*\\\\Software\\\\BulletProof Software\\\\BulletProof FTP Client.*"
        ]

        for indicator in file_indicators:
            file_match = self.check_file(pattern=indicator, regex=True)
            if file_match:
                self.data.append({"file" : file_match })
                return True
        for indicator in registry_indicators:
            key_match = self.check_key(pattern=indicator, regex=True)
            if key_match:
                self.data.append({"key" : key_match })
                return True
        return False
