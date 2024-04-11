import { Component } from '@angular/core';
import { FilterService } from 'src/app/services/filter.service';

@Component({
  selector: 'app-topnav-filters',
  templateUrl: './topnav-filters.component.html',
  styleUrls: ['./topnav-filters.component.scss']
})
export class TopnavFiltersComponent{
  constructor(public filter: FilterService) {}

  quantityOptions: number[] = [
    this.filter.quantity$.getValue(),
    this.filter.quantity$.getValue() * 2,
    this.filter.quantity$.getValue() * 3
  ];

  quantity: number = this.filter.quantity$.getValue();
}
