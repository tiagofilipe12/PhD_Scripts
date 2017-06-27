#!/bin/sh
mafft --maxiterate 1000 --localpair $1 > "1aligned_" + $1
