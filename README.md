# pastasoss

Predicting Accurate Spectral Traces in Astrophysical SOSS Spectra

By: Tyler Baines, STScI Science Support Analyst (NIRISS/SOSS Team) email: tbaines@stsci.edu

This tool is capable of predicting the spectral trace positions in a NIRISS SOSS observations with the GR700XD at given a pupil wheel position with sub-pixel accuracy. The tool currently supports spectral order 1 and 2, with future support for order 3. In addition, future updates will include both spectral traces poisition and their associated wavelengths. 

As more and more JWST NIRISS/SOSS data becomes available we plan on updating the tool and reference data files. 

Current trace position ranges for each spectral order:
- order 1: x | [4, 2043]
- order 2: x | [1000, 1750] (support to extended range to 650 will be available soon)
- order 3: TBD

The wavelength calibration model supports full range of order 1 while order 2 supports from pixel column 650 to 1750. 

(TBD)To install the package via pip:
```bash
pip install pastasoss
```

Altneratively, you can clone the repository and navigate to directory:
```bash
pip install .
```

To use the package:
```bash
import pastasoss

# predict gr700xd traces position for order 1
pastasoss.get_soss_traces(245.84, order='1')

# predict gr700xd traces position for order 2
pastasoss.get_soss_traces(245.84, order='2')

# predict gr700xd traces position for orders 1 and 2
pastasoss.get_soss_traces(245.84, order='12')
```

A very short demo [notebook](https://github.com/tbainesUA/pastasoss/blob/develop/notebooks/pastasoss_demo.ipynb) is included with the package and we encourage users to checkout. 

Community feedback  and contribution is encouraged! 

