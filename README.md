# abbreviations-latex

Contains a abbr.tex file containing all my used abbreviations in LaTeX.
The repo also contains an action where the abbr.tex file is read and sorted whenever a commit is pushed. 
The old abbr file is stored in the arxiv folder.

Put your files you wanna merge with the base abbr file in a folder "to-be-merged" in the root directory.
This action will automatically include the newly defined keys in the abbr file and clear the to-be-merged folder.
