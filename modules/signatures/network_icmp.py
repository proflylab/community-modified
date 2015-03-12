# Copyright (C) 2013 David Maciejak
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

class NetworkICMP(Signature):
    name = "network_icmp"
    description = "Generates some ICMP traffic"
    severity = 4
    categories = ["icmp"]
    authors = ["David Maciejak"]
    minimum = "1.0"

    def run(self):
        if "network" in self.results:
            if "icmp" in self.results["network"]:
                if len(self.results["network"]["icmp"]) > 0:
                    return True

        return False
