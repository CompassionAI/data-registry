from datasets import load_dataset
from cai_garland.models.cai_nllb_tokenizer import CAINllbTokenizerFast

tokenizer = CAINllbTokenizerFast.from_pretrained("facebook/nllb-200-distilled-600M", src_lang="bod_Tibt", tgt_lang="eng_Latn")

datasets = load_dataset("../../../../garland/cai_garland/data/parallel_dataset_loader_hf.py", "raw_with_context")

lines = []
for split in datasets.keys():
    dataset = datasets[split]
    lines.extend([ex['english'] for ex in dataset])

tokenizer.make_remapping_file(lines, "champion_models/tokenizer-nllb-variants/en/token_remapping")
