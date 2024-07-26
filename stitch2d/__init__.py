"""Stitches a 2D grid of images into a mosaic"""
from .mosaic import Mosaic, StructuredMosaic, MemmapMosaic,  MemmapStructuredMosaic, create_mosaic, build_grid, is_grid
from .tile import Tile, OpenCVTile, ScikitImageTile, MemmapTile, MemmapOpenCVTile


__version__ = "1.2"
__author__ = "Adam Mansur"
__credits__ = "Smithsonian National Museum of Natural History"
