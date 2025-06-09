=============================
MVAPICH-Plus Dynamic-Tuning
=============================

    :Author: MVAPICH Team
    :Date: 2025/06/09


Using MVAPICH-Plus Dynamic-Tuning
-------------------------------------

MVAPICH-Plus 4.1 supports adaptive, dynamic collective algorithm selection. This process allows MVAPICH-Plus to dynamically adjust its collective algorithm selection over the course of an application run for the best performance on any systems. This feature is enabled by default but can be turned off by setting the CVAR :code:`MPIR_CVAR_ENABLE_DYNAMIC_TUNING=0`. Dynamic tuning can also be disabled for individual collectives by setting the relevant collective algorithm back to :code:`auto` instead of :code:`dynamic`

Other parameters for controlling the behavior of dynamic tuning include:

* :code:`MPIR_CVAR_DYNAMIC_TUNE_THRESHOLD` - the number of iterations before the dynamic tuning results are tested again (default 1000)
* :code:`MPIR_CVAR_DYNAMIC_TUNE_TEST_COUNT` - the number of tests performed during returning (default 5)
* :code:`MPIR_CVAR_DYNAMIC_TUNE_LOCAL_EVAL_METRIC` - the statistic reported by each process for a given collective algorithm (default avg)
* :code:`MPIR_CVAR_DYNAMIC_TUNE_SELECTION_METRIC` - the method used to select the best performing collective algorithm (default max)

