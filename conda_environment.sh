conda config --add channels conda-forge
conda config --set channel_priority strict

# conda create -n test-tsdb-inserts python=3.7.4
conda create -n test-tsdb-inserts
conda activate test-tsdb-inserts
source activate test-tsdb-inserts

# conda install <package-name>
conda install requests
conda install numpy
conda install random
conda install time

