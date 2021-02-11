# Merge the crews table to itself
crews_self_merged = crews.merge(crews, left_on='id', right_on='id', suffixes=('_dir', '_crew'))