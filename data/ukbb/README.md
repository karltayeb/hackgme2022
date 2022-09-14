This folder contains a script for downloading summary stats from UK Biobank
`python3 request_ukbb.py {search}`

Where `search` is a keyword to search for. For example, a phenotype code. The script will find lines in `ukbb_manfisest.tsv` that match the search term, and prompt you to pick one to download. If it has not already been downloaded, it will download the summary statistics to a subdirectory named by `Phenotype Code`

This is just meant to speed things up a bit, and to make sure multiple teams aren't downloading the same data multiple times.


Useful links for exploring UKBB:

UKBB showcase: https://biobank.ndph.ox.ac.uk/showcase/ 
UKBB Manifest: https://docs.google.com/spreadsheets/d/1kvPoupSzsSFBNSztMzl04xMoSC3Kcx3CrjVf4yBmESU/edit#gid=227859291
Neale Lab UKBB webiste: http://www.nealelab.is/uk-biobank