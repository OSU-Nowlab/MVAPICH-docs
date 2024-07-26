=============================
MVAPICH 3.0 Quick Start Guide
=============================

    :Author: MVAPICH Team
    :Date: 2024/02/16 00:00

.. contents::



1 Overview
----------

This Quick Start contains the necessary information for MVAPICH users
to download, install, and use MVAPICH 3.0. Please refer to our
`User Guide <http://mvapich.cse.ohio-state.edu/support/>`_ for the comprehensive list of all features and instructions
about how to use them.

MVAPICH (pronounced as “em-vah-pich”) is an open-source MPI software
to exploit the novel features and mechanisms of high-performance
networking technologies (InfiniBand, iWARP, RDMA over Converged
Enhanced Ethernet (RoCE v1 and v2), Slingshot 10, and Rockport
Networks) and deliver best performance and scalability to MPI
applications. This Release Candidate of MVAPICH 3.0 adds support for
the Cray Slingshot 11, Cornelis OPX, and Intel PSM3 interconnects
through the OFI libfabric library, and for the UCX communication
library.

Please note that as this is a pre-release, performance may not be
optimal. For best performance on Mellanox InfiniBand, RoCE, iWARP,
Slingshot 10 or lower, Rockport Networks, and Intel TrueScale or
Omni-Path adapters with PSM2, please use MVAPICH 2.3.7.

This software is developed in the `Network-Based Computing Laboratory (NBCL) <http://nowlab.cse.ohio-state.edu/>`_,
headed by `Prof. Dhabaleswar K. (DK) Panda <http://www.cse.ohio-state.edu/~panda>`_ since 2001.

More details on MVAPICH software, users list, mailing lists, sample
performance numbers on a wide range of platforms and interconnects, a
set of OSU benchmarks and related publications can be obtained from
our `website <http://mvapich.cse.ohio-state.edu/>`_.

2 Build MVAPICH from Source
---------------------------

The MVAPICH 3.0 source code package includes MPICH 3.4.3. All the required files are present in a single tarball.

2.1 Download & Unpack
~~~~~~~~~~~~~~~~~~~~~

Download the most recent distribution tarball from
`http://mvapich.cse.ohio-state.edu/download/mvapich/mv2/mvapich2-3.0.tar.gz <http://mvapich.cse.ohio-state.edu/download/mvapich/mv2/mvapich2-3.0.tar.gz>`_

.. code:: sh

    $ wget http://mvapich.cse.ohio-state.edu/download/mvapich/mv2/mvapich2-3.0.tar.gz
    $ gzip -dc mvapich2-3.0.tar.gz | tar -x
    $ cd mvapich2-3.0

2.2 Configure
~~~~~~~~~~~~~

If you have either UCX of OFI (libfabric) installed on your system on
a default PATH you can use the default configuration to automatically
detect the installed communication library…

.. code:: sh

    $ ./configure
