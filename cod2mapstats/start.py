import os
import argparse
import yaml
import io

from sqlalchemy import create_engine
import numpy as np
import matplotlib.pyplot as plt
from numpy import genfromtxt
from matplotlib.colors import LogNorm
import matplotlib.image as mpimg
from PIL import Image

from .config import MAPS_PATH, DB_PATH, TABLE_NAME
from .utility import get_config, list_files, get_min_max


def get_data(map, gt=None):
    engine = create_engine('{}:///{}'.format('sqlite', DB_PATH))
    if gt is None:
        query = '''
            SELECT {}
            FROM {}
            WHERE map='{}'        
        '''.format(
            'x,y',
            TABLE_NAME,
            map
        )
    else:
        query = '''
            SELECT {}
            FROM {}
            WHERE map='{}'       
            AND gametype='{}';
        '''.format(
            'x,y',
            TABLE_NAME,
            map,
            gt
        )
    result = engine.execute(query)
    data = result.fetchall()
    return data
    
    
def add_image_conf(path, image, left, right, down, up):
    data = {
        image: {
            'left': left,
            'right': right,
            'down': down,
            'up': up
        }
    }
    with io.open(path, 'a', encoding='utf8') as outfile:
        yaml.dump(data, outfile, default_flow_style=False, allow_unicode=True)
    return 0


def get_bins(minimum, maximum, scale):
    return int((maximum-minimum)/scale)
    
    
def start():
    parser = argparse.ArgumentParser()
    
    # positional
    parser.add_argument('map', type=str, help='map name')
    
    # optional
    parser.add_argument('--images', action='store_true', help='list of all images for the map')
    parser.add_argument('--show', action='store_true', help='list of all images for the map')
    parser.add_argument('--bw', action='store_true', help='black&white image?')
    parser.add_argument('--gt', type=str, help='gametype')
    parser.add_argument('--bins', type=int, help='how much bins use')
    parser.add_argument('--alpha', type=float, default=0.45, help='alpha (from 0 to 1)')
    parser.add_argument('--dpi', type=int, default=200, help='dots per inch')
    parser.add_argument('--output', type=str, default='output.jpg', help='output file')
    parser.add_argument('--image', type=str, default='map1.jpg', help='custom map image')
    parser.add_argument('--title', type=str, default='Heatmap', help='custom image title')
    parser.add_argument('--cmap', type=str, default='jet', help='custom colormap')
    
    args = parser.parse_args()
    if args.images:
        map_dir = os.path.join(MAPS_PATH, args.map)
        images = list_files(map_dir, 'jpg', 'png')
        print(' '.join(images))
    else:
        print('loading data...')
        data = get_data(args.map, args.gt)
        xs = []
        ys = []
        for row in data:
            xs.append(row[0])
            ys.append(row[1])
        xmm = get_min_max(xs)
        ymm = get_min_max(ys)
        print('x min: {}, max: {}'.format(xmm[0], xmm[1]))
        print('y min: {}, max: {}'.format(ymm[0], ymm[1]))
        print('data loaded')
        
        print('loading image...')
        map_dir = os.path.join(MAPS_PATH, args.map)
        image_path = os.path.join(map_dir, args.image)
        if not os.path.isfile(image_path):
            print('* error! no image {} *'.format(image.path))
            return
        config_path = os.path.join(map_dir, 'config.yml')
        try:
            image_config = get_config(config_path)[args.image]
        except (FileNotFoundError, KeyError, TypeError) as e:
            print('no config for the image. creating from min and max values...')
            add_image_conf(config_path, args.image, xmm[0], xmm[1], ymm[0], ymm[1])
            image_config = get_config(config_path)[args.image]
        image_extent = (
            image_config['left'], 
            image_config['right'], 
            image_config['down'], 
            image_config['up']
        )
        if args.bw:
            image = np.asarray(Image.open(image_path).convert("L"))
            im_cmap = 'Greys_r'
        else:
            image = mpimg.imread(image_path)
            im_cmap = None
        fig, ax = plt.subplots()
        im = ax.imshow(image, extent=image_extent, cmap=im_cmap)
        print('image loaded')
        
        print('loading plot...')
        if args.bins is None:
            xbins = get_bins(xmm[0], xmm[1], 100)
            ybins = get_bins(ymm[0], ymm[1], 100)
            print('xbins: {}, ybins: {}'.format(xbins, ybins))
            bins = int((xbins+ybins)/2)
        else:
            bins = args.bins
        print('bins: {}'.format(bins))
        plt.hist2d(xs, ys, bins=bins, cmap=args.cmap, norm=LogNorm(), alpha=args.alpha)
        ax = plt.gca()
        plt.title(args.title)
        plt.colorbar()
        print('plot loaded')
        
        plt.savefig(args.output, dpi=args.dpi)
        print('picture saved')
        
        if args.show:
            try:
                plt.show()
            except KeyboardInterrupt:
                pass
        print('done')
    

if __name__ == '__main__':
    start()
