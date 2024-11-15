=======================================
MVAPICH-Plus GPU Compression
=======================================

    :Author: MVAPICH Team
    :Date: 2024/11/13

.. contents::



1 Overview
----------

MVAPICH-Plus 4.0 supports compression for AMD and NVIDIA GPUs using the `zfp library <https://computing.llnl.gov/projects/zfp>`_.

2 Installation
--------------

The zfp library is shipped with the MVAPICH-Plus 4.0 RPMs.

3 Supported Architectures and Communication
-------------------------------------------

MVAPICH-PLUS 4.0 supports on-the-fly compression floating point and
double-precision data on the following GPU architectures:

3.1 NVIDIA CUDA GPUs
~~~~~~~~~~~~~~~~~~~~

- Tested on A100, GH200 SuperChip.

- Supports point-to-point operations.

- Supports Alltoall, Allgather, Reduce-Scatter and Allreduce.

- Supports multi-stream ZFP decode and encode.

3.2 AMD ROCm GPUs
~~~~~~~~~~~~~~~~~

- Tested on MI100, MI250x.

- Supports Alltoall and Allgather.

4 Runtime Configuration Settings
--------------------------------

Configuration is done via MVAPICH CVAR environment variables.  Please
read the `MVAPICH Environment Variables <https://mvapich-docs.readthedocs.io/en/latest/cvar.html>`_ documentation for details about
specific variables.

4.1 Compression
~~~~~~~~~~~~~~~

*Note: Point-to-point compression is only supported on NVIDIA CUDA GPUs.*

4.1.1 ZFP compression rate
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: sh

    export MPIR_CVAR_ZFP_RATE=8

Compression rate in bits/value, default is 16. Lower values are more
compressed but more lossy.

Ranges:

- 1-32 for float

- 1-64 for double

4.1.2 Set Compression Data Type
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: sh

    export MPIR_CVAR_COMPRESSION_DATA_TYPE=FLOAT

Values:

- DOUBLE

- FLOAT

4.2 Supported Communications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

4.2.1 Point-to-Point Compression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: sh

    export MPIR_CVAR_ENABLE_COMPRESSION=1
    export MPIR_CVAR_COMPRESSION_ALGORITHM=zfp
    export MPIR_CVAR_ENABLE_PT2PT_GPU_COMPRESSION=1

The threshold at which pt2pt compression is used can be controlled
with ``MPIR_CVAR_PT2PT_GPU_COMPRESSION_THRESHOLD`` (default 1MB).

The limit for pt2pt compression is controlled by
``MPIR_CVAR_COMPRESSION_BUFFER_SIZE`` (default 32MB).

Finally, the max number of ongoing pt2pt compressions is controlled by
 ``MPIR_CVAR_COMPRESSION_MAX_NUM_COMPRESSION_BUFFERS`` (default 64).

Note that the amount of GPU memory consumed by the MPI runtime is
affected by these parameters (i.e. higher parameter values means
higher consumption).

4.2.2 Alltoall Compression
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: sh

    export MPIR_CVAR_ENABLE_COMPRESSION=1
    export MPIR_CVAR_COMPRESSION_ALGORITHM=zfp
    export MPIR_CVAR_ALLTOALL_INTRA_ALGORITHM=osu_gpu_compression

4.2.3 Allgather Compression
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: sh

    export MPIR_CVAR_ENABLE_COMPRESSION=1
    export MPIR_CVAR_COMPRESSION_ALGORITHM=zfp
    export MPIR_CVAR_ALLGATHER_INTRA_ALGORITHM=osu_gpu_compression

4.2.4 Reduce-scatter Ring Compression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: sh

    export MPIR_CVAR_ENABLE_COMPRESSION=1
    export MPIR_CVAR_COMPRESSION_ALGORITHM=zfp
    export MPIR_CVAR_REDUCE_SCATTER_INTRA_ALGORITHM=osu_ring_compression

4.2.5 Allreduce Ring Compression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: sh

    export MPIR_CVAR_ENABLE_COMPRESSION=1
    export MPIR_CVAR_COMPRESSION_ALGORITHM=zfp
    export MPIR_CVAR_ALLREDUCE_INTRA_ALGORITHM=osu_ring_compression

4.2.6 Allreduce Recursive Doubling Compression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: sh

    export MPIR_CVAR_ENABLE_COMPRESSION=1
    export MPIR_CVAR_COMPRESSION_ALGORITHM=zfp
    export MPIR_CVAR_ALLREDUCE_INTRA_ALGORITHM=osu_rd_compression

4.3 Optimal Performance on AMD GPUs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

MVAPICH-Plus only supports Default-stream ZFP encoding and decoding
for AMD GPUs, therefore we recommend the following setting for
better performance:

.. code:: sh

    export MPIR_CVAR_COMPRESSION_NUM_STREAM=32
