import { Directive, ElementRef, Input } from '@angular/core';
import { IsVisibleImageService } from '../services/is-visible-image.service';

@Directive({
  selector: '[isVisible]'
})
export class IsVisibleDirective {
  images = document.querySelectorAll("img");
  @Input() imageId: number;

  constructor(
    private element: ElementRef, 
    private visibleService: IsVisibleImageService
    ) {
    const options = {
      threshold: 0.5
    };

    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          this.visibleService.visibleImageId$.next(this.imageId);
        }
      });
    }, options);

    observer.observe(this.element.nativeElement);
  }
}