import { transition, style, animate, trigger, state } from '@angular/animations';

export const fadeInOut = trigger('fadeInOut', [
    state('void', style({
      opacity: 0,
    })),
    transition('void <=> *', animate('200ms')),
])