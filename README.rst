CoD2MapStats
============

With this packet you can analyze some stats on Call of Duty 2 maps. 

E.g. you can draw the death heatmap with `CoD2MapDeaths`_.

Notice: at this moment, there are only top 5 maps (in alphabet order) with configs. On other maps it will create config, but you should configure it.


Features
--------

* All stock Call of Duty 2 maps images from the top. Not mine, but looks good. Thx to all screeshots authors.
* Some settings, like black&white background, plot alpha, custom title, etc.
* Command-line interface. Use "cod2mapstats -h" to see all keys or look in 'Run' part.


Install
-------

Using virtualenv:

* python3 -m venv cod2mapstats
* cd cod2mapstats
* source bin/activate
* git clone https://github.com/lonsofore/cod2mapstats.git
* cd cod2mapstats
* python3 setup.py install


Configure
---------

Set up your config (maps path, db path, table name):

* Linux: '/home/username/.config/cod2mapstats/config.yml'
* Windows: 'C:\\Users\\username\\AppData\\Local\\Lonsofore\\cod2mapstats\\config.yml'
* Mac OS: '/Users/username/Library/Application Support/cod2mapstats/config.yml'


Run
---

Some info from the help (cod2mapstats -h):

===============  ===============================
             positional arguments
------------------------------------------------
    argument                 description
===============  ===============================
map              map name
===============  ===============================

===============  ===============================
              optional arguments
------------------------------------------------
    argument                 description
===============  ===============================
-h, --help       show this help message and exit
--images         list of all images for the map
--show           list of all images for the map
--bw             black&white image?
--gt GT          gametype
--bins BINS      how much bins use
--alpha ALPHA    alpha (from 0 to 1)
--dpi DPI        dots per inch
--output OUTPUT  output file
--image IMAGE    custom map image
--title TITLE    custom image title
--cmap CMAP      custom colormap
===============  ===============================

Example:

cod2mapstats mp_toujane --bw --gt tdm --output mp_toujane_heatmap.jpg --title Heatmap

  
Result
-------

Heatmap of deaths on Toujane (of all gametypes):

.. image:: https://raw.githubusercontent.com/Lonsofore/CoD2MapDeaths/master/heatmaps/mp_toujane.jpg


Support
-------

`Killtube.org`_


License
-------

Licensed under the Apache License, Version 2.0


.. _CoD2MapDeaths: https://github.com/Lonsofore/CoD2MapDeaths
.. _Killtube.org: https://killtube.org/showthread.php?3123-CoD2MapStats-Draw-your-stats-on-CoD2-maps&p=17605#post17605