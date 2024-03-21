import { Component, Input } from '@angular/core';
import { ElementRef } from '@angular/core';
import { BehaviorSubject } from 'rxjs';
import { TypeDataFilter } from 'src/app/models/filter';

@Component({
  selector: 'app-search-filter',
  templateUrl: './search-filter.component.html',
  styleUrls: ['./search-filter.component.scss']
})
export class SearchFilterComponent{
  @Input() title: string;
  @Input() observableObject: BehaviorSubject<string[]>;
  @Input() list: TypeDataFilter[];
  @Input() functionUpdate: Function;

  search: string = "";

  constructor(private elementRef: ElementRef) {}

  clear(): void{
    const checkboxes: HTMLInputElement[] = this.elementRef.nativeElement.querySelectorAll('input[type=checkbox]');
    this.search = "";
    this.observableObject.next([]);
    
    checkboxes.forEach(checkbox => {
      checkbox.checked = false;
    })
  }

  getActiveCheckboxes(): number{
    const checkboxes: HTMLInputElement[] = this.elementRef.nativeElement.querySelectorAll('input[type=checkbox]');

    let activeCount: number = 0;

    checkboxes.forEach(checkbox => {
      if (checkbox.checked){
        activeCount++;
      }
    })

    return activeCount;
  }

  empty(list: TypeDataFilter[]) : boolean{
    return !(list.length > 0);
  }
}
