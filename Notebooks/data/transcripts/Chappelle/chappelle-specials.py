# %%
import pandas as pd
import numpy as np
import json

chappelle_df = pd.read_json(
    "/mnt/c/Users/prp12.000/github-repos/Binder/Notebooks/data/transcripts/Chappelle/Chappelle-Specials.json"
)
chappelle_df = chappelle_df[["value", "PSChildName"]]
chappelle_df
#%%
json_df = pd.DataFrame.to_json(chappelle_df, force_ascii=True)
json_df
# %%
df_string = pd.DataFrame.to_string(chappelle_df)
df_string
# %%
pd.DataFrame.describe(chappelle_df)

# %%
pd.DataFrame.to_csv(
    chappelle_df,
    path_or_buf="chappelle_data.csv",
    sep=",",
    encoding="utf-8",
    doublequote=True,
    escapechar="\\",
)

# %%
chappelle_df[0:110]
