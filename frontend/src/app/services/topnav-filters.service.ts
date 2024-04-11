import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';
import { TypeDataField } from '../models/filter';

@Injectable({
  providedIn: 'root'
})
export class TopnavFiltersService {
  refs$ = new BehaviorSubject<TypeDataField[]>([]);
}
