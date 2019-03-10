#!/usr/bin/env python
# -*- coding: utf-8 -*-

import clasify

from train import Train

if __name__ == '__main__':
    Train.create_model()
    clasify.main()