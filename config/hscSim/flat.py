import os
root.load(os.path.join(os.environ['OBS_SUBARU_DIR'], 'config', 'hscSim', 'isr.py'))

from lsst.obs.hscSim.detrends import HscFlatCombineTask
root.combination.retarget(HscFlatCombineTask)
root.combination.badAmpCcdList = [0]
root.combination.badAmpList =    [2]
root.combination.xCenter = -6.22
root.combination.yCenter = -113.26
root.combination.radius = 18250
