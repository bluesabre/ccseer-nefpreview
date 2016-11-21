#!/usr/bin/env python
# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
#   ccseer-nefpreview - NEF Previewer for Seer
#   Copyright (C) 2016 Sean Davis <smd.seandavis@gmail.com>
#
#   This program is free software: you can redistribute it and/or modify it
#   under the terms of the GNU General Public License version 3, as published
#   by the Free Software Foundation.
#
#   This program is distributed in the hope that it will be useful, but
#   WITHOUT ANY WARRANTY; without even the implied warranties of
#   MERCHANTABILITY, SATISFACTORY QUALITY, or FITNESS FOR A PARTICULAR
#   PURPOSE.  See the GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License along
#   with this program.  If not, see <http://www.gnu.org/licenses/>.


import rawpy
import imageio
import tempfile
import os

postprocessing = rawpy.Params(
    demosaic_algorithm=rawpy.DemosaicAlgorithm.LINEAR,
    use_camera_wb=True, use_auto_wb=False, user_wb=None,
    output_color=rawpy.ColorSpace.Adobe, output_bps=8,
    user_flip=None, user_black=None, user_sat=None,
    no_auto_bright=False, auto_bright_thr=None,
    adjust_maximum_thr=0.75,
    exp_shift=None, exp_preserve_highlights=0.0,
    gamma=None, bad_pixels_path=None)


def render(filename, output):
    raw = rawpy.imread(filename)
    rgb = raw.postprocess(postprocessing)
    imageio.imsave(output, rgb)


def usage(execname):
    print()
    print("RAW previewer -- plugin for the Seer app: "
          "http://sourceforge.net/projects/ccseer")
    print("----------------------------------------------------------")
    print("Usage: " + execname + " inputpath.nef outputpath")
    print()
    sys.exit()


if __name__ == '__main__':
    import getopt
    import sys

    execname = sys.argv[0]

    if len(sys.argv) < 3:
        usage(execname)

    try:
        opts, args = getopt.getopt(sys.argv[1:], 't:', )
    except getopt.GetoptError:
        usage(execname)

    if args.__len__() != 2:
        usage(execname)

    path_input = args[0]
    path_output = args[1].lower()
    if path_output.endswith('.jpg') is False:
        path_output = args[1] + '.jpg'

    render(path_input, path_output)
