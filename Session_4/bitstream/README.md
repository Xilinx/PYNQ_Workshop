# Session 4 designs

This repository contains the compiled bitstreams for the PYNQ workshop session 4 examples and corresponding HWH and Tcl files. The Tcl files can be used to rebuild the hardware design in Vivado.



## PS GPIO

* In Vivado, from the Tcl command prompt, change to this directory. 

* Source the following file from the Tcl prompt:

```
source ps_gpio.tcl
```

This will create the Vivado design, generate the top level wrapper, and apply pin constraints. If you want to create the bitstream, you will need to run this step separately. 

## AXI GPIO

* In Vivado, from the Tcl command prompt, change to this directory. 

* Source the following file from the Tcl prompt:

```
axi_gpio.tcl
```

This will create the Vivado design, generate the top level wrapper, and apply pin constraints. If you want to create the bitstream, you will need to run this step separately. 

## DMA Tutorial

* In Vivado, from the Tcl command prompt, change to this directory. 

* Source the following file from the Tcl prompt:

dma_tutorial.tcl

This will create the Vivado design, generate the top level wrapper. There are no external pins required for this design. If you want to create the bitstream, you will need to run this step separately. 

## Resizer

The resizer example sources are part of a larger "PYNQ_HelloWorld" example and can be found here: 

<https://github.com/Xilinx/PYNQ-HelloWorld>