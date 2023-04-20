#!/usr/bin/env python
"""
Galaxia
======

Provides a set of utilities to run a modified version of the synthetic star
survey generator Galaxia (`Sharma et al 2011 <http://ascl.net/1101.007>`).

How to use
----------

Galaxia comes with the function make_survey_from_particles, please refer to
its documentation for further help.
"""
from .__metadata__ import *
from .constants import *
from .Input import Input
from .Survey import Survey

__all__ = []


# check Galaxia installation
assert GALAXIA.exists(), f"Galaxia's executable {GALAXIA} doesn't exist, which means that {NAME}'s installation didn't build the backend {GALAXIA_SUBMODULE_NAME} submodule appropriately.\nPlease consult {__url__}/#Troubleshooting-installation for troubleshooting."


def make_survey_from_particles(*args, pname=None, kname=None, photo_sys=DEFAULT_PSYS, cmd_magnames=DEFAULT_CMD, simname='sim', surveyname='survey', fsample=1, ngb=64, knorm=0.596831, **kwargs):  # args is (particles, rho_pos, rho_vel)
    """
        Returns a handler object representing the synthetic star survey
        generated by Galaxia given the properties of an input set of particles
        and various survey parameters.

        Call signatures::

            output = make_survey_from_particles(particles, rho_pos, rho_vel,
             photo_sys=DEFAULT_PSYS, cmd_magnames=DEFAULT_CMD, simname='sim',
             surveyname='survey', fsample=1, ngb=64, knorm=0.596831, **kwargs)

            output = make_survey_from_particles(pname=None, kname=None,
             photo_sys=DEFAULT_PSYS, cmd_magnames=DEFAULT_CMD,
             surveyname='survey', fsample=1, **kwargs)
        
        Parameters
        ----------
        particles : dict
            Dictionary where each elements represent the properties of the
            input particles, given as equal-length array_like objects. Refer
            to Input documentation for appropriate formatting.

        rho_pos : array_like
            Contains the position-determined kernel density estimates for the
            input particles. Must have equal lengths as the elements in the
            particles dictionary.

        rho_vel : array_like
            Contains the velocity-determined kernel density estimates for the
            input particles. Must have equal lengths as the elements in the
            particles dictionary.

        pname : string
            Path to existing pre-formatted particles EBF files to use as input
            for Galaxia. This keyword argument must be used in conjunction
            with kname. Default to None if unused.

        kname : string
            Path to existing pre-formatted kernel EBF files to use as input
            for Galaxia. This keyword argument must be used in conjunction
            with pname. Default to None if unused.
            
        photo_sys : string or list
            Name(s) of the photometric system(s) Galaxia should use to generate
            the survey. Default to DEFAULT_PSYS - refer to the package
            constants. Available photometric systems can be found with the
            photometry submodule - please refer to its documentation for
            further details.

        cmd_magnames : string
            Names of the filters Galaxia should use for the color-magnitude
            diagram box selection. The given string must meet the following
            format: f"{band1},{band2}-{band3}" where band1 is the magnitude
            filter and (band2, band3) are the filters that define the
            band2-band3 color index. The filter names must correspond to
            filters that are part of the first chosen photometric system in
            photo_sys. Default to DEFAULT_CMD - refer to the package
            constants.

        simname : string
            Optional name Galaxia should use for the input files. Default to
            'sim'.
        
        surveyname : string
            Optional name Galaxia should use for the output files. Default to
            'survey'.

        fsample : float
            Sampling rate from 0 to 1 for the resulting synthetic star survey.
            1 returns a full sample while any value below returns partial
            surveys. Default to 1.
        
        ngb : int
            Number of neighbouring particles Galaxia should consider. Default to
            64.
        
        knorm : float
            TBD. Default to 0.596831.
        
        **kwargs
            Additional keyword arguments to customize the survey. Refer to
            constant PARFILE_TEMPLATE for all the possible keyword arguments.
        
        Returns
        ----------
        output : :obj:`Output`
            Handler with utilities to utilize the output survey and its data.
    """
    if pname is not None and kname is not None:
        input = Input(pname=pname, kname=kname)
    elif len(args) == 3:
        input = Input(*args,  name=simname, knorm=knorm, ngb=ngb)
    survey = Survey(input, photo_sys=photo_sys, surveyname=surveyname)
    output = survey.make_survey(cmd_magnames=cmd_magnames, fsample=fsample, **kwargs)
    return output


if __name__ == '__main__':
    pass
