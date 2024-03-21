import { Pipe, PipeTransform } from '@angular/core';
import { TypeDataFilter } from '../models/filter';

@Pipe({
  name: 'searchProducts'
})
export class SearchProductsPipe implements PipeTransform {
  transform(list: TypeDataFilter[], search: string): TypeDataFilter[] {
    return list.filter((option: TypeDataFilter) => option.viewed_name.toLowerCase().includes(search.toLowerCase()));
  }
}