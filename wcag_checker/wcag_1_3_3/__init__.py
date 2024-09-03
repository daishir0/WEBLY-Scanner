from .check_shape_dependency import check as check_shape_dependency
from .check_color_dependency import check as check_color_dependency
from .check_size_dependency import check as check_size_dependency
from .check_visual_location_dependency import check as check_visual_location_dependency
from .check_orientation_dependency import check as check_orientation_dependency
from .check_sound_dependency import check as check_sound_dependency

class WCAG1_3_3Checker:
    def __init__(self, url):
        self.url = url
        self.results = {
            'check_shape_dependency': False,
            'check_color_dependency': False,
            'check_size_dependency': False,
            'check_visual_location_dependency': False,
            'check_orientation_dependency': False,
            'check_sound_dependency': False
        }

    def run_checks(self):
        self.results['check_shape_dependency'] = check_shape_dependency(self.url)
        self.results['check_color_dependency'] = check_color_dependency(self.url)
        self.results['check_size_dependency'] = check_size_dependency(self.url)
        self.results['check_visual_location_dependency'] = check_visual_location_dependency(self.url)
        self.results['check_orientation_dependency'] = check_orientation_dependency(self.url)
        self.results['check_sound_dependency'] = check_sound_dependency(self.url)

    def evaluate(self):
        overall_pass = all(self.results.values())
        return overall_pass, self.results