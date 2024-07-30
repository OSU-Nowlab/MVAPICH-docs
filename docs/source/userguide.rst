=========================
MVAPICH2 2.3.7 User Guide
=========================

    :Author: MVAPICH Team

    :Organization: Network-Based Computing Laboratory
                   :raw-html:`<br />`
                   Department of Computer Science and Engineering
    :Address: The Ohio State University

    :Contact: http://mvapich.cse.ohio-state.edu

    :Copyright: | Copyright (c) 2001-2022
                | Network-Based Computing Laboratory,
                | headed by Dr. D. K. Panda.
                | All rights reserved.
    :Date: Last revised: July 30th, 2024


.. contents::



1 Overview of the MVAPICH Project
---------------------------------

InfiniBand, Omni-Path, Ethernet/iWARP RDMA over
Converged Ethernet (RoCE), Slingshot 10, and Rockport Networks are
high-performance networking technologies to deliver low latency and
high bandwidth.  They are also achieving widespread acceptance due to their
*open standards*.

MVAPICH (pronounced as \`\`em-vah-pich'') is an *open-source* MPI software to
exploit the novel features and mechanisms of these networking technologies and
deliver best performance and scalability to MPI applications.  This software is
developed in the `Network-Based Computing Laboratory (NBCL) <http://nowlab.cse.ohio-state.edu>`_, headed by
`Prof. Dhabaleswar K. (DK) Panda <http://www.cse.ohio-state.edu/~panda>`_.

The MVAPICH2 MPI library supports MPI-3 semantics.  This *open-source* MPI
software project started in 2001 and a first high-performance implementation was
demonstrated at SuperComputing '02 conference.  After that, this software has
been steadily gaining acceptance in the HPC, InfiniBand, Omni-Path,
Ethernet/iWARP and
RoCE communities. As of  March 2022, more than 3,200
organizations (National Labs, Universities and Industry) world-wide (in 89
countries) have registered as MVAPICH users at MVAPICH project web site. There
have also been more than 1.56 million downloads of this
software from the MVAPICH
project site directly.  In addition, many InfiniBand, Omni-Path, Ethernet/iWARP
and
RoCE vendors, server vendors, systems integrators and Linux distributors have
been incorporating MVAPICH2 into their software stacks and distributing it.
MVAPICH2 distribution is available under BSD licensing.

Several InfiniBand systems using MVAPICH2 have obtained positions in
the TOP 500
ranking.  The Nov '21 list includes the following systems:

- 4th, 10,649,600-core (Sunway TaihuLight) at National Supercomputing Center in Wuxi, China;

- 13th, 448,448 cores (Frontera) at TACC;

- 26th, 391,680 cores (ABCI) in Japan;

- 38st, 570,020 cores (Neurion) in South Korea;

- 39nd, 556,104 cores (Oakforest-PACS) in Japan;

- 44th, 367,024 cores (Stampede2) at TACC.

More details on MVAPICH software, users list, mailing lists, sample performance
numbers on a wide range of platforms and interconnects, a set of OSU benchmarks,
related publications, and other InfiniBand-, RoCE, Omni-Path, and iWARP-related projects (High-Performance Big Data and High-Performance Deep Learning)
can be obtained from our
website:`http://mvapich.cse.ohio-state.edu}{http//mvapich.cse.ohio-state.edu <http://mvapich.cse.ohio-state.edu}{http//mvapich.cse.ohio-state.edu>`_.


This document contains necessary information for MVAPICH2 users to download,
install, test, use, tune and troubleshoot MVAPICH2 2.3.7.  We
continuously fix bugs and update update this document as per user feedback.
Therefore, we strongly encourage you to refer to our web page for updates.

2 TODO Installation Instructions
--------------------------------

3 TODO Basic Usage Instructions
-------------------------------

4 TODO OSU Benchmarks
---------------------

5 TODO Scalability features and Performance Tuning for Large Scale Clusters
---------------------------------------------------------------------------

6 TODO FAQ and Troubleshooting with MVAPICH2
--------------------------------------------

7 TODO MVAPICH2 General Parameters
----------------------------------

8 TODO MVAPICH2 Parameters (CH3-Based Interfaces)
-------------------------------------------------

9 TODO MVAPICH2 Parameters (OFA-IB-Nemesis Interface)
-----------------------------------------------------

10 TODO MPIRUN\\\_RSH Parameters
--------------------------------
