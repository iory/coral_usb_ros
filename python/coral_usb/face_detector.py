from coral_usb.cfg import EdgeTPUFaceDetectorConfig
from coral_usb.cfg import EdgeTPUPanoramaFaceDetectorConfig
from coral_usb.detector_base import EdgeTPUDetectorBase
from coral_usb.detector_base import EdgeTPUPanoramaDetectorBase


class EdgeTPUFaceDetector(EdgeTPUDetectorBase):

    _config_class = EdgeTPUFaceDetectorConfig

    def __init__(self, namespace='~'):
        super(EdgeTPUFaceDetector, self).__init__(None, None, namespace)

        # only for human face
        self.label_ids = [0]
        self.label_names = ['face']


class EdgeTPUPanoramaFaceDetector(EdgeTPUPanoramaDetectorBase):

    _config_class = EdgeTPUPanoramaFaceDetectorConfig

    def __init__(self, namespace='~'):
        super(EdgeTPUPanoramaFaceDetector, self).__init__(
            None, None, namespace)

        # only for human face
        self.label_ids = [0]
        self.label_names = ['face']
