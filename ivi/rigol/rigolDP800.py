"""

Python Interchangeable Virtual Instrument Library

Copyright (c) 2012 Alex Forencich

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

"""

from .. import ivi
from .. import dcpwr
from .. import scpi

TrackingType = set(['floating'])
TriggerSourceMapping = {
        'immediate': 'imm',
        'bus': 'bus'}

class rigolDP800(scpi.dcpwr.Base, scpi.dcpwr.Trigger, scpi.dcpwr.SoftwareTrigger,
                scpi.dcpwr.Measurement):
    "Rigol DP800 series IVI DC power supply driver"
    
    def __init__(self, *args, **kwargs):
        super(rigolDP800, self).__init__(*args, **kwargs)
        
        self._instrument_id = 'Rigol Technologies,DP800'
        
        self._output_count = 3
        
        self._output_range = [[(8.0, 5.0)], [(30.0, 2.0)], [(-30.0, 2.0)]]
        self._output_range_name = [['P8V'], ['P30V'], ['N30V']]
        self._output_ovp_max = [8.8, 33.0, -33.0]
        self._output_ocp_max = [5.5, 2.2, 2.2]
        self._output_voltage_max = [8.0, 30.0, -30.0]
        self._output_current_max = [5.0, 2.0, 2.0]
        
        self._memory_size = 10
        
        self._identity_description = "Rigol DP800 series DC power supply driver"
        self._identity_identifier = ""
        self._identity_revision = ""
        self._identity_vendor = ""
        self._identity_instrument_manufacturer = "Rigol Technologies"
        self._identity_instrument_model = ""
        self._identity_instrument_firmware_revision = ""
        self._identity_specification_major_version = 3
        self._identity_specification_minor_version = 0
        self._identity_supported_instrument_models = ['DP831A', 'DP832', 'DP832A']
        
        ivi.add_method(self, 'memory.save',
                        self._memory_save)
        ivi.add_method(self, 'memory.recall',
                        self._memory_recall)
        
        self._init_outputs()
        
    
    def _memory_save(self, index):
        index = int(index)
        if index < 1 or index > self._memory_size:
            raise OutOfRangeException()
        if not self._driver_operation_simulate:
            self._write("*sav %d" % index)
    
    def _memory_recall(self, index):
        index = int(index)
        if index < 1 or index > self._memory_size:
            raise OutOfRangeException()
        if not self._driver_operation_simulate:
            self._write("*rcl %d" % index)
    
    
    

