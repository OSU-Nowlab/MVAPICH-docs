=======================================
MVAPICH Launchers
=======================================

    :Author: MVAPICH Team
    :Date: 2025/02/14

.. contents::



1 Overview
----------

MVAPICH 4.0 supports multiple launchers for different system configurations. 

2 Hydra
-------

Hydra is the default launcher of MVAPICH and follows the mpiexec interface.  More info can be found in our :ref:`hydra guide<hydra>`.

2.1 Building with Hydra
~~~~~~~~~~~~~~~~~~~~~~~

No alterations to your configure line are necessary.

3 SLURM
-------

Using SLURM as a launcher allows for the tighter integration with srun and slurm environment variables.

3.1 Building on Cray Systems
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For Cray systems using srun as the launcher add the following to your configure line :code:`--with-pm=none --with-pmi=pmi2 --with-pmi2=/opt/cray/pe/pmi/default`. The provided path is standard on most Cray PE systems, but may be unique on your particular system. Testing for Cray PE builds was performed on ORNL Frontier and changes may have been made to your particular system. Contact your system administrator if you have trouble finding the location of your Cray PMI installation.

3.2 Building on Non-Cray Systems
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For non-cray systems using srun as the launcher add the following to your configure line :code:`--with-pm=none --with-pmi=slurm`

4 Flux
------

Flux as a launcher allows for tighter integration with the scheduler and its environment variables.

4.1 Building with Flux
~~~~~~~~~~~~~~~~~~~~~~

Flux will work with standard mpiexec/hydra builds, However if the user wishes to not build the hydra binary add the following to the configure line :code:`--with-pm=none`
