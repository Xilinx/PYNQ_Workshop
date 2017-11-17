#   Copyright (c) 2016, Xilinx, Inc.
#   All rights reserved.
# 
#   Redistribution and use in source and binary forms, with or without 
#   modification, are permitted provided that the following conditions are met:
#
#   1.  Redistributions of source code must retain the above copyright notice, 
#       this list of conditions and the following disclaimer.
#
#   2.  Redistributions in binary form must reproduce the above copyright 
#       notice, this list of conditions and the following disclaimer in the 
#       documentation and/or other materials provided with the distribution.
#
#   3.  Neither the name of the copyright holder nor the names of its 
#       contributors may be used to endorse or promote products derived from 
#       this software without specific prior written permission.
#
#   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
#   AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, 
#   THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR 
#   PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR 
#   CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, 
#   EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, 
#   PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
#   OR BUSINESS INTERRUPTION). HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, 
#   WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR 
#   OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF 
#   ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

__author__      = "Cathal McCabe, Yun Rock Qu"
__copyright__   = "Copyright 2016, Xilinx"
__email__       = "pynq_support@xilinx.com"


import time
from pynq.lib import Pmod

PYNQ_TUTORIAL_PROGRAM = "./pynq_tutorial.bin"

class Pynq_Tutorial(object):
    """This class writes data to a memory buffer that is passed to the class.
    

    Attributes
    ----------
    iop : _IOP
        I/O processor instance used by ALS
    mmio : MMIO
        Memory-mapped I/O instance to read and write instructions and data.

    """
    def __init__(self, mb_info):
        """Return a new instance of an ALS object. 
        
        Parameters
        ----------
        A dictionary storing PynqMicroblaze information, such as the
            IP name and the reset name.
            
        """
            
        self.microblaze = Pmod(mb_info, PYNQ_TUTORIAL_PROGRAM)

        
    def write_to_buffer(self, buffer, length, data):
        """Write data to a memory buffer. 
        
        
        Parameters
        ----------
        buffer: unsigned
            Address of buffer in DDR memory.
        length: unsigned
            Number of samples in memory buffer to write. 
        data: unsigned
            Initialization data value to send to IOP.
            
        Returns
        -------
        None
        
        """
        self.microblaze.write_mailbox(8, data)
        self.microblaze.write_mailbox(4, length)
        self.microblaze.write_mailbox(0, buffer)
     
