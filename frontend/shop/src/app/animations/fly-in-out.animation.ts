import { transition, style, animate, trigger, state, keyframes } from '@angular/animations';

export const flyInOut = trigger('flyInOut', [
    state('in', style({
        transform: 'translateX(0)'
    })),
    transition('void => *', [
        animate(300, keyframes([
            style({opacity: 1, transform: 'translateX(400%)', offset: 0}),
            style({opacity: 1, transform: 'translateX(0)', offset: 1.0})
        ]))
    ])
])