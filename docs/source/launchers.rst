=======================================
MVAPICH Launchers
=======================================

    :Author: MVAPICH Team
    :Date: 2025/02/14

.. contents::



1 Overview
----------

MVAPICH 4.0 supports multiple launchers for different system configurations. 

2 SLURM
-------
Using SLURM as a launcher allows for the tighter integration with srun and slurm environment variables.

2.1 Building on Cray Systems
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
For Cray systems using srun as the launcher add the following to your configure line :code:`--with-pm=none --with-pmi=pmi2 --with-pmi2=/opt/cray/pe/pmi/default`, this should work on most cray systems but some may use a different path if they are configured differently.

2.2 Building on Non-Cray Systems
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
For non-cray systems using srun as the launcher add the following to your configure line :code:`--with-pm=none --with-pmi=slurm`
