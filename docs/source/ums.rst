=============================
MVAPICH-Plus Frontier UMS
=============================

    :Author: MVAPICH Team
    :Date: 2025/02/11


Using MVAPICH-Plus Frontier UMS
--------------------------------

The Frontier UMS program allows users to access a pre-built MVAPICH installation that interfaces with the existing Cray programming environment. The MVAPICH project ID is ums038. Default installations are available for several existing program environments and more will be added as we are able to test them, these will load the MVAPICH-Plus installation into the relevant library paths to act as the default MPI installation. MVAPICH preset environments are also available as modules to control suites of runtime behaviour.

To Enable MVAPICH-Plus run:

.. code:: sh

    ml load ums ums038
    #To enable on-the-fly compression
    ml load mvp-compression

.. note::
    Currently the UMS module supports PrgEnv-amd/8.5.0 and PrgEnv-gnu/8.5.0
