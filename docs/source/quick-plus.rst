=============================
MVAPICH 4.0 Quick Start Guide
=============================

    :Author: MVAPICH Team
    :Date: 2024/02/16

.. contents::



1 Overview
----------

This Quick Start contains the necessary information for MVAPICH users
to download, install, and use MVAPICH-Plus 4.0.

MVAPICH (pronounced as “em-vah-pich”) is an open-source MPI software
to exploit the novel features and mechanisms of high-performance
networking technologies (InfiniBand, iWARP, RDMA over Converged
Enhanced Ethernet (RoCE v1 and v2), Slingshot 10, and Rockport
Networks) and deliver best performance and scalability to MPI
applications. This Release Candidate of MVAPICH 4.0 adds support for
the Cray Slingshot 11, Cornelis OPX, and Intel PSM3 interconnects
through the OFI libfabric library, and for the UCX communication
library.

MVAPICH-Plus provides a GPU aware MPI implementation and additional 
enhancements that are still under active research.

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

2 Install MVAPICH-Plus from RPM
-------------------------------

The MVAPICH-Plus RPM contains the pre-built binaries for an MVAPICH-Plus installation. Select an RPM
that matches your system specifications. If a matching RPM is not avaiable on our website, please use
the provided form to request a custom RPM.

2.1 Download & Install with RPM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Download the appropriate MVAPICH-Plus RPM from the website:
`https://mvapich.cse.ohio-state.edu/downloads/ <https://mvapich.cse.ohio-state.edu/downloads/>`_

.. code:: sh

	$ wget http://mvapich.cse.ohio-state.edu/download/mvapich/plus/4.0/<mvp-plus-rpm-name>.rpm
	$ rpm -Uvh --nodeps <mvp-gdr-rpm-name>.rpm 

The RPMs contained in our libraries are relocatable and can be installed using a
prefix other than the default of ./opt/mvapich/ used by the
library in the previous example.

To install the library on a custom path:

.. code:: sh

	$ rpm --prefix /custom/install/prefix -Uvh --nodeps <mvp-plus-rpm-name>.rpm 

If you do not have root permission you can use rpm2cpio to extract the library.

.. code:: sh

	$ rpm2cpio <mvp-plus-rpm-name>.rpm | cpio -id 

When using the rpm2cpio method, you will need to update the MPI compiler
scripts, such as mpicc, in order to point to the correct path of where you
place the library.

2.2 Installing MVAPICH-Plus using Spack
---------------------------------------
MVAPICH-Plus can be installed using Spack without building
it from source. See the Spack userguide for details:
https://mvapich.cse.ohio-state.edu/userguide/userguide_spack/


3 Run MPI Program
-----------------

In this section we will demonstrate how to build and run a hello world
program which uses mpi.

.Sample MPI code [mpihello.c]

.. code:: text

    #include <mpi.h>
    #include <stdio.h>
    #include <unistd.h>

    int main(int argc, char ⋆argv[])
    {
        int rank;
        char hostname[256];

        MPI_Init(&argc, &argv);
        gethostname(hostname, 256);
        MPI_Comm_rank(MPI_COMM_WORLD, &rank);
        printf("rank %d on %s says hello!\n", rank, hostname);
        MPI_Finalize();
        return 0;
    }

3.1 Build & Run
~~~~~~~~~~~~~~~

.. code:: sh

    $ mpicc -o mpihello mpihello.c <1>
    $ mpiexec -f hosts -np 2 ./mpihello <2>

1. mpicc is one of the basic commands used to compile MPI
   applications. This, along with mpicxx, mpif77, and mpif90, are
   wrapper scripts that invoke the compiler used to compile the
   MVAPICH library. Use of these scripts are recommended over invoking
   the compiler directly and adding the CFLAGS and LDFLAGS

2. mpiexec is used to launch MPI programs. This command tells mpiexec
   to launch 2 ./mpihello processes using the nodes specified in the
   hostfile hosts.

3.1.1 Using mpiexec
^^^^^^^^^^^^^^^^^^^

**syntax**

::

    mpiexec <options> -genvlist <env_var1>[,<env_var2>...] <command>

**options**

::

    **bold** test

**-hostfile**

specify the location of the hostfile

**Hostfile Format** The mpiexec hostfile format allows for users to
specify hostnames, one per line.

The following demonstrates the distribution of MPI ranks when using
different hostfiles:

Examples:

::

    hosts1
        node1
        node2
    hosts2
        node1
        node1
        node2
        node2

Output of mpihello with different hostfiles

::

    $ mpiexec -f hosts1 -n 4 ./mpihello
    rank 0 on node1 says hello!
    rank 1 on node2 says hello!
    rank 2 on node1 says hello!
    rank 3 on node2 says hello!

    $ mpiexec -f hosts2 -n 4 ./mpihello
    rank 0 on node1 says hello!
    rank 1 on node1 says hello!
    rank 2 on node2 says hello!
    rank 3 on node2 says hello!

**-n**

Number of mpi processes to launch.

**-ppn**

Number of mpi processes to launch per node.

[IMPORTANT]


------------

The -ppn option will create a block of N processes on each node in the
hostfile. This is analogous to using the ‘:#‘ syntax in the
hostfile. Using both of these capabilities to create a block ordering
will be multiplicitive. Ie: setting node1:2 in the hostfile and -ppn 2
on the command line will result in 4 processes being allocated to
node1.

If you are using the SLURM resource manager, ommitting a hostfile will
result in mpiexec using the SLURM\ :sub:`JOB`\ \ :sub:`HOSTLIST`\ environment variable to
determine the hosts. It will distribute processes accross all active
nodes in the job according the value set by -ppn.


**env variables**

Environment variables are specified using the ‘NAME=VALUE’ syntax
using either the ‘-genv‘ or ‘-genvlist‘ flag. These are used to export
MPICH\ :sub:`CVAR`\ values to control underlying MPICH functionality as well as
MVP\_ CVARS to control MVAPICH specific functionality.

Pass an environment variable named FOO with the value BAR

.. code:: sh

    $ mpiexec -f hosts -np 2 -genv FOO=BAR ./mpihello


4 More Information
------------------

Please see the following for more information.

- `User Guides <http://mvapich.cse.ohio-state.edu/support/>`_

- `OSU Micro-Benchmarks <http://mvapich.cse.ohio-state.edu/benchmarks/>`_

- `FAQ <http://mvapich.cse.ohio-state.edu/faq/>`_
