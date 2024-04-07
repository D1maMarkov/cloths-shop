import { FilterService } from 'src/app/services/filter.service';
import { Component, ElementRef } from '@angular/core';

@Component({
  selector: 'app-main-filter',
  templateUrl: './main-filter.component.html',
  styleUrls: ['./main-filter.component.scss'],
})
export class MainFilterComponent{
  constructor(
    public filter: FilterService,
    private elementRef: ElementRef
  ) {
    this.filter.price$.subscribe(price => {
      this.price = price
    })
    this.filter.priceRange$.subscribe(range => {
      this.defaultPrice = range.max_price;
      this.price = range.max_price;
    })
  }

  defaultPrice: number
  price: number;

  validReset(): boolean{
    const checkboxes: HTMLInputElement[] = this.elementRef.nativeElement.querySelectorAll('input[type=checkbox]');
    let valid: boolean = false;

    checkboxes.forEach(checkbox => {
      if (checkbox.checked){
        valid = true;
      }
    })

    if (this.price !== this.defaultPrice){
      valid = true;
    }

    return valid;
  }
}
