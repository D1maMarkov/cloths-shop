import { transition, style, animate, trigger, state } from '@angular/animations';

export const fadeInOutTopnav = trigger('fadeInOutTopnav', [
    state('void', style({
      opacity: 0,
      transform: "translateY(20vh)"
    })),
    transition('void <=> *', animate('150ms')),
])