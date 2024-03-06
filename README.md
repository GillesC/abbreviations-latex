# abbreviations-latex

Contains a `abbr.tex` file containing all my used abbreviations in LaTeX.
The repo also contains an action where the `abbr.tex` file is read and sorted whenever a commit is pushed. 
The old abbr file is stored in the `arxiv` folder.

Put your files you wanna merge with the base abbr file in a folder "to-be-merged" in the root directory.
This action will automatically include the newly defined keys in the abbr file and clear the `to-be-merged` folder, i.e., all files are moved to the `arxiv` folder.


To use it in Overleaf:
- Github pull
- add your files 
- Github push
- wait till action is complete 
- Github pull

No longer need to run the Python file locally to merge files (`merge-abbr.py`).
The only downside is that the user is now unable to overwrite existing keys with the above-described procedure. If absolutely necessary, the abbreviations can still be manually changed in the abbr.tex, which after pushing, will be automatically sorted.
