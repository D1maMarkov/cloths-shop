import { Directive } from '@angular/core';
import { ElementRef } from '@angular/core';
import { HostListener } from '@angular/core';

@Directive({
  selector: '[appCopyText]'
})
export class CopyTextDirective {

  constructor(private element: ElementRef) {}

  @HostListener('click') onClick() {
    this.element.nativeElement.querySelector(".tooltiptext").style.opacity = 1;
    setTimeout(() => {
      this.element.nativeElement.querySelector(".tooltiptext").style.opacity = 0;
    }, 1000);
  }

}
