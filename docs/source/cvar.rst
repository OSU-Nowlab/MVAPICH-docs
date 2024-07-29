=============================
MVAPICH Environment Variables
=============================

    :Author: MVAPICH Team
    :Date: 2024/07/26


CVAR Environment Variables
--------------------------

These are set as environment variables setting the CVAR or it's alias
to potential values. For example, setting the barrier intra-node algorithm:

.. code:: sh

    MVP_BARRIER_INTRA_ALGORITHM="osu_pairwise"

MPIR\_CVAR\_BARRIER\_INTRA\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_BARRIER\_INTRA\_ALGORITHM

  - MPICH\_BARRIER\_INTRA\_ALGORITHM

- **Description**: Variable to select barrier algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - nb            - Force nonblocking algorithm

  - smp           - Force smp algorithm

  - k\_dissemination - Force high radix dissemination algorithm

  - recexch       - Force recursive exchange algorithm

  - osu\_pairwise  - Force OSU mcast based design

- **Default:** auto

MPIR\_CVAR\_BARRIER\_INTER\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_BARRIER\_INTER\_ALGORITHM

  - MPICH\_BARRIER\_INTER\_ALGORITHM

- **Description**: Variable to select barrier algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - bcast - Force bcast algorithm

  - nb    - Force nonblocking algorithm

- **Default:** auto

MPIR\_CVAR\_BARRIER\_DISSEM\_KVAL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_BARRIER\_DISSEM\_KVAL

  - MPICH\_BARRIER\_DISSEM\_KVAL

- **Description**: k value for dissemination exchange based barrier algorithm

- **Default:** 2

MPIR\_CVAR\_BARRIER\_RECEXCH\_KVAL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_BARRIER\_RECEXCH\_KVAL

  - MPICH\_BARRIER\_RECEXCH\_KVAL

- **Description**: k value for recursive exchange based allreduce based barrier

- **Default:** 2

MPIR\_CVAR\_BARRIER\_RECEXCH\_SINGLE\_PHASE\_RECV
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_BARRIER\_RECEXCH\_SINGLE\_PHASE\_RECV

  - MPICH\_BARRIER\_RECEXCH\_SINGLE\_PHASE\_RECV

- **Description**: This CVAR controls whether the recv is posted for one phase or two phases in recexch algos. By default, we post the recvs for 2 phases.

- **Default:** false

MPIR\_CVAR\_IBARRIER\_RECEXCH\_KVAL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IBARRIER\_RECEXCH\_KVAL

  - MPICH\_IBARRIER\_RECEXCH\_KVAL

- **Description**: k value for recursive exchange based ibarrier

- **Default:** 2

MPIR\_CVAR\_IBARRIER\_DISSEM\_KVAL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IBARRIER\_DISSEM\_KVAL

  - MPICH\_IBARRIER\_DISSEM\_KVAL

- **Description**: k value for dissemination exchange based ibarrier

- **Default:** 2

MPIR\_CVAR\_IBARRIER\_INTRA\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IBARRIER\_INTRA\_ALGORITHM

  - MPICH\_IBARRIER\_INTRA\_ALGORITHM

- **Description**: Variable to select ibarrier algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - sched\_auto - Internal algorithm selection for sched-based algorithms

  - sched\_recursive\_doubling - Force recursive doubling algorithm

  - tsp\_recexch - Force generic transport based recursive exchange algorithm

  - tsp\_k\_dissemination - Force generic transport based high-radix dissemination algorithm

- **Default:** auto

MPIR\_CVAR\_IBARRIER\_INTER\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IBARRIER\_INTER\_ALGORITHM

  - MPICH\_IBARRIER\_INTER\_ALGORITHM

- **Description**: Variable to select ibarrier algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - sched\_auto - Internal algorithm selection for sched-based algorithms

  - sched\_bcast - Force bcast algorithm

- **Default:** auto

MPIR\_CVAR\_BCAST\_MIN\_PROCS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_BCAST\_MIN\_PROCS

  - MPICH\_BCAST\_MIN\_PROCS

- **Description**: Let's define short messages as messages with size < MPIR\_CVAR\_BCAST\_SHORT\_MSG\_SIZE, and medium messages as messages with size >= MPIR\_CVAR\_BCAST\_SHORT\_MSG\_SIZE but < MPIR\_CVAR\_BCAST\_LONG\_MSG\_SIZE, and long messages as messages with size >= MPIR\_CVAR\_BCAST\_LONG\_MSG\_SIZE. The broadcast algorithms selection procedure is as follows. For short messages or when the number of processes is < MPIR\_CVAR\_BCAST\_MIN\_PROCS, we do broadcast using the binomial tree algorithm. Otherwise, for medium messages and with a power-of-two number of processes, we do broadcast based on a scatter followed by a recursive doubling allgather algorithm. Otherwise, for long messages or with non power-of-two number of processes, we do broadcast based on a scatter followed by a ring allgather algorithm. (See also: MPIR\_CVAR\_BCAST\_SHORT\_MSG\_SIZE, MPIR\_CVAR\_BCAST\_LONG\_MSG\_SIZE)

- **Default:** 8

MPIR\_CVAR\_BCAST\_SHORT\_MSG\_SIZE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_BCAST\_SHORT\_MSG\_SIZE

  - MPICH\_BCAST\_SHORT\_MSG\_SIZE

- **Description**: Let's define short messages as messages with size < MPIR\_CVAR\_BCAST\_SHORT\_MSG\_SIZE, and medium messages as messages with size >= MPIR\_CVAR\_BCAST\_SHORT\_MSG\_SIZE but < MPIR\_CVAR\_BCAST\_LONG\_MSG\_SIZE, and long messages as messages with size >= MPIR\_CVAR\_BCAST\_LONG\_MSG\_SIZE. The broadcast algorithms selection procedure is as follows. For short messages or when the number of processes is < MPIR\_CVAR\_BCAST\_MIN\_PROCS, we do broadcast using the binomial tree algorithm. Otherwise, for medium messages and with a power-of-two number of processes, we do broadcast based on a scatter followed by a recursive doubling allgather algorithm. Otherwise, for long messages or with non power-of-two number of processes, we do broadcast based on a scatter followed by a ring allgather algorithm. (See also: MPIR\_CVAR\_BCAST\_MIN\_PROCS, MPIR\_CVAR\_BCAST\_LONG\_MSG\_SIZE)

- **Default:** 12288

MPIR\_CVAR\_BCAST\_LONG\_MSG\_SIZE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_BCAST\_LONG\_MSG\_SIZE

  - MPICH\_BCAST\_LONG\_MSG\_SIZE

- **Description**: Let's define short messages as messages with size < MPIR\_CVAR\_BCAST\_SHORT\_MSG\_SIZE, and medium messages as messages with size >= MPIR\_CVAR\_BCAST\_SHORT\_MSG\_SIZE but < MPIR\_CVAR\_BCAST\_LONG\_MSG\_SIZE, and long messages as messages with size >= MPIR\_CVAR\_BCAST\_LONG\_MSG\_SIZE. The broadcast algorithms selection procedure is as follows. For short messages or when the number of processes is < MPIR\_CVAR\_BCAST\_MIN\_PROCS, we do broadcast using the binomial tree algorithm. Otherwise, for medium messages and with a power-of-two number of processes, we do broadcast based on a scatter followed by a recursive doubling allgather algorithm. Otherwise, for long messages or with non power-of-two number of processes, we do broadcast based on a scatter followed by a ring allgather algorithm. (See also: MPIR\_CVAR\_BCAST\_MIN\_PROCS, MPIR\_CVAR\_BCAST\_SHORT\_MSG\_SIZE)

- **Default:** 524288

MPIR\_CVAR\_MAX\_SMP\_BCAST\_MSG\_SIZE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_MAX\_SMP\_BCAST\_MSG\_SIZE

  - MPICH\_MAX\_SMP\_BCAST\_MSG\_SIZE

- **Description**: Maximum message size for which SMP-aware broadcast is used.  A value of '0' uses SMP-aware broadcast for all message sizes.

- **Default:** 0

MPIR\_CVAR\_BCAST\_INTRA\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_BCAST\_INTRA\_ALGORITHM

  - MPICH\_BCAST\_INTRA\_ALGORITHM

- **Description**: Variable to select bcast algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - binomial                                - Force Binomial Tree

  - nb                                      - Force nonblocking algorithm

  - smp                                     - Force smp algorithm

  - scatter\_recursive\_doubling\_allgather    - Force Scatter Recursive-Doubling Allgather

  - scatter\_ring\_allgather                  - Force Scatter Ring

  - pipelined\_tree                          - Force tree-based pipelined algorithm

  - tree                                    - Force tree-based algorithm

  - osu\_knomial                             - Force OSU knomial algorithm

  - osu\_pairwise                            - Force OSU pairwise algorithm

  - osu\_pipelined                           - Force OSU pipelined algorithm

- **Default:** auto

MPIR\_CVAR\_BCAST\_TREE\_KVAL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_BCAST\_TREE\_KVAL

  - MPICH\_BCAST\_TREE\_KVAL

- **Description**: k value for tree (kary, knomial, etc.) based bcast

- **Default:** 2

MPIR\_CVAR\_BCAST\_TREE\_TYPE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_BCAST\_TREE\_TYPE

  - MPICH\_BCAST\_TREE\_TYPE

- **Description**: Tree type for tree based bcast kary      - kary tree type knomial\_1 - knomial\_1 tree type knomial\_2 - knomial\_2 tree type topology\_aware - topology\_aware tree type topology\_aware\_k - topology\_aware tree type with branching factor k topology\_wave - topology\_wave tree type

- **Default:** kary

MPIR\_CVAR\_BCAST\_TOPO\_REORDER\_ENABLE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_BCAST\_TOPO\_REORDER\_ENABLE

  - MPICH\_BCAST\_TOPO\_REORDER\_ENABLE

- **Description**: This cvar controls if the leaders are reordered based on the number of ranks in each group.

- **Default:** true

MPIR\_CVAR\_BCAST\_TOPO\_OVERHEAD
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_BCAST\_TOPO\_OVERHEAD

  - MPICH\_BCAST\_TOPO\_OVERHEAD

- **Description**: This cvar controls the size of the overhead.

- **Default:** 200

MPIR\_CVAR\_BCAST\_TOPO\_DIFF\_GROUPS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_BCAST\_TOPO\_DIFF\_GROUPS

  - MPICH\_BCAST\_TOPO\_DIFF\_GROUPS

- **Description**: This cvar controls the latency between different groups.

- **Default:** 2800

MPIR\_CVAR\_BCAST\_TOPO\_DIFF\_SWITCHES
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_BCAST\_TOPO\_DIFF\_SWITCHES

  - MPICH\_BCAST\_TOPO\_DIFF\_SWITCHES

- **Description**: This cvar controls the latency between different switches in the same groups.

- **Default:** 1900

MPIR\_CVAR\_BCAST\_TOPO\_SAME\_SWITCHES
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_BCAST\_TOPO\_SAME\_SWITCHES

  - MPICH\_BCAST\_TOPO\_SAME\_SWITCHES

- **Description**: This cvar controls the latency in the same switch.

- **Default:** 1600

MPIR\_CVAR\_BCAST\_IS\_NON\_BLOCKING
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_BCAST\_IS\_NON\_BLOCKING

  - MPICH\_BCAST\_IS\_NON\_BLOCKING

- **Description**: If set to true, MPI\_Bcast will use non-blocking send.

- **Default:** true

MPIR\_CVAR\_BCAST\_TREE\_PIPELINE\_CHUNK\_SIZE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_BCAST\_TREE\_PIPELINE\_CHUNK\_SIZE

  - MPICH\_BCAST\_TREE\_PIPELINE\_CHUNK\_SIZE

- **Description**: Indicates the chunk size for pipelined bcast.

- **Default:** 8192

MPIR\_CVAR\_BCAST\_RECV\_PRE\_POST
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_BCAST\_RECV\_PRE\_POST

  - MPICH\_BCAST\_RECV\_PRE\_POST

- **Description**: If set to true, MPI\_Bcast will pre-post all the receives.

- **Default:** false

MPIR\_CVAR\_BCAST\_INTER\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_BCAST\_INTER\_ALGORITHM

  - MPICH\_BCAST\_INTER\_ALGORITHM

- **Description**: Variable to select bcast algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - nb                      - Force nonblocking algorithm

  - remote\_send\_local\_bcast - Force remote-send-local-bcast algorithm

- **Default:** auto

MPIR\_CVAR\_IBCAST\_TREE\_KVAL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IBCAST\_TREE\_KVAL

  - MPICH\_IBCAST\_TREE\_KVAL

- **Description**: k value for tree (kary, knomial, etc.) based ibcast

- **Default:** 2

MPIR\_CVAR\_IBCAST\_TREE\_TYPE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IBCAST\_TREE\_TYPE

  - MPICH\_IBCAST\_TREE\_TYPE

- **Description**: Tree type for tree based ibcast kary      - kary tree type knomial\_1 - knomial\_1 tree type knomial\_2 - knomial\_2 tree type

- **Default:** kary

MPIR\_CVAR\_IBCAST\_TREE\_PIPELINE\_CHUNK\_SIZE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IBCAST\_TREE\_PIPELINE\_CHUNK\_SIZE

  - MPICH\_IBCAST\_TREE\_PIPELINE\_CHUNK\_SIZE

- **Description**: Maximum chunk size (in bytes) for pipelining in tree based ibcast. Default value is 0, that is, no pipelining by default

- **Default:** 0

MPIR\_CVAR\_IBCAST\_RING\_CHUNK\_SIZE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IBCAST\_RING\_CHUNK\_SIZE

  - MPICH\_IBCAST\_RING\_CHUNK\_SIZE

- **Description**: Maximum chunk size (in bytes) for pipelining in ibcast ring algorithm. Default value is 0, that is, no pipelining by default

- **Default:** 0

MPIR\_CVAR\_IBCAST\_INTRA\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IBCAST\_INTRA\_ALGORITHM

  - MPICH\_IBCAST\_INTRA\_ALGORITHM

- **Description**: Variable to select ibcast algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - sched\_auto - Internal algorithm selection for sched-based algorithms

  - sched\_binomial                             - Force Binomial algorithm

  - sched\_smp                                  - Force smp algorithm

  - sched\_scatter\_recursive\_doubling\_allgather - Force Scatter Recursive Doubling Allgather algorithm

  - sched\_scatter\_ring\_allgather               - Force Scatter Ring Allgather algorithm

  - tsp\_tree                               - Force Generic Transport Tree algorithm

  - tsp\_scatterv\_recexch\_allgatherv        - Force Generic Transport Scatterv followed by Recursive Exchange Allgatherv algorithm

  - tsp\_scatterv\_ring\_allgatherv           - Force Generic Transport Scatterv followed by Ring Allgatherv algorithm

  - tsp\_ring                               - Force Generic Transport Ring algorithm

- **Default:** auto

MPIR\_CVAR\_IBCAST\_SCATTERV\_KVAL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IBCAST\_SCATTERV\_KVAL

  - MPICH\_IBCAST\_SCATTERV\_KVAL

- **Description**: k value for tree based scatter in scatter\_recexch\_allgather algorithm

- **Default:** 2

MPIR\_CVAR\_IBCAST\_ALLGATHERV\_RECEXCH\_KVAL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IBCAST\_ALLGATHERV\_RECEXCH\_KVAL

  - MPICH\_IBCAST\_ALLGATHERV\_RECEXCH\_KVAL

- **Description**: k value for recursive exchange based allgather in scatter\_recexch\_allgather algorithm

- **Default:** 2

MPIR\_CVAR\_IBCAST\_INTER\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IBCAST\_INTER\_ALGORITHM

  - MPICH\_IBCAST\_INTER\_ALGORITHM

- **Description**: Variable to select ibcast algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - sched\_auto - Internal algorithm selection for sched-based algorithms

  - sched\_flat - Force flat algorithm

- **Default:** auto

MPIR\_CVAR\_GATHER\_INTER\_SHORT\_MSG\_SIZE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_GATHER\_INTER\_SHORT\_MSG\_SIZE

  - MPICH\_GATHER\_INTER\_SHORT\_MSG\_SIZE

- **Description**: use the short message algorithm for intercommunicator MPI\_Gather if the send buffer size is < this value (in bytes) (See also: MPIR\_CVAR\_GATHER\_VSMALL\_MSG\_SIZE)

- **Default:** 2048

MPIR\_CVAR\_GATHER\_INTRA\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_GATHER\_INTRA\_ALGORITHM

  - MPICH\_GATHER\_INTRA\_ALGORITHM

- **Description**: Variable to select gather algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - binomial - Force binomial algorithm

  - nb       - Force nonblocking algorithm

  - osu\_direct - Force OSU direct algorithm

  - osu\_direct\_block - Force OSU direct block algorithm

- **Default:** auto

MPIR\_CVAR\_GATHER\_INTER\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_GATHER\_INTER\_ALGORITHM

  - MPICH\_GATHER\_INTER\_ALGORITHM

- **Description**: Variable to select gather algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - linear                   - Force linear algorithm

  - local\_gather\_remote\_send - Force local-gather-remote-send algorithm

  - nb                       - Force nonblocking algorithm

- **Default:** auto

MPIR\_CVAR\_IGATHER\_INTRA\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IGATHER\_INTRA\_ALGORITHM

  - MPICH\_IGATHER\_INTRA\_ALGORITHM

- **Description**: Variable to select igather algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - sched\_auto - Internal algorithm selection for sched-based algorithms

  - sched\_binomial     - Force binomial algorithm

  - tsp\_tree       - Force genetric transport based tree algorithm

- **Default:** auto

MPIR\_CVAR\_IGATHER\_TREE\_KVAL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IGATHER\_TREE\_KVAL

  - MPICH\_IGATHER\_TREE\_KVAL

- **Description**: k value for tree based igather

- **Default:** 2

MPIR\_CVAR\_IGATHER\_INTER\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IGATHER\_INTER\_ALGORITHM

  - MPICH\_IGATHER\_INTER\_ALGORITHM

- **Description**: Variable to select igather algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - sched\_auto - Internal algorithm selection for sched-based algorithms

  - sched\_long  - Force long inter algorithm

  - sched\_short - Force short inter algorithm

- **Default:** auto

MPIR\_CVAR\_GATHERV\_INTRA\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_GATHERV\_INTRA\_ALGORITHM

  - MPICH\_GATHERV\_INTRA\_ALGORITHM

- **Description**: Variable to select gatherv algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - linear - Force linear algorithm

  - nb     - Force nonblocking algorithm

- **Default:** auto

MPIR\_CVAR\_GATHERV\_INTER\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_GATHERV\_INTER\_ALGORITHM

  - MPICH\_GATHERV\_INTER\_ALGORITHM

- **Description**: Variable to select gatherv algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - linear - Force linear algorithm

  - nb     - Force nonblocking algorithm

- **Default:** auto

MPIR\_CVAR\_IGATHERV\_INTRA\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IGATHERV\_INTRA\_ALGORITHM

  - MPICH\_IGATHERV\_INTRA\_ALGORITHM

- **Description**: Variable to select igatherv algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - sched\_auto - Internal algorithm selection for sched-based algorithms

  - sched\_linear         - Force linear algorithm

  - tsp\_linear       - Force generic transport based linear algorithm

- **Default:** auto

MPIR\_CVAR\_IGATHERV\_INTER\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IGATHERV\_INTER\_ALGORITHM

  - MPICH\_IGATHERV\_INTER\_ALGORITHM

- **Description**: Variable to select igatherv algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - sched\_auto - Internal algorithm selection for sched-based algorithms

  - sched\_linear - Force linear algorithm

  - tsp\_linear - Force generic transport based linear algorithm

- **Default:** auto

MPIR\_CVAR\_SCATTER\_INTER\_SHORT\_MSG\_SIZE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_SCATTER\_INTER\_SHORT\_MSG\_SIZE

  - MPICH\_SCATTER\_INTER\_SHORT\_MSG\_SIZE

- **Description**: use the short message algorithm for intercommunicator MPI\_Scatter if the send buffer size is < this value (in bytes)

- **Default:** 2048

MPIR\_CVAR\_SCATTER\_INTRA\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_SCATTER\_INTRA\_ALGORITHM

  - MPICH\_SCATTER\_INTRA\_ALGORITHM

- **Description**: Variable to select scatter algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - binomial - Force binomial algorithm

  - nb       - Force nonblocking algorithm

  - osu\_direct - Force OSU direct alogirthm

- **Default:** auto

MPIR\_CVAR\_SCATTER\_INTER\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_SCATTER\_INTER\_ALGORITHM

  - MPICH\_SCATTER\_INTER\_ALGORITHM

- **Description**: Variable to select scatter algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - linear                    - Force linear algorithm

  - nb                        - Force nonblocking algorithm

  - remote\_send\_local\_scatter - Force remote-send-local-scatter algorithm

- **Default:** auto

MPIR\_CVAR\_ISCATTER\_INTRA\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ISCATTER\_INTRA\_ALGORITHM

  - MPICH\_ISCATTER\_INTRA\_ALGORITHM

- **Description**: Variable to select iscatter algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - sched\_auto - Internal algorithm selection for sched-based algorithms

  - sched\_binomial     - Force binomial algorithm

  - tsp\_tree       - Force genetric transport based tree algorithm

- **Default:** auto

MPIR\_CVAR\_ISCATTER\_TREE\_KVAL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ISCATTER\_TREE\_KVAL

  - MPICH\_ISCATTER\_TREE\_KVAL

- **Description**: k value for tree based iscatter

- **Default:** 2

MPIR\_CVAR\_ISCATTER\_INTER\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ISCATTER\_INTER\_ALGORITHM

  - MPICH\_ISCATTER\_INTER\_ALGORITHM

- **Description**: Variable to select iscatter algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - sched\_auto - Internal algorithm selection for sched-based algorithms

  - sched\_linear                    - Force linear algorithm

  - sched\_remote\_send\_local\_scatter - Force remote-send-local-scatter algorithm

- **Default:** auto

MPIR\_CVAR\_SCATTERV\_INTRA\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_SCATTERV\_INTRA\_ALGORITHM

  - MPICH\_SCATTERV\_INTRA\_ALGORITHM

- **Description**: Variable to select scatterv algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - linear - Force linear algorithm

  - nb     - Force nonblocking algorithm

- **Default:** auto

MPIR\_CVAR\_SCATTERV\_INTER\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_SCATTERV\_INTER\_ALGORITHM

  - MPICH\_SCATTERV\_INTER\_ALGORITHM

- **Description**: Variable to select scatterv algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - linear - Force linear algorithm

  - nb     - Force nonblocking algorithm

- **Default:** auto

MPIR\_CVAR\_ISCATTERV\_INTRA\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ISCATTERV\_INTRA\_ALGORITHM

  - MPICH\_ISCATTERV\_INTRA\_ALGORITHM

- **Description**: Variable to select iscatterv algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - sched\_auto - Internal algorithm selection for sched-based algorithms

  - sched\_linear    - Force linear algorithm

  - tsp\_linear  - Force generic transport based linear algorithm

- **Default:** auto

MPIR\_CVAR\_ISCATTERV\_INTER\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ISCATTERV\_INTER\_ALGORITHM

  - MPICH\_ISCATTERV\_INTER\_ALGORITHM

- **Description**: Variable to select iscatterv algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - sched\_auto - Internal algorithm selection for sched-based algorithms

  - sched\_linear - Force linear algorithm

  - tsp\_linear - Force generic transport based linear algorithm

- **Default:** auto

MPIR\_CVAR\_ALLGATHER\_SHORT\_MSG\_SIZE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ALLGATHER\_SHORT\_MSG\_SIZE

  - MPICH\_ALLGATHER\_SHORT\_MSG\_SIZE

- **Description**: For MPI\_Allgather and MPI\_Allgatherv, the short message algorithm will be used if the send buffer size is < this value (in bytes). (See also: MPIR\_CVAR\_ALLGATHER\_LONG\_MSG\_SIZE)

- **Default:** 81920

MPIR\_CVAR\_ALLGATHER\_LONG\_MSG\_SIZE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ALLGATHER\_LONG\_MSG\_SIZE

  - MPICH\_ALLGATHER\_LONG\_MSG\_SIZE

- **Description**: For MPI\_Allgather and MPI\_Allgatherv, the long message algorithm will be used if the send buffer size is >= this value (in bytes) (See also: MPIR\_CVAR\_ALLGATHER\_SHORT\_MSG\_SIZE)

- **Default:** 524288

MPIR\_CVAR\_ALLGATHER\_INTRA\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ALLGATHER\_INTRA\_ALGORITHM

  - MPICH\_ALLGATHER\_INTRA\_ALGORITHM

- **Description**: Variable to select allgather algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - brucks              - Force brucks algorithm

  - k\_brucks            - Force brucks algorithm

  - nb                  - Force nonblocking algorithm

  - recursive\_doubling  - Force recursive doubling algorithm

  - ring                - Force ring algorithm

  - recexch\_doubling    - Force recexch distance doubling algorithm

  - recexch\_halving     - Force recexch distance halving algorithm

  - osu\_direct          - Force MVAPICH direct algorithm

  - osu\_direct\_spread   - Force MVAPICH direct spread algorithm

  - osu\_gather\_bcast    - Force MVAPICH gather-bcast algorithm

  - osu\_gpu\_compression - Force MVAPICH gpu compression algorithm

- **Default:** auto

MPIR\_CVAR\_ALLGATHER\_BRUCKS\_KVAL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ALLGATHER\_BRUCKS\_KVAL

  - MPICH\_ALLGATHER\_BRUCKS\_KVAL

- **Description**: radix (k) value for generic transport brucks based allgather

- **Default:** 2

MPIR\_CVAR\_ALLGATHER\_RECEXCH\_KVAL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ALLGATHER\_RECEXCH\_KVAL

  - MPICH\_ALLGATHER\_RECEXCH\_KVAL

- **Description**: k value for recursive exchange based allgather

- **Default:** 2

MPIR\_CVAR\_ALLGATHER\_RECEXCH\_SINGLE\_PHASE\_RECV
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ALLGATHER\_RECEXCH\_SINGLE\_PHASE\_RECV

  - MPICH\_ALLGATHER\_RECEXCH\_SINGLE\_PHASE\_RECV

- **Description**: This CVAR controls whether the recv is posted for one phase or two phases in recexch algos. By default, we post the recvs for 2 phases.

- **Default:** false

MPIR\_CVAR\_ALLGATHER\_INTER\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ALLGATHER\_INTER\_ALGORITHM

  - MPICH\_ALLGATHER\_INTER\_ALGORITHM

- **Description**: Variable to select allgather algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - local\_gather\_remote\_bcast - Force local-gather-remote-bcast algorithm

  - nb                        - Force nonblocking algorithm

- **Default:** auto

MPIR\_CVAR\_IALLGATHER\_RECEXCH\_KVAL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IALLGATHER\_RECEXCH\_KVAL

  - MPICH\_IALLGATHER\_RECEXCH\_KVAL

- **Description**: k value for recursive exchange based iallgather

- **Default:** 2

MPIR\_CVAR\_IALLGATHER\_BRUCKS\_KVAL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IALLGATHER\_BRUCKS\_KVAL

  - MPICH\_IALLGATHER\_BRUCKS\_KVAL

- **Description**: k value for radix in brucks based iallgather

- **Default:** 2

MPIR\_CVAR\_IALLGATHER\_INTRA\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IALLGATHER\_INTRA\_ALGORITHM

  - MPICH\_IALLGATHER\_INTRA\_ALGORITHM

- **Description**: Variable to select iallgather algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - sched\_auto - Internal algorithm selection for sched-based algorithms

  - sched\_ring               - Force ring algorithm

  - sched\_brucks             - Force brucks algorithm

  - sched\_recursive\_doubling - Force recursive doubling algorithm

  - tsp\_ring       - Force generic transport ring algorithm

  - tsp\_brucks     - Force generic transport based brucks algorithm

  - tsp\_recexch\_doubling - Force generic transport recursive exchange with neighbours doubling in distance in each phase

  - tsp\_recexch\_halving  - Force generic transport recursive exchange with neighbours halving in distance in each phase

- **Default:** auto

MPIR\_CVAR\_IALLGATHER\_INTER\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IALLGATHER\_INTER\_ALGORITHM

  - MPICH\_IALLGATHER\_INTER\_ALGORITHM

- **Description**: Variable to select iallgather algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - sched\_auto - Internal algorithm selection for sched-based algorithms

  - sched\_local\_gather\_remote\_bcast - Force local-gather-remote-bcast algorithm

- **Default:** auto

MPIR\_CVAR\_ALLGATHERV\_PIPELINE\_MSG\_SIZE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ALLGATHERV\_PIPELINE\_MSG\_SIZE

  - MPICH\_ALLGATHERV\_PIPELINE\_MSG\_SIZE

- **Description**: The smallest message size that will be used for the pipelined, large-message, ring algorithm in the MPI\_Allgatherv implementation.

- **Default:** 32768

MPIR\_CVAR\_ALLGATHERV\_INTRA\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ALLGATHERV\_INTRA\_ALGORITHM

  - MPICH\_ALLGATHERV\_INTRA\_ALGORITHM

- **Description**: Variable to select allgatherv algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - brucks             - Force brucks algorithm

  - nb                 - Force nonblocking algorithm

  - recursive\_doubling - Force recursive doubling algorithm

  - ring               - Force ring algorithm

- **Default:** auto

MPIR\_CVAR\_ALLGATHERV\_INTER\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ALLGATHERV\_INTER\_ALGORITHM

  - MPICH\_ALLGATHERV\_INTER\_ALGORITHM

- **Description**: Variable to select allgatherv algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - nb                        - Force nonblocking algorithm

  - remote\_gather\_local\_bcast - Force remote-gather-local-bcast algorithm

- **Default:** auto

MPIR\_CVAR\_IALLGATHERV\_RECEXCH\_KVAL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IALLGATHERV\_RECEXCH\_KVAL

  - MPICH\_IALLGATHERV\_RECEXCH\_KVAL

- **Description**: k value for recursive exchange based iallgatherv

- **Default:** 2

MPIR\_CVAR\_IALLGATHERV\_BRUCKS\_KVAL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IALLGATHERV\_BRUCKS\_KVAL

  - MPICH\_IALLGATHERV\_BRUCKS\_KVAL

- **Description**: k value for radix in brucks based iallgatherv

- **Default:** 2

MPIR\_CVAR\_IALLGATHERV\_INTRA\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IALLGATHERV\_INTRA\_ALGORITHM

  - MPICH\_IALLGATHERV\_INTRA\_ALGORITHM

- **Description**: Variable to select iallgatherv algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - sched\_auto - Internal algorithm selection for sched-based algorithms

  - sched\_brucks             - Force brucks algorithm

  - sched\_recursive\_doubling - Force recursive doubling algorithm

  - sched\_ring               - Force ring algorithm

  - tsp\_recexch\_doubling - Force generic transport recursive exchange with neighbours doubling in distance in each phase

  - tsp\_recexch\_halving  - Force generic transport recursive exchange with neighbours halving in distance in each phase

  - tsp\_ring             - Force generic transport ring algorithm

  - tsp\_brucks           - Force generic transport based brucks algorithm

- **Default:** auto

MPIR\_CVAR\_IALLGATHERV\_INTER\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IALLGATHERV\_INTER\_ALGORITHM

  - MPICH\_IALLGATHERV\_INTER\_ALGORITHM

- **Description**: Variable to select iallgatherv algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - sched\_auto - Internal algorithm selection for sched-based algorithms

  - sched\_remote\_gather\_local\_bcast - Force remote-gather-local-bcast algorithm

- **Default:** auto

MPIR\_CVAR\_ALLTOALL\_SHORT\_MSG\_SIZE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ALLTOALL\_SHORT\_MSG\_SIZE

  - MPICH\_ALLTOALL\_SHORT\_MSG\_SIZE

- **Description**: the short message algorithm will be used if the per-destination message size (sendcount\*size(sendtype)) is <= this value (See also: MPIR\_CVAR\_ALLTOALL\_MEDIUM\_MSG\_SIZE)

- **Default:** 256

MPIR\_CVAR\_ALLTOALL\_MEDIUM\_MSG\_SIZE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ALLTOALL\_MEDIUM\_MSG\_SIZE

  - MPICH\_ALLTOALL\_MEDIUM\_MSG\_SIZE

- **Description**: the medium message algorithm will be used if the per-destination message size (sendcount\*size(sendtype)) is <= this value and larger than MPIR\_CVAR\_ALLTOALL\_SHORT\_MSG\_SIZE (See also: MPIR\_CVAR\_ALLTOALL\_SHORT\_MSG\_SIZE)

- **Default:** 32768

MPIR\_CVAR\_ALLTOALL\_THROTTLE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ALLTOALL\_THROTTLE

  - MPICH\_ALLTOALL\_THROTTLE

- **Description**: max no. of irecvs/isends posted at a time in some alltoall algorithms. Setting it to 0 causes all irecvs/isends to be posted at once

- **Default:** 32

MPIR\_CVAR\_ALLTOALL\_INTRA\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ALLTOALL\_INTRA\_ALGORITHM

  - MPICH\_ALLTOALL\_INTRA\_ALGORITHM

- **Description**: Variable to select alltoall algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - brucks                    - Force brucks algorithm

  - k\_brucks                  - Force Force radix k brucks algorithm

  - nb                        - Force nonblocking algorithm

  - pairwise                  - Force pairwise algorithm

  - pairwise\_sendrecv\_replace - Force pairwise sendrecv replace algorithm

  - scattered                 - Force scattered algorithm

  - osu\_gpu\_compression       - Force compression algorithm

- **Default:** auto

MPIR\_CVAR\_ALLTOALL\_BRUCKS\_KVAL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ALLTOALL\_BRUCKS\_KVAL

  - MPICH\_ALLTOALL\_BRUCKS\_KVAL

- **Description**: radix (k) value for generic transport brucks based alltoall

- **Default:** 2

MPIR\_CVAR\_ALLTOALL\_INTER\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ALLTOALL\_INTER\_ALGORITHM

  - MPICH\_ALLTOALL\_INTER\_ALGORITHM

- **Description**: Variable to select alltoall algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - nb                - Force nonblocking algorithm

  - pairwise\_exchange - Force pairwise exchange algorithm

- **Default:** auto

MPIR\_CVAR\_IALLTOALL\_INTRA\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IALLTOALL\_INTRA\_ALGORITHM

  - MPICH\_IALLTOALL\_INTRA\_ALGORITHM

- **Description**: Variable to select ialltoall algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - sched\_auto - Internal algorithm selection for sched-based algorithms

  - sched\_brucks            - Force brucks algorithm

  - sched\_inplace           - Force inplace algorithm

  - sched\_pairwise          - Force pairwise algorithm

  - sched\_permuted\_sendrecv - Force permuted sendrecv algorithm

  - tsp\_ring            - Force generic transport based ring algorithm

  - tsp\_brucks          - Force generic transport based brucks algorithm

  - tsp\_scattered       - Force generic transport based scattered algorithm

- **Default:** auto

MPIR\_CVAR\_IALLTOALL\_INTER\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IALLTOALL\_INTER\_ALGORITHM

  - MPICH\_IALLTOALL\_INTER\_ALGORITHM

- **Description**: Variable to select ialltoall algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - sched\_auto - Internal algorithm selection for sched-based algorithms

  - sched\_pairwise\_exchange - Force pairwise exchange algorithm

- **Default:** auto

MPIR\_CVAR\_ALLTOALLV\_INTRA\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ALLTOALLV\_INTRA\_ALGORITHM

  - MPICH\_ALLTOALLV\_INTRA\_ALGORITHM

- **Description**: Variable to select alltoallv algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - nb                        - Force nonblocking algorithm

  - pairwise\_sendrecv\_replace - Force pairwise\_sendrecv\_replace algorithm

  - scattered                 - Force scattered algorithm

- **Default:** auto

MPIR\_CVAR\_ALLTOALLV\_INTER\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ALLTOALLV\_INTER\_ALGORITHM

  - MPICH\_ALLTOALLV\_INTER\_ALGORITHM

- **Description**: Variable to select alltoallv algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - pairwise\_exchange - Force pairwise exchange algorithm

  - nb                - Force nonblocking algorithm

- **Default:** auto

MPIR\_CVAR\_IALLTOALLV\_INTRA\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IALLTOALLV\_INTRA\_ALGORITHM

  - MPICH\_IALLTOALLV\_INTRA\_ALGORITHM

- **Description**: Variable to select ialltoallv algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - sched\_auto - Internal algorithm selection for sched-based algorithms

  - sched\_blocked           - Force blocked algorithm

  - sched\_inplace           - Force inplace algorithm

  - tsp\_scattered       - Force generic transport based scattered algorithm

  - tsp\_blocked         - Force generic transport blocked algorithm

  - tsp\_inplace         - Force generic transport inplace algorithm

- **Default:** auto

MPIR\_CVAR\_IALLTOALLV\_INTER\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IALLTOALLV\_INTER\_ALGORITHM

  - MPICH\_IALLTOALLV\_INTER\_ALGORITHM

- **Description**: Variable to select ialltoallv algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - sched\_auto - Internal algorithm selection for sched-based algorithms

  - sched\_pairwise\_exchange - Force pairwise exchange algorithm

- **Default:** auto

MPIR\_CVAR\_IALLTOALLV\_SCATTERED\_OUTSTANDING\_TASKS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IALLTOALLV\_SCATTERED\_OUTSTANDING\_TASKS

  - MPICH\_IALLTOALLV\_SCATTERED\_OUTSTANDING\_TASKS

- **Description**: Maximum number of outstanding sends and recvs posted at a time

- **Default:** 64

MPIR\_CVAR\_IALLTOALLV\_SCATTERED\_BATCH\_SIZE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IALLTOALLV\_SCATTERED\_BATCH\_SIZE

  - MPICH\_IALLTOALLV\_SCATTERED\_BATCH\_SIZE

- **Description**: Number of send/receive tasks that scattered algorithm waits for completion before posting another batch of send/receives of that size

- **Default:** 4

MPIR\_CVAR\_ALLTOALLW\_INTRA\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ALLTOALLW\_INTRA\_ALGORITHM

  - MPICH\_ALLTOALLW\_INTRA\_ALGORITHM

- **Description**: Variable to select alltoallw algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - nb                        - Force nonblocking algorithm

  - pairwise\_sendrecv\_replace - Force pairwise sendrecv replace algorithm

  - scattered                 - Force scattered algorithm

- **Default:** auto

MPIR\_CVAR\_ALLTOALLW\_INTER\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ALLTOALLW\_INTER\_ALGORITHM

  - MPICH\_ALLTOALLW\_INTER\_ALGORITHM

- **Description**: Variable to select alltoallw algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - nb                - Force nonblocking algorithm

  - pairwise\_exchange - Force pairwise exchange algorithm

- **Default:** auto

MPIR\_CVAR\_IALLTOALLW\_INTRA\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IALLTOALLW\_INTRA\_ALGORITHM

  - MPICH\_IALLTOALLW\_INTRA\_ALGORITHM

- **Description**: Variable to select ialltoallw algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - sched\_auto - Internal algorithm selection for sched-based algorithms

  - sched\_blocked           - Force blocked algorithm

  - sched\_inplace           - Force inplace algorithm

  - tsp\_blocked   - Force generic transport based blocked algorithm

  - tsp\_inplace   - Force generic transport based inplace algorithm

- **Default:** auto

MPIR\_CVAR\_IALLTOALLW\_INTER\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IALLTOALLW\_INTER\_ALGORITHM

  - MPICH\_IALLTOALLW\_INTER\_ALGORITHM

- **Description**: Variable to select ialltoallw algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - sched\_auto - Internal algorithm selection for sched-based algorithms

  - sched\_pairwise\_exchange - Force pairwise exchange algorithm

- **Default:** auto

MPIR\_CVAR\_REDUCE\_SHORT\_MSG\_SIZE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_REDUCE\_SHORT\_MSG\_SIZE

  - MPICH\_REDUCE\_SHORT\_MSG\_SIZE

- **Description**: the short message algorithm will be used if the send buffer size is <= this value (in bytes)

- **Default:** 2048

MPIR\_CVAR\_MAX\_SMP\_REDUCE\_MSG\_SIZE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_MAX\_SMP\_REDUCE\_MSG\_SIZE

  - MPICH\_MAX\_SMP\_REDUCE\_MSG\_SIZE

- **Description**: Maximum message size for which SMP-aware reduce is used.  A value of '0' uses SMP-aware reduce for all message sizes.

- **Default:** 0

MPIR\_CVAR\_REDUCE\_INTRA\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_REDUCE\_INTRA\_ALGORITHM

  - MPICH\_REDUCE\_INTRA\_ALGORITHM

- **Description**: Variable to select reduce algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - binomial              - Force binomial algorithm

  - nb                    - Force nonblocking algorithm

  - smp                   - Force smp algorithm

  - reduce\_scatter\_gather - Force reduce scatter gather algorithm

  - osu\_knomial           - Force MVAPICH knomial algorithm

  - osu\_allreduce         - Force MVAPICH allreduce algorithm

- **Default:** auto

MPIR\_CVAR\_REDUCE\_INTER\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_REDUCE\_INTER\_ALGORITHM

  - MPICH\_REDUCE\_INTER\_ALGORITHM

- **Description**: Variable to select reduce algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - local\_reduce\_remote\_send - Force local-reduce-remote-send algorithm

  - nb                       - Force nonblocking algorithm

- **Default:** auto

MPIR\_CVAR\_IREDUCE\_TREE\_KVAL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IREDUCE\_TREE\_KVAL

  - MPICH\_IREDUCE\_TREE\_KVAL

- **Description**: k value for tree (kary, knomial, etc.) based ireduce

- **Default:** 2

MPIR\_CVAR\_IREDUCE\_TREE\_TYPE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IREDUCE\_TREE\_TYPE

  - MPICH\_IREDUCE\_TREE\_TYPE

- **Description**: Tree type for tree based ireduce kary      - kary tree knomial\_1 - knomial\_1 tree knomial\_2 - knomial\_2 tree topology\_aware - topology\_aware tree type topology\_aware\_k - topology\_aware tree type with branching factor k topology\_wave - topology\_wave tree type

- **Default:** kary

MPIR\_CVAR\_IREDUCE\_TOPO\_REORDER\_ENABLE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IREDUCE\_TOPO\_REORDER\_ENABLE

  - MPICH\_IREDUCE\_TOPO\_REORDER\_ENABLE

- **Description**: This cvar controls if the leaders are reordered based on the number of ranks in each group.

- **Default:** true

MPIR\_CVAR\_IREDUCE\_TOPO\_OVERHEAD
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IREDUCE\_TOPO\_OVERHEAD

  - MPICH\_IREDUCE\_TOPO\_OVERHEAD

- **Description**: This cvar controls the size of the overhead.

- **Default:** 200

MPIR\_CVAR\_IREDUCE\_TOPO\_DIFF\_GROUPS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IREDUCE\_TOPO\_DIFF\_GROUPS

  - MPICH\_IREDUCE\_TOPO\_DIFF\_GROUPS

- **Description**: This cvar controls the latency between different groups.

- **Default:** 2800

MPIR\_CVAR\_IREDUCE\_TOPO\_DIFF\_SWITCHES
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IREDUCE\_TOPO\_DIFF\_SWITCHES

  - MPICH\_IREDUCE\_TOPO\_DIFF\_SWITCHES

- **Description**: This cvar controls the latency between different switches in the same groups.

- **Default:** 1900

MPIR\_CVAR\_IREDUCE\_TOPO\_SAME\_SWITCHES
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IREDUCE\_TOPO\_SAME\_SWITCHES

  - MPICH\_IREDUCE\_TOPO\_SAME\_SWITCHES

- **Description**: This cvar controls the latency in the same switch.

- **Default:** 1600

MPIR\_CVAR\_IREDUCE\_TREE\_PIPELINE\_CHUNK\_SIZE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IREDUCE\_TREE\_PIPELINE\_CHUNK\_SIZE

  - MPICH\_IREDUCE\_TREE\_PIPELINE\_CHUNK\_SIZE

- **Description**: Maximum chunk size (in bytes) for pipelining in tree based ireduce. Default value is 0, that is, no pipelining by default

- **Default:** -1

MPIR\_CVAR\_IREDUCE\_RING\_CHUNK\_SIZE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IREDUCE\_RING\_CHUNK\_SIZE

  - MPICH\_IREDUCE\_RING\_CHUNK\_SIZE

- **Description**: Maximum chunk size (in bytes) for pipelining in ireduce ring algorithm. Default value is 0, that is, no pipelining by default

- **Default:** 0

MPIR\_CVAR\_IREDUCE\_TREE\_BUFFER\_PER\_CHILD
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IREDUCE\_TREE\_BUFFER\_PER\_CHILD

  - MPICH\_IREDUCE\_TREE\_BUFFER\_PER\_CHILD

- **Description**: If set to true, a rank in tree algorithms will allocate a dedicated buffer for every child it receives data from. This would mean more memory consumption but it would allow preposting of the receives and hence reduce the number of unexpected messages. If set to false, there is only one buffer that is used to receive the data from all the children. The receives are therefore serialized, that is, only one receive can be posted at a time.

- **Default:** 0

MPIR\_CVAR\_IREDUCE\_INTRA\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IREDUCE\_INTRA\_ALGORITHM

  - MPICH\_IREDUCE\_INTRA\_ALGORITHM

- **Description**: Variable to select ireduce algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - sched\_auto - Internal algorithm selection for sched-based algorithms

  - sched\_smp                   - Force smp algorithm

  - sched\_binomial              - Force binomial algorithm

  - sched\_reduce\_scatter\_gather - Force reduce scatter gather algorithm

  - tsp\_tree                - Force Generic Transport Tree

  - tsp\_ring                - Force Generic Transport Ring

- **Default:** auto

MPIR\_CVAR\_IREDUCE\_INTER\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IREDUCE\_INTER\_ALGORITHM

  - MPICH\_IREDUCE\_INTER\_ALGORITHM

- **Description**: Variable to select ireduce algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - sched\_auto - Internal algorithm selection for sched-based algorithms

  - sched\_local\_reduce\_remote\_send - Force local-reduce-remote-send algorithm

- **Default:** auto

MPIR\_CVAR\_ALLREDUCE\_SHORT\_MSG\_SIZE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ALLREDUCE\_SHORT\_MSG\_SIZE

  - MPICH\_ALLREDUCE\_SHORT\_MSG\_SIZE

- **Description**: the short message algorithm will be used if the send buffer size is <= this value (in bytes)

- **Default:** 2048

MPIR\_CVAR\_MAX\_SMP\_ALLREDUCE\_MSG\_SIZE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_MAX\_SMP\_ALLREDUCE\_MSG\_SIZE

  - MPICH\_MAX\_SMP\_ALLREDUCE\_MSG\_SIZE

- **Description**: Maximum message size for which SMP-aware allreduce is used.  A value of '0' uses SMP-aware allreduce for all message sizes.

- **Default:** 0

MPIR\_CVAR\_ALLREDUCE\_INTRA\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ALLREDUCE\_INTRA\_ALGORITHM

  - MPICH\_ALLREDUCE\_INTRA\_ALGORITHM

- **Description**: Variable to select allreduce algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - nb                       - Force nonblocking algorithm

  - smp                      - Force smp algorithm

  - recursive\_doubling       - Force recursive doubling algorithm

  - reduce\_scatter\_allgather - Force reduce scatter allgather algorithm

  - tree                     - Force pipelined tree algorithm

  - recexch                  - Force generic transport recursive exchange algorithm

  - ring                     - Force ring algorithm

  - k\_reduce\_scatter\_allgather - Force reduce scatter allgather algorithm

  - osu\_rd\_compression - Force GPU compression recursive doubling

  - osu\_rsa\_ring\_compression - Force GPU compression ring

- **Default:** auto

MPIR\_CVAR\_ALLREDUCE\_TREE\_TYPE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ALLREDUCE\_TREE\_TYPE

  - MPICH\_ALLREDUCE\_TREE\_TYPE

- **Description**: Tree type for tree based allreduce knomial\_1 is default as it supports both commutative and non-commutative reduce operations kary      - kary tree type knomial\_1 - knomial\_1 tree type (tree grows starting from the left of the root) knomial\_2 - knomial\_2 tree type (tree grows starting from the right of the root) topology\_aware - topology\_aware tree type topology\_aware\_k - topology\_aware tree type with branching factor k topology\_wave - topology\_wave tree type

- **Default:** knomial\_1

MPIR\_CVAR\_ALLREDUCE\_TREE\_KVAL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ALLREDUCE\_TREE\_KVAL

  - MPICH\_ALLREDUCE\_TREE\_KVAL

- **Description**: Indicates the branching factor for kary or knomial trees.

- **Default:** 2

MPIR\_CVAR\_ALLREDUCE\_TOPO\_REORDER\_ENABLE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ALLREDUCE\_TOPO\_REORDER\_ENABLE

  - MPICH\_ALLREDUCE\_TOPO\_REORDER\_ENABLE

- **Description**: This cvar controls if the leaders are reordered based on the number of ranks in each group.

- **Default:** true

MPIR\_CVAR\_ALLREDUCE\_TOPO\_OVERHEAD
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ALLREDUCE\_TOPO\_OVERHEAD

  - MPICH\_ALLREDUCE\_TOPO\_OVERHEAD

- **Description**: This cvar controls the size of the overhead.

- **Default:** 200

MPIR\_CVAR\_ALLREDUCE\_TOPO\_DIFF\_GROUPS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ALLREDUCE\_TOPO\_DIFF\_GROUPS

  - MPICH\_ALLREDUCE\_TOPO\_DIFF\_GROUPS

- **Description**: This cvar controls the latency between different groups.

- **Default:** 2800

MPIR\_CVAR\_ALLREDUCE\_TOPO\_DIFF\_SWITCHES
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ALLREDUCE\_TOPO\_DIFF\_SWITCHES

  - MPICH\_ALLREDUCE\_TOPO\_DIFF\_SWITCHES

- **Description**: This cvar controls the latency between different switches in the same groups.

- **Default:** 1900

MPIR\_CVAR\_ALLREDUCE\_TOPO\_SAME\_SWITCHES
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ALLREDUCE\_TOPO\_SAME\_SWITCHES

  - MPICH\_ALLREDUCE\_TOPO\_SAME\_SWITCHES

- **Description**: This cvar controls the latency in the same switch.

- **Default:** 1600

MPIR\_CVAR\_ALLREDUCE\_TREE\_PIPELINE\_CHUNK\_SIZE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ALLREDUCE\_TREE\_PIPELINE\_CHUNK\_SIZE

  - MPICH\_ALLREDUCE\_TREE\_PIPELINE\_CHUNK\_SIZE

- **Description**: Maximum chunk size (in bytes) for pipelining in tree based allreduce. Default value is 0, that is, no pipelining by default

- **Default:** 0

MPIR\_CVAR\_ALLREDUCE\_TREE\_BUFFER\_PER\_CHILD
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ALLREDUCE\_TREE\_BUFFER\_PER\_CHILD

  - MPICH\_ALLREDUCE\_TREE\_BUFFER\_PER\_CHILD

- **Description**: If set to true, a rank in tree\_kary and tree\_knomial algorithms will allocate a dedicated buffer for every child it receives data from. This would mean more memory consumption but it would allow preposting of the receives and hence reduce the number of unexpected messages. If set to false, there is only one buffer that is used to receive the data from all the children. The receives are therefore serialized, that is, only one receive can be posted at a time.

- **Default:** 0

MPIR\_CVAR\_ALLREDUCE\_RECEXCH\_KVAL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ALLREDUCE\_RECEXCH\_KVAL

  - MPICH\_ALLREDUCE\_RECEXCH\_KVAL

- **Description**: k value for recursive exchange based allreduce

- **Default:** 2

MPIR\_CVAR\_ALLREDUCE\_RECEXCH\_SINGLE\_PHASE\_RECV
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ALLREDUCE\_RECEXCH\_SINGLE\_PHASE\_RECV

  - MPICH\_ALLREDUCE\_RECEXCH\_SINGLE\_PHASE\_RECV

- **Description**: This CVAR controls whether the recv is posted for one phase or two phases in recexch algos. By default, we post the recvs for 2 phases.

- **Default:** false

MPIR\_CVAR\_ALLREDUCE\_INTER\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ALLREDUCE\_INTER\_ALGORITHM

  - MPICH\_ALLREDUCE\_INTER\_ALGORITHM

- **Description**: Variable to select allreduce algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - nb                    - Force nonblocking algorithm

  - reduce\_exchange\_bcast - Force reduce-exchange-bcast algorithm

- **Default:** auto

MPIR\_CVAR\_IALLREDUCE\_TREE\_KVAL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IALLREDUCE\_TREE\_KVAL

  - MPICH\_IALLREDUCE\_TREE\_KVAL

- **Description**: k value for tree based iallreduce (for tree\_kary and tree\_knomial)

- **Default:** 2

MPIR\_CVAR\_IALLREDUCE\_TREE\_TYPE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IALLREDUCE\_TREE\_TYPE

  - MPICH\_IALLREDUCE\_TREE\_TYPE

- **Description**: Tree type for tree based ibcast kary      - kary tree type knomial\_1 - knomial\_1 tree type knomial\_2 - knomial\_2 tree type

- **Default:** kary

MPIR\_CVAR\_IALLREDUCE\_TREE\_PIPELINE\_CHUNK\_SIZE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IALLREDUCE\_TREE\_PIPELINE\_CHUNK\_SIZE

  - MPICH\_IALLREDUCE\_TREE\_PIPELINE\_CHUNK\_SIZE

- **Description**: Maximum chunk size (in bytes) for pipelining in tree based iallreduce. Default value is 0, that is, no pipelining by default

- **Default:** 0

MPIR\_CVAR\_IALLREDUCE\_TREE\_BUFFER\_PER\_CHILD
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IALLREDUCE\_TREE\_BUFFER\_PER\_CHILD

  - MPICH\_IALLREDUCE\_TREE\_BUFFER\_PER\_CHILD

- **Description**: If set to true, a rank in tree\_kary and tree\_knomial algorithms will allocate a dedicated buffer for every child it receives data from. This would mean more memory consumption but it would allow preposting of the receives and hence reduce the number of unexpected messages. If set to false, there is only one buffer that is used to receive the data from all the children. The receives are therefore serialized, that is, only one receive can be posted at a time.

- **Default:** 0

MPIR\_CVAR\_IALLREDUCE\_RECEXCH\_KVAL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IALLREDUCE\_RECEXCH\_KVAL

  - MPICH\_IALLREDUCE\_RECEXCH\_KVAL

- **Description**: k value for recursive exchange based iallreduce

- **Default:** 2

MPIR\_CVAR\_IALLREDUCE\_INTRA\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IALLREDUCE\_INTRA\_ALGORITHM

  - MPICH\_IALLREDUCE\_INTRA\_ALGORITHM

- **Description**: Variable to select iallreduce algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - sched\_auto - Internal algorithm selection for sched-based algorithms

  - sched\_naive                      - Force naive algorithm

  - sched\_smp                        - Force smp algorithm

  - sched\_recursive\_doubling         - Force recursive doubling algorithm

  - sched\_reduce\_scatter\_allgather   - Force reduce scatter allgather algorithm

  - tsp\_recexch\_single\_buffer    - Force generic transport recursive exchange with single buffer for receives

  - tsp\_recexch\_multiple\_buffer  - Force generic transport recursive exchange with multiple buffers for receives

  - tsp\_tree                     - Force generic transport tree algorithm

  - tsp\_ring                     - Force generic transport ring algorithm

  - tsp\_recexch\_reduce\_scatter\_recexch\_allgatherv  - Force generic transport recursive exchange with reduce scatter and allgatherv

- **Default:** auto

MPIR\_CVAR\_IALLREDUCE\_INTER\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IALLREDUCE\_INTER\_ALGORITHM

  - MPICH\_IALLREDUCE\_INTER\_ALGORITHM

- **Description**: Variable to select iallreduce algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - sched\_auto - Internal algorithm selection for sched-based algorithms

  - sched\_remote\_reduce\_local\_bcast - Force remote-reduce-local-bcast algorithm

- **Default:** auto

MPIR\_CVAR\_REDUCE\_SCATTER\_COMMUTATIVE\_LONG\_MSG\_SIZE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_REDUCE\_SCATTER\_COMMUTATIVE\_LONG\_MSG\_SIZE

  - MPICH\_REDUCE\_SCATTER\_COMMUTATIVE\_LONG\_MSG\_SIZE

- **Description**: the long message algorithm will be used if the operation is commutative and the send buffer size is >= this value (in bytes)

- **Default:** 524288

MPIR\_CVAR\_REDUCE\_SCATTER\_INTRA\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_REDUCE\_SCATTER\_INTRA\_ALGORITHM

  - MPICH\_REDUCE\_SCATTER\_INTRA\_ALGORITHM

- **Description**: Variable to select reduce\_scatter algorithm

  - auto                 - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - nb                   - Force nonblocking algorithm

  - noncommutative       - Force noncommutative algorithm

  - pairwise             - Force pairwise algorithm

  - recursive\_doubling   - Force recursive doubling algorithm

  - recursive\_halving    - Force recursive halving algorithm

  - osu\_basic            - Force MVAPICH basic algorithm

  - osu\_ring             - Force MVAPICH ring algorithm

  - osu\_ring\_compression - Force compression algorithm

- **Default:** auto

MPIR\_CVAR\_REDUCE\_SCATTER\_INTER\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_REDUCE\_SCATTER\_INTER\_ALGORITHM

  - MPICH\_REDUCE\_SCATTER\_INTER\_ALGORITHM

- **Description**: Variable to select reduce\_scatter algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - nb                          - Force nonblocking algorithm

  - remote\_reduce\_local\_scatter - Force remote-reduce-local-scatter algorithm

- **Default:** auto

MPIR\_CVAR\_IREDUCE\_SCATTER\_RECEXCH\_KVAL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IREDUCE\_SCATTER\_RECEXCH\_KVAL

  - MPICH\_IREDUCE\_SCATTER\_RECEXCH\_KVAL

- **Description**: k value for recursive exchange based ireduce\_scatter

- **Default:** 2

MPIR\_CVAR\_IREDUCE\_SCATTER\_INTRA\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IREDUCE\_SCATTER\_INTRA\_ALGORITHM

  - MPICH\_IREDUCE\_SCATTER\_INTRA\_ALGORITHM

- **Description**: Variable to select ireduce\_scatter algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - sched\_auto - Internal algorithm selection for sched-based algorithms

  - sched\_noncommutative     - Force noncommutative algorithm

  - sched\_recursive\_doubling - Force recursive doubling algorithm

  - sched\_pairwise           - Force pairwise algorithm

  - sched\_recursive\_halving  - Force recursive halving algorithm

  - tsp\_recexch          - Force generic transport recursive exchange algorithm

- **Default:** auto

MPIR\_CVAR\_IREDUCE\_SCATTER\_INTER\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IREDUCE\_SCATTER\_INTER\_ALGORITHM

  - MPICH\_IREDUCE\_SCATTER\_INTER\_ALGORITHM

- **Description**: Variable to select ireduce\_scatter algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - sched\_auto - Internal algorithm selection for sched-based algorithms

  - sched\_remote\_reduce\_local\_scatterv - Force remote-reduce-local-scatterv algorithm

- **Default:** auto

MPIR\_CVAR\_REDUCE\_SCATTER\_BLOCK\_INTRA\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_REDUCE\_SCATTER\_BLOCK\_INTRA\_ALGORITHM

  - MPICH\_REDUCE\_SCATTER\_BLOCK\_INTRA\_ALGORITHM

- **Description**: Variable to select reduce\_scatter\_block algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - noncommutative     - Force noncommutative algorithm

  - recursive\_doubling - Force recursive doubling algorithm

  - pairwise           - Force pairwise algorithm

  - recursive\_halving  - Force recursive halving algorithm

  - nb                 - Force nonblocking algorithm

- **Default:** auto

MPIR\_CVAR\_REDUCE\_SCATTER\_BLOCK\_INTER\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_REDUCE\_SCATTER\_BLOCK\_INTER\_ALGORITHM

  - MPICH\_REDUCE\_SCATTER\_BLOCK\_INTER\_ALGORITHM

- **Description**: Variable to select reduce\_scatter\_block algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - nb                          - Force nonblocking algorithm

  - remote\_reduce\_local\_scatter - Force remote-reduce-local-scatter algorithm

- **Default:** auto

MPIR\_CVAR\_IREDUCE\_SCATTER\_BLOCK\_RECEXCH\_KVAL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IREDUCE\_SCATTER\_BLOCK\_RECEXCH\_KVAL

  - MPICH\_IREDUCE\_SCATTER\_BLOCK\_RECEXCH\_KVAL

- **Description**: k value for recursive exchange based ireduce\_scatter\_block

- **Default:** 2

MPIR\_CVAR\_IREDUCE\_SCATTER\_BLOCK\_INTRA\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IREDUCE\_SCATTER\_BLOCK\_INTRA\_ALGORITHM

  - MPICH\_IREDUCE\_SCATTER\_BLOCK\_INTRA\_ALGORITHM

- **Description**: Variable to select ireduce\_scatter\_block algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - sched\_auto - Internal algorithm selection for sched-based algorithms

  - sched\_noncommutative     - Force noncommutative algorithm

  - sched\_recursive\_doubling - Force recursive doubling algorithm

  - sched\_pairwise           - Force pairwise algorithm

  - sched\_recursive\_halving  - Force recursive halving algorithm

  - tsp\_recexch          - Force generic transport recursive exchange algorithm

- **Default:** auto

MPIR\_CVAR\_IREDUCE\_SCATTER\_BLOCK\_INTER\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IREDUCE\_SCATTER\_BLOCK\_INTER\_ALGORITHM

  - MPICH\_IREDUCE\_SCATTER\_BLOCK\_INTER\_ALGORITHM

- **Description**: Variable to select ireduce\_scatter\_block algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - sched\_auto - Internal algorithm selection for sched-based algorithms

  - sched\_remote\_reduce\_local\_scatterv - Force remote-reduce-local-scatterv algorithm

- **Default:** auto

MPIR\_CVAR\_SCAN\_INTRA\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_SCAN\_INTRA\_ALGORITHM

  - MPICH\_SCAN\_INTRA\_ALGORITHM

- **Description**: Variable to select allgather algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - nb                 - Force nonblocking algorithm

  - smp                - Force smp algorithm

  - recursive\_doubling - Force recursive doubling algorithm

- **Default:** auto

MPIR\_CVAR\_ISCAN\_INTRA\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ISCAN\_INTRA\_ALGORITHM

  - MPICH\_ISCAN\_INTRA\_ALGORITHM

- **Description**: Variable to select allgather algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - sched\_auto - Internal algorithm selection for sched-based algorithms

  - sched\_smp                  - Force smp algorithm

  - sched\_recursive\_doubling   - Force recursive doubling algorithm

  - tsp\_recursive\_doubling - Force generic transport recursive doubling algorithm

- **Default:** auto

MPIR\_CVAR\_EXSCAN\_INTRA\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_EXSCAN\_INTRA\_ALGORITHM

  - MPICH\_EXSCAN\_INTRA\_ALGORITHM

- **Description**: Variable to select allgather algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - nb                 - Force nonblocking algorithm

  - recursive\_doubling - Force recursive doubling algorithm

- **Default:** auto

MPIR\_CVAR\_IEXSCAN\_INTRA\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IEXSCAN\_INTRA\_ALGORITHM

  - MPICH\_IEXSCAN\_INTRA\_ALGORITHM

- **Description**: Variable to select iexscan algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - sched\_auto - Internal algorithm selection for sched-based algorithms

  - sched\_recursive\_doubling - Force recursive doubling algorithm

- **Default:** auto

MPIR\_CVAR\_NEIGHBOR\_ALLGATHER\_INTRA\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_NEIGHBOR\_ALLGATHER\_INTRA\_ALGORITHM

  - MPICH\_NEIGHBOR\_ALLGATHER\_INTRA\_ALGORITHM

- **Description**: Variable to select ineighbor\_allgather algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - nb   - Force nonblocking algorithm

- **Default:** auto

MPIR\_CVAR\_NEIGHBOR\_ALLGATHER\_INTER\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_NEIGHBOR\_ALLGATHER\_INTER\_ALGORITHM

  - MPICH\_NEIGHBOR\_ALLGATHER\_INTER\_ALGORITHM

- **Description**: Variable to select ineighbor\_allgather algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - nb   - Force nonblocking algorithm

- **Default:** auto

MPIR\_CVAR\_INEIGHBOR\_ALLGATHER\_INTRA\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_INEIGHBOR\_ALLGATHER\_INTRA\_ALGORITHM

  - MPICH\_INEIGHBOR\_ALLGATHER\_INTRA\_ALGORITHM

- **Description**: Variable to select ineighbor\_allgather algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - sched\_auto - Internal algorithm selection for sched-based algorithms

  - sched\_linear    - Force linear algorithm

  - tsp\_linear  - Force generic transport based linear algorithm

- **Default:** auto

MPIR\_CVAR\_INEIGHBOR\_ALLGATHER\_INTER\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_INEIGHBOR\_ALLGATHER\_INTER\_ALGORITHM

  - MPICH\_INEIGHBOR\_ALLGATHER\_INTER\_ALGORITHM

- **Description**: Variable to select ineighbor\_allgather algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - sched\_auto - Internal algorithm selection for sched-based algorithms

  - sched\_linear    - Force linear algorithm

  - tsp\_linear  - Force generic transport based linear algorithm

- **Default:** auto

MPIR\_CVAR\_NEIGHBOR\_ALLGATHERV\_INTRA\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_NEIGHBOR\_ALLGATHERV\_INTRA\_ALGORITHM

  - MPICH\_NEIGHBOR\_ALLGATHERV\_INTRA\_ALGORITHM

- **Description**: Variable to select neighbor\_allgatherv algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - nb   - Force nb algorithm

- **Default:** auto

MPIR\_CVAR\_NEIGHBOR\_ALLGATHERV\_INTER\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_NEIGHBOR\_ALLGATHERV\_INTER\_ALGORITHM

  - MPICH\_NEIGHBOR\_ALLGATHERV\_INTER\_ALGORITHM

- **Description**: Variable to select neighbor\_allgatherv algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - nb   - Force nb algorithm

- **Default:** auto

MPIR\_CVAR\_INEIGHBOR\_ALLGATHERV\_INTRA\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_INEIGHBOR\_ALLGATHERV\_INTRA\_ALGORITHM

  - MPICH\_INEIGHBOR\_ALLGATHERV\_INTRA\_ALGORITHM

- **Description**: Variable to select ineighbor\_allgatherv algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - sched\_auto - Internal algorithm selection for sched-based algorithms

  - sched\_linear          - Force linear algorithm

  - tsp\_linear        - Force generic transport based linear algorithm

- **Default:** auto

MPIR\_CVAR\_INEIGHBOR\_ALLGATHERV\_INTER\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_INEIGHBOR\_ALLGATHERV\_INTER\_ALGORITHM

  - MPICH\_INEIGHBOR\_ALLGATHERV\_INTER\_ALGORITHM

- **Description**: Variable to select ineighbor\_allgatherv algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - sched\_auto - Internal algorithm selection for sched-based algorithms

  - sched\_linear          - Force linear algorithm

  - tsp\_linear        - Force generic transport based linear algorithm

- **Default:** auto

MPIR\_CVAR\_NEIGHBOR\_ALLTOALL\_INTRA\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_NEIGHBOR\_ALLTOALL\_INTRA\_ALGORITHM

  - MPICH\_NEIGHBOR\_ALLTOALL\_INTRA\_ALGORITHM

- **Description**: Variable to select neighbor\_alltoall algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - nb   - Force nb algorithm

- **Default:** auto

MPIR\_CVAR\_NEIGHBOR\_ALLTOALL\_INTER\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_NEIGHBOR\_ALLTOALL\_INTER\_ALGORITHM

  - MPICH\_NEIGHBOR\_ALLTOALL\_INTER\_ALGORITHM

- **Description**: Variable to select neighbor\_alltoall algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - nb   - Force nb algorithm

- **Default:** auto

MPIR\_CVAR\_INEIGHBOR\_ALLTOALL\_INTRA\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_INEIGHBOR\_ALLTOALL\_INTRA\_ALGORITHM

  - MPICH\_INEIGHBOR\_ALLTOALL\_INTRA\_ALGORITHM

- **Description**: Variable to select ineighbor\_alltoall algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - sched\_auto - Internal algorithm selection for sched-based algorithms

  - sched\_linear          - Force linear algorithm

  - tsp\_linear        - Force generic transport based linear algorithm

- **Default:** auto

MPIR\_CVAR\_INEIGHBOR\_ALLTOALL\_INTER\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_INEIGHBOR\_ALLTOALL\_INTER\_ALGORITHM

  - MPICH\_INEIGHBOR\_ALLTOALL\_INTER\_ALGORITHM

- **Description**: Variable to select ineighbor\_alltoall algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - sched\_auto - Internal algorithm selection for sched-based algorithms

  - sched\_linear          - Force linear algorithm

  - tsp\_linear        - Force generic transport based linear algorithm

- **Default:** auto

MPIR\_CVAR\_NEIGHBOR\_ALLTOALLV\_INTRA\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_NEIGHBOR\_ALLTOALLV\_INTRA\_ALGORITHM

  - MPICH\_NEIGHBOR\_ALLTOALLV\_INTRA\_ALGORITHM

- **Description**: Variable to select neighbor\_alltoallv algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - nb   - Force nb algorithm

- **Default:** auto

MPIR\_CVAR\_NEIGHBOR\_ALLTOALLV\_INTER\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_NEIGHBOR\_ALLTOALLV\_INTER\_ALGORITHM

  - MPICH\_NEIGHBOR\_ALLTOALLV\_INTER\_ALGORITHM

- **Description**: Variable to select neighbor\_alltoallv algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - nb   - Force nb algorithm

- **Default:** auto

MPIR\_CVAR\_INEIGHBOR\_ALLTOALLV\_INTRA\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_INEIGHBOR\_ALLTOALLV\_INTRA\_ALGORITHM

  - MPICH\_INEIGHBOR\_ALLTOALLV\_INTRA\_ALGORITHM

- **Description**: Variable to select ineighbor\_alltoallv algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - sched\_auto - Internal algorithm selection for sched-based algorithms

  - sched\_linear          - Force linear algorithm

  - tsp\_linear  - Force generic transport based linear algorithm

- **Default:** auto

MPIR\_CVAR\_INEIGHBOR\_ALLTOALLV\_INTER\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_INEIGHBOR\_ALLTOALLV\_INTER\_ALGORITHM

  - MPICH\_INEIGHBOR\_ALLTOALLV\_INTER\_ALGORITHM

- **Description**: Variable to select ineighbor\_alltoallv algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - sched\_auto - Internal algorithm selection for sched-based algorithms

  - sched\_linear          - Force linear algorithm

  - tsp\_linear  - Force generic transport based linear algorithm

- **Default:** auto

MPIR\_CVAR\_NEIGHBOR\_ALLTOALLW\_INTRA\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_NEIGHBOR\_ALLTOALLW\_INTRA\_ALGORITHM

  - MPICH\_NEIGHBOR\_ALLTOALLW\_INTRA\_ALGORITHM

- **Description**: Variable to select neighbor\_alltoallw algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - nb   - Force nb algorithm

- **Default:** auto

MPIR\_CVAR\_NEIGHBOR\_ALLTOALLW\_INTER\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_NEIGHBOR\_ALLTOALLW\_INTER\_ALGORITHM

  - MPICH\_NEIGHBOR\_ALLTOALLW\_INTER\_ALGORITHM

- **Description**: Variable to select neighbor\_alltoallw algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - nb   - Force nb algorithm

- **Default:** auto

MPIR\_CVAR\_INEIGHBOR\_ALLTOALLW\_INTRA\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_INEIGHBOR\_ALLTOALLW\_INTRA\_ALGORITHM

  - MPICH\_INEIGHBOR\_ALLTOALLW\_INTRA\_ALGORITHM

- **Description**: Variable to select ineighbor\_alltoallw algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - sched\_auto - Internal algorithm selection for sched-based algorithms

  - sched\_linear          - Force linear algorithm

  - tsp\_linear        - Force generic transport based linear algorithm

- **Default:** auto

MPIR\_CVAR\_INEIGHBOR\_ALLTOALLW\_INTER\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_INEIGHBOR\_ALLTOALLW\_INTER\_ALGORITHM

  - MPICH\_INEIGHBOR\_ALLTOALLW\_INTER\_ALGORITHM

- **Description**: Variable to select ineighbor\_alltoallw algorithm

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - sched\_auto - Internal algorithm selection for sched-based algorithms

  - sched\_linear          - Force linear algorithm

  - tsp\_linear        - Force generic transport based linear algorithm

- **Default:** auto

MPIR\_CVAR\_BARRIER\_DEVICE\_COLLECTIVE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_BARRIER\_DEVICE\_COLLECTIVE

  - MPICH\_BARRIER\_DEVICE\_COLLECTIVE

- **Description**: This CVAR is only used when MPIR\_CVAR\_DEVICE\_COLLECTIVES is set to "percoll".  If set to true, MPI\_Barrier will allow the device to override the MPIR-level collective algorithms.  The device might still call the MPIR-level algorithms manually.  If set to false, the device-override will be disabled.

- **Default:** true

MPIR\_CVAR\_IBARRIER\_DEVICE\_COLLECTIVE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IBARRIER\_DEVICE\_COLLECTIVE

  - MPICH\_IBARRIER\_DEVICE\_COLLECTIVE

- **Description**: This CVAR is only used when MPIR\_CVAR\_DEVICE\_COLLECTIVES is set to "percoll".  If set to true, MPI\_Ibarrier will allow the device to override the MPIR-level collective algorithms.  The device might still call the MPIR-level algorithms manually.  If set to false, the device-override will be disabled.

- **Default:** true

MPIR\_CVAR\_BARRIER\_INIT\_DEVICE\_COLLECTIVE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_BARRIER\_INIT\_DEVICE\_COLLECTIVE

  - MPICH\_BARRIER\_INIT\_DEVICE\_COLLECTIVE

- **Description**: This CVAR is only used when MPIR\_CVAR\_DEVICE\_COLLECTIVES is set to "percoll".  If set to true, MPI\_Barrier will allow the device to override the MPIR-level collective algorithms.  The device might still call the MPIR-level algorithms manually.  If set to false, the device-override will be disabled.

- **Default:** true

MPIR\_CVAR\_BCAST\_DEVICE\_COLLECTIVE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_BCAST\_DEVICE\_COLLECTIVE

  - MPICH\_BCAST\_DEVICE\_COLLECTIVE

- **Description**: This CVAR is only used when MPIR\_CVAR\_DEVICE\_COLLECTIVES is set to "percoll".  If set to true, MPI\_Bcast will allow the device to override the MPIR-level collective algorithms.  The device might still call the MPIR-level algorithms manually.  If set to false, the device-override will be disabled.

- **Default:** true

MPIR\_CVAR\_IBCAST\_DEVICE\_COLLECTIVE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IBCAST\_DEVICE\_COLLECTIVE

  - MPICH\_IBCAST\_DEVICE\_COLLECTIVE

- **Description**: This CVAR is only used when MPIR\_CVAR\_DEVICE\_COLLECTIVES is set to "percoll".  If set to true, MPI\_Ibcast will allow the device to override the MPIR-level collective algorithms.  The device might still call the MPIR-level algorithms manually.  If set to false, the device-override will be disabled.

- **Default:** true

MPIR\_CVAR\_BCAST\_INIT\_DEVICE\_COLLECTIVE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_BCAST\_INIT\_DEVICE\_COLLECTIVE

  - MPICH\_BCAST\_INIT\_DEVICE\_COLLECTIVE

- **Description**: This CVAR is only used when MPIR\_CVAR\_DEVICE\_COLLECTIVES is set to "percoll".  If set to true, MPI\_Bcast\_init will allow the device to override the MPIR-level collective algorithms.  The device might still call the MPIR-level algorithms manually.  If set to false, the device-override will be disabled.

- **Default:** true

MPIR\_CVAR\_GATHER\_DEVICE\_COLLECTIVE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_GATHER\_DEVICE\_COLLECTIVE

  - MPICH\_GATHER\_DEVICE\_COLLECTIVE

- **Description**: This CVAR is only used when MPIR\_CVAR\_DEVICE\_COLLECTIVES is set to "percoll".  If set to true, MPI\_Gather will allow the device to override the MPIR-level collective algorithms.  The device might still call the MPIR-level algorithms manually.  If set to false, the device-override will be disabled.

- **Default:** true

MPIR\_CVAR\_IGATHER\_DEVICE\_COLLECTIVE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IGATHER\_DEVICE\_COLLECTIVE

  - MPICH\_IGATHER\_DEVICE\_COLLECTIVE

- **Description**: This CVAR is only used when MPIR\_CVAR\_DEVICE\_COLLECTIVES is set to "percoll".  If set to true, MPI\_Igather will allow the device to override the MPIR-level collective algorithms.  The device might still call the MPIR-level algorithms manually.  If set to false, the device-override will be disabled.

- **Default:** true

MPIR\_CVAR\_GATHER\_INIT\_DEVICE\_COLLECTIVE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_GATHER\_INIT\_DEVICE\_COLLECTIVE

  - MPICH\_GATHER\_INIT\_DEVICE\_COLLECTIVE

- **Description**: This CVAR is only used when MPIR\_CVAR\_DEVICE\_COLLECTIVES is set to "percoll".  If set to true, MPI\_Gather\_init will allow the device to override the MPIR-level collective algorithms.  The device might still call the MPIR-level algorithms manually.  If set to false, the device-override will be disabled.

- **Default:** true

MPIR\_CVAR\_GATHERV\_DEVICE\_COLLECTIVE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_GATHERV\_DEVICE\_COLLECTIVE

  - MPICH\_GATHERV\_DEVICE\_COLLECTIVE

- **Description**: This CVAR is only used when MPIR\_CVAR\_DEVICE\_COLLECTIVES is set to "percoll".  If set to true, MPI\_Gatherv will allow the device to override the MPIR-level collective algorithms.  The device might still call the MPIR-level algorithms manually.  If set to false, the device-override will be disabled.

- **Default:** true

MPIR\_CVAR\_IGATHERV\_DEVICE\_COLLECTIVE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IGATHERV\_DEVICE\_COLLECTIVE

  - MPICH\_IGATHERV\_DEVICE\_COLLECTIVE

- **Description**: This CVAR is only used when MPIR\_CVAR\_DEVICE\_COLLECTIVES is set to "percoll".  If set to true, MPI\_Igatherv will allow the device to override the MPIR-level collective algorithms.  The device might still call the MPIR-level algorithms manually.  If set to false, the device-override will be disabled.

- **Default:** true

MPIR\_CVAR\_GATHERV\_INIT\_DEVICE\_COLLECTIVE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_GATHERV\_INIT\_DEVICE\_COLLECTIVE

  - MPICH\_GATHERV\_INIT\_DEVICE\_COLLECTIVE

- **Description**: This CVAR is only used when MPIR\_CVAR\_DEVICE\_COLLECTIVES is set to "percoll".  If set to true, MPI\_Gatherv\_init will allow the device to override the MPIR-level collective algorithms.  The device might still call the MPIR-level algorithms manually.  If set to false, the device-override will be disabled.

- **Default:** true

MPIR\_CVAR\_SCATTER\_DEVICE\_COLLECTIVE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_SCATTER\_DEVICE\_COLLECTIVE

  - MPICH\_SCATTER\_DEVICE\_COLLECTIVE

- **Description**: This CVAR is only used when MPIR\_CVAR\_DEVICE\_COLLECTIVES is set to "percoll".  If set to true, MPI\_Scatter will allow the device to override the MPIR-level collective algorithms.  The device might still call the MPIR-level algorithms manually.  If set to false, the device-override will be disabled.

- **Default:** true

MPIR\_CVAR\_ISCATTER\_DEVICE\_COLLECTIVE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ISCATTER\_DEVICE\_COLLECTIVE

  - MPICH\_ISCATTER\_DEVICE\_COLLECTIVE

- **Description**: This CVAR is only used when MPIR\_CVAR\_DEVICE\_COLLECTIVES is set to "percoll".  If set to true, MPI\_Iscatter will allow the device to override the MPIR-level collective algorithms.  The device might still call the MPIR-level algorithms manually.  If set to false, the device-override will be disabled.

- **Default:** true

MPIR\_CVAR\_SCATTER\_INIT\_DEVICE\_COLLECTIVE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_SCATTER\_INIT\_DEVICE\_COLLECTIVE

  - MPICH\_SCATTER\_INIT\_DEVICE\_COLLECTIVE

- **Description**: This CVAR is only used when MPIR\_CVAR\_DEVICE\_COLLECTIVES is set to "percoll".  If set to true, MPI\_Scatter\_init will allow the device to override the MPIR-level collective algorithms.  The device might still call the MPIR-level algorithms manually.  If set to false, the device-override will be disabled.

- **Default:** true

MPIR\_CVAR\_SCATTERV\_DEVICE\_COLLECTIVE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_SCATTERV\_DEVICE\_COLLECTIVE

  - MPICH\_SCATTERV\_DEVICE\_COLLECTIVE

- **Description**: This CVAR is only used when MPIR\_CVAR\_DEVICE\_COLLECTIVES is set to "percoll".  If set to true, MPI\_Scatterv will allow the device to override the MPIR-level collective algorithms.  The device might still call the MPIR-level algorithms manually.  If set to false, the device-override will be disabled.

- **Default:** true

MPIR\_CVAR\_ISCATTERV\_DEVICE\_COLLECTIVE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ISCATTERV\_DEVICE\_COLLECTIVE

  - MPICH\_ISCATTERV\_DEVICE\_COLLECTIVE

- **Description**: This CVAR is only used when MPIR\_CVAR\_DEVICE\_COLLECTIVES is set to "percoll".  If set to true, MPI\_Iscatterv will allow the device to override the MPIR-level collective algorithms.  The device might still call the MPIR-level algorithms manually.  If set to false, the device-override will be disabled.

- **Default:** true

MPIR\_CVAR\_SCATTERV\_INIT\_DEVICE\_COLLECTIVE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_SCATTERV\_INIT\_DEVICE\_COLLECTIVE

  - MPICH\_SCATTERV\_INIT\_DEVICE\_COLLECTIVE

- **Description**: This CVAR is only used when MPIR\_CVAR\_DEVICE\_COLLECTIVES is set to "percoll".  If set to true, MPI\_Scatterv\_init will allow the device to override the MPIR-level collective algorithms.  The device might still call the MPIR-level algorithms manually.  If set to false, the device-override will be disabled.

- **Default:** true

MPIR\_CVAR\_ALLGATHER\_DEVICE\_COLLECTIVE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ALLGATHER\_DEVICE\_COLLECTIVE

  - MPICH\_ALLGATHER\_DEVICE\_COLLECTIVE

- **Description**: This CVAR is only used when MPIR\_CVAR\_DEVICE\_COLLECTIVES is set to "percoll".  If set to true, MPI\_Allgather will allow the device to override the MPIR-level collective algorithms.  The device might still call the MPIR-level algorithms manually.  If set to false, the device-override will be disabled.

- **Default:** true

MPIR\_CVAR\_IALLGATHER\_DEVICE\_COLLECTIVE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IALLGATHER\_DEVICE\_COLLECTIVE

  - MPICH\_IALLGATHER\_DEVICE\_COLLECTIVE

- **Description**: This CVAR is only used when MPIR\_CVAR\_DEVICE\_COLLECTIVES is set to "percoll".  If set to true, MPI\_Iallgather will allow the device to override the MPIR-level collective algorithms.  The device might still call the MPIR-level algorithms manually.  If set to false, the device-override will be disabled.

- **Default:** true

MPIR\_CVAR\_ALLGATHER\_INIT\_DEVICE\_COLLECTIVE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ALLGATHER\_INIT\_DEVICE\_COLLECTIVE

  - MPICH\_ALLGATHER\_INIT\_DEVICE\_COLLECTIVE

- **Description**: This CVAR is only used when MPIR\_CVAR\_DEVICE\_COLLECTIVES is set to "percoll".  If set to true, MPI\_Allgather\_init will allow the device to override the MPIR-level collective algorithms.  The device might still call the MPIR-level algorithms manually.  If set to false, the device-override will be disabled.

- **Default:** true

MPIR\_CVAR\_ALLGATHERV\_DEVICE\_COLLECTIVE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ALLGATHERV\_DEVICE\_COLLECTIVE

  - MPICH\_ALLGATHERV\_DEVICE\_COLLECTIVE

- **Description**: This CVAR is only used when MPIR\_CVAR\_DEVICE\_COLLECTIVES is set to "percoll".  If set to true, MPI\_Allgatherv will allow the device to override the MPIR-level collective algorithms.  The device might still call the MPIR-level algorithms manually.  If set to false, the device-override will be disabled.

- **Default:** true

MPIR\_CVAR\_IALLGATHERV\_DEVICE\_COLLECTIVE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IALLGATHERV\_DEVICE\_COLLECTIVE

  - MPICH\_IALLGATHERV\_DEVICE\_COLLECTIVE

- **Description**: This CVAR is only used when MPIR\_CVAR\_DEVICE\_COLLECTIVES is set to "percoll".  If set to true, MPI\_Iallgatherv will allow the device to override the MPIR-level collective algorithms.  The device might still call the MPIR-level algorithms manually.  If set to false, the device-override will be disabled.

- **Default:** true

MPIR\_CVAR\_ALLGATHERV\_INIT\_DEVICE\_COLLECTIVE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ALLGATHERV\_INIT\_DEVICE\_COLLECTIVE

  - MPICH\_ALLGATHERV\_INIT\_DEVICE\_COLLECTIVE

- **Description**: This CVAR is only used when MPIR\_CVAR\_DEVICE\_COLLECTIVES is set to "percoll".  If set to true, MPI\_Allgatherv\_init will allow the device to override the MPIR-level collective algorithms.  The device might still call the MPIR-level algorithms manually.  If set to false, the device-override will be disabled.

- **Default:** true

MPIR\_CVAR\_ALLTOALL\_DEVICE\_COLLECTIVE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ALLTOALL\_DEVICE\_COLLECTIVE

  - MPICH\_ALLTOALL\_DEVICE\_COLLECTIVE

- **Description**: This CVAR is only used when MPIR\_CVAR\_DEVICE\_COLLECTIVES is set to "percoll".  If set to true, MPI\_Alltoall will allow the device to override the MPIR-level collective algorithms.  The device might still call the MPIR-level algorithms manually.  If set to false, the device-override will be disabled.

- **Default:** true

MPIR\_CVAR\_IALLTOALL\_DEVICE\_COLLECTIVE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IALLTOALL\_DEVICE\_COLLECTIVE

  - MPICH\_IALLTOALL\_DEVICE\_COLLECTIVE

- **Description**: This CVAR is only used when MPIR\_CVAR\_DEVICE\_COLLECTIVES is set to "percoll".  If set to true, MPI\_Ialltoall will allow the device to override the MPIR-level collective algorithms.  The device might still call the MPIR-level algorithms manually.  If set to false, the device-override will be disabled.

- **Default:** true

MPIR\_CVAR\_ALLTOALL\_INIT\_DEVICE\_COLLECTIVE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ALLTOALL\_INIT\_DEVICE\_COLLECTIVE

  - MPICH\_ALLTOALL\_INIT\_DEVICE\_COLLECTIVE

- **Description**: This CVAR is only used when MPIR\_CVAR\_DEVICE\_COLLECTIVES is set to "percoll".  If set to true, MPI\_Alltoall\_init will allow the device to override the MPIR-level collective algorithms.  The device might still call the MPIR-level algorithms manually.  If set to false, the device-override will be disabled.

- **Default:** true

MPIR\_CVAR\_ALLTOALLV\_DEVICE\_COLLECTIVE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ALLTOALLV\_DEVICE\_COLLECTIVE

  - MPICH\_ALLTOALLV\_DEVICE\_COLLECTIVE

- **Description**: This CVAR is only used when MPIR\_CVAR\_DEVICE\_COLLECTIVES is set to "percoll".  If set to true, MPI\_Alltoallv will allow the device to override the MPIR-level collective algorithms.  The device might still call the MPIR-level algorithms manually.  If set to false, the device-override will be disabled.

- **Default:** true

MPIR\_CVAR\_IALLTOALLV\_DEVICE\_COLLECTIVE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IALLTOALLV\_DEVICE\_COLLECTIVE

  - MPICH\_IALLTOALLV\_DEVICE\_COLLECTIVE

- **Description**: This CVAR is only used when MPIR\_CVAR\_DEVICE\_COLLECTIVES is set to "percoll".  If set to true, MPI\_Ialltoallv will allow the device to override the MPIR-level collective algorithms.  The device might still call the MPIR-level algorithms manually.  If set to false, the device-override will be disabled.

- **Default:** true

MPIR\_CVAR\_ALLTOALLV\_INIT\_DEVICE\_COLLECTIVE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ALLTOALLV\_INIT\_DEVICE\_COLLECTIVE

  - MPICH\_ALLTOALLV\_INIT\_DEVICE\_COLLECTIVE

- **Description**: This CVAR is only used when MPIR\_CVAR\_DEVICE\_COLLECTIVES is set to "percoll".  If set to true, MPI\_Alltoallv\_init will allow the device to override the MPIR-level collective algorithms.  The device might still call the MPIR-level algorithms manually.  If set to false, the device-override will be disabled.

- **Default:** true

MPIR\_CVAR\_ALLTOALLW\_DEVICE\_COLLECTIVE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ALLTOALLW\_DEVICE\_COLLECTIVE

  - MPICH\_ALLTOALLW\_DEVICE\_COLLECTIVE

- **Description**: This CVAR is only used when MPIR\_CVAR\_DEVICE\_COLLECTIVES is set to "percoll".  If set to true, MPI\_Alltoallw will allow the device to override the MPIR-level collective algorithms.  The device might still call the MPIR-level algorithms manually.  If set to false, the device-override will be disabled.

- **Default:** true

MPIR\_CVAR\_IALLTOALLW\_DEVICE\_COLLECTIVE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IALLTOALLW\_DEVICE\_COLLECTIVE

  - MPICH\_IALLTOALLW\_DEVICE\_COLLECTIVE

- **Description**: This CVAR is only used when MPIR\_CVAR\_DEVICE\_COLLECTIVES is set to "percoll".  If set to true, MPI\_Ialltoallw will allow the device to override the MPIR-level collective algorithms.  The device might still call the MPIR-level algorithms manually.  If set to false, the device-override will be disabled.

- **Default:** true

MPIR\_CVAR\_ALLTOALLW\_INIT\_DEVICE\_COLLECTIVE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ALLTOALLW\_INIT\_DEVICE\_COLLECTIVE

  - MPICH\_ALLTOALLW\_INIT\_DEVICE\_COLLECTIVE

- **Description**: This CVAR is only used when MPIR\_CVAR\_DEVICE\_COLLECTIVES is set to "percoll".  If set to true, MPI\_Alltoallw\_init will allow the device to override the MPIR-level collective algorithms.  The device might still call the MPIR-level algorithms manually.  If set to false, the device-override will be disabled.

- **Default:** true

MPIR\_CVAR\_REDUCE\_DEVICE\_COLLECTIVE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_REDUCE\_DEVICE\_COLLECTIVE

  - MPICH\_REDUCE\_DEVICE\_COLLECTIVE

- **Description**: This CVAR is only used when MPIR\_CVAR\_DEVICE\_COLLECTIVES is set to "percoll".  If set to true, MPI\_Reduce will allow the device to override the MPIR-level collective algorithms.  The device might still call the MPIR-level algorithms manually.  If set to false, the device-override will be disabled.

- **Default:** true

MPIR\_CVAR\_IREDUCE\_DEVICE\_COLLECTIVE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IREDUCE\_DEVICE\_COLLECTIVE

  - MPICH\_IREDUCE\_DEVICE\_COLLECTIVE

- **Description**: This CVAR is only used when MPIR\_CVAR\_DEVICE\_COLLECTIVES is set to "percoll".  If set to true, MPI\_Ireduce will allow the device to override the MPIR-level collective algorithms.  The device might still call the MPIR-level algorithms manually.  If set to false, the device-override will be disabled.

- **Default:** true

MPIR\_CVAR\_REDUCE\_INIT\_DEVICE\_COLLECTIVE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_REDUCE\_INIT\_DEVICE\_COLLECTIVE

  - MPICH\_REDUCE\_INIT\_DEVICE\_COLLECTIVE

- **Description**: This CVAR is only used when MPIR\_CVAR\_DEVICE\_COLLECTIVES is set to "percoll".  If set to true, MPI\_Reduce\_init will allow the device to override the MPIR-level collective algorithms.  The device might still call the MPIR-level algorithms manually.  If set to false, the device-override will be disabled.

- **Default:** true

MPIR\_CVAR\_ALLREDUCE\_DEVICE\_COLLECTIVE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ALLREDUCE\_DEVICE\_COLLECTIVE

  - MPICH\_ALLREDUCE\_DEVICE\_COLLECTIVE

- **Description**: This CVAR is only used when MPIR\_CVAR\_DEVICE\_COLLECTIVES is set to "percoll".  If set to true, MPI\_Allreduce will allow the device to override the MPIR-level collective algorithms.  The device might still call the MPIR-level algorithms manually.  If set to false, the device-override will be disabled.

- **Default:** true

MPIR\_CVAR\_IALLREDUCE\_DEVICE\_COLLECTIVE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IALLREDUCE\_DEVICE\_COLLECTIVE

  - MPICH\_IALLREDUCE\_DEVICE\_COLLECTIVE

- **Description**: This CVAR is only used when MPIR\_CVAR\_DEVICE\_COLLECTIVES is set to "percoll".  If set to true, MPI\_Iallreduce will allow the device to override the MPIR-level collective algorithms.  The device might still call the MPIR-level algorithms manually.  If set to false, the device-override will be disabled.

- **Default:** true

MPIR\_CVAR\_ALLREDUCE\_INIT\_DEVICE\_COLLECTIVE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ALLREDUCE\_INIT\_DEVICE\_COLLECTIVE

  - MPICH\_ALLREDUCE\_INIT\_DEVICE\_COLLECTIVE

- **Description**: This CVAR is only used when MPIR\_CVAR\_DEVICE\_COLLECTIVES is set to "percoll".  If set to true, MPI\_Allreduce\_init will allow the device to override the MPIR-level collective algorithms.  The device might still call the MPIR-level algorithms manually.  If set to false, the device-override will be disabled.

- **Default:** true

MPIR\_CVAR\_REDUCE\_SCATTER\_DEVICE\_COLLECTIVE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_REDUCE\_SCATTER\_DEVICE\_COLLECTIVE

  - MPICH\_REDUCE\_SCATTER\_DEVICE\_COLLECTIVE

- **Description**: This CVAR is only used when MPIR\_CVAR\_DEVICE\_COLLECTIVES is set to "percoll".  If set to true, MPI\_Reduce\_scatter will allow the device to override the MPIR-level collective algorithms.  The device might still call the MPIR-level algorithms manually.  If set to false, the device-override will be disabled.

- **Default:** true

MPIR\_CVAR\_IREDUCE\_SCATTER\_DEVICE\_COLLECTIVE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IREDUCE\_SCATTER\_DEVICE\_COLLECTIVE

  - MPICH\_IREDUCE\_SCATTER\_DEVICE\_COLLECTIVE

- **Description**: This CVAR is only used when MPIR\_CVAR\_DEVICE\_COLLECTIVES is set to "percoll".  If set to true, MPI\_Ireduce\_scatter will allow the device to override the MPIR-level collective algorithms.  The device might still call the MPIR-level algorithms manually.  If set to false, the device-override will be disabled.

- **Default:** true

MPIR\_CVAR\_REDUCE\_SCATTER\_INIT\_DEVICE\_COLLECTIVE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_REDUCE\_SCATTER\_INIT\_DEVICE\_COLLECTIVE

  - MPICH\_REDUCE\_SCATTER\_INIT\_DEVICE\_COLLECTIVE

- **Description**: This CVAR is only used when MPIR\_CVAR\_DEVICE\_COLLECTIVES is set to "percoll".  If set to true, MPI\_Reduce\_scatter\_init will allow the device to override the MPIR-level collective algorithms.  The device might still call the MPIR-level algorithms manually.  If set to false, the device-override will be disabled.

- **Default:** true

MPIR\_CVAR\_REDUCE\_SCATTER\_BLOCK\_DEVICE\_COLLECTIVE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_REDUCE\_SCATTER\_BLOCK\_DEVICE\_COLLECTIVE

  - MPICH\_REDUCE\_SCATTER\_BLOCK\_DEVICE\_COLLECTIVE

- **Description**: This CVAR is only used when MPIR\_CVAR\_DEVICE\_COLLECTIVES is set to "percoll".  If set to true, MPI\_Reduce\_scatter\_block will allow the device to override the MPIR-level collective algorithms.  The device might still call the MPIR-level algorithms manually.  If set to false, the device-override will be disabled.

- **Default:** true

MPIR\_CVAR\_IREDUCE\_SCATTER\_BLOCK\_DEVICE\_COLLECTIVE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IREDUCE\_SCATTER\_BLOCK\_DEVICE\_COLLECTIVE

  - MPICH\_IREDUCE\_SCATTER\_BLOCK\_DEVICE\_COLLECTIVE

- **Description**: This CVAR is only used when MPIR\_CVAR\_DEVICE\_COLLECTIVES is set to "percoll".  If set to true, MPI\_Ireduce\_scatter\_block will allow the device to override the MPIR-level collective algorithms.  The device might still call the MPIR-level algorithms manually.  If set to false, the device-override will be disabled.

- **Default:** true

MPIR\_CVAR\_REDUCE\_SCATTER\_BLOCK\_INIT\_DEVICE\_COLLECTIVE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_REDUCE\_SCATTER\_BLOCK\_INIT\_DEVICE\_COLLECTIVE

  - MPICH\_REDUCE\_SCATTER\_BLOCK\_INIT\_DEVICE\_COLLECTIVE

- **Description**: This CVAR is only used when MPIR\_CVAR\_DEVICE\_COLLECTIVES is set to "percoll".  If set to true, MPI\_Reduce\_scatter\_block\_init will allow the device to override the MPIR-level collective algorithms.  The device might still call the MPIR-level algorithms manually.  If set to false, the device-override will be disabled.

- **Default:** true

MPIR\_CVAR\_SCAN\_DEVICE\_COLLECTIVE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_SCAN\_DEVICE\_COLLECTIVE

  - MPICH\_SCAN\_DEVICE\_COLLECTIVE

- **Description**: This CVAR is only used when MPIR\_CVAR\_DEVICE\_COLLECTIVES is set to "percoll".  If set to true, MPI\_Scan will allow the device to override the MPIR-level collective algorithms.  The device might still call the MPIR-level algorithms manually.  If set to false, the device-override will be disabled.

- **Default:** true

MPIR\_CVAR\_ISCAN\_DEVICE\_COLLECTIVE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ISCAN\_DEVICE\_COLLECTIVE

  - MPICH\_ISCAN\_DEVICE\_COLLECTIVE

- **Description**: This CVAR is only used when MPIR\_CVAR\_DEVICE\_COLLECTIVES is set to "percoll".  If set to true, MPI\_Iscan will allow the device to override the MPIR-level collective algorithms.  The device might still call the MPIR-level algorithms manually.  If set to false, the device-override will be disabled.

- **Default:** true

MPIR\_CVAR\_SCAN\_INIT\_DEVICE\_COLLECTIVE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_SCAN\_INIT\_DEVICE\_COLLECTIVE

  - MPICH\_SCAN\_INIT\_DEVICE\_COLLECTIVE

- **Description**: This CVAR is only used when MPIR\_CVAR\_DEVICE\_COLLECTIVES is set to "percoll".  If set to true, MPI\_Scan\_init will allow the device to override the MPIR-level collective algorithms.  The device might still call the MPIR-level algorithms manually.  If set to false, the device-override will be disabled.

- **Default:** true

MPIR\_CVAR\_EXSCAN\_DEVICE\_COLLECTIVE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_EXSCAN\_DEVICE\_COLLECTIVE

  - MPICH\_EXSCAN\_DEVICE\_COLLECTIVE

- **Description**: This CVAR is only used when MPIR\_CVAR\_DEVICE\_COLLECTIVES is set to "percoll".  If set to true, MPI\_Exscan will allow the device to override the MPIR-level collective algorithms.  The device might still call the MPIR-level algorithms manually.  If set to false, the device-override will be disabled.

- **Default:** true

MPIR\_CVAR\_IEXSCAN\_DEVICE\_COLLECTIVE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IEXSCAN\_DEVICE\_COLLECTIVE

  - MPICH\_IEXSCAN\_DEVICE\_COLLECTIVE

- **Description**: This CVAR is only used when MPIR\_CVAR\_DEVICE\_COLLECTIVES is set to "percoll".  If set to true, MPI\_Iexscan will allow the device to override the MPIR-level collective algorithms.  The device might still call the MPIR-level algorithms manually.  If set to false, the device-override will be disabled.

- **Default:** true

MPIR\_CVAR\_EXSCAN\_INIT\_DEVICE\_COLLECTIVE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_EXSCAN\_INIT\_DEVICE\_COLLECTIVE

  - MPICH\_EXSCAN\_INIT\_DEVICE\_COLLECTIVE

- **Description**: This CVAR is only used when MPIR\_CVAR\_DEVICE\_COLLECTIVES is set to "percoll".  If set to true, MPI\_Exscan\_init will allow the device to override the MPIR-level collective algorithms.  The device might still call the MPIR-level algorithms manually.  If set to false, the device-override will be disabled.

- **Default:** true

MPIR\_CVAR\_NEIGHBOR\_ALLGATHER\_DEVICE\_COLLECTIVE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_NEIGHBOR\_ALLGATHER\_DEVICE\_COLLECTIVE

  - MPICH\_NEIGHBOR\_ALLGATHER\_DEVICE\_COLLECTIVE

- **Description**: This CVAR is only used when MPIR\_CVAR\_DEVICE\_COLLECTIVES is set to "percoll".  If set to true, MPI\_Neighbor\_allgather will allow the device to override the MPIR-level collective algorithms.  The device might still call the MPIR-level algorithms manually.  If set to false, the device-override will be disabled.

- **Default:** true

MPIR\_CVAR\_INEIGHBOR\_ALLGATHER\_DEVICE\_COLLECTIVE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_INEIGHBOR\_ALLGATHER\_DEVICE\_COLLECTIVE

  - MPICH\_INEIGHBOR\_ALLGATHER\_DEVICE\_COLLECTIVE

- **Description**: This CVAR is only used when MPIR\_CVAR\_DEVICE\_COLLECTIVES is set to "percoll".  If set to true, MPI\_Ineighbor\_allgather will allow the device to override the MPIR-level collective algorithms.  The device might still call the MPIR-level algorithms manually.  If set to false, the device-override will be disabled.

- **Default:** true

MPIR\_CVAR\_NEIGHBOR\_ALLGATHER\_INIT\_DEVICE\_COLLECTIVE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_NEIGHBOR\_ALLGATHER\_INIT\_DEVICE\_COLLECTIVE

  - MPICH\_NEIGHBOR\_ALLGATHER\_INIT\_DEVICE\_COLLECTIVE

- **Description**: This CVAR is only used when MPIR\_CVAR\_DEVICE\_COLLECTIVES is set to "percoll".  If set to true, MPI\_Neighbor\_allgather\_init will allow the device to override the MPIR-level collective algorithms.  The device might still call the MPIR-level algorithms manually.  If set to false, the device-override will be disabled.

- **Default:** true

MPIR\_CVAR\_NEIGHBOR\_ALLGATHERV\_DEVICE\_COLLECTIVE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_NEIGHBOR\_ALLGATHERV\_DEVICE\_COLLECTIVE

  - MPICH\_NEIGHBOR\_ALLGATHERV\_DEVICE\_COLLECTIVE

- **Description**: This CVAR is only used when MPIR\_CVAR\_DEVICE\_COLLECTIVES is set to "percoll".  If set to true, MPI\_Neighbor\_allgatherv will allow the device to override the MPIR-level collective algorithms.  The device might still call the MPIR-level algorithms manually.  If set to false, the device-override will be disabled.

- **Default:** true

MPIR\_CVAR\_INEIGHBOR\_ALLGATHERV\_DEVICE\_COLLECTIVE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_INEIGHBOR\_ALLGATHERV\_DEVICE\_COLLECTIVE

  - MPICH\_INEIGHBOR\_ALLGATHERV\_DEVICE\_COLLECTIVE

- **Description**: This CVAR is only used when MPIR\_CVAR\_DEVICE\_COLLECTIVES is set to "percoll".  If set to true, MPI\_Ineighbor\_allgatherv will allow the device to override the MPIR-level collective algorithms.  The device might still call the MPIR-level algorithms manually.  If set to false, the device-override will be disabled.

- **Default:** true

MPIR\_CVAR\_NEIGHBOR\_ALLGATHERV\_INIT\_DEVICE\_COLLECTIVE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_NEIGHBOR\_ALLGATHERV\_INIT\_DEVICE\_COLLECTIVE

  - MPICH\_NEIGHBOR\_ALLGATHERV\_INIT\_DEVICE\_COLLECTIVE

- **Description**: This CVAR is only used when MPIR\_CVAR\_DEVICE\_COLLECTIVES is set to "percoll".  If set to true, MPI\_Neighbor\_allgatherv\_init will allow the device to override the MPIR-level collective algorithms.  The device might still call the MPIR-level algorithms manually.  If set to false, the device-override will be disabled.

- **Default:** true

MPIR\_CVAR\_NEIGHBOR\_ALLTOALL\_DEVICE\_COLLECTIVE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_NEIGHBOR\_ALLTOALL\_DEVICE\_COLLECTIVE

  - MPICH\_NEIGHBOR\_ALLTOALL\_DEVICE\_COLLECTIVE

- **Description**: This CVAR is only used when MPIR\_CVAR\_DEVICE\_COLLECTIVES is set to "percoll".  If set to true, MPI\_Neighbor\_alltoall will allow the device to override the MPIR-level collective algorithms.  The device might still call the MPIR-level algorithms manually.  If set to false, the device-override will be disabled.

- **Default:** true

MPIR\_CVAR\_INEIGHBOR\_ALLTOALL\_DEVICE\_COLLECTIVE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_INEIGHBOR\_ALLTOALL\_DEVICE\_COLLECTIVE

  - MPICH\_INEIGHBOR\_ALLTOALL\_DEVICE\_COLLECTIVE

- **Description**: This CVAR is only used when MPIR\_CVAR\_DEVICE\_COLLECTIVES is set to "percoll".  If set to true, MPI\_Ineighbor\_alltoall will allow the device to override the MPIR-level collective algorithms.  The device might still call the MPIR-level algorithms manually.  If set to false, the device-override will be disabled.

- **Default:** true

MPIR\_CVAR\_NEIGHBOR\_ALLTOALL\_INIT\_DEVICE\_COLLECTIVE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_NEIGHBOR\_ALLTOALL\_INIT\_DEVICE\_COLLECTIVE

  - MPICH\_NEIGHBOR\_ALLTOALL\_INIT\_DEVICE\_COLLECTIVE

- **Description**: This CVAR is only used when MPIR\_CVAR\_DEVICE\_COLLECTIVES is set to "percoll".  If set to true, MPI\_Neighbor\_alltoall\_init will allow the device to override the MPIR-level collective algorithms.  The device might still call the MPIR-level algorithms manually.  If set to false, the device-override will be disabled.

- **Default:** true

MPIR\_CVAR\_NEIGHBOR\_ALLTOALLV\_DEVICE\_COLLECTIVE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_NEIGHBOR\_ALLTOALLV\_DEVICE\_COLLECTIVE

  - MPICH\_NEIGHBOR\_ALLTOALLV\_DEVICE\_COLLECTIVE

- **Description**: This CVAR is only used when MPIR\_CVAR\_DEVICE\_COLLECTIVES is set to "percoll".  If set to true, MPI\_Neighbor\_alltoallv will allow the device to override the MPIR-level collective algorithms.  The device might still call the MPIR-level algorithms manually.  If set to false, the device-override will be disabled.

- **Default:** true

MPIR\_CVAR\_INEIGHBOR\_ALLTOALLV\_DEVICE\_COLLECTIVE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_INEIGHBOR\_ALLTOALLV\_DEVICE\_COLLECTIVE

  - MPICH\_INEIGHBOR\_ALLTOALLV\_DEVICE\_COLLECTIVE

- **Description**: This CVAR is only used when MPIR\_CVAR\_DEVICE\_COLLECTIVES is set to "percoll".  If set to true, MPI\_Ineighbor\_alltoallv will allow the device to override the MPIR-level collective algorithms.  The device might still call the MPIR-level algorithms manually.  If set to false, the device-override will be disabled.

- **Default:** true

MPIR\_CVAR\_NEIGHBOR\_ALLTOALLV\_INIT\_DEVICE\_COLLECTIVE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_NEIGHBOR\_ALLTOALLV\_INIT\_DEVICE\_COLLECTIVE

  - MPICH\_NEIGHBOR\_ALLTOALLV\_INIT\_DEVICE\_COLLECTIVE

- **Description**: This CVAR is only used when MPIR\_CVAR\_DEVICE\_COLLECTIVES is set to "percoll".  If set to true, MPI\_Neighbor\_alltoallv\_init will allow the device to override the MPIR-level collective algorithms.  The device might still call the MPIR-level algorithms manually.  If set to false, the device-override will be disabled.

- **Default:** true

MPIR\_CVAR\_NEIGHBOR\_ALLTOALLW\_DEVICE\_COLLECTIVE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_NEIGHBOR\_ALLTOALLW\_DEVICE\_COLLECTIVE

  - MPICH\_NEIGHBOR\_ALLTOALLW\_DEVICE\_COLLECTIVE

- **Description**: This CVAR is only used when MPIR\_CVAR\_DEVICE\_COLLECTIVES is set to "percoll".  If set to true, MPI\_Neighbor\_alltoallw will allow the device to override the MPIR-level collective algorithms.  The device might still call the MPIR-level algorithms manually.  If set to false, the device-override will be disabled.

- **Default:** true

MPIR\_CVAR\_INEIGHBOR\_ALLTOALLW\_DEVICE\_COLLECTIVE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_INEIGHBOR\_ALLTOALLW\_DEVICE\_COLLECTIVE

  - MPICH\_INEIGHBOR\_ALLTOALLW\_DEVICE\_COLLECTIVE

- **Description**: This CVAR is only used when MPIR\_CVAR\_DEVICE\_COLLECTIVES is set to "percoll".  If set to true, MPI\_Ineighbor\_alltoallw will allow the device to override the MPIR-level collective algorithms.  The device might still call the MPIR-level algorithms manually.  If set to false, the device-override will be disabled.

- **Default:** true

MPIR\_CVAR\_NEIGHBOR\_ALLTOALLW\_INIT\_DEVICE\_COLLECTIVE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_NEIGHBOR\_ALLTOALLW\_INIT\_DEVICE\_COLLECTIVE

  - MPICH\_NEIGHBOR\_ALLTOALLW\_INIT\_DEVICE\_COLLECTIVE

- **Description**: This CVAR is only used when MPIR\_CVAR\_DEVICE\_COLLECTIVES is set to "percoll".  If set to true, MPI\_Neighbor\_alltoallw\_init will allow the device to override the MPIR-level collective algorithms.  The device might still call the MPIR-level algorithms manually.  If set to false, the device-override will be disabled.

- **Default:** true

MPIR\_CVAR\_COLL\_HYBRID\_MEMORY
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_COLL\_HYBRID\_MEMORY

  - MPICH\_COLL\_HYBRID\_MEMORY

- **Description**: This cvar indicates if the memory used in the collective operations are the same type. It set to true, it means in a collective operation, some buffers could be on the CPU and some buffers could be on the GPU. If set to false, it means all the data in a collective operation are on the same type of memory.

- **Default:** true

MPIR\_CVAR\_GATHER\_VSMALL\_MSG\_SIZE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_GATHER\_VSMALL\_MSG\_SIZE

  - MPICH\_GATHER\_VSMALL\_MSG\_SIZE

- **Description**: use a temporary buffer for intracommunicator MPI\_Gather if the send buffer size is < this value (in bytes) (See also: MPIR\_CVAR\_GATHER\_INTER\_SHORT\_MSG\_SIZE)

- **Default:** 1024

MPIR\_CVAR\_GATHERV\_INTER\_SSEND\_MIN\_PROCS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_GATHERV\_INTER\_SSEND\_MIN\_PROCS

  - MPICH\_GATHERV\_INTER\_SSEND\_MIN\_PROCS

- **Description**: Use Ssend (synchronous send) for intercommunicator MPI\_Gatherv if the "group B" size is >= this value.  Specifying "-1" always avoids using Ssend.  For backwards compatibility, specifying "0" uses the default value.

- **Default:** 32

MPIR\_CVAR\_IALLTOALL\_BRUCKS\_KVAL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IALLTOALL\_BRUCKS\_KVAL

  - MPICH\_IALLTOALL\_BRUCKS\_KVAL

- **Description**: radix (k) value for generic transport brucks based ialltoall

- **Default:** 2

MPIR\_CVAR\_IALLTOALL\_BRUCKS\_BUFFER\_PER\_NBR
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IALLTOALL\_BRUCKS\_BUFFER\_PER\_NBR

  - MPICH\_IALLTOALL\_BRUCKS\_BUFFER\_PER\_NBR

- **Description**: If set to true, the tsp based brucks algorithm will allocate dedicated send and receive buffers for every neighbor in the brucks algorithm. Otherwise, it would reuse a single buffer for sending and receiving data to/from neighbors

- **Default:** 0

MPIR\_CVAR\_IALLTOALL\_SCATTERED\_OUTSTANDING\_TASKS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IALLTOALL\_SCATTERED\_OUTSTANDING\_TASKS

  - MPICH\_IALLTOALL\_SCATTERED\_OUTSTANDING\_TASKS

- **Description**: Maximum number of outstanding sends and recvs posted at a time

- **Default:** 64

MPIR\_CVAR\_IALLTOALL\_SCATTERED\_BATCH\_SIZE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IALLTOALL\_SCATTERED\_BATCH\_SIZE

  - MPICH\_IALLTOALL\_SCATTERED\_BATCH\_SIZE

- **Description**: Number of send/receive tasks that scattered algorithm waits for completion before posting another batch of send/receives of that size

- **Default:** 4

MPIR\_CVAR\_BCAST\_INTER\_KNOMIAL\_FACTOR
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_BCAST\_INTER\_KNOMIAL\_FACTOR

  - MPICH\_BCAST\_INTER\_KNOMIAL\_FACTOR

- **Description**: This defines the degree of the knomial operation during the inter-node knomial broadcast phase.

- **Default:** 4

MPIR\_CVAR\_BCAST\_INTRA\_KNOMIAL\_FACTOR
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_BCAST\_INTRA\_KNOMIAL\_FACTOR

  - MPICH\_BCAST\_INTRA\_KNOMIAL\_FACTOR

- **Description**: This defines the degree of the knomial operation during the intra-node knomial broadcast phase.

- **Default:** 4

MPIR\_CVAR\_BCAST\_SEGMENT\_SIZE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_BCAST\_SEGMENT\_SIZE

  - MPICH\_BCAST\_SEGMENT\_SIZE

- **Description**: Size of the segments used for PIPELINED bcast

- **Default:** 8192

MPIR\_CVAR\_REDUCE\_INTER\_KNOMIAL\_FACTOR
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_REDUCE\_INTER\_KNOMIAL\_FACTOR

  - MPICH\_REDUCE\_INTER\_KNOMIAL\_FACTOR

- **Description**: This defines the degree of the knomial operation during the inter-node knomial reduce phase.

- **Default:** 4

MPIR\_CVAR\_REDUCE\_INTRA\_KNOMIAL\_FACTOR
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_REDUCE\_INTRA\_KNOMIAL\_FACTOR

  - MPICH\_REDUCE\_INTRA\_KNOMIAL\_FACTOR

- **Description**: This defines the degree of the knomial operation during the intra-node knomial reduce phase.

- **Default:** 4

MPIR\_CVAR\_DEVICE\_COLLECTIVES
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_DEVICE\_COLLECTIVES

  - MPICH\_DEVICE\_COLLECTIVES

- **Description**: Variable to select whether the device can override the

  - MPIR-level collective algorithms.

  - all     - Always prefer the device collectives

  - none    - Never pick the device collectives

  - percoll - Use the per-collective CVARs to decide

- **Default:** percoll

MPIR\_CVAR\_COLLECTIVE\_FALLBACK
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_COLLECTIVE\_FALLBACK

  - MPICH\_COLLECTIVE\_FALLBACK

- **Description**: Variable to control what the MPI library should do if the

  - user-specified collective algorithm does not work for the

  - arguments passed in by the user.

  - error   - throw an error

  - print   - print an error message and fallback to the internally selected algorithm

  - silent  - silently fallback to the internally selected algorithm

- **Default:** silent

MPIR\_CVAR\_COLL\_SELECTION\_TUNING\_JSON\_FILE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_COLL\_SELECTION\_TUNING\_JSON\_FILE

  - MPICH\_COLL\_SELECTION\_TUNING\_JSON\_FILE

- **Description**: Defines the location of tuning file.

- **Default:**

MPIR\_CVAR\_HIERARCHY\_DUMP
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_HIERARCHY\_DUMP

  - MPICH\_HIERARCHY\_DUMP

- **Description**: If set to true, each rank will dump the hierarchy data structure to a file named "hierarchy[rank]" in the current folder. If set to false, the hierarchy data structure will not be dumped.

- **Default:** false

MPIR\_CVAR\_COORDINATES\_FILE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_COORDINATES\_FILE

  - MPICH\_COORDINATES\_FILE

- **Description**: Defines the location of the input coordinates file.

- **Default:**

MPIR\_CVAR\_COLL\_TREE\_DUMP
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_COLL\_TREE\_DUMP

  - MPICH\_COLL\_TREE\_DUMP

- **Description**: If set to true, each rank will dump the tree to a file named "colltree[rank].json" in the current folder. If set to false, the tree will not be dumped.

- **Default:** false

MPIR\_CVAR\_COORDINATES\_DUMP
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_COORDINATES\_DUMP

  - MPICH\_COORDINATES\_DUMP

- **Description**: If set to true, rank 0 will dump the network coordinates to a file named "coords" in the current folder. If set to false, the network coordinates will not be dumped.

- **Default:** false

MPIR\_CVAR\_PROGRESS\_MAX\_COLLS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_PROGRESS\_MAX\_COLLS

  - MPICH\_PROGRESS\_MAX\_COLLS

- **Description**: Maximum number of collective operations at a time that the progress engine should make progress on

- **Default:** 0

MPIR\_CVAR\_COMM\_SPLIT\_USE\_QSORT
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_COMM\_SPLIT\_USE\_QSORT

  - MPICH\_COMM\_SPLIT\_USE\_QSORT

- **Description**: Use qsort(3) in the implementation of MPI\_Comm\_split instead of bubble sort.

- **Default:** true

MPIR\_CVAR\_CTXID\_EAGER\_SIZE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CTXID\_EAGER\_SIZE

  - MPICH\_CTXID\_EAGER\_SIZE

- **Description**: The MPIR\_CVAR\_CTXID\_EAGER\_SIZE environment variable allows you to specify how many words in the context ID mask will be set aside for the eager allocation protocol.  If the application is running out of context IDs, reducing this value may help.

- **Default:** 2

MPIR\_CVAR\_DATALOOP\_FAST\_SEEK
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_DATALOOP\_FAST\_SEEK

  - MPICH\_DATALOOP\_FAST\_SEEK

- **Description**: use a datatype-specialized algorithm to shortcut seeking to the correct location in a noncontiguous buffer

- **Default:** 1

MPIR\_CVAR\_YAKSA\_COMPLEX\_SUPPORT
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_YAKSA\_COMPLEX\_SUPPORT

  - MPICH\_YAKSA\_COMPLEX\_SUPPORT

- **Description**: This CVAR indicates that complex type reduction is not supported in yaksa.

- **Default:** 0

MPIR\_CVAR\_GPU\_DOUBLE\_SUPPORT
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_GPU\_DOUBLE\_SUPPORT

  - MPICH\_GPU\_DOUBLE\_SUPPORT

- **Description**: This CVAR indicates that double type is not supported on the GPU.

- **Default:** 0

MPIR\_CVAR\_GPU\_LONG\_DOUBLE\_SUPPORT
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_GPU\_LONG\_DOUBLE\_SUPPORT

  - MPICH\_GPU\_LONG\_DOUBLE\_SUPPORT

- **Description**: This CVAR indicates that double type is not supported on the GPU.

- **Default:** 0

MPIR\_CVAR\_ENABLE\_YAKSA\_REDUCTION
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ENABLE\_YAKSA\_REDUCTION

  - MPICH\_ENABLE\_YAKSA\_REDUCTION

- **Description**: This cvar enables yaksa based reduction for local reduce.

- **Default:** 1

MPIR\_CVAR\_ENABLE\_GDRCOPY
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ENABLE\_GDRCOPY

  - MPICH\_ENABLE\_GDRCOPY

- **Description**: This cvar enables gdrcopy based staging for yaksa operations

- **Default:** 1

MPIR\_CVAR\_GDRCOPY\_MAX\_SIZE\_H2D
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_GDRCOPY\_MAX\_SIZE\_H2D

  - MPICH\_GDRCOPY\_MAX\_SIZE\_H2D

- **Description**: This cvar controls the maximum number of bytes for which gdrcopy will be used for staging from host to device

- **Default:** 32768

MPIR\_CVAR\_GDRCOPY\_MAX\_SIZE\_D2H
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_GDRCOPY\_MAX\_SIZE\_D2H

  - MPICH\_GDRCOPY\_MAX\_SIZE\_D2H

- **Description**: This cvar controls the maximum number of bytes for which gdrcopy will be used for staging from a device to host

- **Default:** 2048

MPIR\_CVAR\_PROCTABLE\_SIZE
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_PROCTABLE\_SIZE

  - MPICH\_PROCTABLE\_SIZE

- **Description**: Size of the "MPIR" debugger interface proctable (process table).

- **Default:** 64

MPIR\_CVAR\_PROCTABLE\_PRINT
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_PROCTABLE\_PRINT

  - MPICH\_PROCTABLE\_PRINT

- **Description**: If true, dump the proctable entries at MPII\_Wait\_for\_debugger-time.

- **Default:** false

MPIR\_CVAR\_PRINT\_ERROR\_STACK
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_PRINT\_ERROR\_STACK

  - MPICH\_PRINT\_ERROR\_STACK

- **Description**: If true, print an error stack trace at error handling time.

- **Default:** true

MPIR\_CVAR\_CHOP\_ERROR\_STACK
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CHOP\_ERROR\_STACK

  - MPICH\_CHOP\_ERROR\_STACK

- **Description**: If >0, truncate error stack output lines this many characters wide.  If 0, do not truncate, and if <0 use a sensible default.

- **Default:** 0

MPIR\_CVAR\_ASYNC\_PROGRESS
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ASYNC\_PROGRESS

  - MPICH\_ASYNC\_PROGRESS

- **Description**: If set to true, MPICH will initiate an additional thread to make asynchronous progress on all communication operations including point-to-point, collective, one-sided operations and I/O.  Setting this variable will automatically increase the thread-safety level to MPI\_THREAD\_MULTIPLE.  While this improves the progress semantics, it might cause a small amount of performance overhead for regular MPI operations.  The user is encouraged to leave one or more hardware threads vacant in order to prevent contention between the application threads and the progress thread(s).  The impact of oversubscription is highly system dependent but may be substantial in some cases, hence this recommendation.

- **Default:** false

MPIR\_CVAR\_PROGRESS\_THREAD\_AFFINITY
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_PROGRESS\_THREAD\_AFFINITY

  - MPICH\_PROGRESS\_THREAD\_AFFINITY

- **Description**: Specifies affinity for all progress threads of local processes. Can be set to auto or comma-separated list of logical processors. When set to auto - MPICH will automatically select logical CPU cores to decide affinity of the progress threads. When set to comma-separated list of logical processors - In case of N progress threads per process, the first N logical processors from list will be assigned to threads of first local process, the next N logical processors from list - to second local process and so on. For example, thread affinity is "0,1,2,3", 2 progress threads per process and 2 processes per node. Progress threads of first local process will be pinned on logical processors "0,1", progress threads of second local process - on "2,3". Cannot work together with MPIR\_CVAR\_NUM\_CLIQUES or MPIR\_CVAR\_ODD\_EVEN\_CLIQUES.

- **Default:**

MPIR\_CVAR\_SUPPRESS\_ABORT\_MESSAGE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_SUPPRESS\_ABORT\_MESSAGE

  - MPICH\_SUPPRESS\_ABORT\_MESSAGE

- **Description**: Disable printing of abort error message.

- **Default:** false

MPIR\_CVAR\_COREDUMP\_ON\_ABORT
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_COREDUMP\_ON\_ABORT

  - MPICH\_COREDUMP\_ON\_ABORT

- **Description**: Call libc abort() to generate a corefile

- **Default:** false

MPIR\_CVAR\_ERROR\_CHECKING
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ERROR\_CHECKING

  - MPICH\_ERROR\_CHECKING

- **Description**: If true, perform checks for errors, typically to verify valid inputs to MPI routines.  Only effective when MPICH is configured with --enable-error-checking=runtime .

- **Default:** true

MPIR\_CVAR\_MEMDUMP
~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_MEMDUMP

  - MPICH\_MEMDUMP

- **Description**: If true, list any memory that was allocated by MPICH and that remains allocated when MPI\_Finalize completes.

- **Default:** true

MPIR\_CVAR\_DEBUG\_SUMMARY
~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_DEBUG\_SUMMARY

  - MPICH\_DEBUG\_SUMMARY

  - MPIR\_CVAR\_MEM\_CATEGORY\_INFORMATION

  - MPIR\_CVAR\_CH4\_OFI\_CAPABILITY\_SETS\_DEBUG

  - MPIR\_CVAR\_CH4\_UCX\_CAPABILITY\_DEBUG

  - MVP\_MEM\_CATEGORY\_INFORMATION

  - MVP\_CH4\_OFI\_CAPABILITY\_SETS\_DEBUG

  - MVP\_CH4\_UCX\_CAPABILITY\_DEBUG

  - MPICH\_MEM\_CATEGORY\_INFORMATION

  - MPICH\_CH4\_OFI\_CAPABILITY\_SETS\_DEBUG

  - MPICH\_CH4\_UCX\_CAPABILITY\_DEBUG

- **Description**: 1: Print internal summary of various debug information, such as memory allocation by category. Each layer may print their own summary information. For example, ch4-ofi may print its provider capability settings. 2: Also print the preferred NIC for each rank

- **Default:** 0

MPIR\_CVAR\_DEFAULT\_THREAD\_LEVEL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_DEFAULT\_THREAD\_LEVEL

  - MPICH\_DEFAULT\_THREAD\_LEVEL

- **Description**: Sets the default thread level to use when using MPI\_INIT. This variable is case-insensitive.

- **Default:** MPI\_THREAD\_SINGLE

MPIR\_CVAR\_DEBUG\_HOLD
~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_DEBUG\_HOLD

  - MPICH\_DEBUG\_HOLD

- **Description**: If true, causes processes to wait in MPI\_Init and MPI\_Initthread for a debugger to be attached.  Once the debugger has attached, the variable 'hold' should be set to 0 in order to allow the process to continue (e.g., in gdb, "set hold=0").

- **Default:** false

MPIR\_CVAR\_GPU\_USE\_IMMEDIATE\_COMMAND\_LIST
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_GPU\_USE\_IMMEDIATE\_COMMAND\_LIST

  - MPICH\_GPU\_USE\_IMMEDIATE\_COMMAND\_LIST

- **Description**: If true, mpl/ze will use immediate command list for copying

- **Default:** false

MPIR\_CVAR\_GPU\_ROUND\_ROBIN\_COMMAND\_QUEUES
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_GPU\_ROUND\_ROBIN\_COMMAND\_QUEUES

  - MPICH\_GPU\_ROUND\_ROBIN\_COMMAND\_QUEUES

- **Description**: If true, mpl/ze will use command queues in a round-robin fashion. If false, only command queues of index 0 will be used.

- **Default:** false

MPIR\_CVAR\_NO\_COLLECTIVE\_FINALIZE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_NO\_COLLECTIVE\_FINALIZE

  - MPICH\_NO\_COLLECTIVE\_FINALIZE

- **Description**: If true, prevent MPI\_Finalize to invoke collective behavior such as barrier or communicating to other processes. Consequently, it may result in leaking memory or losing messages due to pre-mature exiting. The default is false, which may invoke collective behaviors at finalize.

- **Default:** false

MPIR\_CVAR\_FINALIZE\_WAIT
~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_FINALIZE\_WAIT

  - MPICH\_FINALIZE\_WAIT

- **Description**: If true, poll progress at MPI\_Finalize until reference count on MPI\_COMM\_WORLD and MPI\_COMM\_SELF reaches zero. This may be necessary to prevent remote processes hanging if it has pending communication protocols, e.g. a rendezvous send.

- **Default:** false

MPIR\_CVAR\_REQUEST\_ERR\_FATAL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_REQUEST\_ERR\_FATAL

  - MPICH\_REQUEST\_ERR\_FATAL

- **Description**: By default, MPI\_Waitall, MPI\_Testall, MPI\_Waitsome, and MPI\_Testsome return MPI\_ERR\_IN\_STATUS when one of the request fails. If MPIR\_CVAR\_REQUEST\_ERR\_FATAL is set to true, these routines will return the error code of the request immediately. The default MPI\_ERRS\_ARE\_FATAL error handler will dump a error stack in this case, which maybe more convenient for debugging. This cvar will also make nonblocking shched return error right away as it issues operations.

- **Default:** false

MPIR\_CVAR\_REQUEST\_POLL\_FREQ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_REQUEST\_POLL\_FREQ

  - MPICH\_REQUEST\_POLL\_FREQ

- **Description**: How frequent to poll during MPI\_{Waitany,Waitsome} in terms of number of processed requests before polling.

- **Default:** 8

MPIR\_CVAR\_REQUEST\_BATCH\_SIZE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_REQUEST\_BATCH\_SIZE

  - MPICH\_REQUEST\_BATCH\_SIZE

- **Description**: The number of requests to make completion as a batch in MPI\_Waitall and MPI\_Testall implementation. A large number is likely to cause more cache misses.

- **Default:** 64

MPIR\_CVAR\_DEBUG\_PROGRESS\_TIMEOUT
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_DEBUG\_PROGRESS\_TIMEOUT

  - MPICH\_DEBUG\_PROGRESS\_TIMEOUT

- **Description**: Sets the timeout in seconds to dump outstanding requests when progress wait is not making progress for some time.

- **Default:** 0

MPIR\_CVAR\_DIMS\_VERBOSE
~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_DIMS\_VERBOSE

  - MPICH\_DIMS\_VERBOSE

- **Description**: If true, enable verbose output about the actions of the implementation of MPI\_Dims\_create.

- **Default:** false

MPIR\_CVAR\_QMPI\_TOOL\_LIST
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_QMPI\_TOOL\_LIST

  - MPICH\_QMPI\_TOOL\_LIST

- **Description**: Set the number and order of QMPI tools to be loaded by the MPI library when it is initialized.

- **Default:** NULL

MPIR\_CVAR\_NAMESERV\_FILE\_PUBDIR
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_NAMESERV\_FILE\_PUBDIR

  - MPICH\_NAMESERV\_FILE\_PUBDIR

  - MPIR\_CVAR\_NAMEPUB\_DIR

  - MVP\_NAMEPUB\_DIR

  - MPICH\_NAMEPUB\_DIR

- **Description**: Sets the directory to use for MPI service publishing in the file nameserv implementation.  Allows the user to override where the publish and lookup information is placed for connect/accept based applications.

- **Default:** NULL

MPIR\_CVAR\_ENABLE\_COMPRESSION
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ENABLE\_COMPRESSION

  - MPICH\_ENABLE\_COMPRESSION

- **Description**: Possible values: 0, 1 If set to 1, turn on compression If set to 2, turn off ompression

- **Default:** 0

MPIR\_CVAR\_COMPRESSION\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_COMPRESSION\_ALGORITHM

  - MPICH\_COMPRESSION\_ALGORITHM

- **Description**: Used to force a particular GPU compression algorithm

  - mpc - Use MPC lossless compression algorithm

  - zfp - Use ZFP lossy compression algorithm

- **Default:** mpc

MPIR\_CVAR\_COMPRESSION\_GPU\_BLOCKS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_COMPRESSION\_GPU\_BLOCKS

  - MPICH\_COMPRESSION\_GPU\_BLOCKS

- **Description**: GPU thread blocks

- **Default:** 216

MPIR\_CVAR\_COMPRESSION\_DIMENSION
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_COMPRESSION\_DIMENSION

  - MPICH\_COMPRESSION\_DIMENSION

- **Description**: Dimensionality in compression Possible values: integer between 1 and 32

- **Default:** 1

MPIR\_CVAR\_COMPRESSION\_NUM\_STREAM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_COMPRESSION\_NUM\_STREAM

  - MPICH\_COMPRESSION\_NUM\_STREAM

- **Description**: Number of streams in compression

- **Default:** 512

MPIR\_CVAR\_COMPRESSION\_DATA\_TYPE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_COMPRESSION\_DATA\_TYPE

  - MPICH\_COMPRESSION\_DATA\_TYPE

- **Description**: Used to force a particular GPU compression algorithm

  - FLOAT  - use compression with floating point type

  - DOUBLE - use compression with double precision type

- **Default:** FLOAT

MPIR\_CVAR\_ENABLE\_PT2PT\_GPU\_COMPRESSION
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ENABLE\_PT2PT\_GPU\_COMPRESSION

  - MPICH\_ENABLE\_PT2PT\_GPU\_COMPRESSION

- **Description**: Possible values: 0, 1 If set to 0, turn off point to point compression If set to 1, use point to point compression

- **Default:** 1

MPIR\_CVAR\_COMPRESSION\_REDUCE\_SCATTER\_CHUNK\_SIZE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_COMPRESSION\_REDUCE\_SCATTER\_CHUNK\_SIZE

  - MPICH\_COMPRESSION\_REDUCE\_SCATTER\_CHUNK\_SIZE

- **Description**: Chunk data size for COLLECTIVEective compression in ring-based reduce-scatter

- **Default:** (2\*1024\*1024)

MPIR\_CVAR\_COMPRESSION\_BCAST\_CHUNKS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_COMPRESSION\_BCAST\_CHUNKS

  - MPICH\_COMPRESSION\_BCAST\_CHUNKS

- **Description**: Default number of chunks for chunked-chain bcast with compression

- **Default:** 2

MPIR\_CVAR\_COMPRESSION\_BCAST\_CHUNK\_SIZE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_COMPRESSION\_BCAST\_CHUNK\_SIZE

  - MPICH\_COMPRESSION\_BCAST\_CHUNK\_SIZE

- **Description**: Default chunk size for chunked-chain bcast with compression

- **Default:** (512\*1024)

MPIR\_CVAR\_ZFP\_NUM\_STREAM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ZFP\_NUM\_STREAM

  - MPICH\_ZFP\_NUM\_STREAM

- **Description**: number of zfp streams to preallocate pool Possible values: integer greater than 1

- **Default:** 64

MPIR\_CVAR\_ZFP\_RATE
~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ZFP\_RATE

  - MPICH\_ZFP\_RATE

- **Description**: Possible values: [1,32] for float, [1-64] for double

- **Default:** 16

MPIR\_CVAR\_ZFP\_NX
~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ZFP\_NX

  - MPICH\_ZFP\_NX

- **Description**: For 2D dimension Possible values: Positive integer, multiple of 4

- **Default:** 4

MPIR\_CVAR\_ZFP\_NY
~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ZFP\_NY

  - MPICH\_ZFP\_NY

- **Description**: For 3D dimension Possible values: Positive integer, multiple of 4

- **Default:** 4

MPIR\_CVAR\_ZFP\_ALLOC\_WARNING
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ZFP\_ALLOC\_WARNING

  - MPICH\_ZFP\_ALLOC\_WARNING

- **Description**: Possible values: 0, 1 If set to 0, turn off warning for allocation of zfp stream pool If set to 1, turn on warning for allocation of zfp stream pool

- **Default:** 1

MPIR\_CVAR\_ZFP\_PATH
~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ZFP\_PATH

  - MPICH\_ZFP\_PATH

- **Description**: Path to an alternate ZFP library to be opened with dlsym at runtime. By default ZFP is linked to an included version.

- **Default:** NULL

MPIR\_CVAR\_ENABLE\_ALLREDUCE\_COMPRESSION
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ENABLE\_ALLREDUCE\_COMPRESSION

  - MPICH\_ENABLE\_ALLREDUCE\_COMPRESSION

- **Description**: Possible values: 0, 1 If set to 0, turn off collective compression for allreduce If set to 1, use collective compression for allreduce

- **Default:** 0

MPIR\_CVAR\_ABORT\_ON\_LEAKED\_HANDLES
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ABORT\_ON\_LEAKED\_HANDLES

  - MPICH\_ABORT\_ON\_LEAKED\_HANDLES

- **Description**: If true, MPI will call MPI\_Abort at MPI\_Finalize if any MPI object handles have been leaked.  For example, if MPI\_Comm\_dup is called without calling a corresponding MPI\_Comm\_free.  For uninteresting reasons, enabling this option may prevent all known object leaks from being reported.  MPICH must have been configure with "--enable-g=handlealloc" or better in order for this functionality to work.

- **Default:** false

MPIR\_CVAR\_NETLOC\_NODE\_FILE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_NETLOC\_NODE\_FILE

  - MPICH\_NETLOC\_NODE\_FILE

- **Description**: Subnet json file

- **Default:** auto

MPIR\_CVAR\_NOLOCAL
~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_NOLOCAL

  - MPICH\_NOLOCAL

  - MPIR\_CVAR\_NO\_LOCAL

  - MVP\_NO\_LOCAL

  - MPICH\_NO\_LOCAL

- **Description**: If true, force all processes to operate as though all processes are located on another node.  For example, this disables shared memory communication hierarchical collectives.

- **Default:** false

MPIR\_CVAR\_ODD\_EVEN\_CLIQUES
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ODD\_EVEN\_CLIQUES

  - MPICH\_ODD\_EVEN\_CLIQUES

  - MPIR\_CVAR\_EVEN\_ODD\_CLIQUES

  - MVP\_EVEN\_ODD\_CLIQUES

  - MPICH\_EVEN\_ODD\_CLIQUES

- **Description**: If true, odd procs on a node are seen as local to each other, and even procs on a node are seen as local to each other.  Used for debugging on a single machine. Deprecated in favor of MPIR\_CVAR\_NUM\_CLIQUES.

- **Default:** false

MPIR\_CVAR\_NUM\_CLIQUES
~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_NUM\_CLIQUES

  - MPICH\_NUM\_CLIQUES

- **Description**: Specify the number of cliques that should be used to partition procs on a local node. Procs with the same clique number are seen as local to each other. Used for debugging on a single machine.

- **Default:** 1

MPIR\_CVAR\_CLIQUES\_BY\_BLOCK
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CLIQUES\_BY\_BLOCK

  - MPICH\_CLIQUES\_BY\_BLOCK

- **Description**: Specify to divide processes into cliques by uniform blocks. The default is to divide in round-robin fashion. Used for debugging on a single machine.

- **Default:** false

MPIR\_CVAR\_PMI\_VERSION
~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_PMI\_VERSION

  - MPICH\_PMI\_VERSION

- **Description**: Variable to select runtime PMI version.

  - 1        - PMI (default)

  - 2        - PMI2

  - x        - PMIx

- **Default:** 1

MPIR\_CVAR\_COLL\_ALIAS\_CHECK
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_COLL\_ALIAS\_CHECK

  - MPICH\_COLL\_ALIAS\_CHECK

- **Description**: Enable checking of aliasing in collective operations

- **Default:** 1

MPIR\_CVAR\_ENABLE\_GPU
~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ENABLE\_GPU

  - MPICH\_ENABLE\_GPU

- **Description**: Control MPICH GPU support. If set to 0, all GPU support is disabled and we do not query the buffer type internally because we assume no GPU buffer is use.

- **Default:** 1

MPIR\_CVAR\_GPU\_HAS\_WAIT\_KERNEL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_GPU\_HAS\_WAIT\_KERNEL

  - MPICH\_GPU\_HAS\_WAIT\_KERNEL

- **Description**: If set to 1, avoid allocate allocating GPU registered host buffers for temporary buffers. When stream workq and GPU wait kernels are in use, access APIs for GPU registered memory may cause deadlock.

- **Default:** 0

MPIR\_CVAR\_ENABLE\_GPU\_REGISTER
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ENABLE\_GPU\_REGISTER

  - MPICH\_ENABLE\_GPU\_REGISTER

- **Description**: Control whether to actually register buffers with the GPU runtime in MPIR\_gpu\_register\_host. This could lower the latency of certain GPU communication at the cost of some amount of GPU memory consumed by the MPI library. By default, registration is enabled.

- **Default:** true

MPIR\_CVAR\_LMEM\_POOL\_SIZE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_LMEM\_POOL\_SIZE

  - MPICH\_LMEM\_POOL\_SIZE

- **Description**: Sets the amount of space allocated at init time to be used by internal functions for local temp buffers.

- **Default:** 32 \* 1024 \* 1024

MPIR\_CVAR\_POLLS\_BEFORE\_YIELD
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_POLLS\_BEFORE\_YIELD

  - MPICH\_POLLS\_BEFORE\_YIELD

- **Description**: When MPICH is in a busy waiting loop, it will periodically call a function to yield the processor.  This cvar sets the number of loops before the yield function is called.  A value of 0 disables yielding.

- **Default:** 1000

MPIR\_CVAR\_CH3\_INTERFACE\_HOSTNAME
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH3\_INTERFACE\_HOSTNAME

  - MPICH\_CH3\_INTERFACE\_HOSTNAME

  - MPIR\_CVAR\_INTERFACE\_HOSTNAME

  - MVP\_INTERFACE\_HOSTNAME

  - MPICH\_INTERFACE\_HOSTNAME

- **Description**: If non-NULL, this cvar specifies the IP address that other processes should use when connecting to this process. This cvar is mutually exclusive with the MPIR\_CVAR\_CH3\_NETWORK\_IFACE cvar and it is an error to set them both.

- **Default:** NULL

MPIR\_CVAR\_CH3\_PORT\_RANGE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH3\_PORT\_RANGE

  - MPICH\_CH3\_PORT\_RANGE

  - MPIR\_CVAR\_PORTRANGE

  - MPIR\_CVAR\_PORT\_RANGE

  - MVP\_PORTRANGE

  - MVP\_PORT\_RANGE

  - MPICH\_PORTRANGE

  - MPICH\_PORT\_RANGE

- **Description**: The MPIR\_CVAR\_CH3\_PORT\_RANGE environment variable allows you to specify the range of TCP ports to be used by the process manager and the MPICH library. The format of this variable is <low>:<high>.  To specify any available port, use 0:0.

- **Default:** 0:0

MPIR\_CVAR\_NEMESIS\_TCP\_NETWORK\_IFACE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_NEMESIS\_TCP\_NETWORK\_IFACE

  - MPICH\_NEMESIS\_TCP\_NETWORK\_IFACE

  - MPIR\_CVAR\_NETWORK\_IFACE

  - MVP\_NETWORK\_IFACE

  - MPICH\_NETWORK\_IFACE

- **Description**: If non-NULL, this cvar specifies which pseudo-ethernet interface the tcp netmod should use (e.g., "eth1", "ib0"). Note, this is a Linux-specific cvar. This cvar is mutually exclusive with the MPIR\_CVAR\_CH3\_INTERFACE\_HOSTNAME cvar and it is an error to set them both.

- **Default:** NULL

MPIR\_CVAR\_NEMESIS\_TCP\_HOST\_LOOKUP\_RETRIES
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_NEMESIS\_TCP\_HOST\_LOOKUP\_RETRIES

  - MPICH\_NEMESIS\_TCP\_HOST\_LOOKUP\_RETRIES

- **Description**: This cvar controls the number of times to retry the gethostbyname() function before giving up.

- **Default:** 10

MPIR\_CVAR\_NEMESIS\_ENABLE\_CKPOINT
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_NEMESIS\_ENABLE\_CKPOINT

  - MPICH\_NEMESIS\_ENABLE\_CKPOINT

- **Description**: If true, enables checkpointing support and returns an error if checkpointing library cannot be initialized.

- **Default:** false

MPIR\_CVAR\_NEMESIS\_SHM\_EAGER\_MAX\_SZ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_NEMESIS\_SHM\_EAGER\_MAX\_SZ

  - MPICH\_NEMESIS\_SHM\_EAGER\_MAX\_SZ

- **Description**: This cvar controls the message size at which Nemesis switches from eager to rendezvous mode for shared memory. If this cvar is set to -1, then Nemesis will choose an appropriate value.

- **Default:** -1

MPIR\_CVAR\_NEMESIS\_SHM\_READY\_EAGER\_MAX\_SZ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_NEMESIS\_SHM\_READY\_EAGER\_MAX\_SZ

  - MPICH\_NEMESIS\_SHM\_READY\_EAGER\_MAX\_SZ

- **Description**: This cvar controls the message size at which Nemesis switches from eager to rendezvous mode for ready-send messages.  If this cvar is set to -1, then ready messages will always be sent eagerly.  If this cvar is set to -2, then Nemesis will choose an appropriate value.

- **Default:** -2

MPIR\_CVAR\_ENABLE\_FT
~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ENABLE\_FT

  - MPICH\_ENABLE\_FT

- **Description**: Enable fault tolerance functions

- **Default:** false

MPIR\_CVAR\_NEMESIS\_NETMOD
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_NEMESIS\_NETMOD

  - MPICH\_NEMESIS\_NETMOD

- **Description**: If non-empty, this cvar specifies which network module should be used for communication. This variable is case-insensitive.

- **Default:**

MPIR\_CVAR\_CH3\_ENABLE\_HCOLL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH3\_ENABLE\_HCOLL

  - MPICH\_CH3\_ENABLE\_HCOLL

- **Description**: If true, enable HCOLL collectives.

- **Default:** false

MPIR\_CVAR\_CH3\_COMM\_CONNECT\_TIMEOUT
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH3\_COMM\_CONNECT\_TIMEOUT

  - MPICH\_CH3\_COMM\_CONNECT\_TIMEOUT

- **Description**: The default time out period in seconds for a connection attempt to the server communicator where the named port exists but no pending accept. User can change the value for a specified connection through its info argument.

- **Default:** 180

MPIR\_CVAR\_CH3\_RMA\_OP\_PIGGYBACK\_LOCK\_DATA\_SIZE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH3\_RMA\_OP\_PIGGYBACK\_LOCK\_DATA\_SIZE

  - MPICH\_CH3\_RMA\_OP\_PIGGYBACK\_LOCK\_DATA\_SIZE

- **Description**: Specify the threshold of data size of a RMA operation which can be piggybacked with a LOCK message. It is always a positive value and should not be smaller than MPIDI\_RMA\_IMMED\_BYTES. If user sets it as a small value, for middle and large data size, we will lose performance because of always waiting for round-trip of LOCK synchronization; if user sets it as a large value, we need to consume more memory on target side to buffer this lock request when lock is not satisfied.

- **Default:** 65536

MPIR\_CVAR\_CH3\_RMA\_ACTIVE\_REQ\_THRESHOLD
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH3\_RMA\_ACTIVE\_REQ\_THRESHOLD

  - MPICH\_CH3\_RMA\_ACTIVE\_REQ\_THRESHOLD

- **Description**: Threshold of number of active requests to trigger blocking waiting in operation routines. When the value is negative, we never blockingly wait in operation routines. When the value is zero, we always trigger blocking waiting in operation routines to wait until no. of active requests becomes zero. When the value is positive, we do blocking waiting in operation routines to wait until no. of active requests being reduced to this value.

- **Default:** 65536

MPIR\_CVAR\_CH3\_RMA\_POKE\_PROGRESS\_REQ\_THRESHOLD
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH3\_RMA\_POKE\_PROGRESS\_REQ\_THRESHOLD

  - MPICH\_CH3\_RMA\_POKE\_PROGRESS\_REQ\_THRESHOLD

- **Description**: Threshold at which the RMA implementation attempts to complete requests while completing RMA operations and while using the lazy synchronization approach.  Change this value if programs fail because they run out of requests or other internal resources

- **Default:** 128

MPIR\_CVAR\_CH3\_RMA\_SCALABLE\_FENCE\_PROCESS\_NUM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH3\_RMA\_SCALABLE\_FENCE\_PROCESS\_NUM

  - MPICH\_CH3\_RMA\_SCALABLE\_FENCE\_PROCESS\_NUM

- **Description**: Specify the threshold of switching the algorithm used in FENCE from the basic algorithm to the scalable algorithm. The value can be negative, zero or positive. When the number of processes is larger than or equal to this value, FENCE will use a scalable algorithm which do not use O(P) data structure; when the number of processes is smaller than the value, FENCE will use a basic but fast algorithm which requires an O(P) data structure.

- **Default:** 1024

MPIR\_CVAR\_CH3\_RMA\_DELAY\_ISSUING\_FOR\_PIGGYBACKING
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH3\_RMA\_DELAY\_ISSUING\_FOR\_PIGGYBACKING

  - MPICH\_CH3\_RMA\_DELAY\_ISSUING\_FOR\_PIGGYBACKING

- **Description**: Specify if delay issuing of RMA operations for piggybacking LOCK/UNLOCK/FLUSH is enabled. It can be either 0 or 1. When it is set to 1, the issuing of LOCK message is delayed until origin process see the first RMA operation and piggyback LOCK with that operation, and the origin process always keeps the current last operation until the ending synchronization call in order to piggyback UNLOCK/FLUSH with that operation. When it is set to 0, in WIN\_LOCK/UNLOCK case, the LOCK message is sent out as early as possible, in WIN\_LOCK\_ALL/UNLOCK\_ALL case, the origin process still tries to piggyback LOCK message with the first operation; for UNLOCK/FLUSH message, the origin process no longer keeps the current last operation but only piggyback UNLOCK/FLUSH if there is an operation available in the ending synchronization call.

- **Default:** 0

MPIR\_CVAR\_CH3\_RMA\_SLOTS\_SIZE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH3\_RMA\_SLOTS\_SIZE

  - MPICH\_CH3\_RMA\_SLOTS\_SIZE

- **Description**: Number of RMA slots during window creation. Each slot contains a linked list of target elements. The distribution of ranks among slots follows a round-robin pattern. Requires a positive value.

- **Default:** 262144

MPIR\_CVAR\_CH3\_RMA\_TARGET\_LOCK\_DATA\_BYTES
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH3\_RMA\_TARGET\_LOCK\_DATA\_BYTES

  - MPICH\_CH3\_RMA\_TARGET\_LOCK\_DATA\_BYTES

- **Description**: Size (in bytes) of available lock data this window can provided. If current buffered lock data is more than this value, the process will drop the upcoming operation data. Requires a positive value.

- **Default:** 655360

MPIR\_CVAR\_CH3\_EAGER\_MAX\_MSG\_SIZE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH3\_EAGER\_MAX\_MSG\_SIZE

  - MPICH\_CH3\_EAGER\_MAX\_MSG\_SIZE

- **Description**: This cvar controls the message size at which CH3 switches from eager to rendezvous mode.

- **Default:** 131072

MPIR\_CVAR\_CH3\_PG\_VERBOSE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH3\_PG\_VERBOSE

  - MPICH\_CH3\_PG\_VERBOSE

- **Description**: If set, print the PG state on finalize.

- **Default:** 0

MPIR\_CVAR\_CH3\_RMA\_OP\_WIN\_POOL\_SIZE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH3\_RMA\_OP\_WIN\_POOL\_SIZE

  - MPICH\_CH3\_RMA\_OP\_WIN\_POOL\_SIZE

- **Description**: Size of the window-private RMA operations pool (in number of operations) that stores information about RMA operations that could not be issued immediately.  Requires a positive value.

- **Default:** 256

MPIR\_CVAR\_CH3\_RMA\_OP\_GLOBAL\_POOL\_SIZE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH3\_RMA\_OP\_GLOBAL\_POOL\_SIZE

  - MPICH\_CH3\_RMA\_OP\_GLOBAL\_POOL\_SIZE

- **Description**: Size of the Global RMA operations pool (in number of operations) that stores information about RMA operations that could not be issued immediately.  Requires a positive value.

- **Default:** 16384

MPIR\_CVAR\_CH3\_RMA\_TARGET\_WIN\_POOL\_SIZE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH3\_RMA\_TARGET\_WIN\_POOL\_SIZE

  - MPICH\_CH3\_RMA\_TARGET\_WIN\_POOL\_SIZE

- **Description**: Size of the window-private RMA target pool (in number of targets) that stores information about RMA targets that could not be issued immediately.  Requires a positive value.

- **Default:** 256

MPIR\_CVAR\_CH3\_RMA\_TARGET\_GLOBAL\_POOL\_SIZE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH3\_RMA\_TARGET\_GLOBAL\_POOL\_SIZE

  - MPICH\_CH3\_RMA\_TARGET\_GLOBAL\_POOL\_SIZE

- **Description**: Size of the Global RMA targets pool (in number of targets) that stores information about RMA targets that could not be issued immediately.  Requires a positive value.

- **Default:** 16384

MPIR\_CVAR\_CH3\_RMA\_TARGET\_LOCK\_ENTRY\_WIN\_POOL\_SIZE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH3\_RMA\_TARGET\_LOCK\_ENTRY\_WIN\_POOL\_SIZE

  - MPICH\_CH3\_RMA\_TARGET\_LOCK\_ENTRY\_WIN\_POOL\_SIZE

- **Description**: Size of the window-private RMA lock entries pool (in number of lock entries) that stores information about RMA lock requests that could not be satisfied immediately.  Requires a positive value.

- **Default:** 256

MPIR\_CVAR\_OFI\_USE\_PROVIDER
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_OFI\_USE\_PROVIDER

  - MPICH\_OFI\_USE\_PROVIDER

- **Description**: This variable is no longer supported. Use FI\_PROVIDER instead to select libfabric providers.

- **Default:** NULL

MPIR\_CVAR\_SINGLE\_HOST\_ENABLED
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_SINGLE\_HOST\_ENABLED

  - MPICH\_SINGLE\_HOST\_ENABLED

- **Description**: Set this variable to true to indicate that processes are launched on a single host. The current implication is to avoid the cxi provider to prevent the use of scarce hardware resources.

- **Default:** true

MPIR\_CVAR\_CH4\_OFI\_AM\_LONG\_FORCE\_PIPELINE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_OFI\_AM\_LONG\_FORCE\_PIPELINE

  - MPICH\_CH4\_OFI\_AM\_LONG\_FORCE\_PIPELINE

- **Description**: For long message to be sent using pipeline rather than default RDMA read.

- **Default:** false

MPIR\_CVAR\_BCAST\_OFI\_INTRA\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_BCAST\_OFI\_INTRA\_ALGORITHM

  - MPICH\_BCAST\_OFI\_INTRA\_ALGORITHM

- **Description**: Variable to select algorithm for intra-node bcast

  - mpir                        - Fallback to MPIR collectives

  - trigger\_tree\_tagged         - Force triggered ops based Tagged Tree

  - trigger\_tree\_rma            - Force triggered ops based RMA Tree

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_CH4\_OFI\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

- **Default:** auto

MPIR\_CVAR\_OFI\_SKIP\_IPV6
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_OFI\_SKIP\_IPV6

  - MPICH\_OFI\_SKIP\_IPV6

- **Description**: Skip IPv6 providers.

- **Default:** false

MPIR\_CVAR\_CH4\_OFI\_ENABLE\_DATA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_OFI\_ENABLE\_DATA

  - MPICH\_CH4\_OFI\_ENABLE\_DATA

- **Description**: Enable immediate data fields in OFI to transmit source rank outside of the match bits

- **Default:** -1

MPIR\_CVAR\_CH4\_OFI\_ENABLE\_AV\_TABLE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_OFI\_ENABLE\_AV\_TABLE

  - MPICH\_CH4\_OFI\_ENABLE\_AV\_TABLE

- **Description**: If true, the OFI addressing information will be stored with an FI\_AV\_TABLE. If false, an FI\_AV\_MAP will be used.

- **Default:** -1

MPIR\_CVAR\_CH4\_OFI\_ENABLE\_SCALABLE\_ENDPOINTS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_OFI\_ENABLE\_SCALABLE\_ENDPOINTS

  - MPICH\_CH4\_OFI\_ENABLE\_SCALABLE\_ENDPOINTS

- **Description**: If true, use OFI scalable endpoints.

- **Default:** -1

MPIR\_CVAR\_CH4\_OFI\_ENABLE\_SHARED\_CONTEXTS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_OFI\_ENABLE\_SHARED\_CONTEXTS

  - MPICH\_CH4\_OFI\_ENABLE\_SHARED\_CONTEXTS

- **Description**: If set to false (zero), MPICH does not use OFI shared contexts. If set to -1, it is determined by the OFI capability sets based on the provider. Otherwise, MPICH tries to use OFI shared contexts. If they are unavailable, it'll fall back to the mode without shared contexts.

- **Default:** 0

MPIR\_CVAR\_CH4\_OFI\_ENABLE\_MR\_VIRT\_ADDRESS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_OFI\_ENABLE\_MR\_VIRT\_ADDRESS

  - MPICH\_CH4\_OFI\_ENABLE\_MR\_VIRT\_ADDRESS

- **Description**: If true, enable virtual addressing for OFI memory regions. This variable is only meaningful for OFI versions 1.5+. It is equivalent to using FI\_MR\_BASIC in versions of OFI older than 1.5.

- **Default:** -1

MPIR\_CVAR\_CH4\_OFI\_ENABLE\_MR\_ALLOCATED
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_OFI\_ENABLE\_MR\_ALLOCATED

  - MPICH\_CH4\_OFI\_ENABLE\_MR\_ALLOCATED

- **Description**: If true, require all OFI memory regions must be backed by physical memory pages at the time the registration call is made. This variable is only meaningful for OFI versions 1.5+. It is equivalent to using FI\_MR\_BASIC in versions of OFI older than 1.5.

- **Default:** -1

MPIR\_CVAR\_CH4\_OFI\_ENABLE\_MR\_REGISTER\_NULL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_OFI\_ENABLE\_MR\_REGISTER\_NULL

  - MPICH\_CH4\_OFI\_ENABLE\_MR\_REGISTER\_NULL

- **Description**: If true, memory registration call supports registering with NULL addresses.

- **Default:** -1

MPIR\_CVAR\_CH4\_OFI\_ENABLE\_MR\_PROV\_KEY
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_OFI\_ENABLE\_MR\_PROV\_KEY

  - MPICH\_CH4\_OFI\_ENABLE\_MR\_PROV\_KEY

- **Description**: If true, enable provider supplied key for OFI memory regions. This variable is only meaningful for OFI versions 1.5+. It is equivalent to using FI\_MR\_BASIC in versions of OFI older than 1.5.

- **Default:** -1

MPIR\_CVAR\_CH4\_OFI\_ENABLE\_TAGGED
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_OFI\_ENABLE\_TAGGED

  - MPICH\_CH4\_OFI\_ENABLE\_TAGGED

- **Description**: If true, use tagged message transmission functions in OFI.

- **Default:** -1

MPIR\_CVAR\_CH4\_OFI\_ENABLE\_AM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_OFI\_ENABLE\_AM

  - MPICH\_CH4\_OFI\_ENABLE\_AM

- **Description**: If true, enable OFI active message support.

- **Default:** -1

MPIR\_CVAR\_CH4\_OFI\_ENABLE\_RMA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_OFI\_ENABLE\_RMA

  - MPICH\_CH4\_OFI\_ENABLE\_RMA

- **Description**: If true, enable OFI RMA support for MPI RMA operations. OFI support for basic RMA is always required to implement large messgage transfers in the active message code path.

- **Default:** -1

MPIR\_CVAR\_CH4\_OFI\_ENABLE\_ATOMICS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_OFI\_ENABLE\_ATOMICS

  - MPICH\_CH4\_OFI\_ENABLE\_ATOMICS

- **Description**: If true, enable OFI Atomics support.

- **Default:** -1

MPIR\_CVAR\_CH4\_OFI\_FETCH\_ATOMIC\_IOVECS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_OFI\_FETCH\_ATOMIC\_IOVECS

  - MPICH\_CH4\_OFI\_FETCH\_ATOMIC\_IOVECS

- **Description**: Specifies the maximum number of iovecs that can be used by the OFI provider for fetch\_atomic operations. The default value is -1, indicating that no value is set.

- **Default:** -1

MPIR\_CVAR\_CH4\_OFI\_ENABLE\_DATA\_AUTO\_PROGRESS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_OFI\_ENABLE\_DATA\_AUTO\_PROGRESS

  - MPICH\_CH4\_OFI\_ENABLE\_DATA\_AUTO\_PROGRESS

- **Description**: If true, enable MPI data auto progress.

- **Default:** -1

MPIR\_CVAR\_CH4\_OFI\_ENABLE\_CONTROL\_AUTO\_PROGRESS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_OFI\_ENABLE\_CONTROL\_AUTO\_PROGRESS

  - MPICH\_CH4\_OFI\_ENABLE\_CONTROL\_AUTO\_PROGRESS

- **Description**: If true, enable MPI control auto progress.

- **Default:** -1

MPIR\_CVAR\_CH4\_OFI\_ENABLE\_PT2PT\_NOPACK
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_OFI\_ENABLE\_PT2PT\_NOPACK

  - MPICH\_CH4\_OFI\_ENABLE\_PT2PT\_NOPACK

- **Description**: If true, enable iovec for pt2pt.

- **Default:** -1

MPIR\_CVAR\_CH4\_OFI\_ENABLE\_HMEM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_OFI\_ENABLE\_HMEM

  - MPICH\_CH4\_OFI\_ENABLE\_HMEM

- **Description**: If true, uses GPU direct RDMA support in the provider.

- **Default:** 0

MPIR\_CVAR\_CH4\_OFI\_ENABLE\_MR\_HMEM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_OFI\_ENABLE\_MR\_HMEM

  - MPICH\_CH4\_OFI\_ENABLE\_MR\_HMEM

- **Description**: If true, need to register the buffer to use GPU direct RDMA.

- **Default:** -1

MPIR\_CVAR\_CH4\_OFI\_GPU\_RDMA\_THRESHOLD
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_OFI\_GPU\_RDMA\_THRESHOLD

  - MPICH\_CH4\_OFI\_GPU\_RDMA\_THRESHOLD

- **Description**: The threshold to start using GPU direct RDMA.

- **Default:** 0

MPIR\_CVAR\_CH4\_OFI\_CONTEXT\_ID\_BITS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_OFI\_CONTEXT\_ID\_BITS

  - MPICH\_CH4\_OFI\_CONTEXT\_ID\_BITS

- **Description**: Specifies the number of bits that will be used for matching the context ID. The default value is -1, indicating that no value is set and that the default will be defined in the ofi\_types.h file.

- **Default:** -1

MPIR\_CVAR\_CH4\_OFI\_RANK\_BITS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_OFI\_RANK\_BITS

  - MPICH\_CH4\_OFI\_RANK\_BITS

- **Description**: Specifies the number of bits that will be used for matching the MPI rank. The default value is -1, indicating that no value is set and that the default will be defined in the ofi\_types.h file.

- **Default:** -1

MPIR\_CVAR\_CH4\_OFI\_TAG\_BITS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_OFI\_TAG\_BITS

  - MPICH\_CH4\_OFI\_TAG\_BITS

- **Description**: Specifies the number of bits that will be used for matching the user tag. The default value is -1, indicating that no value is set and that the default will be defined in the ofi\_types.h file.

- **Default:** -1

MPIR\_CVAR\_CH4\_OFI\_MAJOR\_VERSION
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_OFI\_MAJOR\_VERSION

  - MPICH\_CH4\_OFI\_MAJOR\_VERSION

- **Description**: Specifies the major version of the OFI library. The default is the major version of the OFI library used with MPICH. If using this CVAR, it is recommended that the user also specifies a specific OFI provider.

- **Default:** -1

MPIR\_CVAR\_CH4\_OFI\_MINOR\_VERSION
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_OFI\_MINOR\_VERSION

  - MPICH\_CH4\_OFI\_MINOR\_VERSION

- **Description**: Specifies the major version of the OFI library. The default is the minor version of the OFI library used with MPICH. If using this CVAR, it is recommended that the user also specifies a specific OFI provider.

- **Default:** -1

MPIR\_CVAR\_CH4\_OFI\_MAX\_RMA\_SEP\_CTX
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_OFI\_MAX\_RMA\_SEP\_CTX

  - MPICH\_CH4\_OFI\_MAX\_RMA\_SEP\_CTX

- **Description**: If set to positive, this CVAR specifies the maximum number of transmit contexts RMA can utilize in a scalable endpoint. This value is effective only when scalable endpoint is available, otherwise it will be ignored.

- **Default:** 0

MPIR\_CVAR\_CH4\_OFI\_MAX\_EAGAIN\_RETRY
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_OFI\_MAX\_EAGAIN\_RETRY

  - MPICH\_CH4\_OFI\_MAX\_EAGAIN\_RETRY

- **Description**: If set to positive, this CVAR specifies the maximum number of retries of an ofi operations before returning MPIX\_ERR\_EAGAIN. This value is effective only when the communicator has the MPI\_OFI\_set\_eagain info hint set to true.

- **Default:** -1

MPIR\_CVAR\_CH4\_OFI\_NUM\_AM\_BUFFERS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_OFI\_NUM\_AM\_BUFFERS

  - MPICH\_CH4\_OFI\_NUM\_AM\_BUFFERS

- **Description**: Specifies the number of buffers for receiving active messages.

- **Default:** -1

MPIR\_CVAR\_CH4\_OFI\_NUM\_OPTIMIZED\_MEMORY\_REGIONS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_OFI\_NUM\_OPTIMIZED\_MEMORY\_REGIONS

  - MPICH\_CH4\_OFI\_NUM\_OPTIMIZED\_MEMORY\_REGIONS

- **Description**: Specifies the number of optimized memory regions supported by the provider. An optimized memory region is used for lower-overhead, unordered RMA operations. It uses a low-overhead RX path and additionally, a low-overhead packet format may be used to target an optimized memory region.

- **Default:** 0

MPIR\_CVAR\_CH4\_OFI\_RMA\_PROGRESS\_INTERVAL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_OFI\_RMA\_PROGRESS\_INTERVAL

  - MPICH\_CH4\_OFI\_RMA\_PROGRESS\_INTERVAL

- **Description**: Specifies the interval for manually flushing RMA operations when automatic progress is not enabled. It the underlying OFI provider supports auto data progress, this value is ignored. If the value is -1, this optimization will be turned off.

- **Default:** 100

MPIR\_CVAR\_CH4\_OFI\_RMA\_IOVEC\_MAX
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_OFI\_RMA\_IOVEC\_MAX

  - MPICH\_CH4\_OFI\_RMA\_IOVEC\_MAX

- **Description**: Specifies the maximum number of iovecs to allocate for RMA operations to/from noncontiguous buffers.

- **Default:** 16384

MPIR\_CVAR\_CH4\_OFI\_EAGER\_MAX\_MSG\_SIZE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_OFI\_EAGER\_MAX\_MSG\_SIZE

  - MPICH\_CH4\_OFI\_EAGER\_MAX\_MSG\_SIZE

- **Description**: This cvar controls the message size at which OFI native path switches from eager to rendezvous mode. It does not affect the AM path eager limit. Having this gives a way to reliably test native non-path. If the number is positive, OFI will init the MPIDI\_OFI\_global.max\_msg\_size to the value of cvar. If the number is negative, OFI will init the MPIDI\_OFI\_globa.max\_msg\_size using whatever provider gives (which might be unlimited for socket provider).

- **Default:** -1

MPIR\_CVAR\_CH4\_OFI\_MAX\_NICS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_OFI\_MAX\_NICS

  - MPICH\_CH4\_OFI\_MAX\_NICS

- **Description**: If set to positive number, this cvar determines the maximum number of physical nics to use (if more than one is available). If the number is -1, underlying netmod or shmmod automatically uses an optimal number depending on what is detected on the system up to the limit determined by MPIDI\_MAX\_NICS (in ofi\_types.h).

- **Default:** -1

MPIR\_CVAR\_CH4\_OFI\_ENABLE\_MULTI\_NIC\_STRIPING
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_OFI\_ENABLE\_MULTI\_NIC\_STRIPING

  - MPICH\_CH4\_OFI\_ENABLE\_MULTI\_NIC\_STRIPING

- **Description**: If true, this cvar enables striping of large messages across multiple NICs.

- **Default:** 0

MPIR\_CVAR\_CH4\_OFI\_MULTI\_NIC\_STRIPING\_THRESHOLD
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_OFI\_MULTI\_NIC\_STRIPING\_THRESHOLD

  - MPICH\_CH4\_OFI\_MULTI\_NIC\_STRIPING\_THRESHOLD

- **Description**: Striping will happen for message sizes beyond this threshold.

- **Default:** 1048576

MPIR\_CVAR\_CH4\_OFI\_ENABLE\_MULTI\_NIC\_HASHING
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_OFI\_ENABLE\_MULTI\_NIC\_HASHING

  - MPICH\_CH4\_OFI\_ENABLE\_MULTI\_NIC\_HASHING

- **Description**: Multi-NIC hashing means to use more than one NIC to send and receive messages above a certain size.  If set to positive number, this feature will be turned on. If set to 0, this feature will be turned off. If the number is -1, MPICH automatically determines whether to use multi-nic hashing depending on what is detected on the system (e.g., number of NICs available, number of processes sharing the NICs).

- **Default:** 0

MPIR\_CVAR\_CH4\_OFI\_MULTIRECV\_BUFFER\_SIZE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_OFI\_MULTIRECV\_BUFFER\_SIZE

  - MPICH\_CH4\_OFI\_MULTIRECV\_BUFFER\_SIZE

- **Description**: Controls the multirecv am buffer size. It is recommended to match this to the hugepage size so that the buffer can be allocated at the page boundary.

- **Default:** 2097152

MPIR\_CVAR\_OFI\_USE\_MIN\_NICS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_OFI\_USE\_MIN\_NICS

  - MPICH\_OFI\_USE\_MIN\_NICS

- **Description**: If true and all nodes do not have the same number of NICs, MPICH will fall back to using the fewest number of NICs instead of returning an error.

- **Default:** true

MPIR\_CVAR\_CH4\_OFI\_ENABLE\_TRIGGERED
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_OFI\_ENABLE\_TRIGGERED

  - MPICH\_CH4\_OFI\_ENABLE\_TRIGGERED

- **Description**: If true, enable OFI triggered ops for MPI collectives.

- **Default:** -1

MPIR\_CVAR\_CH4\_OFI\_GPU\_SEND\_ENGINE\_TYPE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_OFI\_GPU\_SEND\_ENGINE\_TYPE

  - MPICH\_CH4\_OFI\_GPU\_SEND\_ENGINE\_TYPE

- **Description**: Specifies GPU engine type for GPU pt2pt on the sender side.

  - compute - use a compute engine

  - copy\_high\_bandwidth - use a high-bandwidth copy engine

  - copy\_low\_latency - use a low-latency copy engine

  - yaksa - use Yaksa

- **Default:** copy\_low\_latency

MPIR\_CVAR\_CH4\_OFI\_GPU\_RECEIVE\_ENGINE\_TYPE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_OFI\_GPU\_RECEIVE\_ENGINE\_TYPE

  - MPICH\_CH4\_OFI\_GPU\_RECEIVE\_ENGINE\_TYPE

- **Description**: Specifies GPU engine type for GPU pt2pt on the receiver side.

  - compute - use a compute engine

  - copy\_high\_bandwidth - use a high-bandwidth copy engine

  - copy\_low\_latency - use a low-latency copy engine

  - yaksa - use Yaksa

- **Default:** copy\_low\_latency

MPIR\_CVAR\_CH4\_OFI\_ENABLE\_GPU\_PIPELINE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_OFI\_ENABLE\_GPU\_PIPELINE

  - MPICH\_CH4\_OFI\_ENABLE\_GPU\_PIPELINE

- **Description**: If true, enable pipeline for GPU data transfer. GPU pipeline does not support non-contiguous datatypes or mixed buffer types (i.e. GPU send buffer, host recv buffer). If GPU pipeline is enabled, the unsupported scenarios will cause undefined behavior if encountered.

- **Default:** false

MPIR\_CVAR\_CH4\_OFI\_GPU\_PIPELINE\_THRESHOLD
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_OFI\_GPU\_PIPELINE\_THRESHOLD

  - MPICH\_CH4\_OFI\_GPU\_PIPELINE\_THRESHOLD

- **Description**: This is the threshold to start using GPU pipeline.

- **Default:** 131072

MPIR\_CVAR\_CH4\_OFI\_GPU\_PIPELINE\_BUFFER\_SZ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_OFI\_GPU\_PIPELINE\_BUFFER\_SZ

  - MPICH\_CH4\_OFI\_GPU\_PIPELINE\_BUFFER\_SZ

- **Description**: Specifies the buffer size (in bytes) for GPU pipeline data transfer.

- **Default:** 1048576

MPIR\_CVAR\_CH4\_OFI\_GPU\_PIPELINE\_NUM\_BUFFERS\_PER\_CHUNK
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_OFI\_GPU\_PIPELINE\_NUM\_BUFFERS\_PER\_CHUNK

  - MPICH\_CH4\_OFI\_GPU\_PIPELINE\_NUM\_BUFFERS\_PER\_CHUNK

- **Description**: Specifies the number of buffers for GPU pipeline data transfer in each block/chunk of the pool.

- **Default:** 32

MPIR\_CVAR\_CH4\_OFI\_GPU\_PIPELINE\_MAX\_NUM\_BUFFERS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_OFI\_GPU\_PIPELINE\_MAX\_NUM\_BUFFERS

  - MPICH\_CH4\_OFI\_GPU\_PIPELINE\_MAX\_NUM\_BUFFERS

- **Description**: Specifies the total number of buffers for GPU pipeline data transfer

- **Default:** 32

MPIR\_CVAR\_CH4\_OFI\_GPU\_PIPELINE\_D2H\_ENGINE\_TYPE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_OFI\_GPU\_PIPELINE\_D2H\_ENGINE\_TYPE

  - MPICH\_CH4\_OFI\_GPU\_PIPELINE\_D2H\_ENGINE\_TYPE

- **Description**: Specifies the GPU engine type for GPU pipeline on the sender side, default is MPL\_GPU\_ENGINE\_TYPE\_COMPUTE

- **Default:** 0

MPIR\_CVAR\_CH4\_OFI\_GPU\_PIPELINE\_H2D\_ENGINE\_TYPE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_OFI\_GPU\_PIPELINE\_H2D\_ENGINE\_TYPE

  - MPICH\_CH4\_OFI\_GPU\_PIPELINE\_H2D\_ENGINE\_TYPE

- **Description**: Specifies the GPU engine type for GPU pipeline on the receiver side, default is MPL\_GPU\_ENGINE\_TYPE\_COMPUTE

- **Default:** 0

MPIR\_CVAR\_CH4\_OFI\_PREF\_NIC
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_OFI\_PREF\_NIC

  - MPICH\_CH4\_OFI\_PREF\_NIC

- **Description**: Accept the NIC value from a user

- **Default:** -1

MPIR\_CVAR\_CH4\_OFI\_DISABLE\_INJECT\_WRITE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_OFI\_DISABLE\_INJECT\_WRITE

  - MPICH\_CH4\_OFI\_DISABLE\_INJECT\_WRITE

- **Description**: Avoid use fi\_inject\_write. For some provider, e.g. tcp;ofi\_rxm, inject write may break the synchronization.

- **Default:** false

MPIR\_CVAR\_UCX\_DT\_RECV
~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_UCX\_DT\_RECV

  - MPICH\_UCX\_DT\_RECV

- **Description**: Variable to select method for receiving noncontiguous data

  - true                - Use UCX datatype with pack/unpack callbacks

  - false               - MPICH will decide to pack/unpack at completion or use IOVs

  - based on the datatype

- **Default:** false

MPIR\_CVAR\_CH4\_IPC\_GPU\_HANDLE\_CACHE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_IPC\_GPU\_HANDLE\_CACHE

  - MPICH\_CH4\_IPC\_GPU\_HANDLE\_CACHE

- **Description**: By default, we will cache ipc handles using the specialized cache mechanism. If the

  - gpu-specific backend does not implement a specialized cache, then we will fallback to

  - the generic cache mechanism. Users can optionally force the generic cache mechanism or

  - disable ipc caching entirely.

  - generic - use the cache mechanism in the generic layer

  - specialized - use the cache mechanism in a gpu-specific mpl layer (if applicable)

  - disabled - disable caching completely

- **Default:** specialized

MPIR\_CVAR\_CH4\_IPC\_GPU\_P2P\_THRESHOLD
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_IPC\_GPU\_P2P\_THRESHOLD

  - MPICH\_CH4\_IPC\_GPU\_P2P\_THRESHOLD

- **Description**: If a send message size is greater than or equal to MPIR\_CVAR\_CH4\_IPC\_GPU\_P2P\_THRESHOLD (in bytes), then enable GPU-based single copy protocol for intranode communication. The environment variable is valid only when then GPU IPC shmmod is enabled.

- **Default:** (16 \* 1024)

MPIR\_CVAR\_CH4\_IPC\_GPU\_FAST\_COPY\_MAX\_SIZE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_IPC\_GPU\_FAST\_COPY\_MAX\_SIZE

  - MPICH\_CH4\_IPC\_GPU\_FAST\_COPY\_MAX\_SIZE

- **Description**: If a send message size is less than or equal to MPIR\_CVAR\_CH4\_IPC\_GPU\_FAST\_COPY\_MAX\_SIZE (in bytes), then enable GPU-basedfast memcpy. The environment variable is valid only when then GPU IPC shmmod is enabled.

- **Default:** 1024

MPIR\_CVAR\_CH4\_IPC\_ZE\_SHAREABLE\_HANDLE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_IPC\_ZE\_SHAREABLE\_HANDLE

  - MPICH\_CH4\_IPC\_ZE\_SHAREABLE\_HANDLE

- **Description**: Variable to select implementation for ZE shareable IPC handle

  - pidfd - use pidfd\_getfd syscall to implement shareable IPC handle

  - drmfd - force to use device fd-based shareable IPC handle

- **Default:** drmfd

MPIR\_CVAR\_CH4\_IPC\_GPU\_ENGINE\_TYPE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_IPC\_GPU\_ENGINE\_TYPE

  - MPICH\_CH4\_IPC\_GPU\_ENGINE\_TYPE

- **Description**: By default, select engine type automatically

  - auto - select automatically

  - compute - use compute engine

  - copy\_high\_bandwidth - use high-bandwidth copy engine

  - copy\_low\_latency - use low-latency copy engine

- **Default:** auto

MPIR\_CVAR\_CH4\_IPC\_GPU\_READ\_WRITE\_PROTOCOL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_IPC\_GPU\_READ\_WRITE\_PROTOCOL

  - MPICH\_CH4\_IPC\_GPU\_READ\_WRITE\_PROTOCOL

- **Description**: By default, use read protocol.

  - auto - select automatically

  - read - use read protocol

  - write - use write protocol if remote device is visible

- **Default:** read

MPIR\_CVAR\_CH4\_IPC\_GPU\_RMA\_ENGINE\_TYPE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_IPC\_GPU\_RMA\_ENGINE\_TYPE

  - MPICH\_CH4\_IPC\_GPU\_RMA\_ENGINE\_TYPE

- **Description**: By default, select engine type automatically

  - yaksa - don't select, use yaksa

  - auto - select automatically

  - compute - use compute engine

  - copy\_high\_bandwidth - use high-bandwidth copy engine

  - copy\_low\_latency - use low-latency copy engine

- **Default:** auto

MPIR\_CVAR\_CH4\_IPC\_CMA\_ENABLE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_IPC\_CMA\_ENABLE

  - MPICH\_CH4\_IPC\_CMA\_ENABLE

- **Description**: To manually disable MVAPICH CMA designs, set to 0. This CVAR is valid only when the CMA submodule is enabled.

- **Default:** 1

MPIR\_CVAR\_CH4\_IPC\_CMA\_P2P\_THRESHOLD
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_IPC\_CMA\_P2P\_THRESHOLD

  - MPICH\_CH4\_IPC\_CMA\_P2P\_THRESHOLD

- **Description**: If a send message size is greater than or equal to MPIR\_CVAR\_CH4\_CMA\_P2P\_THRESHOLD (in bytes), then enable CMA-based read/write based protocol for intra-node communication. At this time, only CMA read based operations are supported. This CVAR is valid only when the CMA submodule is enabled.

- **Default:** 16384

MPIR\_CVAR\_CH4\_IPC\_RNDV\_PROTOCOL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_IPC\_RNDV\_PROTOCOL

  - MPICH\_CH4\_IPC\_RNDV\_PROTOCOL

- **Description**: Variable to select the RNDV protocol.

  - coop    - RNDV COOP Protocol

  - rget    - RNDV RGET Protocol

  - rput    - RNDV RPUT Protocol

- **Default:** coop

MPIR\_CVAR\_CH4\_IPC\_MAP\_REPEAT\_ADDR
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_IPC\_MAP\_REPEAT\_ADDR

  - MPICH\_CH4\_IPC\_MAP\_REPEAT\_ADDR

- **Description**: If an address is used more than once in the last ten send operations, map it for IPC use even if it is below the IPC threshold.

- **Default:** true

MPIR\_CVAR\_CH4\_XPMEM\_ENABLE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_XPMEM\_ENABLE

  - MPICH\_CH4\_XPMEM\_ENABLE

- **Description**: To manually disable XPMEM set to 0. The environment variable is valid only when the XPMEM submodule is enabled.

- **Default:** 1

MPIR\_CVAR\_CH4\_IPC\_XPMEM\_P2P\_THRESHOLD
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_IPC\_XPMEM\_P2P\_THRESHOLD

  - MPICH\_CH4\_IPC\_XPMEM\_P2P\_THRESHOLD

- **Description**: If a send message size is greater than or equal to MPIR\_CVAR\_CH4\_IPC\_XPMEM\_P2P\_THRESHOLD (in bytes), then enable XPMEM-based single copy protocol for intranode communication. The environment variable is valid only when the XPMEM submodule is enabled.

- **Default:** 16384

MPIR\_CVAR\_BCAST\_POSIX\_INTRA\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_BCAST\_POSIX\_INTRA\_ALGORITHM

  - MPICH\_BCAST\_POSIX\_INTRA\_ALGORITHM

- **Description**: Variable to select algorithm for intra-node bcast

  - mpir           - Fallback to MPIR collectives

  - release\_gather - Force shm optimized algo using release, gather primitives

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_CH4\_POSIX\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

  - ipc\_read - Uses read-based collective with ipc

- **Default:** auto

MPIR\_CVAR\_IBCAST\_POSIX\_INTRA\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IBCAST\_POSIX\_INTRA\_ALGORITHM

  - MPICH\_IBCAST\_POSIX\_INTRA\_ALGORITHM

- **Description**: Variable to select algorithm for intra-node bcast

  - mpir           - Fallback to MPIR collectives

  - release\_gather - Force shm optimized algo using release, gather primitives

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_CH4\_POSIX\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

- **Default:** auto

MPIR\_CVAR\_REDUCE\_POSIX\_INTRA\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_REDUCE\_POSIX\_INTRA\_ALGORITHM

  - MPICH\_REDUCE\_POSIX\_INTRA\_ALGORITHM

- **Description**: Variable to select algorithm for intra-node reduce

  - mpir           - Fallback to MPIR collectives

  - release\_gather - Force shm optimized algo using release, gather primitives

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_CH4\_POSIX\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

- **Default:** auto

MPIR\_CVAR\_IREDUCE\_POSIX\_INTRA\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_IREDUCE\_POSIX\_INTRA\_ALGORITHM

  - MPICH\_IREDUCE\_POSIX\_INTRA\_ALGORITHM

- **Description**: Variable to select algorithm for intra-node reduce

  - mpir           - Fallback to MPIR collectives

  - release\_gather - Force shm optimized algo using release, gather primitives

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_CH4\_POSIX\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

- **Default:** auto

MPIR\_CVAR\_ALLREDUCE\_POSIX\_INTRA\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ALLREDUCE\_POSIX\_INTRA\_ALGORITHM

  - MPICH\_ALLREDUCE\_POSIX\_INTRA\_ALGORITHM

- **Description**: Variable to select algorithm for intra-node allreduce

  - mpir           - Fallback to MPIR collectives

  - release\_gather - Force shm optimized algo using release, gather primitives

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_CH4\_POSIX\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

- **Default:** auto

MPIR\_CVAR\_BARRIER\_POSIX\_INTRA\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_BARRIER\_POSIX\_INTRA\_ALGORITHM

  - MPICH\_BARRIER\_POSIX\_INTRA\_ALGORITHM

- **Description**: Variable to select algorithm for intra-node barrier

  - mpir           - Fallback to MPIR collectives

  - release\_gather - Force shm optimized algo using release, gather primitives

  - auto - Internal algorithm selection (can be overridden with MPIR\_CVAR\_CH4\_POSIX\_COLL\_SELECTION\_TUNING\_JSON\_FILE)

- **Default:** auto

MPIR\_CVAR\_ALLTOALL\_POSIX\_INTRA\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ALLTOALL\_POSIX\_INTRA\_ALGORITHM

  - MPICH\_ALLTOALL\_POSIX\_INTRA\_ALGORITHM

- **Description**: Variable to select algorithm for intra-node alltoall

  - mpir           - Fallback to MPIR collectives (default)

  - ipc\_read    - Uses read-based collective with ipc

- **Default:** mpir

MPIR\_CVAR\_ALLGATHER\_POSIX\_INTRA\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ALLGATHER\_POSIX\_INTRA\_ALGORITHM

  - MPICH\_ALLGATHER\_POSIX\_INTRA\_ALGORITHM

- **Description**: Variable to select algorithm for intra-node allgather

  - mpir        - Fallback to MPIR collectives (default)

  - ipc\_read    - Uses read-based collective with ipc

- **Default:** mpir

MPIR\_CVAR\_ALLGATHERV\_POSIX\_INTRA\_ALGORITHM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ALLGATHERV\_POSIX\_INTRA\_ALGORITHM

  - MPICH\_ALLGATHERV\_POSIX\_INTRA\_ALGORITHM

- **Description**: Variable to select algorithm for intra-node allgatherv

  - mpir        - Fallback to MPIR collectives (default)

  - ipc\_read    - Uses read-based collective with ipc

- **Default:** mpir

MPIR\_CVAR\_POSIX\_POLL\_FREQUENCY
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_POSIX\_POLL\_FREQUENCY

  - MPICH\_POSIX\_POLL\_FREQUENCY

- **Description**: This cvar sets the number of loops before the yield function is called.  A value of 0 disables yielding.

- **Default:** 1000

MPIR\_CVAR\_BCAST\_IPC\_READ\_MSG\_SIZE\_THRESHOLD
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_BCAST\_IPC\_READ\_MSG\_SIZE\_THRESHOLD

  - MPICH\_BCAST\_IPC\_READ\_MSG\_SIZE\_THRESHOLD

- **Description**: Use gpu ipc read bcast only when the message size is larger than this threshold.

- **Default:** 256

MPIR\_CVAR\_ALLTOALL\_IPC\_READ\_MSG\_SIZE\_THRESHOLD
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ALLTOALL\_IPC\_READ\_MSG\_SIZE\_THRESHOLD

  - MPICH\_ALLTOALL\_IPC\_READ\_MSG\_SIZE\_THRESHOLD

- **Description**: Use gpu ipc read alltoall only when the message size is larger than this threshold.

- **Default:** 256

MPIR\_CVAR\_ALLGATHER\_IPC\_READ\_MSG\_SIZE\_THRESHOLD
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ALLGATHER\_IPC\_READ\_MSG\_SIZE\_THRESHOLD

  - MPICH\_ALLGATHER\_IPC\_READ\_MSG\_SIZE\_THRESHOLD

- **Description**: Use gpu ipc read allgather only when the message size is larger than this threshold.

- **Default:** 256

MPIR\_CVAR\_ALLGATHERV\_IPC\_READ\_MSG\_SIZE\_THRESHOLD
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ALLGATHERV\_IPC\_READ\_MSG\_SIZE\_THRESHOLD

  - MPICH\_ALLGATHERV\_IPC\_READ\_MSG\_SIZE\_THRESHOLD

- **Description**: Use gpu ipc read allgatherv only when the message size is larger than this threshold.

- **Default:** 256

MPIR\_CVAR\_POSIX\_NUM\_COLLS\_THRESHOLD
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_POSIX\_NUM\_COLLS\_THRESHOLD

  - MPICH\_POSIX\_NUM\_COLLS\_THRESHOLD

- **Description**: Use posix optimized collectives (release\_gather) only when the total number of Bcast, Reduce, Barrier, and Allreduce calls on the node level communicator is more than this threshold.

- **Default:** 5

MPIR\_CVAR\_CH4\_SHM\_POSIX\_EAGER
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_SHM\_POSIX\_EAGER

  - MPICH\_CH4\_SHM\_POSIX\_EAGER

- **Description**: If non-empty, this cvar specifies which shm posix eager module to use

- **Default:**

MPIR\_CVAR\_CH4\_POSIX\_COLL\_SELECTION\_TUNING\_JSON\_FILE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_POSIX\_COLL\_SELECTION\_TUNING\_JSON\_FILE

  - MPICH\_CH4\_POSIX\_COLL\_SELECTION\_TUNING\_JSON\_FILE

- **Description**: Defines the location of tuning file.

- **Default:**

MPIR\_CVAR\_CH4\_POSIX\_COLL\_SELECTION\_TUNING\_JSON\_FILE\_GPU
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_POSIX\_COLL\_SELECTION\_TUNING\_JSON\_FILE\_GPU

  - MPICH\_CH4\_POSIX\_COLL\_SELECTION\_TUNING\_JSON\_FILE\_GPU

- **Description**: Defines the location of tuning file for GPU.

- **Default:**

MPIR\_CVAR\_CH4\_SHM\_POSIX\_TOPO\_ENABLE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_SHM\_POSIX\_TOPO\_ENABLE

  - MPICH\_CH4\_SHM\_POSIX\_TOPO\_ENABLE

- **Description**: Controls topology-aware communication in POSIX.

- **Default:** false

MPIR\_CVAR\_CH4\_SHM\_POSIX\_IQUEUE\_NUM\_CELLS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_SHM\_POSIX\_IQUEUE\_NUM\_CELLS

  - MPICH\_CH4\_SHM\_POSIX\_IQUEUE\_NUM\_CELLS

- **Description**: The number of cells used for the depth of the iqueue.

- **Default:** 64

MPIR\_CVAR\_CH4\_SHM\_POSIX\_IQUEUE\_CELL\_SIZE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_SHM\_POSIX\_IQUEUE\_CELL\_SIZE

  - MPICH\_CH4\_SHM\_POSIX\_IQUEUE\_CELL\_SIZE

- **Description**: Size of each cell.

- **Default:** 16384

MPIR\_CVAR\_COLL\_SHM\_LIMIT\_PER\_NODE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_COLL\_SHM\_LIMIT\_PER\_NODE

  - MPICH\_COLL\_SHM\_LIMIT\_PER\_NODE

- **Description**: Maximum shared memory created per node for optimized intra-node collectives (in KB)

- **Default:** 65536

MPIR\_CVAR\_BCAST\_INTRANODE\_BUFFER\_TOTAL\_SIZE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_BCAST\_INTRANODE\_BUFFER\_TOTAL\_SIZE

  - MPICH\_BCAST\_INTRANODE\_BUFFER\_TOTAL\_SIZE

- **Description**: Total size of the bcast buffer (in bytes)

- **Default:** 32768

MPIR\_CVAR\_BCAST\_INTRANODE\_NUM\_CELLS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_BCAST\_INTRANODE\_NUM\_CELLS

  - MPICH\_BCAST\_INTRANODE\_NUM\_CELLS

- **Description**: Number of cells the bcast buffer is divided into

- **Default:** 4

MPIR\_CVAR\_REDUCE\_INTRANODE\_BUFFER\_TOTAL\_SIZE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_REDUCE\_INTRANODE\_BUFFER\_TOTAL\_SIZE

  - MPICH\_REDUCE\_INTRANODE\_BUFFER\_TOTAL\_SIZE

- **Description**: Total size of the reduce buffer per rank (in bytes)

- **Default:** 32768

MPIR\_CVAR\_REDUCE\_INTRANODE\_NUM\_CELLS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_REDUCE\_INTRANODE\_NUM\_CELLS

  - MPICH\_REDUCE\_INTRANODE\_NUM\_CELLS

- **Description**: Number of cells the reduce buffer is divided into, for each rank

- **Default:** 4

MPIR\_CVAR\_BCAST\_INTRANODE\_TREE\_KVAL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_BCAST\_INTRANODE\_TREE\_KVAL

  - MPICH\_BCAST\_INTRANODE\_TREE\_KVAL

- **Description**: K value for the kary/knomial tree for intra-node bcast

- **Default:** 64

MPIR\_CVAR\_BCAST\_INTRANODE\_TREE\_TYPE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_BCAST\_INTRANODE\_TREE\_TYPE

  - MPICH\_BCAST\_INTRANODE\_TREE\_TYPE

- **Description**: Tree type for intra-node bcast tree kary      - kary tree type knomial\_1 - knomial\_1 tree type (ranks are added in order from the left side) knomial\_2 - knomial\_2 tree type (ranks are added in order from the right side) knomial\_2 is only supported with non topology aware trees.

- **Default:** kary

MPIR\_CVAR\_REDUCE\_INTRANODE\_TREE\_KVAL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_REDUCE\_INTRANODE\_TREE\_KVAL

  - MPICH\_REDUCE\_INTRANODE\_TREE\_KVAL

- **Description**: K value for the kary/knomial tree for intra-node reduce

- **Default:** 4

MPIR\_CVAR\_REDUCE\_INTRANODE\_TREE\_TYPE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_REDUCE\_INTRANODE\_TREE\_TYPE

  - MPICH\_REDUCE\_INTRANODE\_TREE\_TYPE

- **Description**: Tree type for intra-node reduce tree kary      - kary tree type knomial\_1 - knomial\_1 tree type (ranks are added in order from the left side) knomial\_2 - knomial\_2 tree type (ranks are added in order from the right side) knomial\_2 is only supported with non topology aware trees.

- **Default:** kary

MPIR\_CVAR\_ENABLE\_INTRANODE\_TOPOLOGY\_AWARE\_TREES
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ENABLE\_INTRANODE\_TOPOLOGY\_AWARE\_TREES

  - MPICH\_ENABLE\_INTRANODE\_TOPOLOGY\_AWARE\_TREES

- **Description**: Enable collective specific intra-node trees which leverage the memory hierarchy of a machine. Depends on hwloc to extract the binding information of each rank. Pick a leader rank per package (socket), then create a per\_package tree for ranks on a same package, package leaders tree for package leaders. For Bcast - Assemble the per\_package and package\_leaders tree in such a way that leaders interact among themselves first before interacting with package local ranks. Both the package\_leaders and per\_package trees are left skewed (children are added from left to right, first child to be added is the first one to be processed in traversal) For Reduce - Assemble the per\_package and package\_leaders tree in such a way that a leader rank interacts with its package local ranks first, then with the other package leaders. Both the per\_package and package\_leaders tree is right skewed (children are added in reverse order, first child to be added is the last one to be processed in traversal) The tree radix and tree type of package\_leaders and per\_package tree is MPIR\_CVAR\_BCAST{REDUCE}\_INTRANODE\_TREE\_KVAL and MPIR\_CVAR\_BCAST{REDUCE}\_INTRANODE\_TREE\_TYPE respectively for bast and reduce. But of as now topology aware trees are only kary and knomial\_1. knomial\_2 is not implemented.

- **Default:** 1

MPIR\_CVAR\_BARRIER\_COMPOSITION
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_BARRIER\_COMPOSITION

  - MPICH\_BARRIER\_COMPOSITION

- **Description**: Select composition (inter\_node + intra\_node) for Barrier 0 Auto selection 1 NM + SHM 2 NM only

- **Default:** 0

MPIR\_CVAR\_BCAST\_COMPOSITION
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_BCAST\_COMPOSITION

  - MPICH\_BCAST\_COMPOSITION

- **Description**: Select composition (inter\_node + intra\_node) for Bcast 0 Auto selection 1 NM + SHM with explicit send-recv between rank 0 and root 2 NM + SHM without the explicit send-recv 3 NM only

- **Default:** 0

MPIR\_CVAR\_ALLREDUCE\_COMPOSITION
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ALLREDUCE\_COMPOSITION

  - MPICH\_ALLREDUCE\_COMPOSITION

- **Description**: Select composition (inter\_node + intra\_node) for Allreduce 0 Auto selection 1 NM + SHM with reduce + bcast 2 NM only composition 3 SHM only composition 4 Multi leaders based inter node + intra node composition

- **Default:** 0

MPIR\_CVAR\_ALLGATHER\_COMPOSITION
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ALLGATHER\_COMPOSITION

  - MPICH\_ALLGATHER\_COMPOSITION

- **Description**: Select composition (inter\_node + intra\_node) for Allgather 0 Auto selection 1 Multi leaders based inter node + intra node composition 2 NM only composition

- **Default:** 0

MPIR\_CVAR\_ALLTOALL\_COMPOSITION
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ALLTOALL\_COMPOSITION

  - MPICH\_ALLTOALL\_COMPOSITION

- **Description**: Select composition (inter\_node + intra\_node) for Alltoall 0 Auto selection 1 Multi leaders based inter node + intra node composition 2 NM only composition

- **Default:** 0

MPIR\_CVAR\_REDUCE\_COMPOSITION
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_REDUCE\_COMPOSITION

  - MPICH\_REDUCE\_COMPOSITION

- **Description**: Select composition (inter\_node + intra\_node) for Reduce 0 Auto selection 1 NM + SHM with explicit send-recv between rank 0 and root 2 NM + SHM without the explicit send-recv 3 NM only

- **Default:** 0

MPIR\_CVAR\_ALLTOALL\_SHM\_PER\_RANK
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ALLTOALL\_SHM\_PER\_RANK

  - MPICH\_ALLTOALL\_SHM\_PER\_RANK

- **Description**: Shared memory region per rank for multi-leaders based composition for MPI\_Alltoall (in bytes)

- **Default:** 4096

MPIR\_CVAR\_ALLGATHER\_SHM\_PER\_RANK
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ALLGATHER\_SHM\_PER\_RANK

  - MPICH\_ALLGATHER\_SHM\_PER\_RANK

- **Description**: Shared memory region per rank for multi-leaders based composition for MPI\_Allgather (in bytes)

- **Default:** 4096

MPIR\_CVAR\_NUM\_MULTI\_LEADS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_NUM\_MULTI\_LEADS

  - MPICH\_NUM\_MULTI\_LEADS

- **Description**: Number of leader ranks per node to be used for multi-leaders based collective algorithms

- **Default:** 4

MPIR\_CVAR\_ALLREDUCE\_SHM\_PER\_LEADER
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ALLREDUCE\_SHM\_PER\_LEADER

  - MPICH\_ALLREDUCE\_SHM\_PER\_LEADER

- **Description**: Shared memory region per node-leader for multi-leaders based composition for MPI\_Allreduce (in bytes) If it is undefined by the user, it is set to the message size of the first call to the algorithm. Max shared memory size is limited to 4MB.

- **Default:** -1

MPIR\_CVAR\_ALLREDUCE\_CACHE\_PER\_LEADER
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ALLREDUCE\_CACHE\_PER\_LEADER

  - MPICH\_ALLREDUCE\_CACHE\_PER\_LEADER

- **Description**: Amount of data reduced in allreduce delta composition's reduce local step (in bytes). Smaller msg size per leader avoids cache misses and improves performance. Experiments indicate 512 to be the best value.

- **Default:** 512

MPIR\_CVAR\_ALLREDUCE\_LOCAL\_COPY\_OFFSETS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ALLREDUCE\_LOCAL\_COPY\_OFFSETS

  - MPICH\_ALLREDUCE\_LOCAL\_COPY\_OFFSETS

- **Description**: number of offsets in the allreduce delta composition's local copy The value of 2 performed the best in our 2 NIC test cases.

- **Default:** 2

MPIR\_CVAR\_CH4\_NETMOD
~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_NETMOD

  - MPICH\_CH4\_NETMOD

- **Description**: If non-empty, this cvar specifies which network module to use

- **Default:**

MPIR\_CVAR\_CH4\_SHM
~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_SHM

  - MPICH\_CH4\_SHM

- **Description**: If non-empty, this cvar specifies which shm module to use

- **Default:**

MPIR\_CVAR\_CH4\_ROOTS\_ONLY\_PMI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_ROOTS\_ONLY\_PMI

  - MPICH\_CH4\_ROOTS\_ONLY\_PMI

- **Description**: Enables an optimized business card exchange over PMI for node root processes only.

- **Default:** false

MPIR\_CVAR\_CH4\_RUNTIME\_CONF\_DEBUG
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_RUNTIME\_CONF\_DEBUG

  - MPICH\_CH4\_RUNTIME\_CONF\_DEBUG

- **Description**: If enabled, CH4-level runtime configurations are printed out

- **Default:** false

MPIR\_CVAR\_CH4\_MT\_MODEL
~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_MT\_MODEL

  - MPICH\_CH4\_MT\_MODEL

- **Description**: Specifies the CH4 multi-threading model. Possible values are: direct (default) lockless

- **Default:**

MPIR\_CVAR\_CH4\_NUM\_VCIS
~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_NUM\_VCIS

  - MPICH\_CH4\_NUM\_VCIS

- **Description**: Sets the number of VCIs to be implicitly used (should be a subset of MPIDI\_CH4\_MAX\_VCIS).

- **Default:** 1

MPIR\_CVAR\_CH4\_RESERVE\_VCIS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_RESERVE\_VCIS

  - MPICH\_CH4\_RESERVE\_VCIS

- **Description**: Sets the number of VCIs that user can explicitly allocate (should be a subset of MPIDI\_CH4\_MAX\_VCIS).

- **Default:** 0

MPIR\_CVAR\_CH4\_COLL\_SELECTION\_TUNING\_JSON\_FILE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_COLL\_SELECTION\_TUNING\_JSON\_FILE

  - MPICH\_CH4\_COLL\_SELECTION\_TUNING\_JSON\_FILE

- **Description**: Defines the location of tuning file.

- **Default:**

MPIR\_CVAR\_CH4\_COLL\_SELECTION\_TUNING\_JSON\_FILE\_GPU
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_COLL\_SELECTION\_TUNING\_JSON\_FILE\_GPU

  - MPICH\_CH4\_COLL\_SELECTION\_TUNING\_JSON\_FILE\_GPU

- **Description**: Defines the location of tuning file for GPU.

- **Default:**

MPIR\_CVAR\_CH4\_IOV\_DENSITY\_MIN
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_IOV\_DENSITY\_MIN

  - MPICH\_CH4\_IOV\_DENSITY\_MIN

- **Description**: Defines the threshold of high-density datatype. The density is calculated by (datatype\_size / datatype\_num\_contig\_blocks).

- **Default:** 16384

MPIR\_CVAR\_CH4\_PACK\_BUFFER\_SIZE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_PACK\_BUFFER\_SIZE

  - MPICH\_CH4\_PACK\_BUFFER\_SIZE

- **Description**: Specifies the number of buffers for packing/unpacking active messages in each block of the pool. The size here should be greater or equal to the max of the eager buffer limit of SHM and NETMOD.

- **Default:** 16384

MPIR\_CVAR\_CH4\_NUM\_PACK\_BUFFERS\_PER\_CHUNK
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_NUM\_PACK\_BUFFERS\_PER\_CHUNK

  - MPICH\_CH4\_NUM\_PACK\_BUFFERS\_PER\_CHUNK

- **Description**: Specifies the number of buffers for packing/unpacking active messages in each block of the pool.

- **Default:** 64

MPIR\_CVAR\_CH4\_MAX\_NUM\_PACK\_BUFFERS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_MAX\_NUM\_PACK\_BUFFERS

  - MPICH\_CH4\_MAX\_NUM\_PACK\_BUFFERS

- **Description**: Specifies the max number of buffers for packing/unpacking buffers in the pool. Use 0 for unlimited.

- **Default:** 0

MPIR\_CVAR\_CH4\_GPU\_COLL\_SWAP\_BUFFER\_SZ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_GPU\_COLL\_SWAP\_BUFFER\_SZ

  - MPICH\_CH4\_GPU\_COLL\_SWAP\_BUFFER\_SZ

- **Description**: Specifies the buffer size (in bytes) for GPU collectives data transfer.

- **Default:** 1048576

MPIR\_CVAR\_CH4\_GPU\_COLL\_NUM\_BUFFERS\_PER\_CHUNK
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_GPU\_COLL\_NUM\_BUFFERS\_PER\_CHUNK

  - MPICH\_CH4\_GPU\_COLL\_NUM\_BUFFERS\_PER\_CHUNK

- **Description**: Specifies the number of buffers for GPU collectives data transfer in each block/chunk of the pool.

- **Default:** 1

MPIR\_CVAR\_CH4\_GPU\_COLL\_MAX\_NUM\_BUFFERS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_GPU\_COLL\_MAX\_NUM\_BUFFERS

  - MPICH\_CH4\_GPU\_COLL\_MAX\_NUM\_BUFFERS

- **Description**: Specifies the total number of buffers for GPU collectives data transfer.

- **Default:** 256

MPIR\_CVAR\_CH4\_GLOBAL\_PROGRESS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_GLOBAL\_PROGRESS

  - MPICH\_CH4\_GLOBAL\_PROGRESS

- **Description**: If on, poll global progress every once a while. With per-vci configuration, turning global progress off may improve the threading performance.

- **Default:** 1

MPIR\_CVAR\_CH4\_COMM\_CONNECT\_TIMEOUT
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_COMM\_CONNECT\_TIMEOUT

  - MPICH\_CH4\_COMM\_CONNECT\_TIMEOUT

- **Description**: The default time out period in seconds for a connection attempt to the server communicator where the named port exists but no pending accept. User can change the value for a specified connection through its info argument.

- **Default:** 180

MPIR\_CVAR\_CH4\_ENABLE\_STREAM\_WORKQ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_ENABLE\_STREAM\_WORKQ

  - MPICH\_CH4\_ENABLE\_STREAM\_WORKQ

- **Description**: Enable stream enqueue operations via stream work queue. Requires progress thread on the corresponding MPIX stream. Reference: MPIX\_Stream\_progress and MPIX\_Start\_progress\_thread.

- **Default:** false

MPIR\_CVAR\_CH4\_RMA\_MEM\_EFFICIENT
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_RMA\_MEM\_EFFICIENT

  - MPICH\_CH4\_RMA\_MEM\_EFFICIENT

- **Description**: If true, memory-saving mode is on, per-target object is released at the epoch end call. If false, performance-efficient mode is on, all allocated target objects are cached and freed at win\_finalize.

- **Default:** false

MPIR\_CVAR\_CH4\_RMA\_ENABLE\_DYNAMIC\_AM\_PROGRESS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_RMA\_ENABLE\_DYNAMIC\_AM\_PROGRESS

  - MPICH\_CH4\_RMA\_ENABLE\_DYNAMIC\_AM\_PROGRESS

- **Description**: If true, allows RMA synchronization calls to dynamically reduce the frequency of internal progress polling for incoming RMA active messages received on the target process. The RMA synchronization call initially polls progress with a low frequency (defined by MPIR\_CVAR\_CH4\_RMA\_AM\_PROGRESS\_LOW\_FREQ\_INTERVAL) to reduce synchronization overhead. Once any RMA active message has been received, it will always poll progress once at every synchronization call to ensure prompt target-side progress. Effective only for passive target synchronization MPI\_Win\_flush{\_all} and MPI\_Win\_flush\_local{\_all}.

- **Default:** false

MPIR\_CVAR\_CH4\_RMA\_AM\_PROGRESS\_INTERVAL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_RMA\_AM\_PROGRESS\_INTERVAL

  - MPICH\_CH4\_RMA\_AM\_PROGRESS\_INTERVAL

- **Description**: Specifies a static interval of progress polling for incoming RMA active messages received on the target process. Effective only for passive-target synchronization MPI\_Win\_flush{\_all} and MPI\_Win\_flush\_local{\_all}. Interval indicates the number of performed flush calls before polling. It is counted globally across all windows. Invalid when MPIR\_CVAR\_CH4\_RMA\_ENABLE\_DYNAMIC\_AM\_PROGRESS is true.

- **Default:** 1

MPIR\_CVAR\_CH4\_RMA\_AM\_PROGRESS\_LOW\_FREQ\_INTERVAL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_CH4\_RMA\_AM\_PROGRESS\_LOW\_FREQ\_INTERVAL

  - MPICH\_CH4\_RMA\_AM\_PROGRESS\_LOW\_FREQ\_INTERVAL

- **Description**: Specifies the interval of progress polling with low frequency for incoming RMA active message received on the target process. Effective only for passive-target synchronization MPI\_Win\_flush{\_all} and MPI\_Win\_flush\_local{\_all}. Interval indicates the number of performed flush calls before polling. It is counted globally across all windows. Used when MPIR\_CVAR\_CH4\_RMA\_ENABLE\_DYNAMIC\_AM\_PROGRESS is true.

- **Default:** 100

MPIR\_CVAR\_GENQ\_SHMEM\_POOL\_FREE\_QUEUE\_SENDER\_SIDE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_GENQ\_SHMEM\_POOL\_FREE\_QUEUE\_SENDER\_SIDE

  - MPICH\_GENQ\_SHMEM\_POOL\_FREE\_QUEUE\_SENDER\_SIDE

- **Description**: The genq shmem code allocates pools of cells on each process and, when needed, a cell is removed from the pool and passed to another process. This can happen by either removing a cell from the pool of the sending process or from the pool of the receiving process. This CVAR determines which pool to use. If true, the cell will come from the sender-side. If false, the cell will com from the receiver-side. There are specific advantages of using receiver-side cells when combined with the "avx" fast configure option, which allows MPICH to use AVX streaming copy intrintrinsics, when available, to avoid polluting the cache of the sender with the data being copied to the receiver. Using receiver-side cells does have the trade-off of requiring an MPMC lock for the free queue rather than an MPSC lock, which is used for sender-side cells. Initial performance analysis shows that using the MPMC lock in this case had no significant performance loss. By default, the queue will continue to use sender-side queues until the performance impact is verified.

- **Default:** true

MPIR\_CVAR\_ENABLE\_HCOLL
~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ENABLE\_HCOLL

  - MPICH\_ENABLE\_HCOLL

- **Description**: Enable hcoll collective support.

- **Default:** false

MPIR\_CVAR\_COLL\_SCHED\_DUMP
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_COLL\_SCHED\_DUMP

  - MPICH\_COLL\_SCHED\_DUMP

- **Description**: Print schedule data for nonblocking collective operations.

- **Default:** false

MPIR\_CVAR\_SHM\_RANDOM\_ADDR\_RETRY
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_SHM\_RANDOM\_ADDR\_RETRY

  - MPICH\_SHM\_RANDOM\_ADDR\_RETRY

- **Description**: The default number of retries for generating a random address. A retrying involves only local operations.

- **Default:** 100

MPIR\_CVAR\_SHM\_SYMHEAP\_RETRY
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_SHM\_SYMHEAP\_RETRY

  - MPICH\_SHM\_SYMHEAP\_RETRY

- **Description**: The default number of retries for allocating a symmetric heap in shared memory. A retrying involves collective communication over the group in the shared memory.

- **Default:** 100

MPIR\_CVAR\_ENABLE\_HEAVY\_YIELD
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Aliases:**

  - MVP\_ENABLE\_HEAVY\_YIELD

  - MPICH\_ENABLE\_HEAVY\_YIELD

- **Description**: If enabled, use nanosleep to ensure other threads have a chance to grab the lock. Note: this may not work with some thread runtimes, e.g. non-preemptive user-level threads.

- **Default:** 0
