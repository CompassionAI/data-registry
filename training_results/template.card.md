# Template model training results card

Use the headline "Card: _model-name_".

Use this as a template to make cards for model training results. The file name is "_model-name_.card.md".

There should be a corresponding champion model added for the training run. Include the following boilerplate in the card header, without the blockquote:

> The general information on the model being trained is in the champion model card. Here we only have information specific to the training run.

## Champion model name (only if different)

Only include this if the champion model name is different from the name of the training run.

## Code links

Record the repo _and commit SHA_ here. For copying convenience, the commit SHA should be in a blockquote as follows:

> Commit SHA only, no period at the end

If possible, include the following links to Github:

- Driver file
- Config files/directory

## Execution steps (optional)

If the training run requires something more than running the driver with no arguments, write down the steps here. Include the exact shell commands inside Markdown code boxes. If there's a separate Markdown file, point to the file and include a Github link if you can (in the training run commit SHA).

If you can reproduce the training by running the driver with no arguments, include this here without the blockquote:

> Execute the training driver with no arguments.

## Hyperparameters

Record the hyperparameters for this run.

If all relevant information is recorded in the config files, include this here without the blockquote:

> The hyperparameters are in the config files.

If the hyperparameters were set from command line or hard-coded, record them here again (for convenience) even if they show up in the "Execution Steps" section.

If there were sweeps, briefly describe the sweep strategy and point to the configs and code. Otherwise, include this here without the blockquote:

> There was no sweeping.

## Champion selection

Describe how the champion was selected from the training run. If there is separate testing code, point to it here. Include a link to the Github page if you can.

## Additional comments (optional)

Serious real-world machine learning is very messy. This is a catch-all section for the mess.
