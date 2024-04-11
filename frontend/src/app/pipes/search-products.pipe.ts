import { Pipe, PipeTransform } from '@angular/core';
import { TypeDataField } from '../models/filter';

@Pipe({
  name: 'searchProducts'
})
export class SearchProductsPipe implements PipeTransform {
  transform(list: TypeDataField[], search: string): TypeDataField[] {
    return list.filter((option: TypeDataField) => option.viewed_name.toLowerCase().includes(search.toLowerCase()));
  }
}
