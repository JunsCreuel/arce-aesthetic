module.exports = {
  content: ['./*.html', './assets/js/*.js', './src/build.py'],
  future: { hoverOnlyWhenSupported: true },
  theme: {
    screens: {
      sm: '600px',
      md: '700px',
      lg: '900px',
      xl: '1024px',
      '2xl': '1100px'
    },
    extend: {
      colors: {
        ivory: '#F8F3EA',
        mist: '#F1E9DC',
        beige: '#EEE3D2',
        cream: '#EADFCE',
        paper: '#E6D8C3',
        ink: '#3A3029',
        espresso: '#2E2621',
        text: '#2B241E',
        sub: '#665F57',
        mute: '#CFC5B8',
        line: '#E2D6C4',
        bronze: '#8A6A47',
        sand: '#C9AE86',
        champagne: '#D9C2A0',
        linen: '#F3EBDD',
        error: '#B3261E'
      },
      fontFamily: {
        sans: ['"Pretendard Variable"', 'Pretendard', '-apple-system', '"Apple SD Gothic Neo"', 'sans-serif'],
        mark: ['Marcellus', 'Georgia', 'serif'],
        serif: ['"Noto Serif KR"', '"Nanum Myeongjo"', 'serif'],
        display: ['"Cormorant Garamond"', 'Marcellus', 'Georgia', 'serif']
      },
      spacing: {
        gutter: 'var(--gutter)',
        hh: 'var(--hh)'
      },
      maxWidth: {
        site: '1360px'
      },
      transitionTimingFunction: {
        soft: 'cubic-bezier(0.23,1,0.32,1)',
        io: 'cubic-bezier(0.77,0,0.175,1)'
      },
      keyframes: {
        fill: { to: { transform: 'scaleX(1)' } },
        swap: { from: { opacity: '0', transform: 'translateY(10px)' }, to: { opacity: '1', transform: 'none' } },
        rise: { from: { opacity: '0', transform: 'translateY(16px) scale(.97)' }, to: { opacity: '1', transform: 'none' } },
        pop: { from: { opacity: '0', transform: 'scale(.96)' }, to: { opacity: '1', transform: 'none' } },
        fade: { from: { opacity: '0' }, to: { opacity: '1' } }
      },
      animation: {
        swap: 'swap .4s cubic-bezier(0.23,1,0.32,1)',
        'swap-slow': 'swap .8s cubic-bezier(0.23,1,0.32,1)',
        rise: 'rise .6s cubic-bezier(0.23,1,0.32,1)',
        pop: 'pop .25s cubic-bezier(0.23,1,0.32,1)',
        fade: 'fade .2s cubic-bezier(0.23,1,0.32,1)',
        'fill-6': 'fill 6s linear forwards',
        'fill-step': 'fill var(--dur,5s) linear forwards'
      }
    }
  },
  plugins: []
};
