=============================
MVAPICH 4.0 Quick Start Guide
=============================

    :Author: MVAPICH Team
    :Date: 2025/03/07

.. contents::



1 Overview
----------

This Quick Start contains the necessary information for MVAPICH users
to download, build, install, and use MVAPICH 4.0.

MVAPICH (pronounced as “em-vah-pich”) is an open-source MPI software
to exploit the novel features and mechanisms of high-performance
networking technologies (InfiniBand, iWARP, RDMA over Converged
Enhanced Ethernet (RoCE v1 and v2), Slingshot 10, and Rockport
Networks) and deliver best performance and scalability to MPI
applications. MVAPICH 4.0 has support for
the Cray Slingshot 11, Cornelis OPX, and Intel PSM3 interconnects
through the OFI libfabric library, and for the UCX communication
library.

This software is developed in the `Network-Based Computing Laboratory (NBCL) <http://nowlab.cse.ohio-state.edu/>`_,
headed by `Prof. Dhabaleswar K. (DK) Panda <http://www.cse.ohio-state.edu/~panda>`_ since 2001.

More details on MVAPICH software, users list, mailing lists, sample
performance numbers on a wide range of platforms and interconnects, a
set of OSU benchmarks and related publications can be obtained from
our `website <http://mvapich.cse.ohio-state.edu/>`_.

2 Build MVAPICH from Source
-------------------------------
The MVAPICH Tarball contains the source code ready to be configured and built.

2.1 Download & Install with Tarball
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This package uses the basic GNU build system. To install a default build of
MVAPICH from the release tarball you can issue the following commands:

.. code:: sh

	$ wget https://mvapich.cse.ohio-state.edu/download/mvapich/mv2/mvapich-4.0.tar.gz
        $ ./configure --prefix=/path/to/install/mvapich
        $ make            # make -j<num threads> for parallel build
        $ make install

Common configure parameters:

.. code:: sh
        
        $ ./configure --prefix=/path/to/install/mvapich --with-device=ch4:ucx #For Infiniband and RoCE systems
        $ ./configure --prefix=/path/to/install/mvapich --with-device=ch4:ofi #For Slingshot11 and PSM/OPX systems
        $ ./configure --prefix=/path/to/install/mvapich --with-pm=slurm --with-pmi=pmi1 #To use Slurms srun launcher
        $ ./configure --prefix=/path/to/install/mvapich --with-pm=slurm --with-pmi=cray #To use Slurms srun launcher on a Cray system


2.2 Installing MVAPICH using Spack
---------------------------------------
MVAPICH can be installed using Spack and the mvapich package.

.. code:: sh

        $ spack install mvapich <spec>



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

    **Output of mpihello with different hostfiles**

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

    **[IMPORTANT]**


------------

    The -ppn option will create a block of N processes on each node in the
    hostfile. This is analogous to using the ‘:#‘ syntax in the
    hostfile. Using both of these capabilities to create a block ordering
    will be multiplicitive. Ie: setting node1:2 in the hostfile and -ppn 2
    on the command line will result in 4 processes being allocated to
    node1.

    If you are using the SLURM resource manager, ommitting a hostfile will
    result in mpiexec using the SLURM_JOB_HOSTLIST environment variable to
    determine the hosts. It will distribute processes accross all active
    nodes in the job according the value set by -ppn.


**env variables**

    Environment variables are specified using the ‘NAME=VALUE’ syntax
    using either the ‘-genv‘ or ‘-genvlist‘ flag. These are used to export
    MPICH_CVAR values to control underlying MPICH functionality as well as
    MVP_CVARS to control MVAPICH specific functionality.

    Pass an environment variable named FOO with the value BAR

    .. code:: sh
    
        $ mpiexec -f hosts -np 2 -genv FOO=BAR ./mpihello


4 More Information
------------------

Please see the following for more information.

- `User Guides <http://mvapich.cse.ohio-state.edu/support/>`_

- `OSU Micro-Benchmarks <http://mvapich.cse.ohio-state.edu/benchmarks/>`_

- `FAQ <http://mvapich.cse.ohio-state.edu/faq/>`_
