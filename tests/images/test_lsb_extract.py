
import logging
logging.basicConfig(level=logging.DEBUG,format='%(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

import tempfile
import os
import hashlib
import stegoveritas

SCRIPTDIR = os.path.dirname(os.path.realpath(__file__))

# lrtb == Left->Right Top->Bottom (Scan method)

def test_extract_red_0_lrtb():

    with tempfile.TemporaryDirectory() as tmpdirname:  
        args = [os.path.join(SCRIPTDIR, 'lsb_red_0.png'), '-out', tmpdirname, '-extractLSB', '-red', '0'] 
        veritas = stegoveritas.StegoVeritas(args=args)
        veritas.run()

        # Verify we're expecting that
        with open(os.path.join(tmpdirname, 'LSBExtracted.bin'),'rb') as f:
            assert hashlib.md5(f.read()).hexdigest() == '20ba8aa2da066e371747502079991071'

def test_extract_green_0_lrtb():

    with tempfile.TemporaryDirectory() as tmpdirname:  
        args = [os.path.join(SCRIPTDIR, 'lsb_green_0.png'), '-out', tmpdirname, '-extractLSB', '-green', '0'] 
        veritas = stegoveritas.StegoVeritas(args=args)
        veritas.run()

        # Verify we're expecting that
        with open(os.path.join(tmpdirname, 'LSBExtracted.bin'),'rb') as f:
            assert hashlib.md5(f.read()).hexdigest() == '592568cbbe556bb24a93c976df0621ec'

def test_extract_blue_0_lrtb():

    with tempfile.TemporaryDirectory() as tmpdirname:  
        args = [os.path.join(SCRIPTDIR, 'lsb_blue_0.png'), '-out', tmpdirname, '-extractLSB', '-blue', '0'] 
        veritas = stegoveritas.StegoVeritas(args=args)
        veritas.run()

        # Verify we're expecting that
        with open(os.path.join(tmpdirname, 'LSBExtracted.bin'),'rb') as f:
            assert hashlib.md5(f.read()).hexdigest() == '5626b080f13e0b8618da1aed934ab33c'

def test_extract_rgb_0_lrtb():

    with tempfile.TemporaryDirectory() as tmpdirname:  
        args = [os.path.join(SCRIPTDIR, 'lsb_rgb_0.png'), '-out', tmpdirname, '-extractLSB', '-red', '0', '-green', '0', '-blue', '0'] 
        veritas = stegoveritas.StegoVeritas(args=args)
        veritas.run()

        # Verify we're expecting that
        with open(os.path.join(tmpdirname, 'LSBExtracted.bin'),'rb') as f:
            assert hashlib.md5(f.read()).hexdigest() == '7cd0b50baaf727f4c6ad7565ab55a2e0'

# TODO: Extract other scan types (bottom->up for example)
# TODO: Extract higher bitplanes (0,1,2 combined for example)
# TODO: Extract other rgb orders
