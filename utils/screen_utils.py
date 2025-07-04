from typing import Tuple
import config

class ScreenUtils:
    """Utility class for screen and window operations"""
    
    @staticmethod
    def get_optimal_window_size() -> Tuple[str, str]:
        """Get optimal window size based on screen resolution"""
        try:
            from screeninfo import get_monitors
            w = ''
            h = ''
            for i in str(get_monitors()).split(' '):
                if('width=' in i):
                    w = str(int(int(i[6:-1])/1.4))
                if('height=' in i):
                    h = str(int(int(i[7:-1])/1.4))
            if not w or not h:
                w, h = str(config.DEFAULT_WINDOW_SIZE[0]), str(config.DEFAULT_WINDOW_SIZE[1])
            return w, h
        except ImportError:
            # Default window size if screeninfo is not available
            return str(config.DEFAULT_WINDOW_SIZE[0]), str(config.DEFAULT_WINDOW_SIZE[1])
