# WBCHSE Result Finder

Finds data of WBCHSE students and saves in csv for analysis.

## Getting Started

Execute Check Valid Roll.py to generate list of valid rolls
Then execute WBCHSE Result Data.py to obtain results.

## Prerequisites

psutil
BeautifulSoup4

## Additional Functionality
To increase output, execute Check greater 2500.py and WBCHSE Result Data.py in order.


In order optimize time usage, the script only searches for roll numbers upto 2500 since it is rare to find schools with rolls exceeding that. To get a more accurate sample, run Check greater 2500.py to find roll numbers missed due to optimization and run the original script to find the data set again.
