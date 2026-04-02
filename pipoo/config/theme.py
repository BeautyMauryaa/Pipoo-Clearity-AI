"""
KivyMD Theme Configuration - UPDATED WITH MODERN DESIGN
"""

# Modern Color Palette (Matching reference design)
COLORS = {
    'primary': '#6366F1',        # Indigo/Purple
    'primary_dark': '#4F46E5',   # Darker purple
    'background': '#1E1B4B',     # Deep purple background
    'surface': '#2D2A5E',        # Card/surface color
    'surface_light': '#3730A3',  # Lighter surface
    'text_primary': '#FFFFFF',   # White text
    'text_secondary': '#A5B4FC', # Light purple text
    'accent': '#818CF8',         # Light purple accent
    'error': '#EF4444',          # Red
    'success': '#10B981',        # Green
    'input_bg': '#1F1D47',       # Input background
    'border': '#4C4791',         # Border color
}

# Typography
FONTS = {
    'heading': {
        'font_name': 'Roboto',
        'font_style': 'Bold',
        'font_size': '32sp',
    },
    'subheading': {
        'font_name': 'Roboto',
        'font_style': 'Medium',
        'font_size': '20sp',
    },
    'body': {
        'font_name': 'Roboto',
        'font_style': 'Regular',
        'font_size': '16sp',
    },
    'button': {
        'font_name': 'Roboto',
        'font_style': 'Medium',
        'font_size': '18sp',
    },
}

# Theme configuration for KivyMD
THEME_CONFIG = {
    'theme_style': 'Dark',
    'primary_palette': 'Indigo',
    'primary_hue': '500',
    'accent_palette': 'Purple',
    'accent_hue': '400',
}