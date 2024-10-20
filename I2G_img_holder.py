import optparse
import vtk
from vtkImageHolder import Vtk_image_holder
import numpy as np

class I2G_IMG_HOLDER(Vtk_image_holder):


    def __init__(self, *args, **kwds):
        super().__init__(*args, **kwds)

        self.vtk_img = None

        self.BG_COLOR = [0.0, 0.0, 0.0]
        self.ren.SetBackground(self.BG_COLOR)

    def clear(self, _refresh=True):
        if hasattr(self, 'ren'):
            self.ren.RemoveAllViewProps()

        if _refresh:
            self.refresh()

    def reset(self):
        if hasattr(self, 'vtk_img'):
            del self.vtk_img
        self.vtk_img = None

        if hasattr(self, 'camera'):
            del self.camera

        try:
            self.sig_resize.disconnect(self.__resized)
        except TypeError as e:
            print("*** CATCH *** " + str(e))

        # TODO!!!!!!!!!!!!
        # is the Clear() better way than reset() ???
        super().reset()
        # self.ren.Clear()
        # and then, re-set bg color
        self.ren.SetBackground(self.BG_COLOR)
        if hasattr(self, "BG_COLOR2"):
            self.ren.SetBackground2(self.BG_COLOR2)
            self.ren.SetGradientBackground(True)

    def refresh(self):
        super().refresh()


    def set_depthpeeling(self, isOn):
        # Depth Peeling
        self.view._RenderWindow.SetAlphaBitPlanes(1)
        self.view._RenderWindow.SetMultiSamples(0)
        self.ren.SetUseDepthPeeling(isOn)
        self.ren.SetUseDepthPeelingForVolumes(isOn)
        # self.ren.SetMaximumNumberOfPeels(100)
        # self.ren.SetOcclusionRatio(0.01)


    def __resized(self):
        if hasattr(self, 'ren2'):
            self.sync_cameras()
