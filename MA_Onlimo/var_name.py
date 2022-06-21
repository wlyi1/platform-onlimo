{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "28fc7bbe",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import datetime \n",
    "from datetime import datetime as dt\n",
    "\n",
    "sheet = list(range(41,45))\n",
    "filename = []\n",
    "varname = []\n",
    "for i in sheet:\n",
    "    filename.append('OL' + str(i) + '_2022.csv')\n",
    "    varname.append('OL' + str(i))\n",
    "    \n",
    "for df in varname:\n",
    "    globals()[f'{df}'] = pd.read_csv(f'{df}_2022.csv')    \n",
    "    globals()[f'{df}']['new_date'] = pd.to_datetime(globals()[f'{df}']['DATE'])\n",
    "    globals()[f'{df}']['tgl'] = pd.to_datetime(globals()[f'{df}']['DATE'] + ' ' + globals()[f'{df}']['TIME'])\n",
    "    globals()[f'pH_{df[2:]}'] = [x for x in globals()[f'{df}'][-24:]['pH']]\n",
    "    globals()[f'ab_pH_{df[2:]}'] = sum(map(lambda x : x<5 and x>9, globals()[f'pH_{df[2:]}']))\n",
    "    globals()[f'DO_{df[2:]}'] = [x for x in globals()[f'{df}'][-24:]['DO']]\n",
    "    globals()[f'ab_DO_{df[2:]}'] = sum(map(lambda x : x<1, globals()[f'DO_{df[2:]}']))\n",
    "    globals()[f'NH4_{df[2:]}'] = [x for x in globals()[f'{df}'][-24:]['NH4']]\n",
    "    globals()[f'ab_NH4_{df[2:]}'] = sum(map(lambda x : x>100, globals()[f'NH4_{df[2:]}']))\n",
    "    globals()[f'NO3_{df[2:]}'] = [x for x in globals()[f'{df}'][-24:]['NO3']]\n",
    "    globals()[f'ab_NO3_{df[2:]}'] = sum(map(lambda x : x>100, globals()[f'NO3_{df[2:]}']))\n",
    "    globals()[f'tgl_{df[2:]}'] = globals()[f'{df}']['tgl'].max().strftime((\"%Y-%m-%d %H:%M:%S\"))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
