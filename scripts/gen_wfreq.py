from pathlib import Path
import json
from wordfreq import word_frequency, top_n_list, iter_wordlist, get_frequency_dict
from typing import Dict

fpath = Path(__file__).resolve()
data_p = fpath.parent.parent / 'data'
lng = "es"
topwl = top_n_list(lng, 1000)
t1000_d: Dict[str, float] = {}

for w in topwl:
    wf = word_frequency(w,lng)
    t1000_d[w] = wf

with open(data_p / "wordfreq_top1000.json", "w") as f:
    json.dump(topwl, f)

with open(data_p / "wordfreq_top1000_withfreq.json", "w") as f:
    json.dump(t1000_d, f)